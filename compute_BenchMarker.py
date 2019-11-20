import csv

from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from time import time

# TODO: vm-ssh

# Note: Chameleon cloud will timeout during vm creation, due to long vm startup time, multiple vm boot isn't possible
#       Azure provider still outputting error, can't instantiate abstract class wait
#       Add more cloud provider such as google and oracle when provider become available
#       Multiple vm boot has been commented out due to long run time
#       Make sure to update the vm name and key in main
"""
AWS: Make sure the AMI-id in cloudmesh.yaml is available within the region
"""

"""
Errors: can't give specific name to cms vm boot command
        vm[ip_public] key error during cms vm ssh, ROBO3T showing key as public_ips in aws_vm collection
"""


class TestCompute:
    cloud_providers = ["chameleon", "aws"]
    res_list = []

    def test_cms_flavor_list(self):
        HEADING()
        command = "cms flavor list --refresh"
        time_record = self.test_base(command)
        self.printer_logger(time_record, "flavor-list")

    def test_cms_image_list(self):
        HEADING()
        command = "cms image list --refresh"
        time_record = self.test_base(command)
        self.printer_logger(time_record, "image-list")

    def test_cms_vm_list(self):
        HEADING()
        command = "cms vm list --refresh"
        time_record = self.test_base(command)
        self.printer_logger(time_record, "vm-list")

    def test_cms_vm_stop(self, name):
        HEADING()
        command = "cms vm stop "+name
        time_record = self.test_base(command)
        self.printer_logger(time_record, "vm-stop")

    def test_cms_vm_start(self, name):
        HEADING()
        command = "cms vm start "+name
        time_record = self.test_base(command)
        self.printer_logger(time_record, "vm-start")

    def test_cms_vm_boot_one(self):
        HEADING()
        command = "cms vm boot"
        time_record = self.test_base(command)
        self.printer_logger(time_record, "vm-boot-1")

    def test_cms_vm_boot_five(self):
        # Excluding chameleon from multiple vm boot
        HEADING()
        self.cloud_providers = ["aws"]
        command = "cms vm boot --n=5"
        time_record = self.test_base(command)
        self.printer_logger(time_record, "vm-boot-5")
        self.cloud_providers = ["chameleon", "aws"]

    def test_cms_vm_boot_ten(self):
        # Excluding chameleon from multiple vm boot
        HEADING()
        self.cloud_providers = ["aws"]
        command = "cms vm boot --n=10"
        time_record = self.test_base(command)
        self.printer_logger(time_record, "vm-boot-10")
        self.cloud_providers = ["chameleon", "aws"]

    def test_cms_vm_terminate(self, name, count):
        # Giving one name will delete all instance with the same name
        # Since all vm has the same name, all instances will be terminated with this command
        HEADING()
        command = "cms vm terminate " + name
        print("TERMINATING ", count, " instance")
        time_record = self.test_base(command)
        self.printer_logger(time_record, "vm-terminate-"+str(count))

    def test_base(self, command):
        time_record = {}
        for cloud_provider in self.cloud_providers:
            Shell.execute("cms set cloud=" + cloud_provider, shell=True)
            print("Working on "+cloud_provider)
            if cloud_provider in ["azure", "aws"]:
                if "image" in command or "flavor" in command:
                    print("This will take some time")
            start = time()
            result = Shell.execute(command, shell=True)
            end = time()
            res = end - start
            time_record.update({cloud_provider: res})
        return time_record

    def printer_logger(self, time_record, method_name):
        result_lst = [method_name]
        for key, val in time_record.items():
            if method_name in ["test_cms_vm_boot_five", "test_cms_vm_boot_ten"] and key == "chameleon":
                result_lst.append("N/A")
            result_lst.append(val)
            print(key, "=>", val)
        self.res_list.append(result_lst)

    def csv_writer(self):
        header = self.cloud_providers
        header.insert(0, " ")
        with open('benchmark_result.csv', 'wt', newline='')as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(header)
            for res in self.res_list:
                writer.writerow(res)


def main():
    # remember to change the default vm name accordingly, in order for vm terminate to work properly
    vm_name = "wang542-vm"
    key = "id_rsa"
    Shell.execute("cms start", shell=True)
    Shell.execute("cms set key="+key, shell=True)
    bench_marker = TestCompute()
    bench_marker.test_cms_flavor_list()
    bench_marker.test_cms_image_list()
    bench_marker.test_cms_vm_boot_one()
    bench_marker.test_cms_vm_stop(vm_name)
    bench_marker.test_cms_vm_start(vm_name)
    bench_marker.test_cms_vm_terminate(vm_name, 1)

    """
    caution the following boot commands will take long time to run
    bench_marker.test_cms_vm_boot_five()
    bench_marker.test_cms_vm_terminate(vm_name, 5)
    bench_marker.test_cms_vm_boot_ten()
    bench_marker.test_cms_vm_terminate(vm_name, 10)
    """
    bench_marker.test_cms_vm_list()

    # output into csv file, look for "benchmark_result.csv
    bench_marker.csv_writer()


if __name__ == "__main__":
    main()

# Benchmarking Cloudmesh Compute Providers

* Gregor von Laszewski
* Chenxu Wang, fa19-516-157

* [fa19-516-157](https://github.com/cloudmesh-community/fa19-516-157)
* [Link to custom benchmark script](https://github.com/cloudmesh-community/fa19-516-157/blob/master/compute_BenchMarker.py)
* [Link to custom benchmark output](https://raw.githubusercontent.com/cloudmesh-community/fa19-516-157/master/benchmarkOutput_v2.txt)

Disclaimer: This report was rewritten and augmented by Gregor von
Laszewski. The report contains only one run for each cloud and therefore
is not a complete benchmark.

The benchmarks are done on an older version of the Chameleon cloud. A newer
has become available during the Fall semester. However, this new
version was not used for testing, and it was not attempted to verify if
Cloudmesh works on this newer version.

In addition a musch better approach for benchmarking has been demonstarted by von Laszewski at 
<https://github.com/cloudmesh/cloudmesh-cloud/blob/master/benchmark/analyse_loop.ipynb>
This can be used and expanded upon for other clouds.

## Introduction

Cloudmesh provides a multi-cloud interface to compute services on AWS,
Azure, OpenStack, and Oracle. From them, we tested the behavior of
managing VMS on AWS, Azure, and Chameleon Cloud.

### Results

The results presented here are not representative but only show a single
benchmark and not a comprehensive benchmark. They are useful as they can
lead to a better benchmark strategy in the future.

The results for a run conducted are depicted in @fig:157-benchmark

![benchmark result](../images/benchmark_res.PNG){#fig:157-benchmark}

We observer that in this example

* AWS is the most efficient out of 3 providers for booting VMS. However
  others have reported different time while observing VM starts ranging
  from 2-77 seconds.

* Openstack and Azure are fast in retrieving flavor and image
  list compared to AWS. This is because far viewer images
  and flavors are available.

* Azure takes a long time to boot the VM compared to AWS because of Azure
  introduces the concept of a *Resource* to which the VM is associated.
  All resources for AWS are already assigned. In a future activity this
  has to be benchmarked in more detail while augmenting the specific
  portions to contrast the resource generation parts versus the booting
  part.
  
* Termination of Azure instances also take a long time. Also here we need
  to investigate in a future activity the details on where this happens.

## Observations

During the creation of the VMS, we observed that AWS and Chameleon cloud did, at times, not return a valid VM. on Chameleon cloud, that cloud was either
down or oversubscribed. On AWS, we have no conducted a sufficient
investigation on what this happens. Future activities must look at the
log file, as well as outage reports. However, in this study, the frequency
of how much this occurs was not conducted. Future activities should
create an automated benchmark running over a long period of time

We list summaries for the specific clouds next.

### General

Cloudmesh includes a cms init command. This command does not
include adding the key to Cloudmesh on purpose. However, we found that users seem to
forget calling the `key add` command, and we need to evaluate if it needs
to be included in the `cms init` command.
 

### Chameleon

Booting VMs often fails. The longest time observed was eleven minutes.
Very often, the provider times out. We have set the timeout time to 360 seconds. Future activities should conduct a benchmark activity on
determining a good time out value (not only for Chameleon but also for
other clouds)

It also seems that a user encounters problems if VMs are started
immediately after stopping a VM, or vice versa. In that case, we seem to
observer delays. A future activity should research this issue in more
detail while varying times between such calls.


### AWS
    
**Mongo import improvement**:
    
It is essential to have MongoDB properly installed and access to the
mongo import command. We found that the user executing this benchmark
had issues with it. We need to evaluate if we need to improve either the
documentation or the access to the location of the import command in the
script to avoid this setup error.

A future user conducting this benchmark on WIndows must fix this
configuration issue. Likely, the path variable that we
communicate in the YAML file and use for starting and stopping mongo
could simply be added here to avoid this error. If so, it is a one line change
in the program.

**VM termination**

We have to verify this error as it was not yet reported by others.
    
The implementation of the termination in the command `vm terminate`
outputs an error but it actually works, it is likely the flatdict function
encountered empty dictionary when trying to display result
 
**Flavor query**

Once all flavors are in Cloudmesh they can be searched with the build-in
cloudmesh search function. However, AWS provides the ability to restrict
the flavors. This is indicated as a prototype developed by another user
in [GitHub](https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/compute/aws/AwsFlavors-dev.py).
However, this implementation was not completed as the introduction of it
into the providers contained side effects. Thus it is just added as a
development example for future activities. Additional pytest should be
developed to make sure that after the integration of this it works.
However, it also seems that this add on does not contain the use of
mongoimport making the add on into the database faster. It needs to be
evaluated if this is needed. As a search already exists, it has to be
evaluated if it is even useful to add the direct query enhanced
functionality.
 
### Azure
    
The `vm terminate` command in  Azure provider should be restructured to
terminate the vm only, currently terminate will delete all resource
related to vm, if two vm share the same resources such as NIC, SecGroup then
terminate can cause an error.
    
The `image list --refresh` only displays the first view images. It is
important to enhance the list function to make clear that not all images
are displayd.

### Using this simple test program

Due to its limitation, the program provided is actually not a benchmark
program but just tests functionality. However, you can use it as follows.
We assume your cloudmesh.yaml file is properly configured.

```bash
mkdir cm
cd cm
git clone https://github.com/cloudmesh-community/fa19-516-157.git
cd
cms init
cms key add
cms key upload NAME --cloud=CLOUD
```

name must be the same as returned by

```bash
cms config cloudmesh.profile.user
```

For Azure the key upload does not have to be conducted as it is
implicitly included in the vm boot command for each vm.

To customize the script, you can adjust the cloud_providers list in line
19 of `compute_BenchMarker.py`. This allows you to, for example, also
add Chameleon cloud or restrict the test. Ideally this script should
have been developed as Cloudmesh command, which is easily possible so
that such modifications can be passed to the script without modifying
the python script. If there are more cloud providers implemented in
Cloudmesh. Please see `cms sys command generate` for future activities.
    
## Links


## References

Towards a better benchmark

* [notebook example](https://github.com/cloudmesh/cloudmesh-cloud/blob/master/benchmark/analyse_loop.ipynb)

A link created by this activity

* [Azure practice script 1](https://github.com/cloudmesh-community/fa19-516-157/blob/master/project/AzurePractice/myAzurePractice.py)
* [Azure practice script 2](https://github.com/wang542/cloudmesh-cloud/blob/azure_wang542/cloudmesh/compute/azure/Provider.py)
* [Simple benchmark script](https://github.com/cloudmesh-community/fa19-516-157/blob/master/compute_BenchMarker.py)
* [Azure account instruction](https://github.com/cloudmesh-community/fa19-516-157/blob/master/azure_credentials.md)


Other References

* [Create VM on Azure using Python](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/python#)
* [Issue/Example related to NSG creation on github-azure](https://github.com/MicrosoftDocs/azure-docs/issues/30555)
* [Discussion regarding NSG security rules](https://stackoverflow.com/questions/55970074/issues-with-network-security-group-deployment-using-python-networksecuritygrou)
* [Azure documentation-Security Group](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)
* [Azure Security Rules Operation class -python](https://docs.microsoft.com/en-us/python/api/azure-mgmt-network/azure.mgmt.network.v2017_03_01.operations.securityrulesoperations?view=azure-python)

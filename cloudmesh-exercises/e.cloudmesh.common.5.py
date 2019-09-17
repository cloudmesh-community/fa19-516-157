# import stopwatch from cloudmesh
from cloudmesh.common.StopWatch import StopWatch as sw
# import default sleep
from time import sleep


sw.start("sleepsession")
print("Im going to sleep")
sleep(8)
sw.stop("sleepsession")
print("how long? "+str(sw.get("sleepsession"))+" hours")


# good use of stop watch
def defaultsort(lst):
    sw.start("sorting")
    print(sorted(lst))
    sw.stop("sorting")
    print("took me " + str(sw.get("sorting")) + " to sort")


# displaying 0 maybe because didn't even take 1 second
defaultsort([1, 4, 5, 2, 56, 2111, 68, 22])

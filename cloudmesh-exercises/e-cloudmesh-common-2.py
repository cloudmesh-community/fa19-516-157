#import dotdict
from cloudmesh.common.dotdict import dotdict


# first set up a simple dict
sample_dict = {
    "breed": "Yorkie",
    "Weight": 12,
    "color": "silver",
    "attribute": "super cute"}


# convert the dict to dotdict using dotdict function
sample_dict = dotdict(sample_dict)

# check dotdict usage
if sample_dict.attribute is "super cute":
    print("dotdict worked, returned " + sample_dict.attribute)
else:
    print("oops")

# import flatdict, note F & D
from cloudmesh.common.FlatDict import FlatDict


# create a simple nested dict
sample_dict = {
    "breed": "Yorkie",
    "Weight": 12,
    "color": "silver",
    "attribute": {
        "plus": "cute",
        "minus": "not interested in food",
        "favorite": {
            "treat": "chicken breast",
            "toy": "lamb chop"
        }
    }}

# transform dict using FlatDict
sample_dict = FlatDict(sample_dict)
print(sample_dict)

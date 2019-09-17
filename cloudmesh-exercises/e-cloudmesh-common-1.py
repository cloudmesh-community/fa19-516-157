# Import banenr function
from cloudmesh.common.util import banner
# Import Heading function
from cloudmesh.common.util import HEADING
# Import VERBOSE
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables
# ---------------------
# create a banner
banner("Chenxu Wang | Graduate Student | IUB")

# ---------------------------
# demostrate usage of Heading
# heading shows the funuction name


def Proof():
    HEADING()
    print("function should be Proof")


Proof()

# setting variables, verbose seems can't work without setting
variables = Variables()
variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10
# --------------------
sample_dict = {"randomname": "foo"}
VERBOSE(sample_dict)

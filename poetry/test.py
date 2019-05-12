from os import getcwd
from os import environ
#from C.Class.Structure.Structure import Semantique

environ["POETRY_PATH"] = getcwd() + "/poetry"

import C.Class.Structure.DEM_parser as test


test1 = test.DEM_parser.CA("M-")
print (test1)
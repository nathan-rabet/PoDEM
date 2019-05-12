from os import getcwd
from os import environ
#from C.Class.Structure.Structure import Semantique

environ["POETRY_PATH"] = getcwd() + "/poetry"

import C.Class.Structure.Semantique as test


test1 = test.Semantique.CA("M-")
print (test1)
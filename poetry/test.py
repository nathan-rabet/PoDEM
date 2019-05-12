from os import getcwd
from os import environ
#from C.Class.Structure.Structure import Semantique
from poetry.C.Class.Structure.DEM_parser import *

environ["POETRY_PATH"] = getcwd() + "/poetry"

test = DEM_parser()

test.PSYl = test.DOM("PSY")
test.wPSY = DEM_parser().M_selec(test.PSYl)
print(test.wPSY)
<<<<<<< HEAD
﻿from os import getcwd
import os

os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from V.visual import *

startup()
=======
from os import getcwd
import os

os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from C.Class.Parser.DEM_parser import *
from C.Class.Structure.Determinant import *

print(style_langage("p"))
>>>>>>> master

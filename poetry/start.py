﻿from os import getcwd
import os

os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from C.Class.Parser.DEM_parser import *
from C.Class.Structure.Determinant import *
from C.Class.Parser.selectionneur_mot import *
from C.Class.Semantique.Constructeur_phrase import *
from V.visual import *


Afficher_phrase(10,'')
from os import getcwd
import os

os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from V.visual import *

startup()
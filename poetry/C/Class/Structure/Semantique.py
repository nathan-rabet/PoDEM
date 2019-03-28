from os import environ
import csv
from pathlib import Path

class Semantique:
    DEM_PATH = environ["POETRY_PATH"] + "/M/DEM.csv"
    DEM_PATH = Path(DEM_PATH)
    DEM = open(DEM_PATH)

    def DOM(DOM, table=None):
        filtered = []
        reader = csv.reader(open(Semantique.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[7] == DOM:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[7] == DOM:
                    filtered.append(ligne)
            return filtered
    DOM = staticmethod(DOM)

    def OP(OP, table=None):
        filtered = []
        reader = csv.reader(open(Semantique.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[8] == OP:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[8] == OP:
                    filtered.append(ligne)
            return filtered
    OP = staticmethod(OP)

    def CA(CA, table=None):
        filtered = []
        reader = csv.reader(open(Semantique.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[11] == CA:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[11] == CA:
                    filtered.append(ligne)
            return filtered
    CA = staticmethod(CA)
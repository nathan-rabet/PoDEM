from os import environ
import csv
from pathlib import Path

class DEM_parser:
    DEM_PATH = environ["POETRY_PATH"] + "/M/DEM.csv"
    DEM_PATH = Path(DEM_PATH)
    DEM = open(DEM_PATH)

    def M_selec(table):
        words = []
        for ligne in table:
            words.append(ligne[0])
        return words
    M_selec = staticmethod(M_selec)

    def M(M, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[0] == M:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[0] == M:
                    filtered.append(ligne)
            return filtered
    M = staticmethod(M)

    def no(no, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[1] == no:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[1] == no:
                    filtered.append(ligne)
            return filtered
    no = staticmethod(no)

    def reflexif(reflexif, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[2] == reflexif:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[2] == reflexif:
                    filtered.append(ligne)
            return filtered
    reflexif = staticmethod(reflexif)

    def exclamatif(exclamatif, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[3] == exclamatif:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[3] == exclamatif:
                    filtered.append(ligne)
            return filtered
    exclamatif = staticmethod(exclamatif)

    def interrogatif(interrogatif, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[4] == interrogatif:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[4] == interrogatif:
                    filtered.append(ligne)
            return filtered
    interrogatif = staticmethod(interrogatif)

    def h_aspire(h_aspire, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[5] == h_aspire:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[5] == h_aspire:
                    filtered.append(ligne)
            return filtered
    h_aspire = staticmethod(h_aspire)

    #Méthode contigente n°1
    def CONT(CONT, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[6] == CONT:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[6] == CONT:
                    filtered.append(ligne)
            return filtered
    CONT = staticmethod(CONT)

    def DOM(DOM, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
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
        reader = csv.reader(open(DEM_parser.DEM_PATH))
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

    #Méthode contigente n°2
    def SENS(SENS, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[9] == SENS:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[9] == SENS:
                    filtered.append(ligne)
            return filtered
    SENS = staticmethod(SENS)

    def OP1(OP1, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
        if table == None:
            for ligne in reader:
                if ligne[10] == OP1:
                    filtered.append(ligne)
            return filtered
        else:
            for ligne in table:
                if ligne[10] == OP1:
                    filtered.append(ligne)
            return filtered
    OP1 = staticmethod(OP1)

    def CA(CA, table=None):
        filtered = []
        reader = csv.reader(open(DEM_parser.DEM_PATH))
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
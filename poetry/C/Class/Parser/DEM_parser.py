from os import environ
import csv
from pathlib import Path
import re

def init_DEM():
    """ 
    Fonction permettant d'initialiser le fichier DEM.
    
    Doit être utilisée en complément avec close_DEM() !!!!!
    """

    global DEM_PATH
    DEM_PATH = Path(environ["POETRY_PATH"] + "/M/DEM.csv")

    global DEM
    DEM = open(DEM_PATH, "r",encoding='utf-8')

    global reader
    sep = "\t"
    reader = csv.reader(DEM, delimiter=sep)

def close_DEM():
    """ 
    Fonction permettant de fermer le fichier DEM.
    
    Doit être utilisée si init_DEM() est exécuter !!!!!
    """

    DEM.close()

def Trouve_ligne_mot(mot):
    """ 
    Fonction renvoyant le numéro d'indexation (ou de ligne) d'un mot dans le fichier DEM.csv.
    """

    init_DEM()
    numero_line = 0
    for ligne in reader:
        if ligne[0] == mot:
            close_DEM()
            return numero_line
        else:
            numero_line += 1

def Donne_ligne_numero(no):
    """
    Renvoie une ligne (sous forme de tableau) à partir d'un numéro d'indexation.
    """

    init_DEM()
    for number, line in enumerate(DEM):
        if number == no:
            close_DEM()
            return (line.replace("\n","")).split(sep)


def Cellule_de_la_ligne(table, index=0):
    """
    Renvoie une cellule précise d'une ligne.
    """

    words = []
    for ligne in table:
        words.append(ligne[index])
    
    return words

def Premiere_lettre_voyelle(mot):
    """
    Précise si un mot commence par une voyelle ou non.
    """

    if mot[0].lower() in ["a","e","i","o","u","y"]:
        return True
    else:
        return False
    

def M(M, table=None):
    """
    Si 1 argument : renvoie les lignes comportant le mot M à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant le mot M à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[0] == M:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[0] == M:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def no(no, table=None):
    """
    Si 1 argument : renvoie les lignes comportant le no indiqué à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant le no indiqué à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[1] == no:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[1] == no:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def reflexif(reflexif, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un M reflexif "(s)" à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un M reflexif "(s)" à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[2] == reflexif:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[2] == reflexif:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def exclamatif(exclamatif, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un M exclamatif "X" à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un M reflexif "X" à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[3] == exclamatif:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[3] == exclamatif:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def interrogatif(interrogatif, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un M interrogatif "X" à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un M interrogatif "X" à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[4] == interrogatif:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[4] == interrogatif:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def h_aspire(h_aspire, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un M avec un h aspiré "X" à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un M avec un h aspiré "X" à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[5] == h_aspire:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[5] == h_aspire:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def CONT(CONT, table=None):
    """
    Si 1 argument : renvoie les lignes contenant l'argument dans CONT à partir du DEM.
    
    Si 2 arguments : renvoie les lignes contenant l'argument dans CONT à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if re.search(CONT,ligne[6]):
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if re.search(CONT,ligne[6]):
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def DOM(DOM, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un DOM précis à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un DOM précis à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[7][0:3] == DOM:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[7][0:3] == DOM:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def OP(OP, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un DOM précis à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un DOM précis à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[8] == OP:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[8] == OP:
                filtered.append(ligne)
        close_DEM()
        return filtered
    
def SENS(SENS, table=None):
    """
    Si 1 argument : renvoie les lignes contenant l'argument dans SENS à partir du DEM.
    
    Si 2 arguments : renvoie les lignes contenant l'argument dans SENS à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if re.search(SENS,ligne[9]):
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if re.search(SENS,ligne[9]):
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def OP1(OP1, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un OP1 précis à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un OP1 précis à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[10] == OP1:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[10] == OP1:
                filtered.append(ligne)
        close_DEM()
        return filtered
    

def CA(CA, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un CA précis à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un CA précis à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if ligne[11] == CA:
                filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if ligne[11] == CA:
                filtered.append(ligne)
        close_DEM()
        return filtered

def style_langage(style, table=None):
    """
    Si 1 argument : renvoie les lignes comportant un style de langage précis à partir du DEM.
    
    Si 2 arguments : renvoie les lignes comportant un style de langage précis à partir de la table donnée.
    """

    init_DEM()
    filtered = []
    if table == None:
        for ligne in reader:
            if len(ligne[7]) == 4:
                if ligne[7][-1] == style:
                    filtered.append(ligne)
        close_DEM()
        return filtered
    else:
        for ligne in table:
            if len(ligne[7]) == 4:
                if ligne[7][-1] == style:
                    filtered.append(ligne)
        close_DEM()
        return filtered


def VERIF_MOT(LISTE):
    """
    Pour éviter toute incohérence, certaine expressions (comme les verbes) ne peuvent être composé que d'un seul mot

    Cette fonction supprime toute les expressions qui possède plusieurs mots
    """

    LISTE_V2 = []
    for i in LISTE :
            mot = i
            if not re.search(' ',mot[1:-2]) :
                    LISTE_V2.append(mot)
    return LISTE_V2
         

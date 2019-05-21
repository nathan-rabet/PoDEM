from C.Modules.Parser.DEM_parser import *
from random import randint

def deter_alea(nom) :

    """
    Selectionne un type de determinant au hasard.
    """

    alea = randint(0,3)

    if alea == 0 :

        deter = article_def(nom)

    elif alea == 1 :

        deter = demonstratif(nom)

    elif alea == 2 :

        deter = possessif(nom)

    elif alea == 3 :

        deter = cardinal(nom)

    return deter





def article_def(nom):

    """
    Donne le determinant de type article définie du nom.
    """

    CA = nom[1]

    if CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "-8" or CA == "-4":
        if Premiere_lettre_voyelle(nom[0]):
            return "l'"
        else:
            return "le "
    
    elif CA == "-2" or CA == "-6" or CA == "-9":
        if Premiere_lettre_voyelle(nom[0]):
            return "l'"
        else:
            return "la "
    else:
        return False

def demonstratif(nom):

    """
    Donne le determinant de type démonstratif du nom.
    """

    CA = nom[1]

    if CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "-8" or CA == "-4":
        if Premiere_lettre_voyelle(nom[0]) or nom[0][0] == "h":
            return "cet "
        else:
            return "ce "
    
    elif CA == "-2" or CA == "-6" or CA == "-9":
        return "cette "
    else:
        return False


def possessif(nom):

    """
    Donne le determinant de type possesif du nom.
    """

    CA = nom[1]


    rand = randint(0,5)

    if CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "-8" or CA == "-4" or Premiere_lettre_voyelle(nom[0]):
        if rand == 0:
            return "mon "
        elif rand == 1:
            return "ton "
        elif rand == 2:
            return "son "
        elif rand == 3:
            return "notre "
        elif rand == 4:
            return "votre "
        elif rand == 5:
            return "leur "
    
    elif (CA == "-2" or CA == "-6" or CA == "-9"):
        if rand == 0:
            return "ma "
        elif rand == 1:
            return "ta "
        elif rand == 2:
            return "sa "
        elif rand == 3:
            return "notre "
        elif rand == 4:
            return "votre "
        elif rand == 5:
            return "leur "
    else:
        return False



def cardinal(nom) :

    """
    Donne le determinant de type cardinal(ou article indéfinie) du nom.
    """

    CA = nom[1]

    if CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "-8" or CA == "-4":
        return "un "
    
    elif CA == "-2" or CA == "-6" or CA == "-9":
        return "une "
        
    else:
        return False



    

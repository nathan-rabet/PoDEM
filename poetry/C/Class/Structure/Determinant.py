<<<<<<< HEAD
from C.Class.Parser.DEM_parser import *
from random import randint

def deter_alea(nom) :

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


    CA = nom[1]

    if CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "-8" or CA == "-4":
        return "un "
    
    elif CA == "-2" or CA == "-6" or CA == "-9":
        return "une "
        
    else:
        return False



    
=======
from C.Class.Parser.DEM_parser import *
from random import randint

def article_def(nom):
    no = Trouve_ligne_mot(nom)
    
    CA = Donne_ligne_numero(no)
    CA = CA[-1]

    M = Donne_ligne_numero(no)
    M = M[0]

    if CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "8":
        if Premiere_lettre_voyelle(M):
            return "l'"
        else:
            return "le"
    
    elif CA == "-2" or CA == "-6" or CA == "-9":
        if Premiere_lettre_voyelle(M):
            return "l'"
        else:
            return "la"
    else:
        return False

def demonstratif(nom):
    no = Trouve_ligne_mot(nom)
    CA = Donne_ligne_numero(no)
    CA = CA[-1]

    M = Donne_ligne_numero(no)
    M = M[0]

    if CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "8":
        if Premiere_lettre_voyelle(nom) or nom[0] == "h":
            return "cet"
        else:
            return "ce"
    
    elif CA == "-2" or CA == "-6" or CA == "-9":
        return "cette"
    else:
        return False

def possessif(nom):

    no = Trouve_ligne_mot(nom)
    
    CA = Donne_ligne_numero(no)
    CA = CA[-1]

    M = Donne_ligne_numero(no)
    M = M[0]


    rand = randint(0,5)

    if (CA == "-1" or CA == "-3" or CA == "-5" or CA == "-7" or CA == "8"):
        if rand == 0:
            return "mon"
        elif rand == 1:
            return "ton"
        elif rand == 2:
            return "son"
        elif rand == 3:
            return "notre"
        elif rand == 4:
            return "votre"
        elif rand == 5:
            return "leur"
    
    elif (CA == "-2" or CA == "-6" or CA == "-9"):
        if rand == 0:
            return "ma"
        elif rand == 1:
            return "ta"
        elif rand == 2:
            return "sa"
        elif rand == 3:
            return "notre"
        elif rand == 4:
            return "votre"
        elif rand == 5:
            return "leur"
    else:
        return False
>>>>>>> master

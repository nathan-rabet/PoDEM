from sys import platform as _platform
import platform
from os import system
import os

def clear_console():

    """
    Nettoie la console(cmd)
    """

    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        # Linux et MacOS
        system('clear')
    elif _platform == "win32" :
        # Windows
        system('cls')


"""

Couleur des textes

"""

        
def error_message(txt):
    #rouge   
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin"  :
        return "\033[91m{}\033[00m".format(txt)
    elif _platform == "win32" or _platform == "win64" :
        ver = platform.version()
        if ver[:2] == '10':
            return "\033[91m{}\033[00m".format(txt)
        else :
            return txt        
    else :
        return txt

def correct_message(txt):
    #vert
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin" :
        return "\033[92m{}\033[00m".format(txt)
    elif _platform == "win32" :
        ver = platform.version()
        if ver[:2] == '10':
            return "\033[92m{}\033[00m".format(txt)
        else :
            return txt 

    else :  
        return txt

def warning_message(txt):
    #jaune
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin" :
        return "\033[93m{}\033[00m".format(txt)
    elif _platform == "win32" :
        ver = platform.version()
        if ver[:2] == '10':
            return "\033[93m{}\033[00m".format(txt)
        else :
            return txt 

    else :
        return txt

def tps_gen(nb_lignes) :

    """
    Donne une aproximation du temps de géneration du poème
    """

    tps = float(nb_lignes)*0.51568 # 0.50568 = Temps moyen pour afficher une phrase, Calculer sur 10 000 phrase via le calcul suivant :
                                   # Temps mis pour afficher 10 000 phrases divisé 10 000 (le nombre de phrase)
    
    print("Temps de génération estimé : " + str(time_long(tps)) + " s\n")


def time_long(tps):

    """
    Change la couleau de l'estimation de temps de géneration selon le temps
    """

    if float(tps) <= 10.0:
        return correct_message(str(tps))
    elif float(tps) <= 30.0:
        return warning_message(str(tps))
    else:
        return error_message(str(tps))



def banner(flower=True,txt=True,info=True):

    """
    IL s'agit de la page d'acceuil du programme 
    """

    t = ""
    if flower == True:
        t += """ 
            .-~~-.--.
           :         )
     .~ ~ -.\       /.- ~~ .
     >       `.   .'       <
    (         .- -.         )
     `- -.-~  `- -'  ~-.- -'
       (        :        )           _ _ .-:
        ~--.    :    .--~        .-~  .-~  }
            ~-.-^-.-~ \_      .~  .-~   .~
                     \ \      \ '_ _ -~
                      `.`.    //
             . - ~ ~-.__`.`-.//
         .-~   . - ~  }~ ~ ~-.~-.
       .' .-~      .-~       :/~-.~-./:
      /_~_ _ . - ~                 ~-.~-._
                                       ~-.< 
            """
        t += "\n\n\n"
    if txt == True:
        t += """
    8888888b.           8888888b.  8888888888 888b     d888 
    888   Y88b          888  "Y88b 888        8888b   d8888 
    888    888          888    888 888        88888b.d88888 
    888   d88P  .d88b.  888    888 8888888    888Y88888P888 
    8888888P"  d88""88b 888    888 888        888 Y888P 888 
    888        888  888 888    888 888        888  Y8P  888 
    888        Y88..88P 888  .d88P 888        888   "   888 
    888         "Y88P"  8888888P"  8888888888 888       888

            """
        t += "\n\n"
    if info == True :
         t += """

Pour afficher le menu d'aide, tapez : 'help'
Pour afficher les paramètres actifs, tapez : 'options'
Pour sortir du programme, tapez : 'exit'


              """


    return t
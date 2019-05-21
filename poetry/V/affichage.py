from sys import platform
from os import system


def clear_console():

    """
    Nettoie la console(cmd)
    """

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # Linux et MacOS
        system('clear')
    elif platform == "win32":
        # Windows
        system('cls')


"""

Couleur des textes

"""

def error_message(txt): 
    #rouge
    return "\033[91m{}\033[00m".format(txt)

def correct_message(txt):
    #vert
    return "\033[92m{}\033[00m".format(txt)

def warning_message(txt):
    #jaune
    return "\033[93m{}\033[00m".format(txt)


def tps_gen(type_phrase) :

    """
    Donne une aproximation du temps de géneration du poème
    """
    tps = 0

    for i in type_phrase :
        

        if int(i) == 0 :
            tps += 1#Phrase_intj

        elif int(i) == 1 :
    
            tps += 1#Phrase_prono

        elif int(i) == 2 :

            tps += 1#Phrase_bruit

        elif int(i) == 3 :

            tps += 1#Phrase_bruit2

        elif int(i) == 4 :

            tps += 1#Phrase_normal

        elif int(i) == 5 :

            tps += 1#Phrase_question

        elif int(i) == 6 :

            tps += 1#Phrase_normal_futur

        elif int(i) == 7 :

            tps += 1#Phrase_normal_passe

        elif int(i) == 8 :

            tps += 1#Phrase_excla1
        elif int(i) == 9 :

            tps += 1#Phrase_excla2

        elif int(i) == 10 :

            tps += 1#Phrase_Vpro1

        elif int(i) == 11 :

            tps += 1#Phrase_question2
  
        elif int(i) == 12 :

            tps += 1#Phrase_question3

        elif int(i) == 13 :

            tps += 1#Phrase_Vpro2

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



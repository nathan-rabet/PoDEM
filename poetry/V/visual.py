from sys import platform
from os import system

import csv
from os import environ
from pathlib import Path

import re

from C.Class.Semantique.Constructeur_phrase import *

def error_message(txt): 
    return "\033[91m{}\033[00m".format(txt)

def correct_message(txt):
    return "\033[92m{}\033[00m".format(txt)

def warning_message(txt):
    return "\033[93m{}\033[00m".format(txt)

def time_long(tps):
    if float(tps) <= 10.0:
        return correct_message(str(tps))
    elif float(tps) <= 30.0:
        return warning_message(str(tps))
    else:
        return error_message(str(tps))

def startup():
    on = True
    
    init_DOM()
    
    clear_console()
    print(banner())
    print("Pour afficher le menu d'aide, tapez : 'help'\n")
    print("Pour afficher les paramètres actifs, tapez : 'options'\n")
    print("Pour sortir du programme, tapez : 'exit'\n")
    
    global nb_lignes
    global DOM_input
    global style
    global DOM_valeur
    global style_valeur

    nb_lignes = 4
    DOM_input = ''
    style = ''
    DOM_valeur = ''
    style_valeur = ''

    while on:
        
        cmd = input("GÉNÉRATEUR DE POÈMES >> ")
        cmd_no_space = ""
        for i in cmd:
            if i != " ":
                cmd_no_space += i

        #Détection
        start_detec = re.match('start',cmd_no_space) and len(cmd_no_space) == len('start')
        
        DOM_detec = re.match('DOM=',cmd_no_space)
        style_detec = re.match('style=',cmd_no_space)
        nb_lignes_detec = re.match('nb_lignes=',cmd_no_space)

        help_detec = re.match('help',cmd_no_space) and len(cmd_no_space) == len('help')
        exit_detec = re.match('exit',cmd_no_space) and len(cmd_no_space) == len('exit')
        
        show_DOM_detec = re.match('show_DOM',cmd_no_space) and len(cmd_no_space) == len('show_DOM')
        show_style_detec = re.match('show_style',cmd_no_space) and len(cmd_no_space) == len('show_style')

        options_detec = re.match('options',cmd_no_space) and len(cmd_no_space) == len('options')

        if start_detec:
            clear_console()

            temps = str(nb_lignes * 0.50568)

            print("Temps de génération estimé : " + str(time_long(temps)) + " s\n")
            start()
            print("\n")

        elif show_DOM_detec:
            show_DOM()
        
        elif show_style_detec:
            show_style()

        elif options_detec:
            clear_console()
            print("DOM\t" + DOM_input + " (" + DOM_valeur + ")" )
            print("style\t" + style + " (" + style_valeur + ")" )
            print("nb_lignes\t" + str(nb_lignes))
        
        elif nb_lignes_detec:
            if len(cmd_no_space) == 10:
                print(error_message("Vous n'avez entré aucun nombre !"))
                print("Pour savoir comment utiliser cette fonctionnalité, tapez : 'help'")
            elif not cmd_no_space[10:].isdigit():
                print(error_message("La donnée que vous venez de rentrer n'est pas un nombre entier !"))
                print("Pour savoir comment utiliser cette fonctionnalité, tapez : 'help'")
            else:
                nb_lignes = int(cmd_no_space[10:])
                print(correct_message("Le poème sera composé de " + str(nb_lignes) + " lignes."))
            

        elif DOM_detec and not (start_detec or style_detec) :
            DOM_input = None
            if len(cmd_no_space) == 4 :
                DOM_input = ""
                DOM_valeur = ""
                print(warning_message("Vous n'avez séléctionné aucun thème !"))
                print("Le poème sera donc généré sans contrainte de thème")
            else:
                for i in readerDOM:
                    if re.search(i[0], cmd_no_space):
                        DOM_input = i[0]
                        DOM_valeur = i[1]
                        break
                del i
                if DOM_input == None:
                    print(error_message("Le thème que vous avez saisi n'existe pas dans notre base de donnée !"))
                    print("Aucun thème n'est donc appliqué.")
                    print("Veuillez saisir un thème correct.")
                    print("Pour connaître la liste des thèmes, tapez : 'show_DOM'")
                else:
                    print(correct_message('Vous avez renseigné le code "' + DOM_input + '" qui correspond au thème "' + DOM_valeur + '".' ))
                    print('Le poème sera donc généré selon le thème "' + DOM_valeur + '".')
        
        elif style_detec and not (start_detec or DOM_detec) :
            style = None
            if len(cmd_no_space) == 6 :
                style = ""
                style_valeur = ""
                print(warning_message("Vous n'avez séléctionné aucun style de langage !"))
                print("Le poème sera donc généré sans cette contrainte.")
            else:
                styles_langage = [['f','b','p','v','t','c','s','m','n','d'],['familier','belge','populaire','vieux','littéraire','canadien, québécois', 'suisse','maj/min selon la catégorie (Français, le français)','maj/min selon le sens (administration, l’Administration)', 'nom déposé (Altuglass)']]
                for i in range(0,len(styles_langage[0])):
                    if re.search(styles_langage[0][i], cmd_no_space[5:]):
                        style = styles_langage[0][i]
                        style_valeur = styles_langage[1][i]
                        break
                del i
                if style == None :
                    print(error_message("Le style de langage que vous avez saisi n'existe pas dans notre base de donnée !"))
                    print("Aucun style n'est donc appliqué.")
                    print("Veuillez saisir un style correct.")
                    print("Pour connaître la liste des styles, tapez : 'show_style'")
                else:
                    print(correct_message('Vous avez renseigné le code "' + style + '" qui correspond au style de langage "' + style_valeur + '".' ))
                    print('Le poème sera donc généré selon le style "' + style_valeur + '".')
        
        elif help_detec:
            help()

        elif exit_detec:
            print("À bientôt pour de nouvelles romances !")
            on = False
        
        



def clear_console():

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # Linux et MacOS
        system('clear')
    elif platform == "win32":
        # Windows
        system('cls')
    



def start():
    Afficher_phrase(nb_lignes,DOM_input,style)

def banner(flower=True,txt=True):
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
    return t

def help():
    print("""
     ___      _        _           
    /   \    (_)    __| |    ___   
    | - |    | |   / _` |   / -_)  
    |_|_|   _|_|_  \__,_|   \___|  
  _|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"| 
   \"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-' 

    Pour générer un poème:
    tapez : 'start'

    Pour sélectionner un domaine (ou un thème):
    tapez : 'DOM=<le domaine>'
    \tex : DOM=LIN
    \t(le domaine sélectionné est donc "linguistique")
    Pour afficher les domaines, utilisez "show_DOM"

    Pour sélectionner un style de langage:
    tapez : 'style=<le style>'
    \tex : style=p
    \t(le style sélectionné est donc "populaire")
    Pour afficher les styles, utilisez "show_style"

    Pour le nombre de lignes:
    tapez 'nb_lignes=<un nombre>'
    \tex : nb_lignes=8
    \t(quand vous taperez 'start', le programme va générer un poème de 8 lignes)

    Pour afficher les paramètres actifs, tapez : 'options'
    Pour sortir du programme, tapez : 'exit'
        """)

def init_DOM():
    global DOM_PATH
    DOM_PATH = Path(environ["POETRY_PATH"] + "/M//correspondance_DEM/DOM.csv")

    global DOM
    DOM = open(DOM_PATH, "r",encoding='utf-8')

    global readerDOM
    global sepDOM
    sepDOM = "\t"
    readerDOM = csv.reader(DOM, delimiter=sepDOM)

def show_DOM():
    init_DOM()
    print("""
    ,--,--'.                     
    `- |   |-. ,-. ,-,-. ,-. ,-. 
     , |   | | |-' | | | |-' `-. 
     `-'   ' ' `-' ' ' ' `-' `-'                                  
    """)
    for dom in readerDOM:
        print(dom[0] + "\t" + dom[1])
    print("\nSi vous ne souhaitez pas définir de thème, entrez 'DOM='.\nLe poème se fera alors sans contrainte de thème.")

def show_style():
    print(""" 
    
        |\ |.   _  _       _| _   | _  _  _  _  _  _ 
        | \||\/(/_(_||_|  (_|(/_  |(_|| |(_|(_|(_|(/_
                                          _|    _|   
    f	familier
    b	belge
    p	populaire
    v	vieux
    t	littéraire

        |~)_  _ . _  _  _ |. _ _ _  _  _
        |~\/_(_||(_)| |(_|||_\| | |(/__\\
              _|                        

    b	belge
    c	canadien, québécois
    s	suisse

        |\/| _ . /|\/|. _    _ _ | _  _   | _    _ _ _|_ _  _  _. _ 
        |  |(_||/ |  ||| |  _\(/_|(_)| |  |(_|  (_(_| | (_|(_)| |(/_
              _|                                         _|         
        
    m	Français, le français

        |\/| _ . /|\/|. _    _ _ | _  _   | _    _ _  _  _
        |  |(_||/ |  ||| |  _\(/_|(_)| |  |(/_  _\(/_| |_\\
              _|

    n	administration, l’Administration

        |\ | _  _ _    _| ~  _  _  _ ~ 
        | \|(_)| | |  (_|(/_|_)(_)_\(/_
                            |          

    d	Altuglass

    Si vous ne souhaitez pas définir de style, entrez 'style='.
    Le poème se fera alors à partir de n'importe quel style.
        """)


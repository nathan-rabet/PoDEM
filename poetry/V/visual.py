from sys import platform
from os import system

import csv
from os import environ
from pathlib import Path

def start():
    on = True
    
    clear_console()
    print(banner())
    print(help_min())
    while on:
        cmd = input("GÉNÉRATEUR DE POÈMES >> ")



def clear_console():

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # Linux et MacOS
        system('clear')
    elif platform == "win32":
        # Windows
        system('cls')
    

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
   ____   __         __           _                        _                     __                      
  / ___| /_/ _ __   /_/ _ __ __ _| |_ ___ _   _ _ __    __| | ___   _ __   ___   \_\ _ __ ___   ___  ___ 
 | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \ | | | '__|  / _` |/ _ \ | '_ \ / _ \ / _ \ '_ ` _ \ / _ \/ __|
 | |_| |  __/ | | |  __/ | | (_| | ||  __/ |_| | |    | (_| |  __/ | |_) | (_) |  __/ | | | | |  __/\__ |
  \____|\___|_| |_|\___|_|  \__,_|\__\___|\__,_|_|     \__,_|\___| | .__/ \___/ \___|_| |_| |_|\___||___/
                                                                   |_|                                   
            """
        t += "\n\n\n"
    return t

def help():
    print("""
     ___      _        _           
    /   \    (_)    __| |    ___   
    | - |    | |   / _` |   / -_)  
    |_|_|   _|_|_  \__,_|   \___|  
  _|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"| 
   \"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-' 

    Entrez dans la console...

    Pour générer un poème:
    \tstart

    Pour sélectionner un domaine (ou un thème):
    \tDOM=<le domaine>
    \t\t ex : DOM=LIN
    \t\t (le domaine sélectionné est donc "linguistique")
    Pour afficher les domaines, utilisez "show_DOM"

    Pour sélectionner un style de langage:
    \tstyle=<le style>
    \t\t ex : style=p
    \t\t (le style sélectionné est donc "populaire")
    Pour afficher les styles, utilisez "show_style"

    Pour le nombre de lignes:
    \tnb_lignes=<un nombre>
    \t\t ex : nb_lignes=7
    \t\t (une fois "start" lancé, le programme va générer un poème de 7 lignes)
        """)


def show_DOM():

    global DOM_PATH
    DOM_PATH = Path(environ["POETRY_PATH"] + "/M//correspondance_DEM/DOM.csv")

    global DOM
    DOM = open(DOM_PATH, "r",encoding='utf-8')

    global readerDOM
    global sepDOM
    sepDOM = "\t"
    readerDOM = csv.reader(DOM, delimiter=sepDOM)

    print("""
  _____ _                              
 |_   _| |__   ___ _ __ ___   ___  ___ 
   | | | '_ \ / _ \ '_ ` _ \ / _ \/ __|
   | | | | | |  __/ | | | | |  __/\__ \\
   |_| |_| |_|\___|_| |_| |_|\___||___/
                                       
    """)
    for dom in readerDOM:
        print(dom[0] + "\t" + dom[1])

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
        """)
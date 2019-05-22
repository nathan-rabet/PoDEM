from V.affichage import *
from V.visual import *
from C.Modules.Semantique.constructeur_phrase import *
from V.input_user import *
import os 
from os import environ
import shutil


def start(nb_lignes,DOM_input,style,DOM_valeur,style_valeur):

    """
    Commande start : lance la génération du poème
    """
    clear_console()
    options(DOM_input,DOM_valeur,style,style_valeur,nb_lignes)
    print()
    tps_gen(nb_lignes)
    Afficher_phrase(nb_lignes,DOM_input,style)


def help():

    """
    Commande help : permet d'obtenir des indications sur comment utilisé le programme
    """
    clear_console()

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


def show_DOM():

    """
    Commande show_DOM : permet d'obtenir la liste des thèmes disponibles
    """
    clear_console()
    readerDOM = init_DOM()
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

    """
    Commande show_style : permet d'obtenir la liste des styles disponibles
    """
    clear_console()
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



def options(DOM_input,DOM_valeur,style,style_valeur,nb_lignes):

    """
    Commande options : Montre à l'utilisateur les options actifs
    """

    clear_console()
    print("DOM\t" + DOM_input + " (" + DOM_valeur + ")" )
    print("style\t" + style + " (" + style_valeur + ")" )
    print("nb_lignes\t" + str(nb_lignes))
    print()


def sup_cache():

    """
    Supprime le cache du programme 
    """
    path = Path(environ["POETRY_PATH"])
    for(path,dirs,files) in os.walk(path):
        if re.search('__pycache__',path):
            shutil.rmtree(path,ignore_errors=True) 
      
    
def exit():

    """
    Commande exit : permet de quitter le programme
    """
    print("À bientôt pour de nouvelles romances !")    
    on = False
    return on
from V.visual import *
from V.affichage import *
import re
from os import environ
from pathlib import Path
import csv

def transform_DOM():
    init_DOM()
    readerDOM_table = []
    for i in readerDOM:
        readerDOM_table.append(i)
    return readerDOM_table

def init_DOM():

    """ 
    Fonction permettant d'initialiser le fichier DOM.
    """

    global DOM_PATH
    DOM_PATH = Path(environ["POETRY_PATH"] + "/M//correspondance_DEM/DOM.csv")

    global DOM
    DOM = open(DOM_PATH, "r",encoding='utf-8')

    global readerDOM
    global sepDOM
    sepDOM = "\t"
    readerDOM = csv.reader(DOM, delimiter=sepDOM)
    return readerDOM
 

def detec(chercher,cmd_no_space):

    """
    Detecte ce qu'a écrit l'utilisateur
    """

    if chercher == 'start':
        dete = re.match('start',cmd_no_space) and len(cmd_no_space) == len('start')
        return dete
    elif chercher == 'DOM':   
        dete = re.match('DOM=',cmd_no_space)
        return dete
    elif chercher == 'style':        
        dete = re.match('style=',cmd_no_space)
        return dete
    elif chercher == 'nb_lignes':
        dete = re.match('nb_lignes=',cmd_no_space)
        return dete
    elif chercher == 'help':
        dete = re.match('help',cmd_no_space) and len(cmd_no_space) == len('help')
        return dete
    elif chercher == 'exit':
        dete = re.match('exit',cmd_no_space) and len(cmd_no_space) == len('exit')
        return dete
    elif chercher == 'show_DOM':
        dete = re.match('show_DOM',cmd_no_space) and len(cmd_no_space) == len('show_DOM')
        return dete
    elif chercher == 'show_style':
        dete = re.match('show_style',cmd_no_space) and len(cmd_no_space) == len('show_style')
        return dete
    elif chercher == 'options':
        dete = re.match('options',cmd_no_space) and len(cmd_no_space) == len('options')
        return dete



def saisie_nb_lignes(cmd_no_space) :

    """
    Permet de choisir le nombre de ligne du poème
    """

    if len(cmd_no_space) == 10:
        print(error_message("Vous n'avez entré aucun nombre !"))
        print("Pour savoir comment utiliser cette fonctionnalité, tapez : 'help'\n")
        return None
    elif not cmd_no_space[10:].isdigit():
        print(error_message("La donnée que vous venez de rentrer n'est pas un nombre entier !"))
        print("Pour savoir comment utiliser cette fonctionnalité, tapez : 'help'\n")
        return None
    else:
        nbr_l = int(cmd_no_space[10:])
        return nbr_l



def saisie_DOM(cmd_no_space):

    """
    Permet de choisir le thème (DOM) du poème
    """

    DOM_input = None
    DOM_IN = []
    if len(cmd_no_space) == 4 :
        DOM_input = ""
        DOM_valeur = ""
        print(warning_message("Vous n'avez séléctionné aucun thème !"))
        print("Le poème sera donc généré sans contrainte de thème\n")
        DOM_IN = [DOM_input,DOM_valeur] 
        return DOM_IN
    else:
        r = transform_DOM()
        k = 0
        while k < (len(r)):
            if re.search(r[k][0], cmd_no_space):
                DOM_input = r[k][0]
                DOM_valeur = r[k][1]
                break
            k += 1
                
            
        if DOM_input == None:
            print(error_message("Le thème que vous avez saisi n'existe pas dans notre base de donnée !"))
            print("Aucun thème n'est donc appliqué.")
            print("Veuillez saisir un thème correct.")
            print("Pour connaître la liste des thèmes, tapez : 'show_DOM'\n")
            DOM_IN = False
            return DOM_IN
        else:
            print(correct_message('Vous avez renseigné le code "' + DOM_input + '" qui correspond au thème "' + DOM_valeur + '".' ))
            print('Le poème sera donc généré selon le thème "' + DOM_valeur + '".\n')
            DOM_IN = [DOM_input,DOM_valeur] 
            return DOM_IN



def saisie_style(cmd_no_space):

    """
    Permet de choisir le style de langue (style) du poème
    """

    style = None
    if len(cmd_no_space) == 6 :
        style = ""
        style_valeur = ""
        print(warning_message("Vous n'avez séléctionné aucun style de langage !"))
        print("Le poème sera donc généré sans cette contrainte.\n")
        style_IN = [style,style_valeur]
        return style_IN
    else:
        styles_langage = [['f','b','p','v','t','c','s','m','n','d'],['familier','belge','populaire','vieux','littéraire','canadien, québécois', 'suisse','maj/min selon la catégorie (Français, le français)','maj/min selon le sens (administration, l’Administration)', 'nom déposé (Altuglass)']]
        for i in range(0,len(styles_langage[0])):
            if re.search(styles_langage[0][i], cmd_no_space[5:]) and len(cmd_no_space) == 7:
                style = styles_langage[0][i]
                style_valeur = styles_langage[1][i]
                break
        if style == None :
            print(error_message("Le style de langage que vous avez saisi n'existe pas dans notre base de donnée !"))
            print("Aucun style n'est donc appliqué.")
            print("Veuillez saisir un style correct.")
            print("Pour connaître la liste des styles, tapez : 'show_style'\n")
            style_IN = False
            return style_IN
        else:
            print(correct_message('Vous avez renseigné le code "' + style + '" qui correspond au style de langage "' + style_valeur + '".' ))
            print('Le poème sera donc généré selon le style "' + style_valeur + '".\n')
            style_IN = [style,style_valeur]
            return style_IN
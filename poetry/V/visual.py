from C.Modules.Semantique.constructeur_phrase import *
from V.affichage import *
from V.command import *
from V.input_user import *

def startup():

    """
    Démarrage du programme
    """

    on = True
    init_DOM()
    clear_console()
    print(banner())

    # Définitons des valeurs par défaut

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

        if detec('start',cmd_no_space):

            clear_console()
            start(nb_lignes,DOM_input,style,DOM_valeur,style_valeur)
            print("\n")

        elif detec('show_DOM',cmd_no_space):
            show_DOM()
        
        elif detec('show_style',cmd_no_space):
            show_style()

        elif detec('options',cmd_no_space):
            options(DOM_input,DOM_valeur,style,style_valeur,nb_lignes)
        
        elif detec('nb_lignes',cmd_no_space):
            if not saisie_nb_lignes(cmd_no_space) == None : 
                nb_lignes = saisie_nb_lignes(cmd_no_space)
                print(correct_message("Le poème sera composé de " + str(nb_lignes) + " lignes.\n"))
            

        elif detec('DOM',cmd_no_space) and not (detec('start',cmd_no_space) or detec('style',cmd_no_space)) :
            DOM_IN = saisie_DOM(cmd_no_space)
            if DOM_IN :
                DOM_input = DOM_IN[0]
                DOM_valeur = DOM_IN[1]
           
        
        elif detec('style',cmd_no_space) and not (detec('start',cmd_no_space) or detec('DOM',cmd_no_space)) :
            style_IN = saisie_style(cmd_no_space)
            if style_IN :
                style = style_IN[0]
                style_valeur = style_IN[1]


        elif detec('help',cmd_no_space):
            help()

        elif detec('exit',cmd_no_space):
            on = exit()
            sup_cache()
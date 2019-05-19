from os import system

def start():
    on = True
    
    clear_console()
    print(banner())
    print(help_min())
    while on:
        cmd = input("GÉNÉRATEUR DE POÈMES >> ")

def clear_console():
    from sys import platform

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

def help_min():
    h = """
             ___      _        _           
            /   \    (_)    __| |    ___   
            | - |    | |   / _` |   / -_)  
            |_|_|   _|_|_  \__,_|   \___|  
          _|' ' '|_| ' ' '|_|'''|_|' ' '| 
          '`-0-0-''`-0-0-''`-0-0-''`-0-0-' 

    Entrez dans la console...

    Pour générer un poème:
    \tstart

    Pour séléctionner un domaine (ou un thème):
    \tDOM=<le domaine>
    \t\t ex : DOM=LIN
    \t\t (le domaine séléctionné est donc "linguistique")
    Pour afficher les domaines, utilisez "show_DOM"

    Pour séléctionner un style de langage:
    \tstyle=<le style>
    \t\t ex : style=p
    \t\t (le style séléctionné est donc "populaire")
    Pour afficher les styles, utilisez "show_style"

    Pour le nombre de lignes:
    \tnb_lignes=<un nombre>
    \t\t ex : nb_lignes=7
    \t\t (une fois "start" lancé, le programme va générer un poème de 7 lignes)
        """
    return h
print(help_min())
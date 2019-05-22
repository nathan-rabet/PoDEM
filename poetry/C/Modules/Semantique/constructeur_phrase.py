from C.Modules.Parser.DEM_parser import *
from C.Class.Structure.Verbe import *
from C.Modules.Parser.selectionneur_mot import *
from C.Modules.Structure.determinant import *
from random import randint



"""
Mots utiles pour composer les phrases
"""


et,vir,e,pi,pe,pts,sdl,qui ='Et',',',' ','?','!','.','\n','Qui'
MOT_PASSE = ['Hier','Avant hier','Il y a longtemps','Il fut un temps','Quelques années auparavant','Quelques jours auparavant','Quelques heures auparavant','Il y a fort longtemps','Dans le passé',"Dans l'ancien temps"]
    
MOT_FUTUR = ['Demain','Après demain','Quelques années plus tard','Quelques jours plus tard','Quelques heures plus tard','Dans le futur','Bien plus tard','Bien longtemps après','Dans fort longtemps','Dans quelques temps']
QUESTION = ['Pourquoi','Comment','Dans quelle mesure','En quoi','Depuis quand','Depuis combien de temps']


def Afficher_phrase(nb_lignes,dom,style=''):
        
    """
    Affiche les phrases genéré par notre programme.
    """
    
    liste_dom = Liste_DOM(dom)

    LISTE = Nombre_phrase(nb_lignes,liste_dom,style)

    for i in LISTE :
        phrase = i.capitalize()
        print(phrase)
    


def Nombre_phrase(nb_lignes,liste_dom,style) :
        
    """
    Génere le nombre de phrase voulue et les retourne sous forme de tableau.
    """

    a = 0
    Txt = []
    
    while a<nb_lignes :

        Txt.append(Constructeur_phrase(liste_dom,style))
        a=a+1

    return Txt



def Constructeur_phrase(liste_dom,style) :
    
    """
    Selectionne un temps aléatoire et un type de phrase aléatoire.
    """

    temps = ['présent', 'imparfait', 'passé simple', 'futur simple']
    tps = temps[randint(0,3)]
    alea = randint(0,13)

    if alea == 0 :

        phrase=Phrase_intj(liste_dom,style,tps)

    elif alea == 1 :

        phrase=Phrase_prono(liste_dom,style,tps)

    elif alea == 2 :

        phrase=Phrase_bruit1(liste_dom,style,tps)

    elif alea == 3 :

        phrase=Phrase_bruit2(liste_dom,style,tps)

    elif alea == 4 :

        phrase=Phrase_normal(liste_dom,style,tps)

    elif alea == 5 :

        phrase=Phrase_question(liste_dom,style,tps)

    elif alea == 6 :

        phrase=Phrase_normal_futur(liste_dom,style)

    elif alea == 7 :

        phrase=Phrase_normal_passe(liste_dom,style)

    elif alea == 8 :

        phrase=Phrase_excla1(liste_dom,style,tps)

    elif alea== 9 :

        phrase=Phrase_excla2(liste_dom,style,tps)

    elif alea == 10 :

        phrase=Phrase_Vpro1(liste_dom,style,tps)

    elif alea == 11 :

        phrase=Phrase_question2(liste_dom,style,tps)

    elif alea == 12 :

        phrase=Phrase_question3(liste_dom,style,tps)

    elif alea == 13 :

        phrase=Phrase_Vpro2(liste_dom,style,tps)

    return phrase



def Phrase_intj(liste_dom,style,tps):
        
    """
    Un des types de phrase (ex: Bas les pattes, ce repiochage maïsiculteur étrépe ce semoir récoltant.)
    """    


    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style) 
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)
    I = INTER(style)
    V = VerbeM('Vt',N,liste_dom,style,tps)
    
    Phrase = I+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
    return Phrase



def Phrase_bruit1(liste_dom,style,tps):

    """
    Un des types de phrase (ex: Et rataplan, cet ostyak entérorragique théologise.)
    """    

    N = NOM(liste_dom,style)
    Dn = deter_alea(N) 
    ADJn = ADJ(N,liste_dom,style)
    B = BRUIT()
    V = VerbeM('Vi',N,liste_dom,style,tps)
    
    Phrase = et+e+B+vir+e+Dn+N[0]+e+ADJn+e+V+pts
    return Phrase



def Phrase_bruit2(liste_dom,style,tps):

    """
    Un des types de phrase (ex: Et badaboum, ton antiprisme rectangulaire parabolise votre sous-module k-lipschitzien.)
    """    

    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style)
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)
    B = BRUIT()
    V = VerbeM('Vt',N,liste_dom,style,tps)
    
    Phrase = et+e+B+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
    return Phrase



def Phrase_normal(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Une butyrine fromagere délactose un échinon beurrier.)
    """    

    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style)
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)
    V = VerbeM('Vt',N,liste_dom,style,tps)
    
    Phrase = Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
    return Phrase



def Phrase_question(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Pourquoi l'élaïdisation couverturière déconditionne à tel point une drague cyanogène ?)
    """    

    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style)
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)
    ADV_M = ADV_MESURE()
    V = VerbeM('Vt',N,liste_dom,style,tps,'sent')
    
    Phrase = QUESTION[randint(0,5)]+e+Dn+N[0]+e+ADJn+e+V+e+ADV_M+e+Dm+M[0]+e+ADJm+e+pi
    return Phrase

def Phrase_question2(liste_dom,style,tps):

    """
    Un des types de phrase (ex: Qui aigrit sérieusement un estonien spiralé ?)
    """    

    N = NOM(liste_dom,style)
    Dn = deter_alea(N)
    ADJn = ADJ(N,liste_dom,style)
    ADV_M = ADV_MESURE()
    V = VerbeM('Vt',N,liste_dom,style,tps,'sent')
    
    Phrase = qui+e+V+e+ADV_M+e+Dn+N[0]+e+ADJn+e+pi
    return Phrase



def Phrase_normal_futur(liste_dom,style):

    """
    Un des types de phrase (ex:Demain, cette achillée bavaysienne columnisera une chondrogenèse anarithmétique.)
    """    

    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style)
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)
    V = VerbeM('Vt',N,liste_dom,style,'futur simple')
    MOT_F = MOT_FUTUR[randint(0,len(MOT_FUTUR)-1)]
    
    Phrase = MOT_F+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
    return Phrase



def Phrase_normal_passe(liste_dom,style):

    """
    Un des types de phrase (ex:Quelques jours auparavant, le cucurbitin motonautique migraina un lunulé vomérien.)
    """    

    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style)
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)
    tps = ['imparfait','passé simple']
    V = VerbeM('Vt',N,liste_dom,style,tps[randint(0,1)])
    MOT_P = MOT_PASSE[randint(0,len(MOT_PASSE)-1)]
    
    Phrase = MOT_P+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
    return Phrase



def Phrase_excla1(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Étant donné que un potentiel-vecteur protégé affaiblit un gaïac caustique !)
    """    

    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style)
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)    
    C = CONJ()
    V = VerbeM('Vt',N,liste_dom,style,tps)
    
    Phrase = C+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+e+pe
    return Phrase



def Phrase_excla2(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Et le bablah sialophagique reneige )
    """    

    N = NOM(liste_dom,style)
    Dn = deter_alea(N)
    ADJn = ADJ(N,liste_dom,style)
    C = CONJ()
    V = VerbeM('Vi',N,liste_dom,style,tps)   
     
    Phrase =  C+e+Dn+N[0]+e+ADJn+e+V+e+pe
    return Phrase



def Phrase_prono(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Ce linolénate fumant se redésiste audiométriquement par accès !)
    """    

    N = NOM(liste_dom,style)
    Dn = deter_alea(N)
    ADJn = ADJ(N,liste_dom,style)
    ADV_M = ADV_MESURE()
    ADV1 = ADV(liste_dom,style)
    V = VerbeM('Vp',N,liste_dom,style,tps)
    
    Phrase = Dn+N[0]+e+ADJn+e+V+e+ADV_M+e+ADV1+e+pe
    return Phrase



def Phrase_Vpro1(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Tu recritiques la choroïdite gaillarde.)
    """    

    N = NOM(liste_dom,style)
    Dn = deter_alea(N)
    ADJn = ADJ(N,liste_dom,style)
    nbr = ['s','p']
    pers = ['1p','2p','3p']
    nbr = nbr[randint(0,len(nbr)-1)]
    pers = pers[randint(0,len(pers)-1)]
    V = VerbeM('Vt',N,liste_dom,style,tps,'',1,pers,nbr)
    
    Phrase = V+e+Dn+N[0]+e+ADJn+pts
    return Phrase

def Phrase_question3(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Depuis quand une portugaise monocaténaire décote ce bandonéon isobare ?)
    """    

    N = NOM(liste_dom,style)
    M = NOM(liste_dom,style)
    Dn = deter_alea(N)
    Dm = deter_alea(M)
    ADJn = ADJ(N,liste_dom,style)
    ADJm = ADJ(M,liste_dom,style)
    V = VerbeM('Vt',N,liste_dom,style,tps,'')
    
    Phrase = QUESTION[randint(0,5)]+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+e+pi
    return Phrase


def Phrase_Vpro2(liste_dom,style,tps):

    """
    Un des types de phrase (ex:Je réaiguillonne abouliquement la blastogenèse ataxique-télangiectasique.)
    """    

    N = NOM(liste_dom,style)
    Dn = deter_alea(N)
    ADJn = ADJ(N,liste_dom,style)
    ADV1 = ADV(liste_dom,style)
    nbr = ['s','p']
    pers = ['1p','2p','3p']
    nbr = nbr[randint(0,len(nbr)-1)]
    pers = pers[randint(0,len(pers)-1)]
    V = VerbeM('Vt',N,liste_dom,style,tps,'sent',1,pers,nbr)
    
    Phrase = V+e+ADV1+e+Dn+N[0]+e+ADJn+pts

    return Phrase
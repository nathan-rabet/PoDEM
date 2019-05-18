from C.Class.Parser.DEM_parser import *
from random import randint
import csv

def ADJ(nom,dom):
    
    """
    Selectionne un adjectif selon le thème (dom) et l'accord selon le nom (nom)
    """
    ADJ_DOM = DOM(dom)
    ADJ_CA = []
    Accords = ''
    Liste_CA = ['A-','K-','L-','A1','A2','A3','A4','A5','A6','A7','A8','A9']
    a = 0
    while (a<len(Liste_CA)):
        
        CA_def = CA(Liste_CA[a],ADJ_DOM)
        ADJ_CA.append(CA_def) 
        a = a+1
    ADJ_V1 = Cellule_de_la_ligne(ADJ_CA)
    ADJ_V2 = VERIF_MOT(ADJ_V1)
    MOT = ADJ_V2[randint(0,len(ADJ_V2)-1)]
    CA_val = Cellule_de_la_ligne(Trouve_ligne_mot(nom))
    if not CA_val == Liste_CA[0] or Liste_CA[1] or Liste_CA[3] or Liste_CA[5] or Liste_CA[6] or Liste_CA[7] or Liste_CA[9] or Liste_CA[10] :
        Accords = 'e'

    return (MOT + Accords)
     


    


def INTER():

    """
    Selectionne une interjection
    """

    INTERJ_V1 = OP('interj')
    INTERJ_V2 = Cellule_de_la_ligne(INTERJ_V1)
    return INTERJ_V2[randint(0,len(INTERJ_V2)-1)]


def BRUIT() :

    """
    Selectionne une onomathopé(ex:Boum)
    """

    SON = OP('son')
    BRUIT_V1 = CA('-R',SON)
    BRUIT_V2 = Cellule_de_la_ligne(BRUIT_V1)
    return BRUIT_V2[randint(0,len(BRUIT_V2)-1)]

def ADV(dom) :

    """
    Selectionne un adverbe selon le thème(dom)
    """

    ADV_DOM = DOM(dom)
    ADV_V1 = CA('M-',ADV_DOM)
    ADV_V2 = Cellule_de_la_ligne(ADV_V1)
    return ADV_V2[randint(0,len(ADV_V2)-1)]

def ADV_MESURE():

    """
    Selectionne un adverbe de quantité(ex:autant)
    """

    ADVm_CA = CA('M-')
    ADVm_V1 = CONT('mesure',ADVm_CA)
    ADVm_V2 = Cellule_de_la_ligne(ADVm_V1)
    return ADVm_V2[randint(0,len(ADVm_V2)-1)]

def CONJ():

    """
    Selectionne une conjonction(ex:Car)
    """

    CONJ_V1 = CA('Q-')
    CONJ_V2 = Cellule_de_la_ligne(CONJ_V1)
    return CONJ_V2[randint(0,len(CONJ_V2)-1)]


def Verbe(type,nom,dom,op='',pers='3p',nbr='s',tps="présent"):

    """
    Selectionne un verbe selon le thème (dom), le type (type) et l'opérateur (op) et le conjuge selon le type(type), le temps (tps) et la personne (pers,nbr)
    """

    a=1
    while a==1 :
        a = 0
        VER_DOM = DOM(dom)
        VER_V1 = CA(type,VER_DOM)
        if op :
            VER_V2 = OP(op,VER_V1)
        else :
            VER_V2 = VER_V1
        VER_V3 = Cellule_de_la_ligne(VER_V2)
        VER_V4 = VERIF_MOT(VER_V3)
        VER = VER_V4[randint(0,len(VER_V4)-1)]
        CA=Cellule_de_la_ligne(Trouve_ligne_mot(nom))
        if CA == -1 or CA == -5 or CA == -8 :
            genre = 'm'
        elif CA == -2 or CA == -6 or CA == -9 :
            genre = 'f'
        else :
            genre = 'n'
        test = Verbe(VER)
        grp = test.groupe()
        if grp == 1 or grp == 2 :
            VER_F = Verbe_1_ou_2(VER,genre,pers,nbr,tps)
        else :
            VER_F = Verbe_3(VER,pers,nbr,tps)
            if VER_F == '':
                a=1
    if type == 'Vp' :
        if pers == "1p" and nombre == "s":
            pro = "m'"  
        elif pers == "2p" and nombre == "s":
            pro = "t'"  
        elif pers == "3p" and nombre == "s":
            pro = "s'"  
        elif pers == "1p" and nombre == "p":
            pro = "nous "  
        elif pers == "2p" and nombre == "p":
            pro = "vous "  
        elif pers == "3p" and nombre == "p":
            pro = "s'"
        return pro + VER_F
    else :
        return VER_F
 

def Verbe_1_ou_2(mot,genre,pers,nbr,tps,pronom=0) :

    """
    Conjuge les verbes du 1er et 2ème goupe
    """

    test = Verbe(mot)
    VER_F = test.conjuger(pers,nbr,genre,tps,pronom)

    return VER_F 


def Verbe_3(mot,pers,nbr,tps):

    """
    Conjuge les verbes du 3ème goupe
    """

    VERB = []
    VERB_V1 = []
    Verbe_PATH = environ["POETRY_PATH"] + "/M/Verbe_3g.csv"
    Verbe_PATH = Path(Verbe_PATH)
    VERBE_3g = open(Verbe_PATH) 
    Vreader = csv.reader(VERBE_3g)
    for ligne in Vreader: 
        if ligne[0] == mot :
            VERB.append(ligne)
    if VERB == [] :
        vide = ''
        VERBE_3g.close()
        return vide
        
    else:
        for ligne in VERB:
            if ligne[1] == tps :
                VERB_V1.append(ligne)

        if pers == "1p" and nombre == "s":
            case = 2  
        elif pers == "2p" and nombre == "s":
            case = 3  
        elif pers == "3p" and nombre == "s":
            case = 4  
        elif pers == "1p" and nombre == "p":
            case = 5  
        elif pers == "2p" and nombre == "p":
            case = 6  
        elif pers == "3p" and nombre == "p":
            case = 7   
    
        VERB_V2 = VERB_V1[case]
        VERBE_3g.close()
        return VERB_V2
    







"""
Mots utiles pour composer les phrases
"""


Et,Vir,E,Pq,Pi,Pe ='Et',',',' ','Pourquoi','?','!'

MOT_PASSE = ['Hier','Avant hier','Il y a longtemps','Il fut un temps','Quelques années auparavant','Quelques jours auparavant','Quelques heures auparavant','Il y a fort longtemps','Dans le passé',"Dans l'ancien temps"]
    
MOT_FUTUR = ['Demain','Après demain','Quelques années plus tard','Quelques jours plus tard','Quelques heures plus tard','Dans le futur','Bien plus tard','Bien longtemps après','Dans fort longtemps','Dans quelques temps']



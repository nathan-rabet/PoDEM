from C.Class.Parser.DEM_parser import *
from C.Class.Structure.Verbe import *
from random import randint
import csv



def NOM(dom) :
    
    """
    Selectionne un nom selon le thème (dom)
    """

    NOM_DOM = DOM(dom)
    Liste_CA = ['-1','-2','-3','-4','-5','-6','-7','-8','-9']
    NOM_CA = []
    a = 0
    while (a<len(Liste_CA)):
        
        CA_def = CA(Liste_CA[a],NOM_DOM)
        if not CA_def == []:
            for i in CA_def:
                NOM_CA.append(i) 
        a = a+1
    NOM_V1 = Cellule_de_la_ligne(NOM_CA)
    NOM = NOM_V1[randint(0,len(NOM_V1)-1)]
    return NOM





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
        if not CA_def == []:
            for i in CA_def:
                ADJ_CA.append(i) 
        a = a+1
    ADJ_V1 = Cellule_de_la_ligne(ADJ_CA)
    MOT = ADJ_V1[randint(0,len(ADJ_V1)-1)]
    CA_val = Cellule_de_la_ligne([Donne_ligne_numero(Trouve_ligne_mot(nom))],-1)
    if not (CA_val == '-1' or '-3'or '-4' or '-5' or '-7' or '-8') :
        Accords = 'e'

    return (MOT + Accords)
     

   


def INTER():

    """
    Selectionne une interjection
    """

    INTERJ_V1 = OP('intj')
    INTERJ_V2 = Cellule_de_la_ligne(INTERJ_V1)
    return INTERJ_V2[randint(0,len(INTERJ_V2)-1)]


def BRUIT() :

    """
    Selectionne une onomathopé(ex:Boum)
    """

    SON = OP('son')
    BRUIT_V1 = CA('R-',SON)
    BRUIT_V2 = Cellule_de_la_ligne(BRUIT_V1)
    return BRUIT_V2[randint(0,len(BRUIT_V2)-1)]

def ADV(dom) :

    """
    Selectionne un adverbe selon le thème(dom)
    """

    ADV_DOM = DOM(dom)
    ADV_V1 = CA('M-',ADV_DOM)
    if ADV_V1 == []:
        ADV_V1 = CA('M-')
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
    retour = "tout... que"
    while retour == "tout... que":
        CONJ_V1 = CA('Q-')
        CONJ_V2 = Cellule_de_la_ligne(CONJ_V1)
        retour = CONJ_V2[randint(0,len(CONJ_V2)-1)]
    if retour == "puisque P":
        retour = "puisque"

    return retour


def VerbeM(type,nom,dom,op='',pers='3p',nbr='s',tps="présent"):

    """
    Selectionne un verbe selon le thème (dom), le type (type) et l'opérateur (op) et le conjuge selon le type(type), le temps (tps) et la personne (pers,nbr)
    """

    a=1
    while a==1 :
        a = 0
        VER_DOM = DOM(dom)
        VER_V1 = CA(type,VER_DOM)
        if VER_V1 == [] :
            VER_V1 = CA(type) 
        if op :
            VER_V2 = OP(op,VER_V1)
        else :
            VER_V2 = VER_V1
        VER_V3 = Cellule_de_la_ligne(VER_V2)
        VER_V4 = VERIF_MOT(VER_V3)
        VER = VER_V4[randint(0,len(VER_V4)-1)]
        CA_val = Cellule_de_la_ligne([Donne_ligne_numero(Trouve_ligne_mot(nom))],-1)
        if CA_val == -1 or CA_val == -5 or CA_val == -8 :
            genre = 'm'
        elif CA_val == -2 or CA_val == -6 or CA_val == -9 :
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
        PLV = Premiere_lettre_voyelle(VER) 
        if pers == "1p" and nbr == "s":
            if PLV :
                pro = "m'"  
            else :
                pro = 'me '
        elif pers == "2p" and nbr == "s":
            if PLV :
                pro = "t'"  
            else :
                pro = 'te '   
        elif pers == "3p" and nbr == "s":
            if PLV :
                pro = "s'"  
            else :
                pro = 'se '  
        elif pers == "1p" and nbr == "p":
            pro = "nous "  
        elif pers == "2p" and nbr == "p":
            pro = "vous "  
        elif pers == "3p" and nbr == "p":
            if PLV :
                pro = "s'"  
            else :
                pro = 'se '
        return pro + VER_F
    else :
        return VER_F
 

def Verbe_1_ou_2(mot,genre,pers,nbr,tps,pronom=0):

    """
    Conjugue les verbes du 1er et 2ème goupe
    """

    test = Verbe(mot)
    VER_F = test.conjuguer(pers,nbr,genre,tps,pronom)

    return VER_F 


def Verbe_3(mot,pers,nbr,tps):

    """
    Conjugue les verbes du 3ème goupe
    """

    VERB = []
    VERB_V1 = []
    Verbe_PATH = environ["POETRY_PATH"] + "/M/Verbe_3g.csv"
    Verbe_PATH = Path(Verbe_PATH)
    VERBE_3g = open(Verbe_PATH,"r",encoding='utf-8') 
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
            if ligne[1].lower() == tps.lower() :
                VERB_V1.append(ligne)

        if pers == "1p" and nbr == "s":
            case = 2  
        elif pers == "2p" and nbr == "s":
            case = 3  
        elif pers == "3p" and nbr == "s":
            case = 4  
        elif pers == "1p" and nbr == "p":
            case = 5  
        elif pers == "2p" and nbr == "p":
            case = 6  
        elif pers == "3p" and nbr == "p":
            case = 7   
    
        VERB_V2 = VERB_V1[0][case]
        VERBE_3g.close()
        return VERB_V2
    







"""
Mots utiles pour composer les phrases
"""


et,vir,e,pq,pi,pe,sdl ='Et',',',' ','Pourquoi','?','!','\n'

MOT_PASSE = ['Hier','Avant hier','Il y a longtemps','Il fut un temps','Quelques années auparavant','Quelques jours auparavant','Quelques heures auparavant','Il y a fort longtemps','Dans le passé',"Dans l'ancien temps"]
    
MOT_FUTUR = ['Demain','Après demain','Quelques années plus tard','Quelques jours plus tard','Quelques heures plus tard','Dans le futur','Bien plus tard','Bien longtemps après','Dans fort longtemps','Dans quelques temps']










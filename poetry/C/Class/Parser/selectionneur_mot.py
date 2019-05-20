from C.Class.Parser.DEM_parser import *
from C.Class.Structure.Verbe import *
from random import randint
import csv


def NOM(liste_dom,style) :
    
    """
    Selectionne un nom selon le thème (liste_dom) et le style de langue (style)
    """

    NOM_DOM = liste_dom
    if not style == '' :
        NOM_DOM2 = style_langage(style,NOM_DOM)
        if NOM_DOM2 == []  :
            NOM_DOM2 = NOM_DOM 
    else :
        NOM_DOM2 = NOM_DOM        
    Liste_CA = ['-1','-2','-3','-4','-5','-6','-7','-8','-9']
    NOM_CA = []
    a = 0
    while (a<len(Liste_CA)):
        
        CA_def = CA(Liste_CA[a],NOM_DOM2)
        if not CA_def == []:
            for i in CA_def:
                NOM_CA.append(i) 
        a = a+1
    NOM_V1 = NOM_CA[randint(0,len(NOM_CA)-1)]
    CA_NOM = NOM_V1[-1]
    NOM = Cellule_de_la_ligne([NOM_V1])
    NOM_CA = [NOM[0],CA_NOM]
    return NOM_CA





def ADJ(nom,liste_dom,style):
    
    """
    Selectionne un adjectif selon le thème (liste_dom), l'accord selon le nom (nom) et le style de langue (style)
    """
    ADJ_DOM = liste_dom
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
    if not style == '' :
        ADJ_CA2 = style_langage(style,ADJ_CA)
        if ADJ_CA2 == []  :
            ADJ_CA2 = ADJ_CA 
    else :
        ADJ_CA2 = ADJ_CA

    ADJ_V1 = Cellule_de_la_ligne(ADJ_CA2)
    MOT = ADJ_V1[randint(0,len(ADJ_V1)-1)]
    CA_val = nom[1]
    if  not (CA_val == '-1' or CA_val == '-3'or CA_val == '-4' or CA_val == '-5' or CA_val == '-7' or CA_val == '-8') :
        if (MOT[-1] == 'l' and MOT[-2] == 'u') or (MOT[-1] == 'l' and MOT[-2] == 'e') or (MOT[-1] == 'l' and MOT[-2] == 'e' and MOT[-3] == 'i') or (MOT[-1] == 'l' and MOT[-2] == 'i' and MOT[-3] == 'e'):
            Accords = 'le'
        elif MOT[-1] == 'u' and MOT[-2] == 'a' and MOT[-3] == 'e' :
            Accords = 'lle'
            MOT = MOT[0:-2]
        elif MOT[-1] == 'u' and MOT[-2] == 'g' :
            Accords = 'üe'
            MOT = MOT[0:-1]
        elif MOT[-1] == 'r' and MOT[-2] == 'e' and MOT[-3] == 'i' :
            Accords = 'ère'
            MOT = MOT[0:-2]
        elif MOT[-1] == 't' and MOT[-2] == 'e' and MOT[-3] == 'i' :
            Accords = 'ète'
            MOT = MOT[0:-2]
        elif (MOT[-1] == 'n' and MOT[-2] == 'o') or (MOT[-1] == 'n' and MOT[-2] == 'e') or (MOT[-1] == 'n' and MOT[-2] == 'e' and MOT[-3] == 'i'):
            Accords = 'ne'
        elif MOT == 'fou' :
            Accords = ''
            MOT = 'folle'
        elif MOT == 'mou' :
            Accords = ''
            MOT = 'molle'
        elif MOT == 'foufou' :
            Accords = ''
            MOT = 'fofolle'
        elif MOT == 'chou' :
            Accords = ''
            MOT = 'choute'
        elif MOT == 'chouchou' :
            Accords = ''
            MOT = 'chouchoute'
        elif MOT == 'andalou ' :
            Accords = ''
            MOT = 'andalouse'
        elif MOT[-1] == 'u' and MOT[-2] == 'o' :
            Accords = 'e'
        elif MOT == 'antérieur' or MOT == 'extérieur' or MOT == 'inférieur' or MOT == 'intérieur' or MOT == 'majeur' or MOT == 'meilleur' or MOT == 'mineur' or MOT == 'postérieur' or MOT == 'supérieur' or MOT == 'ultérieur' :
            Accords = 'e'
        elif MOT[-1] == 'r' and MOT[-2] == 'u' and MOT[-3] == 'e' and MOT[-4] == 't' :
            Accords = 'rice'
            MOT = MOT[0:-3]
        elif MOT[-1] == 'r' and MOT[-2] == 'u' and MOT[-3] == 'e' :
            Accords = 'se'
            MOT = MOT[0:-1]
        elif MOT == 'chérot' :
            Accords = ''
        elif MOT == 'bigot' or MOT == 'dévot' or MOT == 'fiérot' or MOT == 'idiot' or MOT == 'loupiot' or MOT == 'manchot' or MOT == 'petiot' or MOT == 'poivrot' :
            Accords = 'e'
        elif (MOT[-1] == 't' and MOT[-2] == 'o') or (MOT[-1] == 't' and MOT[-2] == 'e') :
            Accords = 'te'
        elif MOT == 'complet':
            MOT = 'complète'
        elif MOT == 'imcomplet':
            MOT = 'imcomplète'
            Accords = ''
        elif MOT == 'discret':
            MOT = 'discrète'
            Accords = ''
        elif MOT == 'indiscret':
            MOT = 'indiscrète'
            Accords = ''
        elif MOT == 'inquiet':
            MOT = 'inquiète'
            Accords = ''
        elif MOT == 'secret':
            MOT = 'secrète'
            Accords = ''
        elif MOT == 'concret':
            MOT = 'concrète'
            Accords = ''
        elif MOT == 'désuet':
            MOT = 'désuète'
            Accords = ''
        elif MOT == 'faux':
            MOT = 'fausse'
            Accords = ''
        elif MOT == 'roux':
            MOT = 'rousse'
            Accords = ''
        elif MOT == 'doux':
            MOT = 'douce'
            Accords = ''
        elif MOT == 'enchanteur':
            MOT = 'enchanteresse'
            Accords = ''
        elif MOT == 'désenchanteur':
            MOT = 'désenchanteresse'
            Accords = ''       
        elif MOT[-1] == 'x' :
            MOT = MOT[0:-1]            
            Accords = 'se'
        elif MOT[-1] == 'c' :           
            Accords = 'he'
        elif MOT[-1] == 'f' :
            MOT = MOT[0:-1]            
            Accords = 've'
        elif MOT[-1] == 's' :            
            Accords = 'se'
        else :
            if not MOT[-1] == 'e':            
                Accords = 'e'

    return (MOT + Accords)

   


def INTER(style):

    """
    Selectionne une interjection selon le style de langue (style)
    """

    INTERJ_V = OP('intj')
    if not style == '' :
        INTERJ_V1 = style_langage(style,INTERJ_V)
        if INTERJ_V1 == []  :
            INTERJ_V1 = INTERJ_V
    else :
        INTERJ_V1 = INTERJ_V
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

def ADV(liste_dom,style) :

    """
    Selectionne un adverbe selon le thème(dom) et le style de langue (style)
    """
    ADV_V3 = 'à peine... que'
    while ADV_V3 == 'à peine... que' :

        ADV_DOM = liste_dom
        ADV_V = CA('M-',ADV_DOM)
        if ADV_V == []:
            ADV_V = CA('M-')
        if not style == '' :
            ADV_V1 = style_langage(style,ADV_V)
            if ADV_V1 == []  :
                ADV_V1 = ADV_V
        else :
            ADV_V1 = ADV_V
        ADV_V2 = Cellule_de_la_ligne(ADV_V1)
        ADV_V3 = ADV_V2[randint(0,len(ADV_V2)-1)]


    return ADV_V3

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


def VerbeM(type,nom,liste_dom,style,tps="présent",op='',pronom=0,pers='3p',nbr='s'):

    """
    Selectionne un verbe selon le thème (dom), le type (type), l'opérateur (op) et le style de langue (style) et le conjuge selon le type (type), le temps (tps) et la personne (pers,nbr)
    """

    a=1
    while a==1 :
        a = 0
        pron = ''
        VER_V1 = liste_dom
        VER_DOM = CA(type,VER_V1)
        if VER_DOM == [] :
            VER_DOM = CA(type) 
        if op :
            VER_V2 = OP(op,VER_DOM)
            if VER_V2 == [] :
                VER_V2 = VER_DOM        
        else :
            VER_V2 = VER_DOM

        if not style == '' :
            VER_V3 = style_langage(style,VER_V2)
            if VER_V3 == []  :
                VER_V3 = VER_V2
        else :
            VER_V3 = VER_V2
        VER_V4 = Cellule_de_la_ligne(VER_V3)
        VER_V5 = VERIF_MOT(VER_V4)
        VER = VER_V5[randint(0,len(VER_V5)-1)]
        CA_val = nom[1]
        if CA_val == -1 or CA_val == -5 or CA_val == -8 :
            genre = 'm'
        elif CA_val == -2 or CA_val == -6 or CA_val == -9 :
            genre = 'f'
        else :
            genre = 'n'
        test = Verbe(VER)
        grp = test.groupe()
        if grp == 1 or grp == 2 :
            VER_F = Verbe_1_ou_2(VER,genre,pers,nbr,tps,pronom)
            if pronom :
                pron = VER_F[1]
                VER_F = VER_F[0]
        else :
            VER_F = Verbe_3(VER,pers,nbr,tps,genre,pronom)
            if pronom and not VER_F == '':
                pron = VER_F[1]
                VER_F = VER_F[0]
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
        if pron == "j'" :
            pron = 'je '
        return pron+pro + VER_F
    else :
        return pron+VER_F
 

def Verbe_1_ou_2(mot,genre,pers,nbr,tps,pronom):

    """
    Conjugue les verbes du 1er et 2ème goupe
    """

    test = Verbe(mot)
    VER_F = test.conjuguer(pers,nbr,genre,tps,pronom)

    return VER_F 


def Verbe_3(mot,pers,nbr,tps,genre,pronom):

    """
    Conjugue les verbes du 3ème goupe
    """
    if tps == 'passé simple' :
        tps = 'passé composé'
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
            if pronom :
                if Premiere_lettre_voyelle(VERB_V1[0][0]):
                    pron = "j'"
                else :
                    pron = 'je '
        elif pers == "2p" and nbr == "s":
            case = 3  
            if pronom :
                pron = 'tu '
        elif pers == "3p" and nbr == "s":
            case = 4  
            if pronom :
                if genre == 'm':
                    pron = 'il '
                elif genre =='f' :
                    pro = 'elle '
                else :
                    pron = 'on '
        elif pers == "1p" and nbr == "p":
            case = 5  
            if pronom :
                pron = "nous "
                
        elif pers == "2p" and nbr == "p":
            case = 6 
            if pronom :
                pron = "vous "
                 
        elif pers == "3p" and nbr == "p":
            case = 7  
            if pronom :
                if genre == 'm' or genre == 'n':
                    pron = "ils "
                else :
                    pron = 'elles ' 
    
        VERB_V2 = VERB_V1[0][case]
        VERBE_3g.close()
        if not pronom :
            return VERB_V2
        else :
            return [VERB_V2,pron]

    
















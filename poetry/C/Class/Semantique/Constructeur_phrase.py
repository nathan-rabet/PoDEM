from C.Class.Parser.DEM_parser import *
from C.Class.Structure.Verbe import *
from C.Class.Parser.selectionneur_mot import *
from C.Class.Structure.Determinant import *
from random import randint



"""
Mots utiles pour composer les phrases
"""


et,vir,e,pq,pi,pe,pts,sdl ='Et',',',' ','Pourquoi','?','!','.','\n'

MOT_PASSE = ['Hier','Avant hier','Il y a longtemps','Il fut un temps','Quelques années auparavant','Quelques jours auparavant','Quelques heures auparavant','Il y a fort longtemps','Dans le passé',"Dans l'ancien temps"]
    
MOT_FUTUR = ['Demain','Après demain','Quelques années plus tard','Quelques jours plus tard','Quelques heures plus tard','Dans le futur','Bien plus tard','Bien longtemps après','Dans fort longtemps','Dans quelques temps']



def Afficher_phrase(nbr_ligne,dom,style=''):

	LISTE = Nombre_phrase(nbr_ligne,dom,style)
	for i in LISTE :
		phrase = i.capitalize()
		print(phrase)




def Nombre_phrase(nbr_ligne,dom,style) :
	a = 0
	Txt = []
	while a<nbr_ligne :
		Txt.append(Constructeur_phrase(dom,style))
		a=a+1
	return Txt



def Constructeur_phrase(dom,style) :

	temps = ['présent', 'imparfait', 'passé simple', 'futur simple']
	tps = temps[randint(0,3)]

	alea = randint(0,9)

	if alea == 0 :

		phrase = Phrase_intj1(dom,style,tps)

	elif alea == 1 :

		phrase = Phrase_prono(dom,style,tps)

	elif alea == 2 :

		phrase = Phrase_bruit1(dom,style,tps)

	elif alea == 3 :

		phrase = Phrase_bruit2(dom,style,tps)

	elif alea == 4 :

		phrase = Phrase_normal(dom,style,tps)

	elif alea == 5 :

		phrase = Phrase_question(dom,style,tps)

	elif alea == 6 :

		phrase = Phrase_normal_futur(dom,style)

	elif alea == 7 :

		phrase = Phrase_normal_passe(dom,style)

	elif alea == 8 :

		phrase = Phrase_excla1(dom,style,tps)

	elif alea == 9 :

		phrase = Phrase_excla2(dom,style,tps)

	return phrase



def Phrase_intj(dom,style,tps):

	N = NOM(dom,style)
	M = NOM(dom,style) 
	Dn = deter_alea(N)
	Dm = deter_alea(M)
	ADJn = ADJ(N,dom,style)
	ADJm = ADJ(M,dom,style)
	I = INTER(style)
	V = VerbeM('Vt',N,dom,style,tps)
	Phrase = I+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
	return Phrase



def Phrase_bruit1(dom,style,tps):

	N = NOM(dom,style)
	Dn = deter_alea(N) 
	ADJn = ADJ(N,dom,style)
	B = BRUIT()
	V = VerbeM('Vi',N,dom,style,tps)
	Phrase = et+e+B+vir+e+Dn+N[0]+e+ADJn+e+V+pts
	return Phrase



def Phrase_bruit2(dom,style,tps):

	N = NOM(dom,style)
	M = NOM(dom,style)
	Dn = deter_alea(N)
	Dm = deter_alea(M)
	ADJn = ADJ(N,dom,style)
	ADJm = ADJ(M,dom,style)
	B = BRUIT()
	V = VerbeM('Vt',N,dom,style,tps)
	Phrase = et+e+B+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
	return Phrase



def Phrase_normal(dom,style,tps):

	N = NOM(dom,style)
	M = NOM(dom,style)
	Dn = deter_alea(N)
	Dm = deter_alea(M)
	ADJn = ADJ(N,dom,style)
	ADJm = ADJ(M,dom,style)
	V = VerbeM('Vt',N,dom,style,tps)
	Phrase = Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
	return Phrase



def Phrase_question(dom,style,tps):

	N = NOM(dom,style)
	M = NOM(dom,style)
	Dn = deter_alea(N)
	Dm = deter_alea(M)
	ADJn = ADJ(N,dom,style)
	ADJm = ADJ(M,dom,style)
	ADV_M = ADV_MESURE()
	V = VerbeM('Vt',N,dom,style,tps,'sent')
	Phrase = pq+e+Dn+N[0]+e+ADJn+e+V+e+ADV_M+e+Dm+M[0]+e+ADJm+e+pi
	return Phrase



def Phrase_normal_futur(dom,style):

	N = NOM(dom,style)
	M = NOM(dom,style)
	Dn = deter_alea(N)
	Dm = deter_alea(M)
	ADJn = ADJ(N,dom,style)
	ADJm = ADJ(M,dom,style)
	V = VerbeM('Vt',N,dom,style,'futur simple')
	MOT_F = MOT_FUTUR[randint(0,len(MOT_FUTUR)-1)]
	Phrase = MOT_F+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
	return Phrase



def Phrase_normal_passe(dom,style):

	N = NOM(dom,style)
	M = NOM(dom,style)
	Dn = deter_alea(N)
	Dm = deter_alea(M)
	ADJn = ADJ(N,dom,style)
	ADJm = ADJ(M,dom,style)
	tps = ['imparfait','passé simple']
	V = VerbeM('Vt',N,dom,style,tps[randint(0,1)])
	MOT_P = MOT_PASSE[randint(0,len(MOT_PASSE)-1)]
	Phrase = MOT_P+vir+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+pts
	return Phrase



def Phrase_excla1(dom,style,tps):

	N = NOM(dom,style)
	M = NOM(dom,style)
	Dn = deter_alea(N)
	Dm = deter_alea(M)
	ADJn = ADJ(N,dom,style)
	ADJm = ADJ(M,dom,style)	
	C = CONJ()
	V = VerbeM('Vt',N,dom,style,tps)
	Phrase = C+e+Dn+N[0]+e+ADJn+e+V+e+Dm+M[0]+e+ADJm+e+pe
	return Phrase



def Phrase_excla2(dom,style,tps):

	N = NOM(dom,style)
	Dn = deter_alea(N)
	ADJn = ADJ(N,dom,style)
	C = CONJ()
	V = VerbeM('Vi',N,dom,style,tps)	
	Phrase =  C+e+Dn+N[0]+e+ADJn+e+V+e+pe
	return Phrase



def Phrase_prono(dom,style,tps):

	N = NOM(dom,style)
	Dn = deter_alea(N)
	ADJn = ADJ(N,dom,style)
	ADV_M = ADV_MESURE()
	ADV1 = ADV(dom,style)
	V = VerbeM('Vp',N,dom,style,tps)
	Phrase = Dn+N[0]+e+ADJn+e+V+e+ADV_M+e+ADV1+e+pe
	return Phrase





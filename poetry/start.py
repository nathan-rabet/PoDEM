from os import getcwd
import os

os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from C.Class.Parser.DEM_parser import *
from C.Class.Structure.Determinant import *
from C.Class.Parser.selectionneur_mot import *
from C.Class.Semantique.Constructeur_phrase import *
from V.visual import *


#Afficher_phrase(4,'')

b=0
while b<100 :
	liste_dom = DOM('')
	a = VerbeM('Vp','athalamie',liste_dom,'',"présent",'',1,'3p','p')

	print(a)
	b = b+1

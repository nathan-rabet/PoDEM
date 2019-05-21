from os import getcwd
import os

os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from V.visual import *
import re

# C:\Users\dimed\OneDrive\Documents\GitHub\Generateur_POEMES\poetry

#startup()
b = 0

liste_dom = DOM('MAT')
style=''
temps = ['présent', 'imparfait', 'passé simple', 'futur simple']
while b<1000 :
    
    tps = temps[randint(0,3)]
    a = Phrase_normal(liste_dom,style,tps)
    print(a)
    b=b+1
   
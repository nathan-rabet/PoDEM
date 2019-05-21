from os import getcwd
import os
from V.visual import startup

# Définition du chemin absolu du dossier 'poetry/'
os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

# Démarrage du programme
startup()
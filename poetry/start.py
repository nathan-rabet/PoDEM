from os import getcwd
import os
# Définition du chemin absolu du dossier 'poetry/'
os.environ["POETRY_PATH"] = os.path.dirname(os.path.abspath(__file__))

from V.visual import startup

# Démarrage du programme
startup()
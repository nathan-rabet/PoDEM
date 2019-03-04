from os import getcwd
from os import environ
from C.Class.Conjugueur.Verbe import Verbe

environ["POETRY_PATH"] = getcwd() + "/poetry"

txt = Verbe("finir")
print(txt.groupe())
print(txt.conjuguer("2p","p","f","futur",True))
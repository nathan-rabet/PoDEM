from os import environ
from C.Modules.Parser.DEM_parser import *

class Verbe:

    """
    Permet de manipuler des verbes à l'infinitif 
    """

    def __init__(self,txt):
        self.txt = txt.lower()

    def groupe(self):
        """ Permet de savoir dans quel groupe se situe le verbe """

        # Premier groupe
        if self.txt != "aller" and self.txt[-2::] == "er":
            return 1
        # Deuxième groupe
        elif self.txt in open(environ["POETRY_PATH"] + "/M//listes_verbes/vb2g.txt").read():
            return 2
        #Troisième groupe
        else:
            return 3

    def pp_radical(self):
        """ Permet de donner le radical du participe passé d'un verbe """
        
        # Si premier groupe
        if self.groupe() == 1:
            self.pp_r = list(self.txt)
            self.pp_r.pop(-1)
            self.pp_r[-1] = "é"
            self.pp_r = "".join(self.pp_r)
            return self.pp_r
        
        # Sinon si deuxième groupe
        elif self.groupe() == 2:
            self.pp_r = list(self.txt)
            self.pp_r.pop(-1)
            self.pp_r[-1] = "i"
            self.pp_r = "".join(self.pp_r)
            return self.pp_r
        
        # Sinon si troisième groupe
        elif self.groupe() == 3:
            # Base de données de conjougaison irrégulière à compléter par Marvin ou Mehdi
            # Tableau Excel dans poetry/M/vb3g_conj.xlsx
            return None
        
    def conjuguer(self, pers="1p", nombre="s", genre="m", temps="présent", pronom=True):
        """ 
        Permet de conjuguer un verbe 

        temps => temps souhaité : présent, imparfait, passé simple, futur simple

        pers => 1p ou 2p

        genre => m ou f ou n (neutre)

        nombre => s ou p
        """

        if self.groupe() == 1:
            
            verbe_radical = self.txt[0:-2]            
            
            # Présent
            if temps == "présent":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "e"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "es"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "e"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "ons"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "ez"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "ent"
            

            # Imparfait
            if temps == "imparfait":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "ais"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "ais"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "ait"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "ions"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "iez"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "aient"


            # Passé simple
            if temps == "passé simple":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "ai"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "as"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "a"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "âmes"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "âtes"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "èrent"

            # Futur
            if temps == "futur simple":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "erai"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "eras"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "era"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "erons"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "erez"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "eront"

        if self.groupe() == 2:
            
            verbe_radical = self.txt[0:-2]

            # Présent
            if temps == "présent":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "is"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "is"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "it"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "issons"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "issez"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "issent"
            

            # Imparfait
            if temps == "imparfait":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "issais"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "issais"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "issait"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "issions"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "issiez"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "issaient"


            # Passé simple
            if temps == "passé simple":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "is"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "is"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "it"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "îmes"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "îtes"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "irent"

            # Futur
            if temps == "futur simple":
                # 1p singulier
                if pers == "1p" and nombre == "s":
                    verbe_radical += "irai"

                # 2p singulier
                elif pers == "2p" and nombre == "s":
                    verbe_radical += "iras"
                
                # 3p singulier
                elif pers == "3p" and nombre == "s":
                    verbe_radical += "ira"
                
                # 1p pluriel
                elif pers == "1p" and nombre == "p":
                    verbe_radical += "irons"
                
                # 2p pluriel
                elif pers == "2p" and nombre == "p":
                    verbe_radical += "irez"
                
                # 3p pluriel
                elif pers == "3p" and nombre == "p":
                    verbe_radical += "iront"
        
        if self.groupe() == 3:
            pass
        
        # Concaténation avec le pronom
        if pronom:
            if pers == '1p':
                if nombre == "s":
                    if Premiere_lettre_voyelle(verbe_radical):
                        pronom = "j'"
                    else:
                        pronom = "je "
                elif nombre == "p":
                    pronom = "nous "
            elif pers == '2p':
                if nombre == "s":
                        pronom = "tu "
                elif nombre == "p":
                    pronom = "vous "
            elif pers == "3p":
                if nombre == "s":
                    if genre == "m":
                        pronom = "il "
                    elif genre == "f":
                        pronom = "elle "
                    elif genre == "n":
                        pronom = "on "
                elif nombre == "p":
                    if genre == "m" or genre == "n":
                        pronom = "ils "
                    elif genre == "f":
                        pronom = "elles "

            verbe_radical = [verbe_radical,pronom]
        
        return verbe_radical

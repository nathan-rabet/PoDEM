from os import environ
import csv

class Semantique:
 
    __DEM_PATH = environ("POETRY_PATH") + "/M/DEM.csv"
    __DEM = open(__DEM_PATH)
    
    @staticmethod
    def DOM(self, DOM):
        filtered = []
        for ligne in open(self.__DEM_PATH):
            if ligne[7] == DOM:
                filtered.append(ligne)
        return filtered

    @staticmethod
    def OP(self, OP):
        filtered = []
        for ligne in open(self.__DEM_PATH):
            if ligne[8] == OP:
                filtered.append(ligne)
        return filtered
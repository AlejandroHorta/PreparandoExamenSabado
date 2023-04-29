from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__nombre =None
        self.__casamotor = None
        self.__pilotoPrincipal = Piloto()
        self.__pilotosSecundario = Piloto ()
        self.__costos =  None

@property
def nombre(self):
    return self.__nombre

@nombre.setter
def nombre(self,dato):
        self.__nombre = dato

@property
def casamotor(self):
    return self.__casamotor

@casamotor.setter
def casamotor(self,dato):
        self.__casamotor = dato


@property
def pilotoPrincipal(self):
    return self.__pilotoPrincipal

@pilotoPrincipal.setter
def casamotor(self,dato):
        self.__pilotoPrincipal = dato

@property
def pilotosSecundario(self):
    return self.__pilotosSecundario

@pilotosSecundario.setter
def pilotosSecundario(self,dato):
        self.__pilotosSecundario = dato

@property
def costos(self):
    return self.__costos

@costos.setter
def costos(self,dato):
        self.__costos = dato




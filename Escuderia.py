from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__nombre = None
        self.__casaMotor = None
        self.__pilotoPrincipal = Piloto()
        self.__pilotoSecundario = Piloto()
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,dato):
        self.__nombre = dato

    @property
    def casaMotor(self):
        return self.__casaMotor

    @casaMotor.setter
    def casaMotor(self,dato):
        self.__casaMotor = dato

    @property
    def pilotoPrincipa(self):
        return self.__pilotoPrincipal

    @pilotoPrincipa.setter
    def pilotoPrincipa(self,dato):
        self.__pilotoPrincipal = dato

    @property
    def pilotoSecundario(self):
        return self.__pilotoSecundario

    @pilotoSecundario.setter
    def pilotoSecundario(self,dato):
        self.__pilotoSecundario = dato
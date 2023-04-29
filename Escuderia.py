from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__name = None
        self.__casaMotor = None
        self.__pilotoPrincipal = Piloto()
        self.__pilotoSecundario = Piloto()
        self.__costos = None

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, dato):
        self.__name = dato
    
    @property
    def casaMotor(self):
        return self.__casaMotor
    
    @casaMotor.setter
    def casaMotor(self, dato):
        self.__casaMotor = dato
    
    @property
    def pilotoPrincipal(self):
        return self.__pilotoPrincipal
    
    @pilotoPrincipal.setter
    def pilotoPrincipal(self, dato):
        self.__pilotoPrincipal = dato
    
    @property
    def pilotoSecundario(self):
        return self.__pilotoSecundario
    
    @pilotoSecundario.setter
    def pilotoSecundario(self, dato):
        self.__pilotoSecundario = dato

    @property
    def costos(self):
        return self.__costos
    
    @costos.setter
    def costos(self, dato):
        self.__costos = dato
    
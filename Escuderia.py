from Piloto import Piloto 

class Escuderia:
    def __init__(self):
        self.__nombre=None
        self.casaMotor=None
        self.pilotoPrincipal=Piloto()
        self.pilotoSegundario=Piloto()


    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato


    @property
    def casaMotor (self):
        return self.__casaMotor
    
    @casaMotor.setter
    def casaMotor(self,dato):
        self.__casaMotor=dato


    @property
    def pilotoPrincipal (self):
        return self.__pilotoPrincipal
    
    @pilotoPrincipal.setter
    def pilotoPrincipal(self,dato):
        self.__pilotoPrincipal=dato
        
    
    @property
    def pilotoSegundario (self):
        return self.__pilotoSegundario
    
    @pilotoSegundario.setter
    def pilotoSegundario(self,dato):
        self.__pilotoSegundario=dato
        
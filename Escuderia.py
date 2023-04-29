from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__nombre= None
        self.__casaMotor = None
        self.__pilotoPrincipal= Piloto()
        self.__piloto2= Piloto()
        self.__costos= None
        

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def CasaMotor(self):
        return self.__casaMotor
    
    @property
    def PilotoPrincipal(self):
        return self.__pilotoPrincipal
    
    @property
    def Piloto2(self):
        return self.__piloto2
    
    @property
    def Costos(self):
        return self.__costos
    
    @nombre.setter
    def nombre(self,dato):
        self.__nombre = dato

    @casamotor.setter
    def CasaMotor(self,dato):
        self.CasaMotor = dato

    @pilotoprincipal.setter
    def PilotoPrincipal(self,dato):
        self.salarioAnual = dato

    @piloto2.setter
    def Piloto2(self,dato):
        self.Piloto2 = dato

    @costos.setter
    def Costos(self,dato):
        self.costos = dato

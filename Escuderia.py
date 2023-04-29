from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__Nombre=None
        self.__CasaMotor=None
        self.__PilotoPrincipal=Piloto()
        self.__Piloto2=Piloto()
        self.__costos=None

    @property
    def nombre(self):
        return self.nombre
    @property
    def CasaMotor(self):
        return self.CasaMotor

    @property
    def PilotoPrincipal(self):
        return self.PilotoPrincipal
    @property
    def Piloto2(self):
        return self.Piloto2
    @property
    def costos(self):
        return self.costos
    #______________________________
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato

    @CasaMotor.setter
    def CasaMotor(self,dato):
        self.__CasaMotor=dato

    @PilotoPrincipal.setter
    def PilotoPrincipal(self,dato):
        self.__PilotoPrincipal=dato
    
    @Piloto2.setter
    def Piloto2(self,dato):
        self.__Piloto2=dato
    
    @costos.setter
    def costos(self,dato):
        self.__costos=dato
    






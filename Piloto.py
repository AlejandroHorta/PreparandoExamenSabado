class Piloto:
    def __init__(self):
        self.__nombre= None
        self.__fechaNacimiento= None
        self.__salarioAnual= None
        self.__Pais= None
    # _________________________________   
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def fechaNacimiento(self):
        return self.nombre
    @property
    def salarioAnual(self):
        return self.nombre
    @property
    def Pais(self):
        return self.nombre
    
    #_______________________________________
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato

    @nombre.setter
    def nombre(self,dato):
        self.__fechaNacimiento=dato

    @nombre.setter
    def nombre(self,dato):
        self.__salarioAnual=dato

    @nombre.setter
    def nombre(self,dato):
        self.__Pais=dato
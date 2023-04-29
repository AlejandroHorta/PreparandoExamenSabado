from Piloto import Piloto

class Escuderia:
    def __init__(self):
      self.__name = None
      self.__type = None
      self.__pilotMain = Piloto()
      self.__pilotTwo = Piloto()
      self.__value = None
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, data):
        self.__name = data
        
        
    @property
    def type(self):
     return self.__type
    
    @type.setter
    def type(self, data):
        self.__type = data
    
    
    @property
    def pilotMain(self):
     return self.__pilotMain
    
    @pilotMain.setter
    def pilotMain(self, data):
        self.__pilotMain = data
     
     
    @property
    def pilotTwo(self):
     return self.__pilotTwo
    
    @pilotTwo.setter
    def pilotTwo(self, data):  
        self.__pilotTwo = data    
    
    @property
    def value(self):
     return self.__value
    
    @value.setter
    def value(self, data):  
        self.__value = data
        
    
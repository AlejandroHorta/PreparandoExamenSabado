class Piloto:
  def __init__(self) -> None:
    self.__name = None
    self.__dateStart = None
    self.__salary = None
    self.__country = None

  @property
  def name(self):
   return self.__name
 
  @name.setter
  def name(self, data):
    self.__name = data
 
    
  @property
  def dateStart(self):
   return self.__dateStart
 
  @dateStart.setter
  def dateStart(self, data):
    self.__dateStart = data
 
  
  @property
  def salary(self):
   return self.salary
 
  @salary.setter
  def salary(self, data):
    self.salary = data
 
  
  @property
  def country(self):
   return self.country
 
  @country.setter
  def country(self, data):
    self.country = data
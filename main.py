from Escuderia import Escuderia

listEscuderias = []
n=1
nroEscuderias = int(input("Type number of escuderias"))
while n <= nroEscuderias:
    n+= 1
    escuderia = Escuderia()
    escuderia.name = input("Type name of escuderia")
    escuderia.type = input("Type the type of esdueria")
    escuderia.pilotMain.name = input("Write the name of the pilot")
    escuderia.pilotMain.dateStart = input("Write the date start")
    escuderia.pilotMain.salary = input("Write the salary")
    escuderia.pilotMain.country = input("Write the country")
    escuderia.pilotTwo = input("type the name of the piloto two")
    escuderia.value = input("type the value")
         
listEscuderias.append(escuderia)
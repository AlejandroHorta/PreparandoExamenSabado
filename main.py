from Escuderia import Escuderia
from Piloto import Piloto

escuderias = []
numEscuderias = int(input('Digita el número de escuderias: '))
count = 0

while count < numEscuderias:
    escuderia = Escuderia()
    escuderia.name = input('Digite el nombre de la escuderias: ')
    escuderia.casaMotor = input('Digite el nombre de la casa motor: ')
    escuderia.pilotoPrincipal.nombre = input('Digite el nombre del piloto: ')
    escuderia.pilotoPrincipal.salarioAnual= input('Digite el monto que gana anualmente: ')
    escuderia.pilotoSecundario.nombre= input('Digite el nombre del copiloto: ')
    escuderia.pilotoSecundario.salarioAnual= input('Digite el monto que gana anualmente: ')
    escuderia.costos = input('Ingrese los costos: ')
    count += 1
    
    escuderias.append(escuderia)
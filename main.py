from Escuderia import Escuderia

escuderias = []
contador = 1

numeroEscuderias = int(input("¿Cuántas escuderías hay esta temporada? "))

while contador < numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre = input("Digite el nombre de la escudería. ")
    escuderia.casaMotor = input("Digite el nombre de la casa motor. ")
    escuderia.pilotoPrincipal.nombre = input("Digite el nombre del piloto principal. ")
    escuderia.pilotoPrincipal.salarioAnual = input("Digite el salario del piloto principal. ")
    escuderia.pilotoPrincipal.Pais = input("Digite el País] del piloto principal. ")
    escuderia.piloto2.nombre = input("Digite el nombre del piloto 2. ")
    escuderia.costos = input("Digite costos. ")

    contador += 1

    escuderias.append(escuderia)

#Recorriendo la lista de escuderias
for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)

costoMayor = 0
nombreEscuderiaMasCara = None

for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        nombreEscuderiaMasCara = escuderia.nombre

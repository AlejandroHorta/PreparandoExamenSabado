from Escuderia import Escuderia

contador = 1

escuderias = []
numeroEscuderias = int(input("Digita el numero de escuderia: "))

while contador < numeroEscuderias:
    escuderia=Escuderia()
    escuderias.nombre=input("Digite el nombre de la escuderia: ")
    escuderias.casaMotor=input("Digite el nombre dela casa motor: ")
    escuderias.pilotoPrincipal.nombre=input("Digite el nombre del piloto: ")
    escuderias.pilotoPrincipal.salarioAnual=input("Digite el salario del piloto: ")
    escuderias.pilotoPrincipal.fechaNacimiento=input("Digite la fecha de nacimiento del piloto: ")
    escuderia.pilotoPrincipal.Pais=input("Digite el pais de origen del piloto: ")
    escuderias.pilotoSegundario.salarioAnual=input("Digite el salario del piloto Segundario: ")
    escuderias.pilotoSegundario.fechaNacimiento=input("Digite la fecha de nacimiento del piloto Segundario: ")
    escuderia.pilotoSegundario.Pais=input("Digite el pais de origen del piloto Segundario: ")
    escuderia.costos=input("Digite los cosotos")

    escuderia.append(escuderia)
    contador = contador +                       1 


#Recorriendo la lista de escuderias

for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)


costoMayor = 0 
nombreEscuderiaMasCara = 0

for escuderia in escuderia:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
    nombreEscuderiaMasCara = escuderia.costos

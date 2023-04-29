from Escuderia import Escuderia

escuderias = []
contador = 1
numeroEscuderias = int(input("Digite el numero de escuderias: "))
while contador <= numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre = input("Digita el nombre de la escuderia: ")
    escuderia.casaMotor = input("Digita el nombre del casamotor: ")
    escuderia.pilotoPrincipal.nombre = input("Digita el nombre del piloto pricipal: ")
    escuderia.pilotoPrincipal.salarioAnual = input("Digita el salario: ")
    escuderia.pilotoPrincipal.fechaNacimiento = input("Digita la fecha de nacimiento: ")
    escuderia.pilotoPrincipal.pais = input("Digita el pais: ")
    escuderia.pilotoSecundario.nombre = input("Digita el nombre del piloto secundario: ")
    escuderia.pilotoSecundario.salarioAnual = input("Digita el salario: ")
    escuderia.pilotoSecundario.fechaNacimiento = input("Digita la fecha de nacimiento: ")
    escuderia.pilotoSecundario.pais = input("Digita el pais del piloto: ")
    escuderia.costos = input("ingrese los costos: ")
    
    escuderias.append(escuderia)
    contador += 1

# Recorriendo la Lista de escuderías

for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)

costoMayor = 0
escuderiaMasCara = None

for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        escuderiaMasCara = escuderia.nombre

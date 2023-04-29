from Escuderia import Escuderia

escuderias=[]
contador = 1
numeroEscuderias = int (input("Digita el número de escuderias: "))

while contador < numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre = input("Digite el nombre del escudero: ")
    escuderia.CasaMotor = input("Digite el nombre de la casa motor: ")
    escuderia.PilotoPrincipal.nombre = input("Digite el nombre del piloto: ")
    escuderia.PilotoPrincipal.fechaNacimiento = input("Digite la fecha del nacimiento del piloto: ")
    escuderia.PilotoPrincipal.salarioAnual = int(input("Digite el salario anual del piloto: "))
    escuderia.PilotoPrincipal.pais = input("Digite el pais del piloto: ")
    escuderia.Piloto2.nombre = input("Digite el nombre del piloto 2: ")
    escuderia.Piloto2.fechaNacimiento = input("Digite la fecha de nacimiento del piloto 2: ")
    escuderia.Piloto2.salarioAnual = int(input("Digite el salario anual del piloto 2: "))
    escuderia.Piloto2.pais = input("Digite el pais del piloto 2: ")
    escuderia.Costos = int(input("Digite el valor de los costos: "))

    escuderias.append(escuderia)
    contador = contador + 1
for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)

costoMayor = 0
nombreEscuderiaMascara = None
for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
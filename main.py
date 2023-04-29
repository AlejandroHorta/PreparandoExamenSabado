from Escuderia import Escuderia

escuderias = []
numeroEscuderias = int(input("Digite el numero de escuderias: "))
contador = 1
while contador <=  numeroEscuderias:
    escuderia= Escuderia()
    escuderia.nombre = input("Digite el nombre  de la escuderia")
    escuderia.casamotor = input("Digite el nombre de la casamotor")
    escuderia.pilotoPrincipal.nombre = input("Digite el nombre de la piloto")
    escuderia.pilotoPrincipal.fechaNacimiento = input("Digite la fecha de nacimiento del piloto")
    escuderia.pilotoPrincipal.salarioAnual = input("Digite el salario del piloto")
    escuderia.pilotoPrincipal.pais = input("Digite el pais del piloto")
    escuderia.pilotosSecundario.nombre = input("Digite el nombre  dos de la piloto")
    escuderia.pilotosSecundario.fechaNacimiento = input("Digite la fecha de nacimiento del piloto 2")
    escuderia.pilotosSecundario.salarioAnual = input("Digite el salario del piloto 2")
    escuderia.pilotosSecundario.pais = input("Digite el pais del piloto 2")
    escuderia.costos = input("Digite el costo de la escuderia")
    escuderias.append(escuderia)
    contador = contador + 1

#recorriendo la lista de escuderias
for escuderias in escuderias:
    print(escuderia.nombre,escuderia.costos)

costoMayor = 0
nombreEscuderiaCara = None
for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        nombreEscuderiaCara = escuderia.nombre
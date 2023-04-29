from Escuderia import Escuderia

escuderias=[]
contador=1
numeroEscuderias = int(input("Digite el numero de escuderias: "))
while contador <= numeroEscuderias:
    escuderia=Escuderia()
    escuderia.nombre= input("digite el nombre de la escuderia")
    escuderia.casaMotor= input("digite el nombre del casamotor")
    escuderia.pilotoPrincipal.nombre= input("digita el nombre del piloto")
    escuderia.pilotoPrincipal.salarioAnual=input("digita el salario")
    escuderia.pilotoPrincipal.fechaNacimiento=input("digita la fecha de nacimiento")
    escuderia.pilotoPrincipal.Pais=input("digita el pais")
    escuderia.piloto2.nombre=input("digita el nombre del piloto")
    escuderia.piloto2.salarioAnual=input("digita el salario")
    escuderia.piloto2.fechaNacimiento=input("digita la fecha de nacimiento")
    escuderia.piloto2.Pais=input("digita el pais del piloto")
    escuderia.costos= input("ingrese los costos")


    escuderias.append(escuderia)
    contador = contador + 1
#recorriendo la lista de escuderias
for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)

costoMayor=0    
nombreEscuderiaMascara=None
for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor= escuderia.costos
        nombreEscuderiaMascara = escuderia.nombre
        
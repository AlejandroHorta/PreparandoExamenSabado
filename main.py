from Escuderia import Escuderia

Escuderias=[]
numeroEscuderias=int(input("Digita el numero de escuderias: "))

contador=1
while contador<= numeroEscuderias:
    escuderia=Escuderia()
    escuderia.nombre=input('Digite el nombre de la escuderia: ')
    escuderia.CasaMotor=input('Digite el nombre de la casa motor: ')
    escuderia.PilotoPrincipal.nombre=input('Digite el nombre del piloto: ')
    escuderia.PilotoPrincipal.salarioAnual=input('Digite el salario anual: ')
    escuderia.PilotoPrincipal.fechaNacimiento=input('Digite la fecha de nacimiento: ')
    escuderia.PilotoPrincipal.Pais=input('Digite el pais')
    escuderia.Piloto2.nombre=input('Digite el nombre del piloto: ')
    escuderia.Piloto2.salarioAnual=input('Digite el salario anual: ')
    escuderia.Piloto2.fechaNacimiento=input('Digite la fecha de nacimiento: ')
    escuderia.Piloto2.Pais=input('Digite el pais')
    escuderia.costos=input('Ingrese los costos ')

    
   
Escuderias.append(escuderia)   
contador=contador+1

# RECORRIENDO LAS LISTA DE ESCUDERIAS 
for escuderia in Escuderias:
    print(escuderia.nombre,escuderia.costos)

costoMayor=0
nombreEscuderiaCara=None
for escuderia in Escuderias:
    if escuderia.costos> costoMayor:
        costoMayor=escuderia.costos
        nombreEscuderiaCara=escuderia.nombre
    
    





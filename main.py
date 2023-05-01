from Escuderia import Escuderia

escuderias=[]
contador=1
numeroEscuderias=int(input('digite el numero de escuderias :'))
while contador <  numeroEscuderias:
   contador=contador +1
   escuderia=Escuderia()
   escuderia.nombre=input("digite nombre de la escuderia :")
   escuderia.casaMotor=input("digite nombre de la  casa Motor :")
   escuderia.pilotoPrincipal.nombre=input("digite nombre del piloto pricipal :")
   escuderia.pilotoPrincipal.salarioAnual=input("digite el eslario :")
   escuderia.pilotoPrincipal.fechaNacimiento=input("digita la fecha de nacimiento :")
   escuderia.pilotoPrincipal.pais=input("digite el pais :")
   escuderia.piloto2.nombre=input("digite nombre :")
   escuderia.piloto2.salarioAnual=input("digite salario :")
   escuderia.piloto2.fechaNacimiento=input("digite fecha :")
   escuderia.piloto2.pais=input("digite pais :")
   escuderia.costos=int(input("digite volor de los costos :"))
   
   escuderias.append(escuderia)
   
#RECORRIENDO LA LISTA DE ESCUDERIA
for escuderia in escuderias:
 print(escuderia.nombre,escuderia.costos)
 
 costoMayor=0
 nombreEscuderiaMasCara=None   
 if escuderia.costos> costoMayor:
       costoMayor=escuderia.costos
       nombreEscuderiaMasCara=escuderia.nombre
       


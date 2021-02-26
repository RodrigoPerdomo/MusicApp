# Aplicacion por consola que trata sobre Musica, en la que te indica la cantidad de canciones que el usuario ingresa y cuanto tiempo dura el Disco en total.

DuracionDisco=0.00
CantidadCanciones=0
Canciones=[]

print("***************************")
print("Ingrese el nombre del Disco")
print("***************************")
nombreDisco=input()
print("**************************************")
print("Desea agregar una cancion al disco S/N")
print("**************************************")
respuesta=input()
while respuesta == "s" or respuesta== "S":
    print("****************************")
    print("Ingrese nombre de la cancion")
    print("****************************")
    nombreCancion=input()
    Canciones.append(nombreCancion)
    CantidadCanciones+=1
    if nombreCancion !="":
        print("******************************")
        print("Ingrese duracion de la cancion")
        print("******************************")
        DuracionCancion=float(input())
        if DuracionCancion >0:
            DuracionDisco+=DuracionCancion
    print("**************************************")
    print("Desea agregar una cancion al disco S/N")
    print("**************************************")
    respuesta=input()
else:
    print("El nombre del Disco es: ",nombreDisco)
    print("Las canciones que ingreso son: ",Canciones)
    print("La cantidad de las canciones es de: ", CantidadCanciones)
    print("El tiempo total del Disco es de: ",DuracionDisco)
    print("Gracias por utilizar mi App <3 !!")
    

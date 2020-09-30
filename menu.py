
#Crear menú con tres opciones: 
#1. Opcion 1: Temperaturas
#2. Opcion 2: Datos de Personas
#3. Opción 3: Salir 
import os 

def Temperaturas():                         #definición de función
    print("****** TEMPERATURAS *****")
    #Ingresar n temperaturas donde n es un numero ingresado por teclado 
    #mostrar el promedio de las temperaturas ingresadas
    suma=0
    veces=int(input("Cuantas temperaturas necesita ingresar?: "))
    for x in range(veces):
        tempe=float(input("Digite una temperatura: "))
        suma=suma+tempe
    
    print("El promedio de las temperaturas ingresadas es: " , round((suma/veces),2))

    pausa=input("Presione una tecla para continuar")

def Personas():
    print("****** DATOS DE PERSONAS ******")

    pausa=input("Presione una tecla para continuar")

seguir=True 
while seguir:
    os.system('cls')
    print ("1. Temmperaturas")
    print ("2. Datos de Personas")
    print ("3. Salir")
    op=int(input("Ingrese opción 1,2,3: "))
    if(op==1):
        Temperaturas()          #invocar o llamar a una función
    elif (op==2):
        Personas()
    else:
        print("Finalizar")
        break
     
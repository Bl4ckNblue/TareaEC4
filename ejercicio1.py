from math import pi 
def areas_figura (f):
    while True:
        figura = input(f)
        if figura == "1":
            radio = int(input("Ingrese el radio del circulo: "))
            areaci = pi*(radio**2)
            return areaci
        elif figura == "2":
            ladocu = int(input("Ingrese el lado del cuadrado: "))
            areacua = ladocu*ladocu
            return areacua    
        elif figura == "3":
            largo = int(input("Ingrese el largo del rectangulo: "))
            ancho = int(input("Ingrese el ancho del rectangulo: "))
            arearec = largo*ancho
            return arearec
        elif figura == "4":
            base = int(input("Ingrese la base del triangulo: "))
            altura = int(input("Ingrese la altura del triangulo: "))
            areatri = (base*altura)/2
            return areatri
        elif figura == "5":
            basema = int(input("Ingrese la base superior: "))
            baseme = int(input("Ingrese la base inferior: "))
            altu = int(input("Ingrese la altura del trapecio: "))
            areatra = (basema+baseme)*altu/2
            return areatra
        else:
            print ("Ingrese un nombre de figura valido")


        
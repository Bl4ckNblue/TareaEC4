from math import pi
def area_circulo ():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio <= 0:
                print ("El valor no puede ser 0. Intente nuevamente")
            else:
                areaci = pi*(radio**2)
                return areaci
        except ValueError:
            print ("ERROR: Debe ingresar un número")
            
def area_cuadrado ():
    while True:
        try:
            ladocu = float(input("Ingrese la longitud del lado del cuadrado: "))
            if ladocu <= 0:
                print ("El valor no puede ser 0. Intente nuevamente")
            else:
                areacua = ladocu*ladocu
                return areacua
        except ValueError:
            print ("ERROR: Debe ingresar un número")
            
def area_rectangulo ():
    while True:
        try:
            largo = float(input("Ingrese la longitud del largo del rectangulo: "))
            ancho = float(input("Ingrese la longitud del ancho del rectangulo: "))
            if largo == ancho or largo == 0 or ancho == 0 :
                print ("El largo y el ancho no pueden ser iguales, ni tampoco pueden ser 0")
            else:
                arearec = largo*ancho
                return arearec
        except ValueError:
            print ("ERROR: Debe ingresar un número")
        
def area_triangulo ():
    while True:
        try:
            base = float(input("Ingrese la longitud de la base del triangulo: "))
            altura = float(input("Ingrese la longitud de la altura del triangulo: "))
            if base == 0 or altura == 0:
                print ("Ninguno de los 2 valores debería ser 0")
            else:
                areatri = (base*altura)/2
                return areatri
        except ValueError:
            print ("ERROR: Debe ingresar un número")
            
def area_trapecio ():
    while True:
        try:
            basema = float(input("Ingrese la longitud de la base superior: "))
            baseme = float(input("Ingrese la longitud de la base inferior: "))
            altura = float(input("Ingrese la longitud de la altura del trapecio: "))
            if basema == 0 or baseme == 0 or altura == 0:
                print ("Ninguno de estos valores debería ser 0")
            elif basema == baseme:
                print ("Estos valores no pueden ser iguales")            
            else:
                areatra = (basema+baseme)*altura/2
                return areatra
        except ValueError:
            print ("ERROR: Debe ingresar un número")

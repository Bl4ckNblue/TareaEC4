from funmath import *
print ("Generador de áreas de figuras geométricas")

inicio = input("\nDesea iniciar? s/n: ")
if inicio == "s":
    while True:
        try:
            print ("\n1.-Circulo \n2.-Cuadrado \n3.-Rectángulo \n4.-Triángulo \n5.-Trapecio")
            areaelegida = int(input("\nIngrese el número de la figura de la cual hallará el área: "))

            while True:
                if areaelegida == 1:
                    ci = area_circulo()
                    print (f"El área del circulo es {ci:.2f}")
                    break
                elif areaelegida == 2:
                    cua = area_cuadrado()
                    print (f"El área del cuadrado es {cua:.2f}")
                    break
                elif areaelegida == 3:
                    rec = area_rectangulo()
                    print (f"El área del rectangulo es {rec:.2f}")
                    break
                elif areaelegida == 4:
                    tri = area_triangulo()
                    print (f"El área del triángulo es {tri:.2f}")
                    break
                elif areaelegida == 5:
                    tra = area_trapecio()
                    print (f"El área del trapecio es {tra:.2f}")
                    break
                else:
                    print ("\nIngrese una opción valida")
                    print ("\n1.-Circulo \n2.-Cuadrado \n3.-Rectángulo \n4.-Triángulo \n5.-Trapecio")
                    areaelegida = int(input("\nIngrese el número de la figura de la cual hallará el área: "))
                
            break
        except ValueError:
            print ("ERROR: Ingrese una opción con caracteres numericos")
else:
    print ("Vuelva pronto")

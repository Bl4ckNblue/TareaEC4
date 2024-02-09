import ejercicio1
print ("Generador de áreas de figuras geométricas")

inicio = input("\nDesea iniciar? y/n: ")
if inicio == "y":
    print ("\nSeleccione el número de la figura de la cual hallará el área: ")
    print ("\n1.-Circulo \n2.-Cuadrado \n3.-Rectángulo \n4.-Triángulo \n5.-Trapecio")
    
    figura = ejercicio1.areas_figura("\n ")
    print (f"El área es {figura:.2f}")
else:
    print ("Gracias, vuelva pronto")
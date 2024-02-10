vocales = ['A','E','I','O','U']
repetir = {}
palabra = input("Ingrese una palabra: ")
for i in palabra.upper():
    if i in vocales:
        if i not in repetir:
            repetir[i] = 1
        else:
            repetir[i] +=1
    else:
        continue
print (repetir)
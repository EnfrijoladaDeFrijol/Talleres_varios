def contarAtras(miNumero): 
    if (miNumero > 0):
        print(miNumero) # Primero imprimimos el valor
        miNumero -= 1 # n = n-1
        contarAtras(miNumero) # Aquí aplicamos recursividad
    else:
        print("Fin de la recursividad")

def contarAtras2(miNumero):
    if (miNumero > 0):
        print(miNumero) # Primero imprimimos el valor
        contarAtras2(miNumero - 1) # Con operación en la función
    else:
        print("Fin de la recursividad 2")

contarAtras(10)
contarAtras2(10) # Mandamos a llamar a la función


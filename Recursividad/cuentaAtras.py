def contarAtras(miNumero): 
    if (miNumero > 0):
        print(miNumero) # Primero imprimimos el valor
        miNumero -= 1 # n = n-1
        contarAtras(miNumero) # Aquí aplicamos recursividad
    else:
        print("Fin de la recursividad")

contarAtras(10) # Mandamos a llamar a la función


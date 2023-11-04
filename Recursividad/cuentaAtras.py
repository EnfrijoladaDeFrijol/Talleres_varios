def contarAtras(miNumero):
    if (miNumero > 0):
        print(miNumero)
        miNumero -= 1 # n = n-1
        contarAtras(miNumero)
    else:
        print("Fin de la recursividad")

contarAtras(10)


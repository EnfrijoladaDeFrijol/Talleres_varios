def calcularFactorial(miNumero):
    if (miNumero == 0 or miNumero == 1): # Caso base
        return 1
    else:
        return miNumero * calcularFactorial(miNumero - 1)

print(calcularFactorial(5))

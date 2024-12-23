 # Operaciones básicas como suma, resta, multiplicación y división

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("División por cero")
    return a / b

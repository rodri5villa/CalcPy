# Operaciones científicas como seno, coseno, tangente, logaritmo y exponencial

import math

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    if math.isclose(math.cos(x), 0, abs_tol=1e-9):
        raise ValueError("Tangente indefinida en este valor")
    return math.tan(x)

def logaritmo(x, base=math.e):
    if x <= 0:
        raise ValueError("Logaritmo definido solo para valores positivos")
    return math.log(x, base)

def exponencial(x):
    return math.exp(x)

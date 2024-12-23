  # Operaciones avanzadas como logaritmos, exponenciales

import math

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial no definido para números no enteros o negativos")
    return math.factorial(n)

def combinaciones(n, k):
    if not (isinstance(n, int) and isinstance(k, int)) or n < k or n < 0 or k < 0:
        raise ValueError("Combinaciones no definidas para estos valores")
    return math.comb(n, k)

def permutaciones(n, k):
    if not (isinstance(n, int) and isinstance(k, int)) or n < k or n < 0 or k < 0:
        raise ValueError("Permutaciones no definidas para estos valores")
    return math.perm(n, k)

def raiz_cuadrada(x):
    if x < 0:
        raise ValueError("Raíz cuadrada no definida para números negativos")
    return math.sqrt(x)

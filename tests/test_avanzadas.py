import pytest
from CalcPy.avanzadas import factorial, combinaciones, permutaciones, raiz_cuadrada

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)  # Factorial no definido para números negativos

def test_combinaciones():
    assert combinaciones(5, 3) == 10
    with pytest.raises(ValueError):
        combinaciones(5, 6)  # n debe ser mayor o igual a k

def test_permutaciones():
    assert permutaciones(5, 3) == 60
    with pytest.raises(ValueError):
        permutaciones(3, 5)  # n debe ser mayor o igual a k

def test_raiz_cuadrada():
    assert raiz_cuadrada(4) == 2.0
    assert raiz_cuadrada(9) == 3.0
    with pytest.raises(ValueError):
        raiz_cuadrada(-1)  # Raíz cuadrada no definida para números negativos

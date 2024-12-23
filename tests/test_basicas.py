import pytest
from CalcPy.basicas import suma, resta, multiplicacion, division

def test_suma():
    assert suma(1, 2) == 3
    assert suma(-1, 2) == 1
    assert suma(-1, -1) == -2

def test_resta():
    assert resta(10, 5) == 5
    assert resta(-1, 2) == -3
    assert resta(-1, -1) == 0

def test_multiplicacion():
    assert multiplicacion(3, 3) == 9
    assert multiplicacion(-1, 2) == -2
    assert multiplicacion(-1, -1) == 1

def test_division():
    assert division(10, 5) == 2
    with pytest.raises(ValueError):
        division(10, 0)  # División por cero
    assert division(-1, -1) == 1
    assert division(-1, 1) == -1

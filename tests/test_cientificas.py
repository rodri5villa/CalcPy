import pytest
import math
from CalcPy.cientificas import seno, coseno, tangente, logaritmo, exponencial

def test_seno():
    assert math.isclose(seno(math.pi / 2), 1.0, abs_tol=1e-9)
    assert math.isclose(seno(math.pi), 0.0, abs_tol=1e-9)

def test_coseno():
    assert math.isclose(coseno(0), 1.0, abs_tol=1e-9)
    assert math.isclose(coseno(math.pi / 2), 0.0, abs_tol=1e-9)

def test_tangente():
    assert math.isclose(tangente(0), 0.0, abs_tol=1e-9)
    with pytest.raises(ValueError):
        tangente(math.pi / 2)  # Tangente indefinida en pi/2

def test_logaritmo():
    assert logaritmo(1) == 0.0
    with pytest.raises(ValueError):
        logaritmo(-1)  # Logaritmo no definido para números negativos

def test_exponencial():
    assert math.isclose(exponencial(1), math.e, abs_tol=1e-9)
    assert exponencial(0) == 1.0

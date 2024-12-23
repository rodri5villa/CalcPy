from .basicas import suma, resta, multiplicacion, division
from .cientificas import seno, coseno, tangente, logaritmo, exponencial
from .avanzadas import factorial, combinaciones, permutaciones, raiz_cuadrada

# Opcionalmente, puedes definir una lista __all__ para controlar qué símbolos
# se importarán cuando se utilice "from src import *"
__all__ = [
    'suma', 'resta', 'multiplicacion', 'division',
    'seno', 'coseno', 'tangente', 'logaritmo', 'exponencial',
    'factorial', 'combinaciones', 'permutaciones', 'raiz_cuadrada'
]

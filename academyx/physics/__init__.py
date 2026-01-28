"""
AcademyX - PHYSICS - Librería Academica para Python
Autor: Emmanuel Ascendra
"""
from .mechanics import Mechanics
from .electromagnetism import Electromagnetism
from .waves import Waves
from .heat import Heat

__all__ = [
    "Mechanics",
    "Electromagnetism",
    "Waves",
    "Heat"
]

# Mensaje de bienvenida (opcional)
def welcome():
    """Muestra información sobre la librería"""
    print(f"Librería Academica - PHYSICS en Python")
    print(f"\nClases disponibles:")
    print(f" - Mechanics")
    print(f" - Electromagnetism")
    print(f" - Waves")
    print(f" - Heat")
    print(f"\nPara más información: help(AcademyX)")
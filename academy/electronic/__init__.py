"""
AcademyX - ELECTRONIC - Librería Academica para Python
Autor: Emmanuel Ascendra
"""
from .circuits import Circuits
from .digital_system import DigitalSystem

__all__ = [
    "Circuits",
    "DigitalSystem"
]

# Mensaje de bienvenida (opcional)
def welcome():
    """Muestra información sobre la librería"""
    print(f"Librería Academica - ELECTRONIC en Python")
    print(f"\nClases disponibles:")
    print(f" - DigitalSystem")
    print(f" - Circuits")
    print(f"\nPara más información: help(AcademyX)")
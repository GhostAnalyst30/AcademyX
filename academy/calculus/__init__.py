"""
AcademyX - CALCULUS - Librería Academica para Python
Autor: Emmanuel Ascendra
"""
from .differential import Differential
from .integral import Integral
from .multivariable import MultiVariable
from .differential_equations import DifferentialEquations

__all__ = [
    "Differential",
    "Integral",
    "MultiVariable",
    "DifferentialEquations"
]

# Mensaje de bienvenida (opcional)
def welcome():
    """Muestra información sobre la librería"""
    print(f"Librería Academica - CALCULUS en Python")
    print(f"\nClases disponibles:")
    print(f" - Differential")
    print(f" - Integral")
    print(f" - MultiVariable")
    print(f" - DifferentialEquations")
    print(f"\nPara más información: help(AcademyX)")
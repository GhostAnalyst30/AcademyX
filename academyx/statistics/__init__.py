"""
AcademyX - STATISTICS - Librería Academica para Python
Autor: Emmanuel Ascendra
"""
from .descriptive import Descriptive
from .inferential import Inferential

__all__ = [
    "Descriptive",
    "Inferential"
]

# Mensaje de bienvenida (opcional)
def welcome():
    """Muestra información sobre la librería"""
    print(f"Librería Academica - STATISTICS en Python")
    print(f"\nClases disponibles:")
    print(f" - Descriptive")
    print(f" - Inferential")
    print(f"\nPara más información: help(AcademyX)")
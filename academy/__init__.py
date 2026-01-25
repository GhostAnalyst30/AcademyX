"""
AcademyX - Librería Academica para Python
Autor: Emmanuel Ascendra
Versión: 0.1.0
"""

__version__ = "0.1.0"
__author__ = "Emmanuel Ascendra"

# Importar las clases principales
from academy.ai.solver import set_openrouter_api
from academy.calculus import Differential, Integral, MultiVariable, DifferentialEquations
from academy.electronic import DigitalSystem, Circuits
from academy.physics import Mechanics, Electromagnetism, Waves, Heat
from academy.statistics import Descriptive, Inferential
from academy.utils import manim_video_steps


# Definir qué se expone cuando se hace: from statslib import *
__all__ = [
    "Differential",
    "Integral",
    "MultiVariable",
    "DifferentialEquations",
    "DigitalSystem",
    "Circuits",
    "Mechanics",
    "Electromagnetism",
    "Waves",
    "Heat",
    "Descriptive",
    "Inferential",
    "set_openrouter_api",
    "manim_video_steps"
]

# Mensaje de bienvenida (opcional)
def welcome():
    """Muestra información sobre la librería"""
    print(f"AcademyX v{__version__}")
    print(f"Librería Academica en Python")
    print(f"Autor: {__author__}")
    print(f"\nClases disponibles:")
    print(f" - Calculus: Differential, Integral, MultiVariable, DifferentialEquations")
    print(f" - Physics: Mechanics, Electromagnetism, Waves, Heat")
    print(f" - Electronic: DigitalSystem, Circuits")
    print(f" - Statistics: Descriptive, Inferential")
    print(f" - Modulos Extras: manim_video_steps, set_openrouter_api")
    print(f"\nPara más información: help(AcademyX)")
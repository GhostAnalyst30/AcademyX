import sympy as sp
from ..utils import to_sympy, manim_video_steps

class Differential:
    def __init__(self, variable='x', api_key=None):
        self.var = sp.symbols(variable)
        self.api_key = api_key

    def derivate(self, expr, order=1, evaluate=True):
        expr = to_sympy(expr, {str(self.var): self.var})
        return sp.diff(expr, self.var, order, evaluate=evaluate)

    def derivate_eval(self, expr, value, order=1):
        """
        Evalúa la derivada en un punto numérico
        """
        d = self.derivative(expr, order)
        return d.subs(self.var, value)



    def solve(self, expr, var='x'):
        manim_video_steps(expr, var, api_key=self.api_key)
    
    
                   # Derivadas básicas
    def partial_derivative():
        
        pass        # Derivadas parciales
    def higher_order_derivative():
        pass   # Derivadas de orden n
    def implicit_derivative():
        pass       # Derivación implícita
    def chain_rule():
        pass                # Regla de la cadena
    def product_rule():
        pass              # Regla del producto
    def quotient_rule():
        pass             # Regla del cociente
    def tangent_line():
        pass              # Recta tangente
    def extrema():
        pass                   # Máximos y mínimos
    def optimization():
        pass              # Problemas de optimización
    def limits():
        pass                    # Límites
    def continuity():
        pass                # Continuidad
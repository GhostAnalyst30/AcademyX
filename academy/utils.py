import json
import subprocess
from pathlib import Path
from textwrap import indent
import sympy as sp
import manim
import subprocess
from manim import *


def to_sympy(expr, locals=None):
    if isinstance(expr, sp.Expr):
        return expr

    if isinstance(expr, sp.Equality):
        return expr

    if isinstance(expr, (int, float)):
        return sp.sympify(expr)

    if isinstance(expr, str):
        expr = expr.replace("^", "**")

        if "=" in expr:
            left, right = expr.split("=")
            return sp.Eq(
                sp.sympify(left.strip(), locals=locals),
                sp.sympify(right.strip(), locals=locals)
            )

        return sp.sympify(expr, locals=locals)

    raise TypeError("Tipo de expresión no soportado")


def is_math_expression(s):
    return all(c not in s for c in "áéíóúÁÉÍÓÚñÑ") and any(
        op in s for op in ["x", "^", "*", "+", "-", "/", "="]
    )



def sympy_to_latex(expr):
    return sp.latex(expr)


# ---------- IA Solver ----------
import os
import json
import requests
import sympy as sp

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

from academy.ai.solver import solve_with_ai

# ---------- Manim Generator ----------
def manim_video_steps(expr, var="x", output_dir="manim_output"):
    sympy_expr = to_sympy(expr, {var: sp.symbols(var)})

    steps = solve_with_ai(sympy_expr, var)

    manim_code = f"""
from manim import *

class SolveEquation(Scene):
    def construct(self):
        steps = {json.dumps(steps, ensure_ascii=False)}
        def split_text_lines(text, words_per_line=4):
            words = text.split()
            lines = [
                " ".join(words[i:i + words_per_line])
                for i in range(0, len(words), words_per_line)
            ]
            return lines


        for step in steps:
            if step["type"] == "math":
                m = MathTex(step["content"])
                self.play(Write(m))
                self.wait(1)
                self.play(FadeOut(m))

            elif step["type"] == "text":
                lines = split_text_lines(step["content"], words_per_line=4)

                text_group = VGroup(*[
                    Text(line, font_size=36)
                    for line in lines
                ]).arrange(DOWN, center=True)

                text_group.move_to(ORIGIN)

                self.play(Write(text_group))
                self.wait(1.5)
                self.play(FadeOut(text_group))
"""

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    manim_file = output_dir / "solve_equation.py"
    manim_file.write_text(manim_code, encoding="utf-8")

    subprocess.run(
        ["manim", str(manim_file), "SolveEquation", "-pql"],
        check=True
    )


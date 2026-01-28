import json
import requests
import sympy as sp

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

OPENROUTER_API_KEY = None
OPENROUTER_MODEL = "mistralai/devstral-2512:free"

def set_openrouter_api(key: str, model: str = None):
    global OPENROUTER_API_KEY, OPENROUTER_MODEL
    OPENROUTER_API_KEY = key
    if model:
        OPENROUTER_MODEL = model



def solve_with_ai(sympy_expr, var="x"):
    if not OPENROUTER_API_KEY:
        raise RuntimeError("API de OpenRouter no configurada")

    if isinstance(sympy_expr, sp.Equality):
        latex_expr = sp.latex(sympy_expr.lhs) + " = " + sp.latex(sympy_expr.rhs)
    else:
        latex_expr = sp.latex(sympy_expr)


    prompt = f"""
Resuelve la expresion matematica respecto a {var}.

Expresion:
{latex_expr}

Devuelve SOLO un JSON valido con este formato exacto, utiliza todos los pasos para resolver la ecuacion matematica:

[
  {{ "type": "text", "content": "Expresion: ..." }},
  {{ "type": "math", "content": "..." }}
  {{ "type": "math", "content": "..." }}
]

Reglas:
- NO acentos
- Texto sin simbolos matematicos
- Matemáticas en LaTeX puro (MathTex)
- NO markdown
- NO texto fuera del JSON
"""

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    r = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=30)

    if r.status_code != 200:
        raise RuntimeError(r.text)

    content = r.json()["choices"][0]["message"]["content"]

    try:
        return extract_json(content)
    except Exception as e:
        raise RuntimeError(
            f"La IA no devolvio JSON valido.\nRespuesta cruda:\n{content}"
        ) from e


def extract_json(text: str):
    start = text.find("[")
    end = text.rfind("]")

    if start == -1 or end == -1:
        raise ValueError("No se encontro JSON en la respuesta")

    return json.loads(text[start:end + 1])


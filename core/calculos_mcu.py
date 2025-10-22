import math

# Importa a função auxiliar (se você a moveu para utils.py, importe de lá)
# Se não, copie a função formatar_passo_a_passo de outro arquivo 'calculos_*.py' para cá.
# Exemplo: from .utils import formatar_passo_a_passo
# Ou copie a definição dela aqui:
def formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado_final):
    """Gera uma string HTML formatada para o passo a passo."""
    entradas_html = "<ul>"
    for item in entradas:
        entradas_html += f"<li>{item}</li>"
    entradas_html += "</ul>"
    html = (
        f"<h3>➡️ {titulo}</h3>"
        f"<p><b>Fórmula Utilizada:</b><br><code>{formula}</code></p>"
        f"<p><b>Onde:</b></p>{entradas_html}"
        f"<p><b>Substituindo os valores:</b><br><code>{substituicao}</code></p>"
        f"<p><b>Resultado:</b><br><code>{resultado_final}</code></p>"
    )
    return html

# --- Funções de Cálculo MCU ---

def calcular_velocidade_linear(r, T=None, f=None, w=None):
    """Calcula a Velocidade Linear (v) no MCU. v = ω·r = 2π·r / T = 2π·r·f"""
    passo_a_passo = "Erro: Forneça Raio (r) e Período (T) ou Frequência (f) ou Velocidade Angular (ω)."
    v = None

    if r is not None:
        if w is not None:
            v = w * r
            titulo = "Cálculo da Velocidade Linear (v) via Velocidade Angular"
            formula = "v = ω · r"
            entradas = [f"ω = Velocidade Angular ({w:.4f} rad/s)", f"r = Raio ({r:.2f} m)"]
            substituicao = f"v = {w:.4f} · {r:.2f}"
            resultado = f"v = <b>{v:.4f} m/s</b>"
            passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
        elif T is not None and T != 0:
            v = (2 * math.pi * r) / T
            titulo = "Cálculo da Velocidade Linear (v) via Período"
            formula = "v = 2π · r / T"
            entradas = [f"r = Raio ({r:.2f} m)", f"T = Período ({T:.4f} s)"]
            substituicao = f"v = 2π · {r:.2f} / {T:.4f}"
            resultado = f"v = <b>{v:.4f} m/s</b>"
            passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
        elif f is not None:
            v = 2 * math.pi * r * f
            titulo = "Cálculo da Velocidade Linear (v) via Frequência"
            formula = "v = 2π · r · f"
            entradas = [f"r = Raio ({r:.2f} m)", f"f = Frequência ({f:.4f} Hz)"]
            substituicao = f"v = 2π · {r:.2f} · {f:.4f}"
            resultado = f"v = <b>{v:.4f} m/s</b>"
            passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return v, passo_a_passo

def calcular_velocidade_angular(T=None, f=None, v=None, r=None):
    """Calcula a Velocidade Angular (ω) no MCU. ω = 2π / T = 2π·f = v / r"""
    passo_a_passo = "Erro: Forneça Período (T) ou Frequência (f) ou Velocidade Linear (v) e Raio (r)."
    w = None

    if T is not None and T != 0:
        w = (2 * math.pi) / T
        titulo = "Cálculo da Velocidade Angular (ω) via Período"
        formula = "ω = 2π / T"
        entradas = [f"T = Período ({T:.4f} s)"]
        substituicao = f"ω = 2π / {T:.4f}"
        resultado = f"ω = <b>{w:.4f} rad/s</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    elif f is not None:
        w = 2 * math.pi * f
        titulo = "Cálculo da Velocidade Angular (ω) via Frequência"
        formula = "ω = 2π · f"
        entradas = [f"f = Frequência ({f:.4f} Hz)"]
        substituicao = f"ω = 2π · {f:.4f}"
        resultado = f"ω = <b>{w:.4f} rad/s</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    elif v is not None and r is not None and r != 0:
        w = v / r
        titulo = "Cálculo da Velocidade Angular (ω) via Velocidade Linear"
        formula = "ω = v / r"
        entradas = [f"v = Velocidade Linear ({v:.4f} m/s)", f"r = Raio ({r:.2f} m)"]
        substituicao = f"ω = {v:.4f} / {r:.2f}"
        resultado = f"ω = <b>{w:.4f} rad/s</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return w, passo_a_passo

def calcular_periodo(f=None, w=None, v=None, r=None):
    """Calcula o Período (T) no MCU. T = 1 / f = 2π / ω = 2π·r / v"""
    passo_a_passo = "Erro: Forneça Frequência (f) ou Velocidade Angular (ω) ou Velocidade Linear (v) e Raio (r)."
    T = None

    if f is not None and f != 0:
        T = 1 / f
        titulo = "Cálculo do Período (T) via Frequência"
        formula = "T = 1 / f"
        entradas = [f"f = Frequência ({f:.4f} Hz)"]
        substituicao = f"T = 1 / {f:.4f}"
        resultado = f"T = <b>{T:.4f} s</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    elif w is not None and w != 0:
        T = (2 * math.pi) / w
        titulo = "Cálculo do Período (T) via Velocidade Angular"
        formula = "T = 2π / ω"
        entradas = [f"ω = Velocidade Angular ({w:.4f} rad/s)"]
        substituicao = f"T = 2π / {w:.4f}"
        resultado = f"T = <b>{T:.4f} s</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    elif v is not None and r is not None and v != 0:
        T = (2 * math.pi * r) / v
        titulo = "Cálculo do Período (T) via Velocidade Linear"
        formula = "T = 2π · r / v"
        entradas = [f"r = Raio ({r:.2f} m)", f"v = Velocidade Linear ({v:.4f} m/s)"]
        substituicao = f"T = 2π · {r:.2f} / {v:.4f}"
        resultado = f"T = <b>{T:.4f} s</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return T, passo_a_passo

def calcular_frequencia(T=None, w=None, v=None, r=None):
    """Calcula a Frequência (f) no MCU. f = 1 / T = ω / 2π = v / (2π·r)"""
    passo_a_passo = "Erro: Forneça Período (T) ou Velocidade Angular (ω) ou Velocidade Linear (v) e Raio (r)."
    f = None

    if T is not None and T != 0:
        f = 1 / T
        titulo = "Cálculo da Frequência (f) via Período"
        formula = "f = 1 / T"
        entradas = [f"T = Período ({T:.4f} s)"]
        substituicao = f"f = 1 / {T:.4f}"
        resultado = f"f = <b>{f:.4f} Hz</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    elif w is not None:
        f = w / (2 * math.pi)
        titulo = "Cálculo da Frequência (f) via Velocidade Angular"
        formula = "f = ω / 2π"
        entradas = [f"ω = Velocidade Angular ({w:.4f} rad/s)"]
        substituicao = f"f = {w:.4f} / 2π"
        resultado = f"f = <b>{f:.4f} Hz</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    elif v is not None and r is not None and r != 0:
        f = v / (2 * math.pi * r)
        titulo = "Cálculo da Frequência (f) via Velocidade Linear"
        formula = "f = v / (2π · r)"
        entradas = [f"v = Velocidade Linear ({v:.4f} m/s)", f"r = Raio ({r:.2f} m)"]
        substituicao = f"f = {v:.4f} / (2π · {r:.2f})"
        resultado = f"f = <b>{f:.4f} Hz</b>"
        passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return f, passo_a_passo

def calcular_aceleracao_centripeta(v=None, r=None, w=None):
    """Calcula a Aceleração Centrípeta (a_cp) no MCU. a_cp = v² / r = ω² · r"""
    passo_a_passo = "Erro: Forneça Raio (r) e Velocidade Linear (v) ou Velocidade Angular (ω)."
    a_cp = None

    if r is not None and r != 0:
        if v is not None:
            a_cp = (v**2) / r
            titulo = "Cálculo da Aceleração Centrípeta (a_cp) via Velocidade Linear"
            formula = "a_cp = v² / r"
            entradas = [f"v = Velocidade Linear ({v:.4f} m/s)", f"r = Raio ({r:.2f} m)"]
            substituicao = f"a_cp = ({v:.4f})² / {r:.2f}"
            resultado = f"a_cp = <b>{a_cp:.4f} m/s²</b>"
            passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
        elif w is not None:
            a_cp = (w**2) * r
            titulo = "Cálculo da Aceleração Centrípeta (a_cp) via Velocidade Angular"
            formula = "a_cp = ω² · r"
            entradas = [f"ω = Velocidade Angular ({w:.4f} rad/s)", f"r = Raio ({r:.2f} m)"]
            substituicao = f"a_cp = ({w:.4f})² · {r:.2f}"
            resultado = f"a_cp = <b>{a_cp:.4f} m/s²</b>"
            passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return a_cp, passo_a_passo
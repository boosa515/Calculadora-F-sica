import math

def formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado_final):
    """Gera uma string HTML formatada para o passo a passo."""
    
    # Monta a lista de entradas
    entradas_html = "<ul>"
    for item in entradas:
        entradas_html += f"<li>{item}</li>"
    entradas_html += "</ul>"
    
    # Monta a string final
    html = (
        f"<h3>➡️ {titulo}</h3>"
        f"<p><b>Fórmula Utilizada:</b><br><code>{formula}</code></p>"
        f"<p><b>Onde:</b></p>{entradas_html}"
        f"<p><b>Substituindo os valores:</b><br><code>{substituicao}</code></p>"
        f"<p><b>Resultado:</b><br><code>{resultado_final}</code></p>"
    )
    return html

def calcular_velocidade_final(v0, a, t):
    """
    Calcula a velocidade final (v) no MRUV.
    Fórmula: v = v0 + a * t
    
    Retorna:
    - resultado (float): O valor da velocidade final.
    - passo_a_passo (str): O texto formatado (HTML) com a explicação do cálculo.
    """
    
    # 1. Realiza o cálculo
    v = v0 + a * t
    
    # 2. Cria o texto do passo a passo
    titulo = "Cálculo da Velocidade Final (v)"
    formula = "v = v₀ + a · t"
    entradas = [
        f"v₀ = Velocidade Inicial ({v0:.2f} m/s)",
        f"a = Aceleração ({a:.2f} m/s²)",
        f"t = Tempo ({t:.2f} s)"
    ]
    substituicao = (
        f"v = {v0:.2f} + ({a:.2f}) · ({t:.2f})<br>"
        f"v = {v0:.2f} + ({a*t:.2f})"
    )
    resultado = f"v = <b>{v:.2f} m/s</b>"
    
    passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    
    return v, passo_a_passo


def calcular_posicao_final(s0, v0, a, t):
    """
    Calcula a posição final (s) no MRUV.
    Fórmula: s = s0 + v0*t + (1/2)*a*t²
    """
    
    # 1. Realiza o cálculo
    s = s0 + v0 * t + 0.5 * a * (t**2)
    
    # 2. Cria o texto do passo a passo
    titulo = "Cálculo da Posição Final (s)"
    formula = "s = s₀ + v₀·t + ½ a·t²"
    entradas = [
        f"s₀ = Posição Inicial ({s0:.2f} m)",
        f"v₀ = Velocidade Inicial ({v0:.2f} m/s)",
        f"a = Aceleração ({a:.2f} m/s²)",
        f"t = Tempo ({t:.2f} s)"
    ]
    substituicao = (
        f"s = {s0:.2f} + ({v0:.2f}) · ({t:.2f}) + 0.5 · ({a:.2f}) · ({t:.2f})²<br>"
        f"s = {s0:.2f} + ({v0*t:.2f}) + ({0.5*a*(t**2):.2f})"
    )
    resultado = f"s = <b>{s:.2f} m</b>"
    
    passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return s, passo_a_passo


def calcular_torricelli(v0, a, ds):
    """
    Calcula a velocidade final (v) usando a Equação de Torricelli (não depende do tempo).
    Fórmula: v² = v0² + 2*a*Δs
    """
    
    # 1. Realiza o cálculo (v² e depois a raiz quadrada)
    v_quadrado = v0**2 + 2 * a * ds
    
    if v_quadrado < 0:
        # Erro de física: v² não pode ser negativo
        return None, "<b>Erro de Física:</b><br>Valores de entrada resultam em velocidade ao quadrado negativa (impossível para grandezas reais).<br>Verifique os sinais de aceleração e deslocamento."

    v = math.sqrt(v_quadrado) # Usamos math.sqrt
    
    # 2. Cria o texto do passo a passo
    titulo = "Cálculo da Velocidade Final (v) por Torricelli"
    formula = "v² = v₀² + 2·a·Δs"
    entradas = [
        f"v₀ = Velocidade Inicial ({v0:.2f} m/s)",
        f"a = Aceleração ({a:.2f} m/s²)",
        f"Δs = Deslocamento ({ds:.2f} m)"
    ]
    substituicao = (
        f"v² = ({v0:.2f})² + 2 · ({a:.2f}) · ({ds:.2f})<br>"
        f"v² = {v0**2:.2f} + {2*a*ds:.2f}<br>"
        f"v² = {v_quadrado:.2f}"
    )
    resultado = f"v = √({v_quadrado:.2f}) = <b>{v:.2f} m/s</b>"
    
    passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return v, passo_a_passo
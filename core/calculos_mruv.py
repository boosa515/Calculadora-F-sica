import math

def calcular_velocidade_final(v0, a, t):
    """
    Calcula a velocidade final (v) no MRUV.
    Fórmula: v = v0 + a * t
    
    Retorna:
    - resultado (float): O valor da velocidade final.
    - passo_a_passo (str): O texto formatado (HTML/LaTeX) com a explicação do cálculo.
    """
    
    # 1. Realiza o cálculo
    v = v0 + a * t
    
    # 2. Cria o texto do passo a passo (usando {{}} para escapar a formatação LaTeX)
    passo_a_passo = (
        f"### ➡️ Cálculo da Velocidade Final (v) \n"
        f"**Fórmula Utilizada:** $$v = v_0 + a \\cdot t$$ \n"
        f"Onde:\n"
        f" - $v_0$ = Velocidade Inicial ({{v0:.2f}} m/s)\n"
        f" - $a$ = Aceleração ({{a:.2f}} m/s²)\n"
        f" - $t$ = Tempo ({{t:.2f}} s)\n\n"
        
        f"**Substituindo os valores:**\n"
        f"$$v = {{v0:.2f}} + ({{a:.2f}}) \\cdot ({{t:.2f}})$$ \n"
        f"$$v = {{v0:.2f}} + ({{a*t:.2f}})$$ \n"
        f"**Resultado:**\n"
        f"$$v = \\mathbf{{{v:.2f}}} \\text{{ m/s}}$$"
    )
    
    return v, passo_a_passo


def calcular_posicao_final(s0, v0, a, t):
    """
    Calcula a posição final (s) no MRUV.
    Fórmula: s = s0 + v0*t + (1/2)*a*t²
    """
    
    # 1. Realiza o cálculo
    s = s0 + v0 * t + 0.5 * a * (t**2)
    
    # 2. Cria o texto do passo a passo
    passo_a_passo = (
        f"### ➡️ Cálculo da Posição Final (s) \n"
        f"**Fórmula Utilizada:** $$s = s_0 + v_0 \\cdot t + \\frac{{1}}{{2}} a \\cdot t^2$$ \n"
        f"Onde:\n"
        f" - $s_0$ = Posição Inicial ({{s0:.2f}} m)\n"
        f" - $v_0$ = Velocidade Inicial ({{v0:.2f}} m/s)\n"
        f" - $a$ = Aceleração ({{a:.2f}} m/s²)\n"
        f" - $t$ = Tempo ({{t:.2f}} s)\n\n"
        
        f"**Substituindo os valores:**\n"
        f"$$s = {{s0:.2f}} + ({{v0:.2f}}) \\cdot ({{t:.2f}}) + 0.5 \\cdot ({{a:.2f}}) \\cdot ({{t:.2f}})^2$$ \n"
        f"$$s = {{s0:.2f}} + ({{v0*t:.2f}}) + ({{0.5*a*(t**2):.2f}})$$ \n"
        f"**Resultado:**\n"
        f"$$s = \\mathbf{{{s:.2f}}} \\text{{ m}}$$"
    )
    
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
        return None, "Erro: Valores de entrada resultam em velocidade ao quadrado negativa (impossível para grandezas reais). Verifique os sinais de aceleração e deslocamento."

    v = math.sqrt(v_quadrado) # Usamos math.sqrt
    
    # 2. Cria o texto do passo a passo
    passo_a_passo = (
        f"### ➡️ Cálculo da Velocidade Final (v) por Torricelli \n"
        f"**Fórmula Utilizada:** $$v^2 = v_0^2 + 2 \\cdot a \\cdot \\Delta s$$ \n"
        f"Onde:\n"
        f" - $v_0$ = Velocidade Inicial ({{v0:.2f}} m/s)\n"
        f" - $a$ = Aceleração ({{a:.2f}} m/s²)\n"
        f" - $\\Delta s$ = Deslocamento ({{ds:.2f}} m)\n\n"
        
        f"**Substituindo os valores:**\n"
        f"$$v^2 = ({{v0:.2f}})^2 + 2 \\cdot ({{a:.2f}}) \\cdot ({{ds:.2f}})$$ \n"
        f"$$v^2 = {{v0**2:.2f}} + {{2*a*ds:.2f}}$$ \n"
        f"$$v^2 = {{v_quadrado:.2f}}$$ \n"
        f"**Resultado:**\n"
        f"$$v = \\sqrt{{{v_quadrado:.2f}}} = \\mathbf{{{v:.2f}}} \\text{{ m/s}}$$"
    )
    
    return v, passo_a_passo
import math

# Aceleração padrão da gravidade na Terra (m/s²)
GRAVIDADE_TERRA = 9.81 

def calcular_altura_final(h0, v0, g, t):
    """
    Calcula a altura final (h) na Queda Livre/Lançamento Vertical.
    Fórmula: h = h0 + v0*t - (1/2)*g*t² (usando g positivo)
    """
    
    h = h0 + v0 * t - 0.5 * g * (t**2)
    
    passo_a_passo = (
        f"### ➡️ Cálculo da Altura Final (h) \n"
        f"**Fórmula Utilizada:** $$h = h_0 + v_0 \\cdot t - \\frac{{1}}{{2}} g \\cdot t^2$$ \n"
        f"Onde:\n"
        f" - $h_0$ = Altura Inicial ({{h0:.2f}} m)\n"
        f" - $v_0$ = Velocidade Inicial ({{v0:.2f}} m/s)\n"
        f" - $g$ = Aceleração da Gravidade ({{g:.2f}} m/s²)\n"
        f" - $t$ = Tempo ({{t:.2f}} s)\n\n"
        
        f"**Substituindo os valores:**\n"
        f"$$h = {{h0:.2f}} + ({{v0:.2f}}) \\cdot ({{t:.2f}}) - 0.5 \\cdot ({{g:.2f}}) \\cdot ({{t:.2f}})^2$$ \n"
        f"$$h = {{h0:.2f}} + ({{v0*t:.2f}}) - ({{0.5*g*(t**2):.2f}})$$ \n"
        f"**Resultado:**\n"
        f"$$h = \\mathbf{{{h:.2f}}} \\text{{ m}}$$"
    )
    
    return h, passo_a_passo


def calcular_velocidade_final_gravidade(v0, g, t):
    """
    Calcula a velocidade final (v) na Queda Livre/Lançamento Vertical.
    Fórmula: v = v0 - g*t (usando g positivo)
    """
    
    v = v0 - g * t
    
    passo_a_passo = (
        f"### ➡️ Cálculo da Velocidade Final (v) \n"
        f"**Fórmula Utilizada:** $$v = v_0 - g \\cdot t$$ \n"
        f"Onde:\n"
        f" - $v_0$ = Velocidade Inicial ({{v0:.2f}} m/s)\n"
        f" - $g$ = Aceleração da Gravidade ({{g:.2f}} m/s²)\n"
        f" - $t$ = Tempo ({{t:.2f}} s)\n\n"
        
        f"**Substituindo os valores:**\n"
        f"$$v = {{v0:.2f}} - ({{g:.2f}}) \\cdot ({{t:.2f}})$$ \n"
        f"$$v = {{v0:.2f}} - ({{g*t:.2f}})$$ \n"
        f"**Resultado:**\n"
        f"$$v = \\mathbf{{{v:.2f}}} \\text{{ m/s}}$$"
    )
    
    return v, passo_a_passo
import math

# (Importa a função auxiliar do calculos_mruv)
# No seu projeto real, você pode mover esta função para um arquivo 'core/utils.py'
# Mas para manter simples, vamos copiá-la aqui.
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

# Aceleração padrão da gravidade na Terra (m/s²)
GRAVIDADE_TERRA = 9.81 

def calcular_altura_final(h0, v0, g, t):
    """
    Calcula a altura final (h) na Queda Livre/Lançamento Vertical.
    Fórmula: h = h0 + v0*t - (1/2)*g*t² (usando g positivo)
    """
    
    h = h0 + v0 * t - 0.5 * g * (t**2)
    
    titulo = "Cálculo da Altura Final (h)"
    formula = "h = h₀ + v₀·t - ½ g·t²"
    entradas = [
        f"h₀ = Altura Inicial ({h0:.2f} m)",
        f"v₀ = Velocidade Inicial ({v0:.2f} m/s)",
        f"g = Aceleração da Gravidade ({g:.2f} m/s²)",
        f"t = Tempo ({t:.2f} s)"
    ]
    substituicao = (
        f"h = {h0:.2f} + ({v0:.2f}) · ({t:.2f}) - 0.5 · ({g:.2f}) · ({t:.2f})²<br>"
        f"h = {h0:.2f} + ({v0*t:.2f}) - ({0.5*g*(t**2):.2f})"
    )
    resultado = f"h = <b>{h:.2f} m</b>"
    
    passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    
    return h, passo_a_passo


def calcular_velocidade_final_gravidade(v0, g, t):
    """
    Calcula a velocidade final (v) na Queda Livre/Lançamento Vertical.
    Fórmula: v = v0 - g*t (usando g positivo)
    """
    
    v = v0 - g * t
    
    titulo = "Cálculo da Velocidade Final (v)"
    formula = "v = v₀ - g·t"
    entradas = [
        f"v₀ = Velocidade Inicial ({v0:.2f} m/s)",
        f"g = Aceleração da Gravidade ({g:.2f} m/s²)",
        f"t = Tempo ({t:.2f} s)"
    ]
    substituicao = (
        f"v = {v0:.2f} - ({g:.2f}) · ({t:.2f})<br>"
        f"v = {v0:.2f} - ({g*t:.2f})"
    )
    resultado = f"v = <b>{v:.2f} m/s</b>"

    passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    
    return v, passo_a_passo
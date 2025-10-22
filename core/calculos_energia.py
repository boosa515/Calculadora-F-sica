# (Importa a função auxiliar do calculos_mruv)
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

def calcular_energia_cinetica(m, v):
    """
    Calcula a Energia Cinética (Ec).
    Fórmula: Ec = (1/2) * m * v²
    """
    
    # 1. Realiza o cálculo
    ec = 0.5 * m * (v**2)
    
    # 2. Cria o passo a passo
    titulo = "Cálculo da Energia Cinética (E_c)"
    formula = "E_c = ½ m·v²"
    entradas = [
        f"m = Massa ({m:.2f} kg)",
        f"v = Velocidade ({v:.2f} m/s)"
    ]
    substituicao = (
        f"E_c = 0.5 · ({m:.2f}) · ({v:.2f})²<br>"
        f"E_c = 0.5 · ({m:.2f}) · ({v**2:.2f})"
    )
    resultado = f"E_c = <b>{ec:.2f} J</b> (Joules)"
    
    passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)
    
    return ec, passo_a_passo


def calcular_energia_potencial_grav(m, g, h):
    """
    Calcula a Energia Potencial Gravitacional (Epg).
    Fórmula: Epg = m * g * h
    """
    
    # 1. Realiza o cálculo
    epg = m * g * h
    
    # 2. Cria o passo a passo
    titulo = "Cálculo da Energia Potencial Gravitacional (E_pg)"
    formula = "E_pg = m·g·h"
    entradas = [
        f"m = Massa ({m:.2f} kg)",
        f"g = Gravidade ({g:.2f} m/s²)",
        f"h = Altura ({h:.2f} m)"
    ]
    substituicao = (
        f"E_pg = ({m:.2f}) · ({g:.2f}) · ({h:.2f})"
    )
    resultado = f"E_pg = <b>{epg:.2f} J</b> (Joules)"
    
    passo_a_passo = formatar_passo_a_passo(titulo, formula, entradas, substituicao, resultado)

    return epg, passo_a_passo
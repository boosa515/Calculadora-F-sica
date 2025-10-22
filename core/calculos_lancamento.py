import math

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

# Aceleração padrão da gravidade na Terra (m/s²)
GRAVIDADE_TERRA = 9.81 

def calcular_lancamento_obliquo(v0, angulo_graus, g=GRAVIDADE_TERRA):
    """
    Calcula Alcance Máximo (A), Altura Máxima (H) e Tempo Total de Voo (T) 
    para um Lançamento Oblíquo.
    """
    
    # 1. Converte o ângulo para radianos
    angulo_rad = math.radians(angulo_graus)
    
    # 2. Decompõe a velocidade inicial
    v0x = v0 * math.cos(angulo_rad)
    v0y = v0 * math.sin(angulo_rad)

    # 3. Cálculo da Altura Máxima (H) - H = (v0y)² / (2 * g)
    altura_max = (v0y**2) / (2 * g)
    
    # 4. Cálculo do Alcance Máximo (A) - A = (v0² * sen(2*theta)) / g
    alcance_max = (v0**2 * math.sin(2 * angulo_rad)) / g
    
    # 5. Cálculo do Tempo Total de Voo (T) - T = 2 * v0y / g
    tempo_total = (2 * v0y) / g
    
    # 6. Cria o passo a passo
    passo_a_passo = (
        f"<h3>➡️ Análise do Lançamento Oblíquo</h3>"
        f"<p><b>Dados Iniciais:</b></p>"
        f"<ul>"
        f" <li>v₀ = Velocidade Inicial ({v0:.2f} m/s)</li>"
        f" <li>θ = Ângulo de Lançamento ({angulo_graus:.2f}°)</li>"
        f" <li>g = Gravidade ({g:.2f} m/s²)</li>"
        f"</ul>"
        
        f"<h4>1. Decomposição Vetorial</h4>"
        f"<p>Decompomos v₀ em seus componentes:</p>"
        f"<ul>"
        f" <li>Velocidade Horizontal (v₀ₓ): <code>v₀ · cos(θ) = {v0:.2f} · cos({angulo_graus:.2f}°) = <b>{v0x:.2f} m/s</b></code></li>"
        f" <li>Velocidade Vertical (v₀ᵧ): <code>v₀ · sin(θ) = {v0:.2f} · sin({angulo_graus:.2f}°) = <b>{v0y:.2f} m/s</b></code></li>"
        f"</ul>"

        f"<h4>2. Altura Máxima (H)</h4>"
        f"<p><b>Fórmula:</b> <code>H = (v₀ᵧ)² / (2g)</code></p>"
        f"<p><b>Cálculo:</b> <code>H = ({v0y:.2f})² / (2 · {g:.2f}) = <b>{altura_max:.2f} m</b></code></p>"

        f"<h4>3. Alcance Máximo (A)</h4>"
        f"<p><b>Fórmula:</b> <code>A = (v₀² · sin(2θ)) / g</code></p>"
        f"<p><b>Cálculo:</b> <code>A = ({v0:.2f})² · sin({2*angulo_graus:.2f}°) / {g:.2f} = <b>{alcance_max:.2f} m</b></code></p>"

        f"<hr><p><b>Tempo Total de Voo:</b> <code><b>{tempo_total:.2f} s</b></code></p>"
    )
    
    return {'H': altura_max, 'A': alcance_max, 'T': tempo_total}, passo_a_passo
import math

# Aceleração padrão da gravidade na Terra (m/s²)
GRAVIDADE_TERRA = 9.81 

def calcular_lancamento_obliquo(v0, angulo_graus, g=GRAVIDADE_TERRA):
    """
    Calcula Alcance Máximo (A), Altura Máxima (H) e Tempo Total de Voo (T) 
    para um Lançamento Oblíquo.
    
    A função decompõe a velocidade inicial e utiliza as equações de movimento 
    uniforme (eixo X) e uniformemente variado (eixo Y).
    
    Parâmetros:
        v0 (float): Velocidade inicial (m/s).
        angulo_graus (float): Ângulo de lançamento (graus).
        g (float, opcional): Aceleração da gravidade (m/s²). Default é 9.81.
        
    Retorna:
        tuple: (dict) Resultados (H, A, T), e (str) o passo a passo formatado.
    """
    
    # 1. Converte o ângulo para radianos
    angulo_rad = math.radians(angulo_graus)
    
    # 2. Decompõe a velocidade inicial
    v0x = v0 * math.cos(angulo_rad)
    v0y = v0 * math.sin(angulo_rad)

    # 3. Cálculo da Altura Máxima (H) - H = (v0y)² / (2 * g)
    altura_max = (v0y**2) / (2 * g)
    
    # 4. Cálculo do Alcance Máximo (A) - A = (v0² * sen(2*theta)) / g
    # O ângulo para a função sen deve ser dobrado em radianos.
    alcance_max = (v0**2 * math.sin(2 * angulo_rad)) / g
    
    # 5. Cálculo do Tempo Total de Voo (T) - T = 2 * v0y / g
    tempo_total = (2 * v0y) / g
    
    # 6. Cria o passo a passo (usando \\ para comandos LaTeX e {{}} para variáveis)
    passo_a_passo = (
        f"### ➡️ Análise do Lançamento Oblíquo \n"
        f"**Dados Iniciais:**\n"
        f" - $v_0$ = Velocidade Inicial ({{v0:.2f}} m/s)\n"
        f" - $\\theta$ = Ângulo de Lançamento ({{angulo_graus:.2f}}°)\n"
        f" - $g$ = Gravidade ({{g:.2f}} m/s²)\n\n"
        
        f"### 1. Decomposição Vetorial \n"
        f"Decompomos $v_0$ em seus componentes:\n"
        
        # Correção dos avisos: Usando \\cos e \\sin
        f" - Velocidade Horizontal ($v_{{0x}}$): $v_0 \\cdot \\cos(\\theta) = {{v0:.2f}} \\cdot \\cos({{angulo_graus:.2f}}°) = \\mathbf{{{v0x:.2f}}} \\text{{ m/s}}$ \n"
        f" - Velocidade Vertical ($v_{{0y}}$): $v_0 \\cdot \\sin(\\theta) = {{v0:.2f}} \\cdot \\sin({{angulo_graus:.2f}}°) = \\mathbf{{{v0y:.2f}}} \\text{{ m/s}}$ \n\n"
        
        f"### 2. Altura Máxima ($H$) \n"
        f"**Fórmula:** $$H = \\frac{{v_{{0y}}^2}}{{2g}}$$ \n"
        f"**Cálculo:** $$H = \\frac{{({{v0y:.2f}})^2}}{{2 \\cdot {{g:.2f}}}} = \\mathbf{{{altura_max:.2f}}} \\text{{ m}}$$\n\n"

        f"### 3. Alcance Máximo ($A$) \n"
        f"**Fórmula:** $$A = \\frac{{v_0^2 \\cdot \\sin(2\\theta)}}{{g}}$$ \n"
        f"**Cálculo:** $$A = \\frac{{({{v0:.2f}})^2 \\cdot \\sin({{2*angulo_graus:.2f}}°)}}{{{{g:.2f}}}} = \\mathbf{{{alcance_max:.2f}}} \\text{{ m}}$$\n\n"
        
        f"**Tempo Total de Voo:** $\\mathbf{{{tempo_total:.2f}}} \\text{{ s}}$"
    )
    
    return {'H': altura_max, 'A': alcance_max, 'T': tempo_total}, passo_a_passo
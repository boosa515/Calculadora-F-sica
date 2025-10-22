def calcular_energia_cinetica(m, v):
    """
    Calcula a Energia Cinética (Ec).
    Fórmula: Ec = (1/2) * m * v²
    """
    
    # 1. Realiza o cálculo
    ec = 0.5 * m * (v**2)
    
    # 2. Cria o passo a passo
    passo_a_passo = (
        f"### ➡️ Cálculo da Energia Cinética ($\text{{E}}_c$) \n"
        f"**Fórmula Utilizada:** $$E_c = \\frac{{1}}{{2}} m \\cdot v^2$$ \n"
        f"Onde:\n"
        f" - $m$ = Massa ({{m:.2f}} kg)\n"
        f" - $v$ = Velocidade ({{v:.2f}} m/s)\n\n"
        
        f"**Substituindo os valores:**\n"
        f"$$E_c = 0.5 \\cdot ({{m:.2f}}) \\cdot ({{v:.2f}})^2$$ \n"
        f"$$E_c = 0.5 \\cdot ({{m:.2f}}) \\cdot ({{v**2:.2f}})$$ \n"
        f"**Resultado:**\n"
        f"$$E_c = \\mathbf{{{ec:.2f}}} \\text{{ J}}$$ (Joules)"
    )
    
    return ec, passo_a_passo


def calcular_energia_potencial_grav(m, g, h):
    """
    Calcula a Energia Potencial Gravitacional (Epg).
    Fórmula: Epg = m * g * h
    """
    
    # 1. Realiza o cálculo
    epg = m * g * h
    
    # 2. Cria o passo a passo
    passo_a_passo = (
        f"### ➡️ Cálculo da Energia Potencial Gravitacional ($\text{{E}}_{{pg}}$) \n"
        f"**Fórmula Utilizada:** $$E_{{pg}} = m \\cdot g \\cdot h$$ \n"
        f"Onde:\n"
        f" - $m$ = Massa ({{m:.2f}} kg)\n"
        f" - $g$ = Gravidade ({{g:.2f}} m/s²)\n"
        f" - $h$ = Altura ({{h:.2f}} m)\n\n"
        
        f"**Substituindo os valores:**\n"
        f"$$E_{{pg}} = ({{m:.2f}}) \\cdot ({{g:.2f}}) \\cdot ({{h:.2f}})$$ \n"
        f"$$E_{{pg}} = \\mathbf{{{epg:.2f}}} \\text{{ J}}$$ (Joules)"
    )
    
    return epg, passo_a_passo
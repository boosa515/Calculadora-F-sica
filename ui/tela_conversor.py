from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFormLayout, QGroupBox, QMessageBox, QComboBox, QTextEdit
)
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QDoubleValidator

# Constantes de Conversão
KMH_TO_MS = 1000 / 3600
JOULES_TO_EV = 6.242e+18
KM_TO_M = 1000
MI_TO_M = 1609.34

class TelaConversor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent 
        self.passo_a_passo_html = "" # Armazena o HTML do resultado

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        # Título
        titulo = QLabel("Conversor de Unidades Comuns")
        titulo.setStyleSheet("font-size: 18pt; font-weight: 600; margin-bottom: 15px;")
        layout.addWidget(titulo)
        
        explicacao = QLabel("Converta rapidamente unidades de Velocidade, Energia, Distância e Temperatura.")
        explicacao.setWordWrap(True)
        layout.addWidget(explicacao)

        # 1. SELETOR DE GRANDEZA
        control_group = QGroupBox("Escolha a Grandeza")
        form_layout_control = QFormLayout(control_group)

        self.combo_grandeza = QComboBox()
        self.combo_grandeza.addItems([
            "Velocidade", 
            "Energia / Trabalho",
            "Distância",
            "Temperatura"
        ])
        self.combo_grandeza.currentIndexChanged.connect(self.atualizar_campos_conversao)
        
        form_layout_control.addRow("Grandeza:", self.combo_grandeza)
        layout.addWidget(control_group)

        # 2. ENTRADA DE DADOS
        dados_group = QGroupBox("Entrada de Valores")
        form_layout_dados = QFormLayout(dados_group)
        
        float_validator = QDoubleValidator()
        float_validator.setLocale(QLocale(QLocale.C)) # Aceita PONTO
        
        # Campo de Entrada
        self.valor_input = QLineEdit()
        self.valor_input.setValidator(float_validator)
        self.valor_input.setPlaceholderText("Insira o valor a ser convertido")

        self.combo_de = QComboBox()
        self.combo_para = QComboBox()
        
        form_layout_dados.addRow("Valor:", self.valor_input)
        form_layout_dados.addRow("De:", self.combo_de)
        form_layout_dados.addRow("Para:", self.combo_para)
        
        layout.addWidget(dados_group)
        
        # 3. BOTÃO DE CÁLCULO
        btn_calcular = QPushButton("Converter")
        btn_calcular.setStyleSheet("padding: 8px; font-weight: bold;")
        btn_calcular.clicked.connect(self.realizar_conversao) 
        layout.addWidget(btn_calcular)
        
        # 4. ÁREA DE RESULTADOS
        self.resultado_output = QTextEdit()
        self.resultado_output.setReadOnly(True)
        self.resultado_output.setPlaceholderText("O resultado da conversão aparecerá aqui.")
        self.resultado_output.setFixedHeight(120) # Deixa a caixa menor
        layout.addWidget(self.resultado_output)

        # 5. BOTÃO AMPLIAR
        self.btn_ampliar = QPushButton("Ampliar Resultado")
        self.btn_ampliar.setStyleSheet("padding: 5px; font-weight: bold; font-size: 9pt;")
        self.btn_ampliar.clicked.connect(self.ampliar_resultado)
        self.btn_ampliar.hide() # Começa escondido
        layout.addWidget(self.btn_ampliar)

        self.atualizar_campos_conversao()


    def atualizar_campos_conversao(self):
        """Atualiza as opções dos ComboBox DE e PARA com base na Grandeza escolhida."""
        self.combo_de.clear()
        self.combo_para.clear()
        self.resultado_output.clear()
        self.valor_input.clear()
        self.btn_ampliar.hide()
        self.passo_a_passo_html = ""

        grandeza = self.combo_grandeza.currentText()
        
        if grandeza == "Velocidade":
            opcoes = ["m/s", "km/h"]
        elif grandeza == "Energia / Trabalho":
            opcoes = ["Joules (J)", "elétron-volts (eV)"]
        elif grandeza == "Distância":
            opcoes = ["Metros (m)", "Quilômetros (km)", "Milhas (mi)"]
        elif grandeza == "Temperatura":
            opcoes = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
        else:
            opcoes = []
            
        self.combo_de.addItems(opcoes)
        self.combo_para.addItems(opcoes)

    def ampliar_resultado(self):
        """Chama a janela principal para mostrar o resultado ampliado."""
        if self.passo_a_passo_html:
            self.parent_window.mostrar_tela_resultado(self.passo_a_passo_html)

    def realizar_conversao(self):
        self.resultado_output.clear()
        self.btn_ampliar.hide()
        
        texto_valor = self.valor_input.text().replace(',', '.')
        try:
            valor = float(texto_valor)
        except ValueError:
            QMessageBox.critical(self, "Erro de Entrada", "Por favor, insira um valor numérico válido.")
            return

        unidade_de = self.combo_de.currentText()
        unidade_para = self.combo_para.currentText()
        grandeza = self.combo_grandeza.currentText()
        
        resultado = 0
        formula = "N/A"
        
        # 2. Lógica de Conversão
        if unidade_de == unidade_para:
            resultado = valor
            formula = "Nenhuma conversão necessária."
            
        # --- VELOCIDADE ---
        elif grandeza == "Velocidade":
            if unidade_de == "km/h" and unidade_para == "m/s":
                resultado = valor * KMH_TO_MS
                formula = f"m/s = km/h / 3.6<br>{valor:.2f} / 3.6"
            elif unidade_de == "m/s" and unidade_para == "km/h":
                resultado = valor / KMH_TO_MS
                formula = f"km/h = m/s * 3.6<br>{valor:.2f} * 3.6"
            
        # --- ENERGIA ---
        elif grandeza == "Energia / Trabalho":
            if unidade_de == "Joules (J)" and unidade_para == "elétron-volts (eV)":
                resultado = valor * JOULES_TO_EV
                formula = f"eV = J · {JOULES_TO_EV:.2e}<br>{valor:.2f} · {JOULES_TO_EV:.2e}"
            elif unidade_de == "elétron-volts (eV)" and unidade_para == "Joules (J)":
                resultado = valor / JOULES_TO_EV
                formula = f"J = eV / {JOULES_TO_EV:.2e}<br>{valor:.2f} / {JOULES_TO_EV:.2e}"

        # --- DISTÂNCIA ---
        elif grandeza == "Distância":
            # Primeiro, converte 'DE' para Metros (base)
            if unidade_de == "Metros (m)":
                base_m = valor
            elif unidade_de == "Quilômetros (km)":
                base_m = valor * KM_TO_M
            elif unidade_de == "Milhas (mi)":
                base_m = valor * MI_TO_M
            
            # Segundo, converte de Metros (base) para 'PARA'
            if unidade_para == "Metros (m)":
                resultado = base_m
            elif unidade_para == "Quilômetros (km)":
                resultado = base_m / KM_TO_M
            elif unidade_para == "Milhas (mi)":
                resultado = base_m / MI_TO_M
            formula = f"Convertendo {unidade_de} para {unidade_para}."

        # --- TEMPERATURA ---
        elif grandeza == "Temperatura":
            # Primeiro, converte 'DE' para Celsius (base)
            if unidade_de == "Celsius (°C)":
                base_c = valor
            elif unidade_de == "Fahrenheit (°F)":
                base_c = (valor - 32) * (5/9)
            elif unidade_de == "Kelvin (K)":
                base_c = valor - 273.15
            
            # Segundo, converte de Celsius (base) para 'PARA'
            if unidade_para == "Celsius (°C)":
                resultado = base_c
                formula = "C = C"
            elif unidade_para == "Fahrenheit (°F)":
                resultado = (base_c * 9/5) + 32
                formula = f"F = (C * 9/5) + 32<br>({base_c:.2f} * 9/5) + 32"
            elif unidade_para == "Kelvin (K)":
                resultado = base_c + 273.15
                formula = f"K = C + 273.15<br>{base_c:.2f} + 273.15"

        # 3. Exibe o Resultado no formato Passo a Passo
        self.passo_a_passo_html = (
            f"<h3>Conversão: {unidade_de} ➡️ {unidade_para}</h3>"
            f"<p><b>Fórmula / Método:</b><br><code>{formula}</code></p>"
            f"<p><b>Resultado:</b><br><code><b>{resultado:.4f}</b> {unidade_para.split(' ')[0]}</code></p>"
        )
        
        self.resultado_output.setHtml(self.passo_a_passo_html)
        self.btn_ampliar.show()
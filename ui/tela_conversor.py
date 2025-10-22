from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFormLayout, QGroupBox, QMessageBox, QComboBox, QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

# Constantes de Conversão
KMH_TO_MS = 1000 / 3600  # Multiplicador de km/h para m/s
JOULES_TO_EV = 6.242e+18 # Multiplicador de Joules para elétron-volts

class TelaConversor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent 

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        # Título
        titulo = QLabel("Conversor de Unidades Comuns")
        titulo.setStyleSheet("font-size: 18pt; font-weight: 600; margin-bottom: 15px;")
        layout.addWidget(titulo)
        
        explicacao = QLabel("Converta rapidamente as unidades mais comuns usadas em problemas de física (Velocidade e Energia).")
        explicacao.setWordWrap(True)
        layout.addWidget(explicacao)

        # 1. SELETOR DE GRANDEZA
        control_group = QGroupBox("Escolha a Grandeza")
        form_layout_control = QFormLayout(control_group)

        self.combo_grandeza = QComboBox()
        self.combo_grandeza.addItems(["Velocidade", "Energia / Trabalho"])
        self.combo_grandeza.currentIndexChanged.connect(self.atualizar_campos_conversao)
        
        form_layout_control.addRow("Grandeza:", self.combo_grandeza)
        layout.addWidget(control_group)

        # 2. ENTRADA DE DADOS
        dados_group = QGroupBox("Entrada de Valores")
        form_layout_dados = QFormLayout(dados_group)
        
        float_validator = QDoubleValidator()
        
        # Campo de Entrada
        self.valor_input = QLineEdit()
        self.valor_input.setValidator(float_validator)
        self.valor_input.setPlaceholderText("Insira o valor a ser convertido")

        # Seletor De
        self.combo_de = QComboBox()
        # Seletor Para
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
        self.resultado_output.setFixedHeight(100) # Deixa a caixa menor
        layout.addWidget(self.resultado_output)

        # Inicializa os combos com base na primeira seleção ("Velocidade")
        self.atualizar_campos_conversao()


    def atualizar_campos_conversao(self):
        """Atualiza as opções dos ComboBox DE e PARA com base na Grandeza escolhida."""
        self.combo_de.clear()
        self.combo_para.clear()
        self.resultado_output.clear()
        self.valor_input.clear()
        
        if self.combo_grandeza.currentText() == "Velocidade":
            opcoes = ["m/s", "km/h"]
        elif self.combo_grandeza.currentText() == "Energia / Trabalho":
            opcoes = ["Joules (J)", "elétron-volts (eV)"]
        else:
            opcoes = []
            
        self.combo_de.addItems(opcoes)
        self.combo_para.addItems(opcoes)


    def realizar_conversao(self):
        self.resultado_output.clear()
        
        # 1. Obter e validar o valor
        texto_valor = self.valor_input.text().replace(',', '.')
        try:
            valor = float(texto_valor)
        except ValueError:
            QMessageBox.critical(self, "Erro de Entrada", "Por favor, insira um valor numérico válido.")
            return

        unidade_de = self.combo_de.currentText()
        unidade_para = self.combo_para.currentText()
        resultado = 0
        
        # 2. Lógica de Conversão
        if unidade_de == unidade_para:
            resultado = valor
            formula = "Nenhuma conversão necessária."
            
        elif self.combo_grandeza.currentText() == "Velocidade":
            if unidade_de == "km/h" and unidade_para == "m/s":
                resultado = valor * KMH_TO_MS
                formula = f"$$m/s = km/h \\times \\frac{{1000}}{{3600}} = {valor:.2f} \\times {KMH_TO_MS:.4f}$$"
            elif unidade_de == "m/s" and unidade_para == "km/h":
                resultado = valor / KMH_TO_MS
                formula = f"$$km/h = m/s \\div \\frac{{1000}}{{3600}} = {valor:.2f} \\div {KMH_TO_MS:.4f}$$"
            
        elif self.combo_grandeza.currentText() == "Energia / Trabalho":
            if unidade_de == "Joules (J)" and unidade_para == "elétron-volts (eV)":
                resultado = valor * JOULES_TO_EV
                formula = f"$$eV = J \\times {{JOULES_TO_EV:.2e}}$$"
            elif unidade_de == "elétron-volts (eV)" and unidade_para == "Joules (J)":
                resultado = valor / JOULES_TO_EV
                formula = f"$$J = eV \\div {{JOULES_TO_EV:.2e}}$$"

        # 3. Exibe o Resultado no formato Passo a Passo
        passo_a_passo = (
            f"### Conversão: {unidade_de} ➡️ {unidade_para} \n"
            f"**Fórmula Utilizada:** \n {formula} \n\n"
            f"**Resultado:** \n"
            f"$$\\mathbf{{{resultado:.4f}}}\\text{{ {unidade_para.split(' ')[0]}}}$$" 
        )
        
        self.resultado_output.setHtml(passo_a_passo)
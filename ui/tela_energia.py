from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFormLayout, QGroupBox, QMessageBox, QComboBox, QTextEdit
)
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QDoubleValidator

from core.calculos_energia import (
    calcular_energia_cinetica,
    calcular_energia_potencial_grav
) 

class TelaEnergia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent 
        self.passo_a_passo_html = "" # Armazena o HTML

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        titulo = QLabel("Cálculo de Energia (Cinética e Potencial)")
        titulo.setStyleSheet("font-size: 18pt; font-weight: 600; margin-bottom: 15px;")
        layout.addWidget(titulo)
        
        explicacao = QLabel("A Energia Cinética depende do movimento, e a Potencial Gravitacional, da posição do corpo em relação a um referencial.")
        explicacao.setWordWrap(True)
        layout.addWidget(explicacao)

        # 1. SELETOR DE CÁLCULO
        formula_group = QGroupBox("Escolha o Cálculo")
        form_layout = QFormLayout(formula_group)
        
        self.combo_formula = QComboBox()
        self.combo_formula.addItems([
            "Energia Cinética (E_c)", 
            "Energia Potencial Gravitacional (E_pg)"
        ])
        self.combo_formula.currentIndexChanged.connect(self.limpar_campos)
        
        form_layout.addRow("Fórmula/Resultado:", self.combo_formula)
        layout.addWidget(formula_group)

        # 2. ENTRADA DE DADOS
        dados_group = QGroupBox("Entrada de Dados (Preencha os dados necessários)")
        self.form_layout_dados = QFormLayout(dados_group)
        
        float_validator = QDoubleValidator()
        float_validator.setDecimals(4) 
        float_validator.setLocale(QLocale(QLocale.C))
        
        self.inputs = {}
        campos = [
            ("m", "Massa (m - kg):"),
            ("v", "Velocidade (v - m/s):"),
            ("h", "Altura (h - m):"),
            ("g", "Gravidade (g - m/s², use 9.81):"),
        ]
        
        for key, label_text in campos:
            label = QLabel(label_text)
            line_edit = QLineEdit()
            line_edit.setValidator(float_validator)
            line_edit.setMaximumWidth(250)
            self.inputs[key] = line_edit
            self.form_layout_dados.addRow(label, line_edit)
            
        self.inputs['g'].setText("9.81")
        layout.addWidget(dados_group)

        # 3. BOTÃO DE CÁLCULO
        btn_calcular = QPushButton("Calcular")
        btn_calcular.setStyleSheet("padding: 8px; font-weight: bold;")
        btn_calcular.clicked.connect(self.realizar_calculo) 
        layout.addWidget(btn_calcular)
        
        # 4. ÁREA DE RESULTADOS
        self.resultado_output = QTextEdit()
        self.resultado_output.setReadOnly(True)
        self.resultado_output.setPlaceholderText("O passo a passo e o resultado do cálculo aparecerão aqui.")
        self.resultado_output.setStyleSheet("font-size: 11pt; padding: 10px;")
        layout.addWidget(self.resultado_output)

        # 5. BOTÃO AMPLIAR (NOVO)
        self.btn_ampliar = QPushButton("Ampliar Resultado")
        self.btn_ampliar.setStyleSheet("padding: 5px; font-weight: bold; font-size: 9pt;")
        self.btn_ampliar.clicked.connect(self.ampliar_resultado)
        self.btn_ampliar.hide() # Começa escondido
        layout.addWidget(self.btn_ampliar)


    def limpar_campos(self):
        """Limpa todos os campos de entrada e a área de resultados."""
        self.inputs['m'].clear()
        self.inputs['v'].clear()
        self.inputs['h'].clear()
        self.resultado_output.clear()
        self.passo_a_passo_html = "" # Limpa o HTML salvo
        self.btn_ampliar.hide() # Esconde o botão

    def ampliar_resultado(self):
        """Chama a janela principal para mostrar o resultado ampliado."""
        if self.passo_a_passo_html:
            self.parent_window.mostrar_tela_resultado(self.passo_a_passo_html)

    def _obter_dados_entrada(self, campos_necessarios):
        """Tenta obter e converter os dados dos campos de entrada necessários."""
        dados = {}
        for campo in campos_necessarios:
            texto = self.inputs[campo].text().replace(',', '.')
            if not texto:
                return None  
            try:
                dados[campo] = float(texto)
            except ValueError:
                return None 
        return dados


    def realizar_calculo(self):
        self.resultado_output.clear()
        self.btn_ampliar.hide()
        self.passo_a_passo_html = ""
        
        formula_index = self.combo_formula.currentIndex()
        
        requisitos = {
            0: {"campos": ["m", "v"], "nome": "Energia Cinética"},
            1: {"campos": ["m", "g", "h"], "nome": "Energia Potencial Gravitacional"},
        }
        
        campos_necessarios = requisitos[formula_index]["campos"]
        nome_calculo = requisitos[formula_index]["nome"]
        
        dados = self._obter_dados_entrada(campos_necessarios)

        if dados is None:
            QMessageBox.warning(self, "Atenção", f"Por favor, preencha todos os campos necessários para calcular a {nome_calculo}.")
            return

        # 2. Chama a função de cálculo correta
        passo_a_passo = "Erro interno de cálculo."
        
        try:
            if formula_index == 0: # Energia Cinética
                _, passo_a_passo = calcular_energia_cinetica(dados['m'], dados['v'])
                
            elif formula_index == 1: # Energia Potencial Gravitacional
                _, passo_a_passo = calcular_energia_potencial_grav(dados['m'], dados['g'], dados['h'])

        except Exception as e:
            QMessageBox.critical(self, "Erro de Execução", f"Ocorreu um erro inesperado no cálculo: {e}")
            return
            
        # 3. Exibe o passo a passo
        self.passo_a_passo_html = passo_a_passo # Salva o HTML
        self.resultado_output.setHtml(passo_a_passo)
        self.btn_ampliar.show() # Mostra o botão
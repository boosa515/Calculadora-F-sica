from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFormLayout, QGroupBox, QMessageBox, QTextEdit
)
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QDoubleValidator

from core.calculos_lancamento import (
    calcular_lancamento_obliquo,
    GRAVIDADE_TERRA
) 

class TelaLancamento(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent 
        self.passo_a_passo_html = "" # Armazena o HTML

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        titulo = QLabel("Lançamento Oblíquo")
        titulo.setStyleSheet("font-size: 18pt; font-weight: 600; margin-bottom: 15px;")
        layout.addWidget(titulo)
        
        explicacao = QLabel("Calcule a Altura Máxima e o Alcance de um projétil lançado em um ângulo, considerando a resistência do ar desprezível.")
        explicacao.setWordWrap(True)
        layout.addWidget(explicacao)

        # 1. ENTRADA DE DADOS
        dados_group = QGroupBox("Entrada de Dados")
        self.form_layout_dados = QFormLayout(dados_group)
        
        float_validator = QDoubleValidator()
        float_validator.setDecimals(4) 
        float_validator.setLocale(QLocale(QLocale.C))
        
        self.inputs = {}
        campos = [
            ("v0", "Velocidade Inicial (v₀ - m/s):"),
            ("angulo", "Ângulo de Lançamento (θ - graus):"),
            ("g", "Gravidade (g - m/s²):"),
        ]
        
        for key, label_text in campos:
            label = QLabel(label_text)
            line_edit = QLineEdit()
            line_edit.setValidator(float_validator)
            line_edit.setMaximumWidth(250)
            self.inputs[key] = line_edit
            self.form_layout_dados.addRow(label, line_edit)
            
        self.inputs['g'].setText(str(GRAVIDADE_TERRA))
        layout.addWidget(dados_group)

        # 2. BOTÃO DE CÁLCULO
        btn_calcular = QPushButton("Calcular Altura e Alcance")
        btn_calcular.setStyleSheet("padding: 8px; font-weight: bold;")
        btn_calcular.clicked.connect(self.realizar_calculo) 
        layout.addWidget(btn_calcular)
        
        # 3. ÁREA DE RESULTADOS
        self.resultado_output = QTextEdit()
        self.resultado_output.setReadOnly(True)
        self.resultado_output.setPlaceholderText("O passo a passo e os resultados (Altura Máxima, Alcance e Tempo de Voo) aparecerão aqui.")
        self.resultado_output.setStyleSheet("font-size: 11pt; padding: 10px;")
        layout.addWidget(self.resultado_output)

        # 4. BOTÃO AMPLIAR (NOVO)
        self.btn_ampliar = QPushButton("Ampliar Resultado")
        self.btn_ampliar.setStyleSheet("padding: 5px; font-weight: bold; font-size: 9pt;")
        self.btn_ampliar.clicked.connect(self.ampliar_resultado)
        self.btn_ampliar.hide() # Começa escondido
        layout.addWidget(self.btn_ampliar)

    def limpar_campos(self):
        """Limpa campos (exceto gravidade)."""
        self.inputs['v0'].clear()
        self.inputs['angulo'].clear()
        self.resultado_output.clear()
        self.passo_a_passo_html = ""
        self.btn_ampliar.hide()
        
    def ampliar_resultado(self):
        """Chama a janela principal para mostrar o resultado ampliado."""
        if self.passo_a_passo_html:
            self.parent_window.mostrar_tela_resultado(self.passo_a_passo_html)

    def realizar_calculo(self):
        self.resultado_output.clear()
        self.btn_ampliar.hide()
        self.passo_a_passo_html = ""
        
        campos_necessarios = ["v0", "angulo", "g"]
        
        # 1. Obtém e valida os dados
        dados = {}
        for campo in campos_necessarios:
            texto = self.inputs[campo].text().replace(',', '.')
            if not texto:
                QMessageBox.warning(self, "Atenção", "Por favor, preencha todos os campos necessários.")
                return
            try:
                dados[campo] = float(texto)
            except ValueError:
                QMessageBox.critical(self, "Erro de Entrada", "Valores numéricos inválidos.")
                return 

        # 2. Validação Específica do Ângulo
        if dados['angulo'] <= 0 or dados['angulo'] >= 90:
            QMessageBox.warning(self, "Atenção", "O ângulo deve estar entre 0° e 90° para um lançamento oblíquo padrão.")
            return

        # 3. Chama a função de cálculo
        try:
            _, passo_a_passo = calcular_lancamento_obliquo(
                dados['v0'], dados['angulo'], dados['g']
            )
        
        except Exception as e:
            QMessageBox.critical(self, "Erro de Execução", f"Ocorreu um erro inesperado no cálculo: {e}")
            return
            
        # 4. Exibe o passo a passo
        self.passo_a_passo_html = passo_a_passo # Salva o HTML
        self.resultado_output.setHtml(passo_a_passo)
        self.btn_ampliar.show() # Mostra o botão
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFormLayout, QGroupBox, QMessageBox, QComboBox, QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

# Importa as funções de cálculo da pasta 'core'
from core.calculos_queda_livre import (
    calcular_altura_final, 
    calcular_velocidade_final_gravidade,
    GRAVIDADE_TERRA
) 

class TelaQuedaLivre(QWidget):
    """
    Define a interface para Queda Livre e Lançamento Vertical.
    Permite escolher o valor da aceleração da gravidade e calcula a altura/velocidade final.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent 

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        # Título e Explicação Teórica
        titulo = QLabel("Queda Livre e Lançamento Vertical")
        titulo.setStyleSheet("font-size: 18pt; font-weight: 600; margin-bottom: 15px;")
        layout.addWidget(titulo)
        
        explicacao = QLabel("Estuda o movimento vertical, onde a única aceleração é a da gravidade ($g$). Usamos o sinal negativo na fórmula para $g$ (aceleração para baixo).")
        explicacao.setWordWrap(True)
        layout.addWidget(explicacao)

        # 1. SELETOR DE GRAVIDADE E FÓRMULA
        control_group = QGroupBox("Controles e Fórmulas")
        form_layout_control = QFormLayout(control_group)

        # Seletor de Gravidade
        self.combo_gravidade = QComboBox()
        self.combo_gravidade.addItems([
            f"Terra (g = {GRAVIDADE_TERRA} m/s²)", 
            "Lua (g ≈ 1.62 m/s²)",
            "Personalizada..."
        ])
        # Conexão que estava faltando ou incorreta
        self.combo_gravidade.currentIndexChanged.connect(self.atualizar_gravidade)
        
        # Campo para Gravidade Personalizada
        self.g_input_personalizado = QLineEdit(str(GRAVIDADE_TERRA))
        self.g_input_personalizado.setPlaceholderText("Insira o valor de g (m/s²)")
        self.g_input_personalizado.setEnabled(False) 
        
        form_layout_control.addRow("Gravidade (g):", self.combo_gravidade)
        form_layout_control.addRow("Valor de g:", self.g_input_personalizado)

        # Seletor de Fórmula
        self.combo_formula = QComboBox()
        self.combo_formula.addItems([
            "Altura Final (h = h₀ + v₀·t - ½ g·t²)", 
            "Velocidade Final (v = v₀ - g·t)", 
        ])
        self.combo_formula.currentIndexChanged.connect(self.limpar_campos)
        
        form_layout_control.addRow("Cálculo:", self.combo_formula)
        layout.addWidget(control_group)

        # 2. ENTRADA DE DADOS
        dados_group = QGroupBox("Entrada de Dados (Preencha os dados necessários)")
        self.form_layout_dados = QFormLayout(dados_group)
        
        # Cria um validador para números flutuantes
        float_validator = QDoubleValidator()
        float_validator.setDecimals(4) 
        
        self.inputs = {}
        campos = [
            ("h0", "Altura Inicial (h₀ - m):"),
            ("v0", "Velocidade Inicial (v₀ - m/s):"),
            ("t", "Tempo (t - s):"),
        ]
        
        for key, label_text in campos:
            label = QLabel(label_text)
            line_edit = QLineEdit()
            line_edit.setValidator(float_validator)
            line_edit.setMaximumWidth(250)
            self.inputs[key] = line_edit
            self.form_layout_dados.addRow(label, line_edit)
        
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
        self.resultado_output.setStyleSheet("font-size: 11pt; border: 1px solid #333; background-color: #eee; padding: 10px;")
        layout.addWidget(self.resultado_output)


    def atualizar_gravidade(self, index):
        """Atualiza o valor de g com base na seleção do ComboBox ou ativa o campo de personalização."""
        if index == 0: # Terra
            self.g_input_personalizado.setText(str(GRAVIDADE_TERRA))
            self.g_input_personalizado.setEnabled(False)
        elif index == 1: # Lua
            self.g_input_personalizado.setText("1.62")
            self.g_input_personalizado.setEnabled(False)
        elif index == 2: # Personalizada
            self.g_input_personalizado.setText("9.81") # Sugere o valor da Terra
            self.g_input_personalizado.setEnabled(True)

    def limpar_campos(self):
        """Limpa todos os campos de entrada e a área de resultados."""
        for key in self.inputs:
            self.inputs[key].clear()
        self.resultado_output.clear()

    def _obter_dados_entrada(self, campos_necessarios):
        """Tenta obter e converter os dados dos campos de entrada, incluindo a gravidade."""
        dados = {}
        
        # Tenta obter a gravidade (g)
        g_texto = self.g_input_personalizado.text().replace(',', '.')
        try:
            dados['g'] = float(g_texto)
        except ValueError:
             QMessageBox.critical(self, "Erro", "Gravidade (g) inválida.")
             return None
        
        # Tenta obter os demais campos necessários
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
        """Lê a entrada, valida e chama a função de cálculo correta no backend."""
        self.resultado_output.clear()
        formula_index = self.combo_formula.currentIndex()
        
        # Mapeamento dos campos necessários para cada fórmula
        requisitos = {
            0: {"campos": ["h0", "v0", "t"], "nome": "Altura Final"},
            1: {"campos": ["v0", "t"], "nome": "Velocidade Final"},
        }
        
        campos_necessarios = requisitos[formula_index]["campos"]
        nome_calculo = requisitos[formula_index]["nome"]
        
        dados = self._obter_dados_entrada(campos_necessarios)

        if dados is None:
            QMessageBox.warning(self, "Atenção", f"Por favor, preencha todos os dados necessários e verifique o valor de g.")
            return

        # 2. Chama a função de cálculo correta
        passo_a_passo = "Erro interno de cálculo."
        
        try:
            if formula_index == 0: # Altura Final
                _, passo_a_passo = calcular_altura_final(dados['h0'], dados['v0'], dados['g'], dados['t'])
                
            elif formula_index == 1: # Velocidade Final
                _, passo_a_passo = calcular_velocidade_final_gravidade(dados['v0'], dados['g'], dados['t'])

        except Exception as e:
            QMessageBox.critical(self, "Erro de Execução", f"Ocorreu um erro inesperado no cálculo: {e}")
            return
            
        # 3. Exibe o passo a passo
        self.resultado_output.setHtml(passo_a_passo)
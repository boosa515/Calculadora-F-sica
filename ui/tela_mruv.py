from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFormLayout, QGroupBox, QMessageBox, QComboBox, QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

# Importa as funções de cálculo da pasta 'core'
from core.calculos_mruv import (
    calcular_velocidade_final, 
    calcular_posicao_final, 
    calcular_torricelli
) 

class TelaMRUV(QWidget):
    """
    Define a interface gráfica para os cálculos de Movimento Retilíneo Uniformemente Variado (MRUV).
    
    Permite ao usuário selecionar entre as três principais fórmulas (Velocidade, Posição e Torricelli) 
    e exibe o resultado junto com o passo a passo detalhado.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent 

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        # Título e Explicação Teórica
        titulo = QLabel("Movimento Retilíneo Uniformemente Variado (MRUV)")
        titulo.setStyleSheet("font-size: 18pt; font-weight: 600; margin-bottom: 15px;")
        layout.addWidget(titulo)
        
        explicacao = QLabel("O MRUV descreve o movimento onde a aceleração (a) é constante e não nula. Escolha a grandeza que você deseja calcular e insira os dados conhecidos.")
        explicacao.setWordWrap(True)
        layout.addWidget(explicacao)

        # 1. SELETOR DE CÁLCULO
        formula_group = QGroupBox("Escolha o Cálculo")
        form_layout = QFormLayout(formula_group)
        
        self.combo_formula = QComboBox()
        self.combo_formula.addItems([
            "Velocidade Final (v = v₀ + a·t)", 
            "Posição Final (s = s₀ + v₀·t + ½ a·t²)", 
            "Velocidade sem Tempo (v² = v₀² + 2·a·Δs)"
        ])
        
        # Conecta o ComboBox ao método que LIMPA os campos
        self.combo_formula.currentIndexChanged.connect(self.limpar_campos)
        
        form_layout.addRow("Fórmula/Resultado:", self.combo_formula)
        layout.addWidget(formula_group)

        # 2. ENTRADA DE DADOS (TODOS OS CAMPOS)
        dados_group = QGroupBox("Entrada de Dados (Preencha os dados necessários)")
        self.form_layout_dados = QFormLayout(dados_group)
        
        # Cria um validador para números flutuantes (decimais)
        float_validator = QDoubleValidator()
        float_validator.setDecimals(4) 
        
        # Dicionário para armazenar o QLineEdit de cada campo
        self.inputs = {}
        
        # Criação de TODOS os campos possíveis
        campos = [
            ("s0", "Posição Inicial (s₀ - m):"),
            ("v0", "Velocidade Inicial (v₀ - m/s):"),
            ("a", "Aceleração (a - m/s²):"),
            ("t", "Tempo (t - s):"),
            ("ds", "Deslocamento (Δs - m):"),
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


    def limpar_campos(self):
        """
        Limpa todos os campos de entrada e a área de resultados.
        Este método é chamado quando o tipo de fórmula é alterado.
        """
        for key in self.inputs:
            self.inputs[key].clear()
        self.resultado_output.clear()

    def _obter_dados_entrada(self, campos_necessarios):
        """
        Tenta obter e converter os dados dos campos de entrada necessários para float.
        Retorna None se houver campos vazios ou erro de conversão (Validação de Dados).
        """
        dados = {}
        
        for campo in campos_necessarios:
            texto = self.inputs[campo].text().replace(',', '.')
            if not texto:
                return None  # Retorna erro se campo necessário estiver vazio
            
            try:
                # Converte o texto para float
                dados[campo] = float(texto)
            except ValueError:
                return None 
                
        return dados


    def realizar_calculo(self):
        """Lê a entrada, valida e chama a função de cálculo correta no backend (core)."""
        self.resultado_output.clear()
        formula_index = self.combo_formula.currentIndex()
        
        # Mapeamento dos campos necessários para cada fórmula
        requisitos = {
            0: {"campos": ["v0", "a", "t"], "nome": "Velocidade Final"},
            1: {"campos": ["s0", "v0", "a", "t"], "nome": "Posição Final"},
            2: {"campos": ["v0", "a", "ds"], "nome": "Torricelli"},
        }
        
        campos_necessarios = requisitos[formula_index]["campos"]
        nome_calculo = requisitos[formula_index]["nome"]
        
        # Validação dos dados
        dados = self._obter_dados_entrada(campos_necessarios)

        if dados is None:
            QMessageBox.warning(self, "Atenção", f"Por favor, preencha todos os campos necessários para calcular a {nome_calculo}.")
            return

        # 2. Chama a função de cálculo correta
        passo_a_passo = "Erro interno de cálculo."
        
        try:
            if formula_index == 0:
                _, passo_a_passo = calcular_velocidade_final(dados['v0'], dados['a'], dados['t'])
                
            elif formula_index == 1:
                _, passo_a_passo = calcular_posicao_final(dados['s0'], dados['v0'], dados['a'], dados['t'])

            elif formula_index == 2:
                resultado, passo_a_passo = calcular_torricelli(dados['v0'], dados['a'], dados['ds'])
                if resultado is None:
                    # Captura o erro físico (raiz de número negativo)
                    QMessageBox.critical(self, "Erro de Física", passo_a_passo)
                    return
        
        except Exception as e:
            QMessageBox.critical(self, "Erro de Execução", f"Ocorreu um erro inesperado no cálculo: {e}")
            return
            
        # 3. Exibe o passo a passo
        self.resultado_output.setHtml(passo_a_passo)
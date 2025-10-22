from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QFormLayout, QGroupBox, QMessageBox, QComboBox, QTextEdit
)
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QDoubleValidator

# Importa as funções de cálculo da pasta 'core'
from core.calculos_mcu import (
    calcular_velocidade_linear,
    calcular_velocidade_angular,
    calcular_periodo,
    calcular_frequencia,
    calcular_aceleracao_centripeta
)
import math # Para usar math.pi na interface se necessário

class TelaMCU(QWidget):
    """
    Define a interface gráfica para os cálculos de Movimento Circular Uniforme (MCU).
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.passo_a_passo_html = "" # Armazena o HTML do resultado

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        # Título e Explicação Teórica
        titulo = QLabel("Movimento Circular Uniforme (MCU)")
        titulo.setStyleSheet("font-size: 18pt; font-weight: 600; margin-bottom: 15px;")
        layout.addWidget(titulo)

        explicacao = QLabel("O MCU descreve o movimento de um objeto em trajetória circular com velocidade escalar (linear) constante. Escolha a grandeza a calcular e insira os dados conhecidos.")
        explicacao.setWordWrap(True)
        layout.addWidget(explicacao)

        # 1. SELETOR DE CÁLCULO
        formula_group = QGroupBox("Escolha o Cálculo")
        form_layout = QFormLayout(formula_group)

        self.combo_formula = QComboBox()
        self.combo_formula.addItems([
            "Velocidade Linear (v)",
            "Velocidade Angular (ω)",
            "Período (T)",
            "Frequência (f)",
            "Aceleração Centrípeta (a_cp)"
        ])
        self.combo_formula.currentIndexChanged.connect(self.limpar_campos)

        form_layout.addRow("Calcular:", self.combo_formula)
        layout.addWidget(formula_group)

        # 2. ENTRADA DE DADOS (TODOS OS CAMPOS POSSÍVEIS)
        dados_group = QGroupBox("Entrada de Dados (Preencha os dados necessários)")
        self.form_layout_dados = QFormLayout(dados_group)

        float_validator = QDoubleValidator()
        float_validator.setDecimals(6) # Aumenta precisão para rad/s etc
        float_validator.setLocale(QLocale(QLocale.C)) # Aceita PONTO

        self.inputs = {}
        campos = [
            ("r", "Raio da Trajetória (r - m):"),
            ("v", "Velocidade Linear (v - m/s):"),
            ("w", "Velocidade Angular (ω - rad/s):"),
            ("T", "Período (T - s):"),
            ("f", "Frequência (f - Hz):"),
        ]

        for key, label_text in campos:
            label = QLabel(label_text)
            line_edit = QLineEdit()
            line_edit.setValidator(float_validator)
            line_edit.setPlaceholderText("Deixe em branco se não souber")
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
        self.resultado_output.setStyleSheet("font-size: 11pt; padding: 10px;")
        layout.addWidget(self.resultado_output)

        # 5. BOTÃO AMPLIAR
        self.btn_ampliar = QPushButton("Ampliar Resultado")
        self.btn_ampliar.setStyleSheet("padding: 5px; font-weight: bold; font-size: 9pt;")
        self.btn_ampliar.clicked.connect(self.ampliar_resultado)
        self.btn_ampliar.hide() # Começa escondido
        layout.addWidget(self.btn_ampliar)

    def limpar_campos(self):
        """Limpa todos os campos de entrada e a área de resultados."""
        for key in self.inputs:
            self.inputs[key].clear()
        self.resultado_output.clear()
        self.passo_a_passo_html = ""
        self.btn_ampliar.hide()

    def ampliar_resultado(self):
        """Chama a janela principal para mostrar o resultado ampliado."""
        if self.passo_a_passo_html:
            self.parent_window.mostrar_tela_resultado(self.passo_a_passo_html)

    def _obter_dados_entrada(self, campos_possiveis):
        """
        Tenta obter e converter os dados dos campos de entrada para float.
        Retorna um dicionário com os valores convertidos ou None se houver erro.
        Campos vazios são ignorados (retornam None no dicionário).
        """
        dados = {}
        for campo in campos_possiveis:
            texto = self.inputs[campo].text().replace(',', '.')
            if not texto:
                dados[campo] = None # Campo vazio é válido (significa não fornecido)
            else:
                try:
                    dados[campo] = float(texto)
                except ValueError:
                    QMessageBox.warning(self, "Erro de Entrada", f"Valor inválido inserido no campo '{campo}'. Use apenas números.")
                    return None # Erro de conversão
        return dados


    def realizar_calculo(self):
        """Lê a entrada, valida e chama a função de cálculo correta."""
        self.resultado_output.clear()
        self.btn_ampliar.hide()
        self.passo_a_passo_html = ""

        formula_index = self.combo_formula.currentIndex()
        campos_possiveis = ["r", "v", "w", "T", "f"] # Todos os campos
        dados = self._obter_dados_entrada(campos_possiveis)

        if dados is None:
            return # Erro já foi mostrado

        # Chama a função de cálculo correta baseada no índice do ComboBox
        resultado = None
        passo_a_passo = "Erro: Combinação de dados insuficiente ou inválida para o cálculo selecionado."

        try:
            if formula_index == 0: # Velocidade Linear (v)
                resultado, passo_a_passo = calcular_velocidade_linear(r=dados['r'], T=dados['T'], f=dados['f'], w=dados['w'])
            elif formula_index == 1: # Velocidade Angular (ω)
                resultado, passo_a_passo = calcular_velocidade_angular(T=dados['T'], f=dados['f'], v=dados['v'], r=dados['r'])
            elif formula_index == 2: # Período (T)
                resultado, passo_a_passo = calcular_periodo(f=dados['f'], w=dados['w'], v=dados['v'], r=dados['r'])
            elif formula_index == 3: # Frequência (f)
                resultado, passo_a_passo = calcular_frequencia(T=dados['T'], w=dados['w'], v=dados['v'], r=dados['r'])
            elif formula_index == 4: # Aceleração Centrípeta (a_cp)
                resultado, passo_a_passo = calcular_aceleracao_centripeta(v=dados['v'], r=dados['r'], w=dados['w'])

            # Verifica se o cálculo foi bem sucedido (resultado não é None)
            if resultado is None:
                # Exibe a mensagem de erro retornada pela função de cálculo
                 QMessageBox.warning(self, "Dados Insuficientes", passo_a_passo.replace("Erro: ","")) # Mostra o erro específico
                 return

        except Exception as e:
            QMessageBox.critical(self, "Erro de Execução", f"Ocorreu um erro inesperado no cálculo: {e}")
            return

        # Exibe o passo a passo
        self.passo_a_passo_html = passo_a_passo
        self.resultado_output.setHtml(passo_a_passo)
        self.btn_ampliar.show()
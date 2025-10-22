from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt

class TelaResultado(QWidget):
    """
    Uma tela simples que exibe um conteúdo HTML em tela cheia (ampliado).
    Usada para mostrar o "passo a passo" dos cálculos de forma mais legível.
    """
    def __init__(self, parent=None, html_content=""):
        super().__init__(parent)
        self.parent_window = parent

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 10) # Margens
        layout.setAlignment(Qt.AlignTop)

        # 1. Caixa de Texto para exibir o resultado
        self.resultado_output = QTextEdit()
        self.resultado_output.setReadOnly(True)
        self.resultado_output.setStyleSheet("font-size: 12pt; padding: 10px;")
        
        # 2. Define o conteúdo
        self.resultado_output.setHtml(html_content)

        layout.addWidget(self.resultado_output)
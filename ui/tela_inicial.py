from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication # Importa QApplication para alternar o tema
from typing import Any

class TelaInicial(QWidget):
    """
    Tela inicial do aplicativo, que exibe o título centralizado 
    e botões grandes para a navegação dos módulos de cálculo.
    """
    def __init__(self, parent: Any):
        super().__init__(parent)
        self.parent_window = parent
        self.tema_atual = "dark" # Padrão, em sincronia com o main.py

        # Layout principal da Tela Inicial
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 1. Header Falso (Apenas para o Botão de Tema no canto superior direito)
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(20, 10, 20, 10)
        header_layout.addStretch() # Empurra o botão para a direita

        # Botão de Tema
        self.btn_alternar_tema = QPushButton("☀ Tema Claro")
        self.btn_alternar_tema.setFixedWidth(120)
        self.btn_alternar_tema.setStyleSheet("QPushButton {padding: 5px; font-weight: bold; font-size: 10pt;}")
        self.btn_alternar_tema.clicked.connect(self.alternar_tema)

        header_layout.addWidget(self.btn_alternar_tema)
        main_layout.addWidget(header_widget)

        # 2. Conteúdo Centralizado
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setAlignment(Qt.AlignCenter)

        # Título Central
        titulo = QLabel("Calculadora de Física")
        # Remova a cor daqui para que o QSS externo controle a cor
        titulo.setStyleSheet("font-size: 36pt; font-weight: bold; margin-bottom: 40px;")

        titulo.setAlignment(Qt.AlignCenter)
        # -- CORREÇÃO: Adiciona o título ao layout de conteúdo, não ao main_layout diretamente --
        content_layout.addWidget(titulo)

        # Layout para os Botões (Grid)
        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setSpacing(20)

        # --- AJUSTE AQUI para incluir MCU ---
        botoes_map = {
            # Linha 0
            "MRUV": (0, 0),
            "MCU": (0, 1),             # <--- NOVO BOTÃO AQUI
            "Queda Livre": (0, 2),     # <--- Posição ajustada
            # Linha 1
            "Energia": (1, 0),
            "Lançamento Oblíquo": (1, 1),
            "Conversor": (1, 2)        # <--- Posição ajustada
            # Você pode continuar adicionando linhas se precisar (ex: (2, 0), (2, 1), ...)
        }
        # --- FIM DO AJUSTE ---

        for nome, pos in botoes_map.items():
            btn = QPushButton(nome)
            btn.setStyleSheet("""
                QPushButton {
                    min-height: 80px; 
                    min-width: 250px;
                    font-size: 16pt;
                    border: 2px solid #5E81AC; /* Cor exemplo, pode ser sobrescrita pelo QSS */
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #81A1C1; /* Cor exemplo, pode ser sobrescrita pelo QSS */
                }
            """)
            # Conecta o clique para chamar a função mostrar_tela da janela principal
            btn.clicked.connect(lambda _, n=nome: self.parent_window.mostrar_tela(n))
            grid_layout.addWidget(btn, pos[0], pos[1])

        content_layout.addWidget(grid_widget)
        # -- CORREÇÃO: Remove o stretch para evitar que os botões subam demais --
        # content_layout.addStretch() 

        main_layout.addWidget(content_widget)
        main_layout.addStretch() # Adiciona stretch no layout principal para centralizar verticalmente


    def alternar_tema(self):
        """Alterna o tema e chama a função global para aplicar o estilo."""
        if self.tema_atual == "dark":
            self.tema_atual = "light"
            self.btn_alternar_tema.setText("☾ Tema Escuro")
        else:
            self.tema_atual = "dark"
            self.btn_alternar_tema.setText("☀ Tema Claro")

        # Chama a função global definida no main.py
        QApplication.instance().aplicar_tema(self.tema_atual)

        # Sincroniza o botão de tema na MainWindow (para quando você sair desta tela)
        # Evita chamar recursivamente se já estiver sincronizado
        if self.parent_window.tema_atual != self.tema_atual:
             self.parent_window.tema_atual = self.tema_atual # Atualiza o estado da janela pai
             if self.tema_atual == "dark":
                 self.parent_window.btn_alternar_tema.setText("☀ Tema Claro")
             else:
                 self.parent_window.btn_alternar_tema.setText("☾ Tema Escuro")
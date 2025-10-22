from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QFrame, QSizePolicy, QApplication
from PyQt5.QtCore import Qt
from typing import Any

# Importa as classes de TODAS as telas
from ui.tela_mruv import TelaMRUV
from ui.tela_queda_livre import TelaQuedaLivre
from ui.tela_energia import TelaEnergia
from ui.tela_lancamento import TelaLancamento
from ui.tela_conversor import TelaConversor
from ui.tela_inicial import TelaInicial 

class MainWindow(QMainWindow):
    """
    Janela principal que gerencia a navegação e o tema (claro/escuro).
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Física") 
        
        # Variável para rastrear o tema atual (dark é o padrão do main.py)
        self.tema_atual = "dark" 
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal vertical: Header (topo) + Área de Conteúdo (baixo)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Mapeia as opções (classes)
        self.telas_map = {
            "INICIAL": TelaInicial,
            "MRUV": TelaMRUV,
            "Queda Livre": TelaQuedaLivre,
            "Energia": TelaEnergia,
            "Lançamento Oblíquo": TelaLancamento,
            "Conversor": TelaConversor,
        }
        
        # Configura o Header e a Área de Conteúdo
        self._setup_header()
        self._setup_content_area()

        # Inicia com a tela inicial
        self.mostrar_tela("INICIAL")
        self.showMaximized()


    def _setup_header(self):
        """Cria e configura o cabeçalho com o botão Voltar e o Alternador de Tema."""
        self.header_widget = QWidget()
        self.header_widget.setObjectName("headerWidget")
        self.header_widget.setFixedHeight(60)
        
        header_layout = QHBoxLayout(self.header_widget)
        header_layout.setContentsMargins(15, 0, 15, 0)
        
        # 1. Botão Voltar (Esquerda)
        self.btn_voltar = QPushButton("← Voltar")
        self.btn_voltar.setFixedWidth(100)
        self.btn_voltar.setStyleSheet("QPushButton {padding: 5px; font-weight: bold; font-size: 10pt;}")
        self.btn_voltar.clicked.connect(lambda: self.mostrar_tela("INICIAL"))
        self.btn_voltar.hide() 
        
        header_layout.addWidget(self.btn_voltar)
        
        # Espaço flexível para empurrar o botão de tema para a direita
        header_layout.addStretch() 
        
        # 2. Alternador de Tema (Direita)
        self.btn_alternar_tema = QPushButton("☀ Tema Claro")
        self.btn_alternar_tema.setFixedWidth(120)
        self.btn_alternar_tema.setStyleSheet("QPushButton {padding: 5px; font-weight: bold; font-size: 10pt;}")
        self.btn_alternar_tema.clicked.connect(self.alternar_tema)
        
        header_layout.addWidget(self.btn_alternar_tema)
        
        self.main_layout.addWidget(self.header_widget)


    def _setup_content_area(self):
        """Configura o contêiner principal para as telas."""
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 0, 0) 
        self.main_layout.addWidget(self.content_area)
        
    
    def alternar_tema(self):
        """Alterna o tema entre escuro e claro e atualiza o texto do botão."""
        if self.tema_atual == "dark":
            self.tema_atual = "light"
            self.btn_alternar_tema.setText("☾ Tema Escuro")
        else:
            self.tema_atual = "dark"
            self.btn_alternar_tema.setText("☀ Tema Claro")
            
        # CHAMA A FUNÇÃO GLOBAL DIRETAMENTE AQUI, JÁ QUE ESTE MÉTODO PODE SER CHAMADO EXTERNAMENTE
        QApplication.instance().aplicar_tema(self.tema_atual) 


    def mostrar_tela(self, nome_tela):
        """
        Alterna a tela principal, gerenciando o botão 'Voltar' e o cabeçalho.
        """
        # 1. Limpa a área de conteúdo
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater() 

        # 2. Cria a nova instância da tela
        if nome_tela in self.telas_map:
            TelaClasse = self.telas_map[nome_tela]
            nova_tela = TelaClasse(self)

        # 3. Gerencia a visibilidade do cabeçalho e navegação
        if nome_tela == "INICIAL":
            self.btn_voltar.hide()
            self.header_widget.hide() 
            
            # Centraliza a tela inicial no layout vertical
            self.content_layout.addStretch()
            self.content_layout.addWidget(nova_tela)
            self.content_layout.addStretch()
        else:
            self.btn_voltar.show()
            self.header_widget.show()
            
            # Adiciona a tela de cálculo (sem stretch)
            self.content_layout.addWidget(nova_tela)
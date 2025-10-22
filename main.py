import sys
import os
from PyQt5.QtWidgets import QApplication

# Importa a classe principal
from ui.main_window import MainWindow

# Função que ajusta o caminho do arquivo para ser encontrado dentro do executável PyInstaller
def resource_path(relative_path):
    """Obtém o caminho absoluto para o recurso."""
    try:
        # Caminho do PyInstaller quando empacotado
        base_path = sys._MEIPASS
    except Exception:
        # Caminho normal quando executado no VS Code
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Variável global para armazenar os estilos carregados
global_styles = {}

def carregar_estilos(app):
    """Carrega os arquivos QSS usando o caminho ajustado e aplica o tema padrão."""
    global global_styles
    
    # 1. Carrega o tema escuro
    try:
        # Usa resource_path para encontrar o arquivo corretamente
        dark_path = resource_path("style.qss") 
        with open(dark_path, "r", encoding="utf-8") as file:
            global_styles['dark'] = file.read()
    except FileNotFoundError:
        print("Aviso: Arquivo 'style.qss' não encontrado.")
        
    # 2. Carrega o tema claro
    try:
        # Usa resource_path para encontrar o arquivo corretamente
        light_path = resource_path("light_style.qss")
        with open(light_path, "r", encoding="utf-8") as file:
            global_styles['light'] = file.read()
    except FileNotFoundError:
        print("Aviso: Arquivo 'light_style.qss' não encontrado.")
            
    # Aplica o tema escuro como padrão, se ele foi carregado
    if 'dark' in global_styles:
        app.setStyleSheet(global_styles['dark'])

def aplicar_tema(app, tema: str):
    """Aplica o tema (dark ou light) à aplicação a partir dos estilos carregados."""
    if tema in global_styles:
        app.setStyleSheet(global_styles[tema])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 1. Carrega todos os estilos (tentando encontrar no caminho PyInstaller)
    carregar_estilos(app) 
    
    # Adiciona a função global ao aplicativo
    app.aplicar_tema = lambda tema: aplicar_tema(app, tema)
    
    # 2. Cria e exibe a Janela Principal
    janela_principal = MainWindow()
    janela_principal.show()
    
    sys.exit(app.exec_())
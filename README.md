# < Calculadora de Física > ⚛️
<br/>

<br/>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/PyQt-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt Badge"/>
  <img src="https://img.shields.io/badge/Desktop_App-D057A7?style=for-the-badge" alt="Desktop App Badge"/>
</p>
<br/>

<br/>

## 💡 Sobre o Projeto

Calculadora de Física desenvolvida em **Python** com a biblioteca **PyQt5** como atividade para a disciplina de **Física Geral e Experimental I**, do curso de Engenharia de Computação.

O principal diferencial é o **motor de exibição de passo a passo** para cada cálculo, focado em auxiliar o estudante a visualizar a aplicação correta das fórmulas. A interface é moderna e possui suporte a **Modo Escuro / Modo Claro**.
<br/>

<br/>

### ⚙️ Principais Funcionalidades

* **Cálculos de MRUV:** Resolve as 3 fórmulas principais (Velocidade Final, Posição Final e Torricelli).
* **Cálculos de Queda Livre:** Calcula a altura e a velocidade final no movimento vertical.
* **Cálculos de Energia:** Calcula Energia Cinética e Energia Potencial Gravitacional.
* **Cálculos de Lançamento Oblíquo:** Encontra a Altura Máxima, Alcance e Tempo de Voo.
* **Conversor de Unidades:** Converte unidades comuns de Velocidade, Distância, Temperatura e Energia.
* **UI Avançada:** Interface gráfica com temas (Claro/Escuro) e uma tela de "Resultado Ampliado" para facilitar a leitura do passo a passo.

---

<br/>

<br/>

## 🛠️ Instalação e Execução

Existem duas maneiras de executar o projeto:

### Método 1: Executando o .exe (Recomendado - Windows)

O executável já compilado está disponível na pasta `dist/`.

1.  Navegue até a pasta `dist/`.
2.  Execute o arquivo `CalculadoraDeFisica.exe`.

<br/>

### Método 2: Executando a partir do Código-Fonte

Este método requer que você tenha o Python e as bibliotecas instaladas.

### Pré-requisitos

* Python 3.x

<br/>

<br/>

# 1. Configurar o Ambiente

Assumindo que você já clonou o repositório e está no diretório do projeto:

  Cria e ativa o ambiente virtual
  ```bash
  python -m venv venv
  ```
  
  Windows:
  ```bash
  .\venv\Scripts\activate
  ```
  
  macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
  
  Instala as dependências (PyQt5)
  ```bash
  pip install PyQt5
  ```
*(Nota: Se um arquivo `requirements.txt` for fornecido, use `pip install -r requirements.txt`)*

<br/>

# 2. Rodar a Aplicação
Com o ambiente virtual ativado, execute o script principal.


  Inicia a aplicação
  ```bash
  python main.py
  ```
  
  Acesso
  ```bash
  A janela principal da calculadora será aberta automaticamente.
  ```

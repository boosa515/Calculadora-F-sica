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

O principal diferencial é o **motor de exibição de passo a passo** para cada cálculo, focado em auxiliar o estudante a visualizar a aplicação correta das fórmulas. A interface possui suporte a **Modo Escuro / Modo Claro**.
<br/>

<br/>

### ⚙️ Principais Funcionalidades

* **Cálculos de MRUV:** Resolve as 3 fórmulas principais (Velocidade Final, Posição Final e Torricelli). Permite calcular MRU definindo a aceleração como zero.
* **Cálculos de MCU:** Calcula Velocidade Linear, Velocidade Angular, Período, Frequência e Aceleração Centrípeta. *(Novo!)*
* **Cálculos de Queda Livre:** Calcula a altura e a velocidade final no movimento vertical.
* **Cálculos de Energia:** Calcula Energia Cinética e Energia Potencial Gravitacional.
* **Cálculos de Lançamento Oblíquo:** Encontra a Altura Máxima, Alcance e Tempo de Voo.
* **Conversor de Unidades:** Converte unidades comuns de Velocidade, Energia, Distância e Temperatura.
* **UI Avançada:** Interface gráfica com temas (Claro/Escuro) e uma tela de "Resultado Ampliado" para facilitar a leitura do passo a passo.

<br/>

## Download
<p align=>
  <strong>Windows:</strong> <a href="https://github.com/boosa515/Calculadora-F-sica/raw/refs/heads/main/dist/CalculadoraDeFisica.exe"><strong>Clique Aqui (Direto)</strong></a> ou <strong></strong> <a href="dist/"><strong>Clique Aqui (Baixar da pasta)</strong></a>
</p>

<br/>


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
  
  Instala as dependências (PyQt5 e PyInstaller)
  ```bash
  pip install PyQt5 pyinstaller
  ```
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

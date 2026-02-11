# 2048 - Algoritmos e Estruturas de Dados (Python Edition) 🔢

Este projeto foi desenvolvido como um trabalho acadêmico para a disciplina de algoritmos, focado na implementação de lógica de matrizes e no desenvolvimento de interfaces híbridas (CLI e GUI). O objetivo principal é consolidar conhecimentos de manipulação de dados e arquitetura modular em Python.

## 🎓 Foco Acadêmico e Habilidades Desenvolvidas

O projeto reflete competências essenciais de Engenharia de Computação, aplicando conceitos teóricos em uma aplicação prática:

* **Manipulação Algorítmica de Matrizes:** Implementação de funções de transposição e inversão para processar movimentos em todas as direções utilizando um único motor de lógica para a esquerda.
* **Arquitetura Modular:** Separação clara entre a lógica de negócio, a interface de usuário e a persistência de dados em módulos distintos.
* **Persistência de Dados e I/O:** Gerenciamento de arquivos para salvar e carregar estados de jogo, além de manter um histórico de pontuação em arquivos de texto.
* **Tratamento de Argumentos de Linha de Comando:** Utilização de flags para permitir que o usuário escolha a experiência de uso (Terminal vs Gráfico) sem alterar o código-fonte.

## 🛠️ Tecnologias e Bibliotecas

* **`Tkinter`**: Utilizada para a criação da interface gráfica, incluindo o gerenciamento da grade de células e atualização dinâmica de cores baseada nos valores.
* **`Argparse`**: Implementada para gerenciar os parâmetros de inicialização do sistema via terminal.
* **`OS` & `Sys`**: Usadas para a portabilidade do sistema de arquivos e controle do fluxo do programa.
* **`Random`**: Aplicada no algoritmo de spawn para gerar novos números (2 ou 4) em espaços vazios da matriz.
* **`Getch` / `Msvcrt`**: Bibliotecas essenciais para a captura de input em tempo real no modo terminal, garantindo jogabilidade fluida no Windows e Linux.

## 🚀 Como Executar

O programa detecta automaticamente o sistema operacional para configurar os comandos de teclado.

1. **Modo Gráfico (Completo):**

    ```bash
    python main.py --gui
    ```

2. **Modo Terminal (Clássico):**

    ```bash
    python main.py
    ```

3. **Carregar um Save Específico:**

    ```bash
    python main.py --carregar nome_do_arquivo
    ```

## 🎮 Comandos do Jogo

* **W, A, S, D** ou **Setas**: Movimentação das peças.
* **P**: Abre o Menu de Pause (Disponível tanto na GUI quanto no Terminal).
* **Enter**: Confirmar seleção nos menus do terminal.

---
**Desenvolvido por:** Pedro Augusto Costa Alves
**Instituição:** Universidade do Estado do Rio de Janeiro (UERJ)

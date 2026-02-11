# 2048 - Algoritmos e Estruturas de Dados (Python Edition) 🔢

[cite_start]Este projeto foi desenvolvido como um trabalho acadêmico para a disciplina de algoritmos, focado na implementação de lógica de matrizes e no desenvolvimento de interfaces híbridas [CLI e GUI](cite:1,3). O objetivo principal é consolidar conhecimentos de manipulação de dados e arquitetura modular em Python.

## 🎓 Foco Acadêmico e Habilidades Desenvolvidas

O projeto reflete competências essenciais de Engenharia de Computação, aplicando conceitos teóricos em uma aplicação prática:

* [cite_start]**Manipulação Algorítmica de Matrizes:** Implementação de funções de transposição (`transpor`) e inversão (`inverter`) para processar movimentos em todas as direções utilizando um único motor de lógica para a esquerda[cite: 11, 12, 13].
* [cite_start]**Arquitetura Modular:** Separação clara entre a lógica de negócio (`logica.py`), a interface de usuário (`gui.py` e `menu.py`) e a persistência de dados (`arquivos.py`)[cite: 6].
* [cite_start]**Persistência de Dados e I/O:** Gerenciamento de arquivos para salvar e carregar estados de jogo, além de manter um histórico de pontuação em arquivos de texto[cite: 19].
* **Tratamento de Argumentos de Linha de Comando:** Utilização de flags para permitir que o usuário escolha a experiência de uso (Terminal vs Gráfico) sem alterar o código-fonte.

## 🛠️ Tecnologias e Bibliotecas

* [cite_start]**`Tkinter`**: Utilizada para a criação da interface gráfica, incluindo o gerenciamento da grade de células e atualização dinâmica de cores baseada nos valores[cite: 20, 21].
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

* [cite_start]**W, A, S, D** ou **Setas**: Movimentação das peças[cite: 17].
* [cite_start]**P**: Abre o Menu de Pause [Disponível tanto na GUI quanto no Terminal](cite: 16, 17).
* [cite_start]**Enter**: Confirmar seleção nos menus do terminal[cite: 18].

---
[cite_start]**Desenvolvido por:** Pedro Augusto Costa Alves [cite: 2]
**Instituição:**  Universidade do Estado do Rio de Janeiro (UERJ)

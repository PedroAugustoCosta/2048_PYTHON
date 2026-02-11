import tkinter as tk
from tkinter import messagebox, filedialog
import os
import logica


CORES_TILES = {
    0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
    16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
    256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
}

def atualizar_interface(dados_gui):
    
    tela = dados_gui['tela']
    estado = dados_gui['estado']
    matriz_celulas = dados_gui['celulas']
    
    tela.title(f"2048 - {estado['nome']} | Score: {estado['pontuacao']}")
    
    tabuleiro = estado['tabuleiro']
    
    for i in range(4):
        for j in range(4):
            valor = tabuleiro[i][j]
            
            cor_fundo = CORES_TILES.get(valor, "#3c3a32") 
            texto = str(valor) if valor > 0 else ""
            cor_texto = "#776e65" if valor < 8 else "#f9f6f2"
            
            label_widget = matriz_celulas[i][j]
            label_widget.configure(text=texto, bg=cor_fundo, fg=cor_texto)

def processar_tecla(event, dados_gui):
    
    tecla = event.keysym.lower()
    
    estado = dados_gui['estado']
    callback_pause = dados_gui['callback_pause']
    tela = dados_gui['tela']

    if tecla == 'p':
        tela.withdraw() 
        acao = callback_pause(estado) 
        
        if acao == "voltar":
            tela.deiconify() 
        else:
            tela.destroy() 
        return

    if tecla in ['w', 'a', 's', 'd', 'up', 'down', 'left', 'right']:
        mapa = {'up':'w', 'down':'s', 'left':'a', 'right':'d'}
        comando = mapa.get(tecla, tecla)
        
        novo_estado, moveu = logica.realiza_jogada(estado, comando)
        
        if moveu:
            dados_gui['estado'] = novo_estado
            
            atualizar_interface(dados_gui)
            
            if logica.checa_game_over(novo_estado):
                messagebox.showinfo("Fim de Jogo", f"Game Over!\nScore Final: {novo_estado['pontuacao']}")
                tela.destroy()

def iniciar_gui_jogo(estado_inicial, callback_pause):
    
    tela = tk.Tk()
    
    
    frame_jogo = tk.Frame(tela, bg="#92877d")
    frame_jogo.pack(padx=10, pady=10)
    
    
    matriz_celulas = []
    for i in range(4):
        linha_celulas = []
        for j in range(4):
            celula = tk.Label(frame_jogo, text="", bg="#cdc1b4", font=("Helvetica", 20, "bold"), width=4, height=2)
            celula.grid(row=i, column=j, padx=5, pady=5)
            linha_celulas.append(celula)
        matriz_celulas.append(linha_celulas)
    
    
    dados_gui = {
        "tela": tela,
        "estado": estado_inicial,
        "celulas": matriz_celulas,
        "callback_pause": callback_pause
    }
    
    
    atualizar_interface(dados_gui)
    
   
    tela.bind("<Key>", lambda event: processar_tecla(event, dados_gui))
    
    
    tela.mainloop()

def menu_botoes(titulo, opcoes):
    janela = tk.Tk()
    janela.title(titulo)
    janela.geometry("300x400")
    
    escolha = [None] 

    def clicar(valor):
        escolha[0] = valor
        janela.destroy()

    tk.Label(janela, text=titulo, font=("Arial", 16, "bold")).pack(pady=20)

    for texto, valor_retorno in opcoes:
        tk.Button(janela, text=texto, command=lambda v=valor_retorno: clicar(v), 
                  width=20, height=2).pack(pady=5)

    janela.wait_window()
    return escolha[0]

def menu_principal_gui():
    opcoes = [
        ("Novo Jogo", "a"),
        ("Carregar Jogo", "b"),
        ("Histórico", "c"),
        ("Sair", "d")
    ]
    return menu_botoes("Menu Principal", opcoes)

def menu_pause_gui(estado):
    opcoes = [
        ("Novo Jogo", "novo"),
        ("Carregar", "load_gui"),
        ("Salvar", "save_gui"),
        ("Voltar ao Jogo", "voltar"),
        ("Menu Principal", "menu"),
        ("Sair", "sair")
    ]
    return menu_botoes(f"Pause ({estado['nome']}: {estado['pontuacao']})", opcoes)

def menu_arquivo_gui(modo):
    tela = tk.Tk()
    tela.withdraw() 
    
    pasta_inicial = os.path.join(os.getcwd(), "saves")
    os.makedirs(pasta_inicial, exist_ok=True)
    
    if modo == 'salvar':
        arquivo = filedialog.asksaveasfilename(
            initialdir=pasta_inicial, 
            title="Salvar Jogo",
            defaultextension=".save",
            filetypes=[("Arquivos 2048", "*.save")]
        )
    else:
        arquivo = filedialog.askopenfilename(
            initialdir=pasta_inicial, 
            title="Carregar Jogo",
            filetypes=[("Arquivos 2048", "*.save")]
        )
    
    tela.destroy()
    
    if not arquivo: return None
    
    return os.path.basename(arquivo).replace(".save", "")
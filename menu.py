import argparse
import os
import sys
from sys import platform
import logica
import arquivos
import gui



if platform == 'linux': 
    from getch import getch
if platform == 'win32': 
    from msvcrt import getch


TECLA_ENTER = 13
TECLA_W = 119  
TECLA_S = 115 
TECLA_A = 97
TECLA_D = 100
TECLA_P = 112



CONFIG_GUI = {
    "principal": False,
    "pause": False,
    "arquivos": False,
    "jogo": False
}



def limpar_tela():
    if platform == 'linux':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')

def pausar_tela():
    input("\nPressione [ENTER] para continuar...")



def navegar_menu(titulo, opcoes):
    
    selecionado = 0
    total = len(opcoes)

    while True:
        limpar_tela()
        print("=" * 30)
        print(f" {titulo}")
        print("=" * 30)
        print("Use 'W' (Cima), 'S' (Baixo) e ENTER\n")

        for i in range(total):
            if i == selecionado:
                print(f" -> {opcoes[i]}  <--")
            else:
                print(f"    {opcoes[i]}")
        
        print("\n" + "=" * 30)

       
        codigo = ord(getch())

        if codigo == TECLA_ENTER:
            return selecionado
        elif codigo == TECLA_W :
            selecionado = (selecionado - 1) % total
        elif codigo == TECLA_S :
            selecionado = (selecionado + 1) % total


def menu_interacao_arquivos(modo):
    if CONFIG_GUI['arquivos']:
        return gui.menu_arquivo_gui(modo)
    
    while True:
        limpar_tela()
        print(f"💾 MENU {modo.upper()}")
        saves = arquivos.listar_saves_disponiveis()
        
        if not saves: print(" (Nenhum save encontrado)")
        else: 
            for s in saves: print(f" - {s}")
        
        print("\nDigite '0' para voltar.")
        nome = input("Nome do arquivo: ").strip()
        
        if nome == '0': 
            return None
        
        if modo == 'salvar':
            if arquivos.verificar_existencia(nome):
               
                idx = navegar_menu(f"Arquivo '{nome}' existe. Sobrescrever?", ["Sim", "Não"])
                if idx == 1: 
                    continue 
            return nome
            
        elif modo == 'carregar':
            if arquivos.verificar_existencia(nome): 
                return nome
            else: 
                print("❌ Arquivo não encontrado."); pausar_tela()



def menu_pause(estado):
    if CONFIG_GUI['pause']:
        op = gui.menu_pause_gui(estado)
    
        if op == "novo": 
            return "novo"
        elif op == "load_gui":
            nome = menu_interacao_arquivos('carregar')
            if nome: 
                return f"load:{nome}"
        elif op == "save_gui":
            nome = menu_interacao_arquivos('salvar')
            if nome: 
                arquivos.salvar_estado(estado, nome)
                if not CONFIG_GUI['jogo']: 
                    print("Salvo!"); pausar_tela()
        elif op == "voltar": 
            return "voltar"
        elif op == "menu": 
            return "menu"
        elif op == "sair": 
            sys.exit()
        return "voltar"
    
  
    opcoes = ["Voltar ao Jogo", "Salvar Jogo", "Carregar Jogo", "Novo Jogo", "Menu Principal", "Sair"]
    idx = navegar_menu(f"PAUSE ({estado['pontuacao']} pts)", opcoes)
    
    if idx == 0: 
        return "voltar"
    elif idx == 1:
        nome = menu_interacao_arquivos('salvar')
        if nome:
            arquivos.salvar_estado(estado, nome)
            print("Salvo!"); pausar_tela()
        return menu_pause(estado) 
    elif idx == 2:
        nome = menu_interacao_arquivos('carregar')
        if nome: 
            return f"carregar:{nome}"
    elif idx == 3: 
        return "novo"
    elif idx == 4: 
        return "menu"
    elif idx == 5: 
        sys.exit()
    return "voltar"


def capturar_input_jogo():
    
    
    
    char = getch()
    
    
    if not char:
        return None

    
    codigo = ord(char)
    
   
    if codigo == TECLA_W : 
        return 'w'
    if codigo == TECLA_A : 
        return 'a'
    if codigo == TECLA_S : 
        return 's'
    if codigo == TECLA_D: 
        return 'd'
    if codigo == TECLA_P : 
        return 'p'
    
   

    if platform == 'win32' and codigo == 224:
        
        char_seta = getch()
        
        if char_seta:
            codigo_seta = ord(char_seta)
            if codigo_seta == 72: 
                return 'w' 
            if codigo_seta == 80: 
                return 's' 
            if codigo_seta == 75: 
                return 'a' 
            if codigo_seta == 77: 
                return 'd' 
         
    return None
    

def loop_jogo(estado_inicial=None):


    if estado_inicial is None:
        if not CONFIG_GUI['jogo']: 
            limpar_tela()
        nome = input("Nome do Jogador: ").strip().upper()
        if not nome: 
            nome = "ANONIMO"
        estado_atual = logica.inicia_jogo(nome)
    
    else:
        estado_atual = estado_inicial
    
    if CONFIG_GUI['jogo']:
        def cb_pause(est): 
            return menu_pause(est)
        gui.iniciar_gui_jogo(estado_atual, cb_pause)
        
        
        return 
    
    melhor_score = arquivos.ler_melhor_score(estado_atual['nome'])
   
    while True:
        limpar_tela()
        print("="*30)
        print(f"JOGADOR: {estado_atual['nome']} | SCORE: {estado_atual['pontuacao']} | REC: {melhor_score}")
        print("="*30)
        for linha in estado_atual['tabuleiro']:
            print("|", end="")
            for num in linha:
                if num != 0 :
                    txt = str(num) 
                else: 
                    txt =" "
                print(f"{txt:^5}|", end="")
            print("\n" + "-"*25)
        print("WASD ou Setas: Mover | P: Pause")
        
        if logica.checa_game_over(estado_atual):
            print("\n💀 GAME OVER!")
            arquivos.escrever_historico(estado_atual['nome'], estado_atual['pontuacao'], "DERROTA")
            pausar_tela()
            break
            
        
        cmd = capturar_input_jogo()
        
        if not cmd: 
            continue 
            
        if cmd == 'p':
            acao = menu_pause(estado_atual)
            if acao == "novo": 
                loop_jogo(None); return
            elif acao == "menu": 
                return
            elif acao == "voltar": 
                continue
            
            elif acao and acao.startswith("carregar:"):
                nome_arq = acao.split(":")[1]
                novo_est = arquivos.carregar_estado(nome_arq)
                
                if novo_est: 
                    estado_atual = novo_est
                    melhor_score = arquivos.ler_melhor_score(estado_atual['nome'])
                    
        
        elif cmd in ['w', 'a', 's', 'd']:
            novo_estado, moveu = logica.realiza_jogada(estado_atual, cmd)
            if moveu:
                
                estado_atual = novo_estado
                if estado_atual['pontuacao'] > melhor_score: 
                    melhor_score = estado_atual['pontuacao']
                    
                arquivos.salvar_estado(estado_atual, arquivos.CONFIG['autosave_nome'], eh_autosave=True)
                


def menu_principal():

    while True:
        op = None
        if CONFIG_GUI['principal']:
            
            op = gui.menu_principal_gui()
            if op is None: 
                sys.exit()
            
            
            if op == 'a': 
                idx = 0
            elif op == 'b': 
                idx = 1
            elif op == 'c': 
                idx = 2
            elif op == 'd': 
                idx = 3
        else:
            
            opcoes = ["Novo Jogo", "Carregar Jogo", "Ver Histórico", "Sair"]

            idx = navegar_menu("2048 - MENU PRINCIPAL", opcoes)
        
        if idx == 0: 
            loop_jogo(None)
        
        elif idx == 1:
            nome = menu_interacao_arquivos('carregar')
            
            if nome:
                est = arquivos.carregar_estado(nome)
                if est: loop_jogo(est)
            
        elif idx == 2:
            limpar_tela()
            txt = arquivos.ler_texto_historico()
            print(txt if txt else "Vazio.")
            pausar_tela()
            
        elif idx == 3: 
            sys.exit()
       



import random




def inicia_jogo(nome_jogador):
   
    tabuleiro = []
    for i in range(4):
        tabuleiro.append([0, 0, 0, 0])
    
    
    adiciona_novo_numero_na_matriz(tabuleiro)
    adiciona_novo_numero_na_matriz(tabuleiro)
    
    
    estado = {
        "nome": nome_jogador,
        "pontuacao": 0,
        "tabuleiro": tabuleiro
    }
    return estado



def adiciona_novo_numero_na_matriz(tabuleiro):
    
    vazios = []
    for l in range(4):
        for c in range(4):
            if tabuleiro[l][c] == 0:
                vazios.append([l, c]) 
    
    if len(vazios) > 0:
        coord = random.choice(vazios)
        r = coord[0]
        c = coord[1]
        if random.random() < 0.9:
            tabuleiro[r][c] = 2
        else:
            tabuleiro[r][c] = 4

def move_peca_sem_zeros(linha):
    nova_linha = []
    for item in linha:
        if item != 0:
            nova_linha.append(item)
    while len(nova_linha) < 4:
        nova_linha.append(0)
    return nova_linha

def fundir(linha):
    
    pontos = 0
    for i in range(3):
        if linha[i] != 0 and linha[i] == linha[i + 1]:
            linha[i] = linha[i] * 2
            pontos = pontos + linha[i] 
            linha[i + 1] = 0
    return linha, pontos

def move_esquerda(linha):
    linha = move_peca_sem_zeros(linha)
    linha, pts = fundir(linha)
    linha = move_peca_sem_zeros(linha)
    return linha, pts

def transpor(tabuleiro):
    novo = []
    for i in range(4):
        novo.append([0]*4)
    for i in range(4):
        for j in range(4):
            novo[i][j] = tabuleiro[j][i]
    return novo

def inverter(linha):
    nova = []
    tam = len(linha)
    for i in range(tam):
        nova.append(linha[tam - 1 - i])
    return nova



def realiza_jogada(estado_atual, direcao):
    tabuleiro_original = estado_atual['tabuleiro']
    tabuleiro_temp = [linha.copy() for linha in tabuleiro_original]
    
    pontos_ganhos_jogada = 0
    
    
    if direcao == 'w':   
        tabuleiro_temp = transpor(tabuleiro_temp)
    elif direcao == 's': 
        tabuleiro_temp = transpor(tabuleiro_temp)
        
        temp = []
        for l in tabuleiro_temp: temp.append(inverter(l))
        tabuleiro_temp = temp
    elif direcao == 'd': 
        temp = []
        for l in tabuleiro_temp: temp.append(inverter(l))
        tabuleiro_temp = temp
    
    
    estado_processado = []
    for linha in tabuleiro_temp:
        nova_l, pts = move_esquerda(linha)
        estado_processado.append(nova_l)
        pontos_ganhos_jogada = pontos_ganhos_jogada + pts
    tabuleiro_temp = estado_processado

   
    if direcao == 'w':
        tabuleiro_temp = transpor(tabuleiro_temp)
    elif direcao == 's':
        temp = []
        for l in tabuleiro_temp: temp.append(inverter(l))
        tabuleiro_temp = temp
        tabuleiro_temp = transpor(tabuleiro_temp)
    elif direcao == 'd':
        temp = []
        for l in tabuleiro_temp: temp.append(inverter(l))
        tabuleiro_temp = temp
    
    
    if tabuleiro_temp != tabuleiro_original:
        
        
        adiciona_novo_numero_na_matriz(tabuleiro_temp)
        
       
        novo_estado = {
            "nome": estado_atual['nome'],
            "pontuacao": estado_atual['pontuacao'] + pontos_ganhos_jogada,
            "tabuleiro": tabuleiro_temp
        }
        
        return novo_estado, True
    else:
        
        return estado_atual, False
def checa_game_over(estado):
    tab = estado['tabuleiro']
    
   
    for linha in tab:
        if 0 in linha: return False
    
    
    for l in range(4):
        for c in range(4):
            val = tab[l][c]
            if c < 3 and val == tab[l][c+1]: return False
            if l < 3 and val == tab[l+1][c]: return False
            
    return True


def validar_estado(estado_dict):
    if isinstance(estado_dict, dict):
        if "nome" in estado_dict and "pontuacao" in estado_dict and "tabuleiro" in estado_dict:
            return True
    return False
import os
import logica

CONFIG = {
    "pasta_saves": "saves",
    "extensao": ".save",
    "arq_registro": "registro_saves.txt",
    "arq_historico": "historico.txt",
    "autosave_nome": "autosave"
}


os.makedirs(CONFIG["pasta_saves"], exist_ok=True)
def gera_caminho(nome_arq):
    nome_completo = nome_arq + CONFIG["extensao"]
    caminho = os.path.join(CONFIG["pasta_saves"], nome_completo)

    return caminho

def verificar_existencia(nome_arq):
    
    caminho = gera_caminho(nome_arq)
    
    if os.path.exists(caminho):
        if os.path.getsize(caminho) > 0:
            return True
    return False

def arquivo_bruto_valido(caminho):
    
    if os.path.exists(caminho):
        if os.path.getsize(caminho) > 0:
            return True
    return False


def registrar_nome_no_indice(nome):
    caminho = CONFIG["arq_registro"]
    nomes = []
    
    if arquivo_bruto_valido(caminho):
        f = open(caminho, 'r')
        nomes = f.read().splitlines()
        f.close()
    
    if nome not in nomes:
        f = open(caminho, 'a')
        f.write(nome + "\n")
        f.close()

def listar_saves_disponiveis():
    caminho = CONFIG["arq_registro"]
    if not arquivo_bruto_valido(caminho):
        return []
        
    f = open(caminho, 'r')
    lista = f.read().splitlines()
    f.close()
    
    
    validos = []
    for nome in lista:
        if verificar_existencia(nome):
            validos.append(nome)
    return validos

def monta_matriz(estado):
    linhas_txt = []
    for linha in estado['tabuleiro']:
        str_nums = []
        for x in linha: 
            str_nums.append(str(x))
        linhas_txt.append(",".join(str_nums))
    matriz_str = ";".join(linhas_txt)
    return matriz_str

def salvar_estado(estado, nome_arq, eh_autosave=False):
    
    
    
    
    matriz_str = monta_matriz(estado)

    texto_final = f"{estado['nome']}|{estado['pontuacao']}|{matriz_str}"

    
    nome_completo = nome_arq + CONFIG["extensao"]
    caminho = os.path.join(CONFIG["pasta_saves"], nome_completo)
    
    f = open(caminho, 'w')
    f.write(texto_final)
    f.close()
    
    if not eh_autosave:
        registrar_nome_no_indice(nome_arq)
        return True 
    return True

def carregar_estado(nome_arq):
    
    caminho = gera_caminho(nome_arq)
    if not arquivo_bruto_valido(caminho): 
        return None

    f = open(caminho, 'r')
    dados = f.read().strip()
    f.close()
    
    partes = dados.split('|')
    if len(partes) < 3: 
        return None
    
    
    nome = partes[0]
    pontos = 0
    if partes[1].isdigit():
        pontos = int(partes[1])
    
    matriz_str = partes[2]
    tab_rec = []
    for l in matriz_str.split(';'):
        linha_int = []
        for n in l.split(','):
            if n.isdigit() :
                linha_int.append(int(n))
            else: 
                linha_int.append(0)
        tab_rec.append(linha_int)
        
    estado = {
        "nome": nome,
        "pontuacao": pontos,
        "tabuleiro": tab_rec
    }
    
   
    if logica.validar_estado(estado):
        return estado
    return None



def ler_melhor_score(nome_jogador):
    melhor = 0
    caminho = CONFIG["arq_historico"]
    if not arquivo_bruto_valido(caminho): 
        return 0
    
    f = open(caminho, 'r')
    linhas = f.read().splitlines()
    f.close()
    
    for linha in linhas:
        partes = linha.split('|')
        if len(partes) >= 2:
            n = partes[0].split(':')[1].strip()
            s_str = partes[1].split(':')[1].strip()
            if s_str.isdigit():
                s = int(s_str)
                if n == nome_jogador and s > melhor: 
                    melhor = s
    return melhor

def escrever_historico(nome, pontos, resultado):
    msg = f"Nome: {nome} | Score: {pontos} | Resultado: {resultado}\n"
    f = open(CONFIG["arq_historico"], 'a')
    f.write(msg)
    f.close()

def ler_texto_historico():
    
    caminho = CONFIG["arq_historico"]
    if arquivo_bruto_valido(caminho):
        f = open(caminho, 'r')
        texto = f.read()
        f.close()
        return texto
    return None
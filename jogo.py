def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota:
        frota[nome_navio] += posicoes
    else:
        frota[nome_navio] = posicoes
    
    return frota
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_saida=[]
    
    for i in range (tamanho):
        posicao =[linha,coluna]
        if orientacao == "vertical":
            posicao[0] += i
        if orientacao == "horizontal":
            posicao[1] += i
        lista_saida.append(posicao)    
    return lista_saida     

def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    

    lista_ocupados=[]
    lista_posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    for i in frota.values():
        for navio in i:
            for posicao in navio:
                if posicao  in lista_posicoes:
                     return False 
          
    # Verificar dentro tabuleiro 
    for posicao in lista_posicoes:
        if posicao[0] <0 or posicao[0] >9 or posicao[1] <0 or posicao[1] >9:
                    return False
                
    return True


def faz_jogada(tabuleiro,linha,coluna):
    print (tabuleiro)
    posicao = tabuleiro[linha][coluna]
    if posicao == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"  
    return tabuleiro    

def posiciona_frota(frota):
    lista = list(frota.items())
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]     
    
    for navio, posicoes in lista:
        for lugar in posicoes:
            for i, j in lugar:
                tabuleiro[i][j] = 1
    return tabuleiro

def afundados(frota, tabuleiro_atual):
    soma = 0
    for navio, posicoes in frota.items():
        for lugar in posicoes:
            afundado = True
            for i, j in lugar:
                if tabuleiro_atual[i][j] != 'X':
                    afundado = False
                    break
            if afundado:
                soma += 1
    return soma

def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_saida=[]
    
    for i in range (tamanho):
        posicao =[linha,coluna]
        if orientacao == "vertical":
            posicao[0] += i
        if orientacao == "horizontal":
            posicao[1] += i
        lista_saida.append(posicao)    
    return lista_saida
    
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [].append(posicoes)

    return frota


def posicao_valida(frota: dict, linha: int, coluna: int, orientacao: str, tamanho: int) -> bool:
    posicoes_ocupadas = []
    for i in frota.values():
        for j in i:
            for k in j:
                posicoes_ocupadas.append(k)

    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    for i in posicao:
        if i[0] >= 10 or i[1] >= 10:
            return False
    for i in posicao:
        if i in posicoes_ocupadas:
            return False
    return True


navios = {
    "porta-aviões": {'quantidade': 1, 'tamanho': 4},
    "navio-tanque": {'quantidade': 2, 'tamanho': 3},
    "contratorpedeiro": {'quantidade': 3, 'tamanho': 2},
    "submarino": {'quantidade': 4, 'tamanho': 1}
}

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for navio, infos in navios.items():
    while infos["quantidade"] > 0:
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {infos['tamanho']}")
        linha = int(input("Qual é a linha? "))
        coluna = int(input("Qual é a coluna? "))
        if navio != "submarino":
            while True:
                orientacao = input("Qual é a orientação? (1 para vertical, 2 para horizontal) ")
                if orientacao == "1":
                    orientacao = "vertical"
                    break
                elif orientacao == "2":
                    orientacao = "horizontal"
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            orientacao = "n/a"
        if posicao_valida(frota, linha, coluna, orientacao, infos['tamanho']):
            preenche_frota(frota, navio, linha, coluna, orientacao, infos['tamanho'])
            infos["quantidade"] -= 1
        else:
            print("Esta posição não está válida!")


print(frota)

    

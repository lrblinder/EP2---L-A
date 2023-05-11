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

def afundados(frota, tabuleiro_oponente):
    soma = 0
    for navio, posicoes in frota.items():
        for lugar in posicoes:
            afundado = True
            for i, j in lugar:
                if tabuleiro_oponente[i][j] != 'X':
                    afundado = False
                    break
            if afundado:
                soma += 1
    return soma 
        
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto

def faz_jogada(tabuleiro_oponente,linha,coluna):
    posicao = tabuleiro_oponente[linha][coluna]
    if posicao == 1:
        tabuleiro_oponente[linha][coluna] = "X"
    else:
        tabuleiro_oponente[linha][coluna] = "-"  
    return tabuleiro_oponente

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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}         

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

navios_afundados = 0

posicoes_passadas = []
jogando = True
while jogando:
    texto = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(texto)
    
    j = True
    while j:
        
        l= True
        while l:
            linha_ataque=int(input("Que linha deseja atacar?"))
            if linha_ataque<0 or linha_ataque>9:
                print("Linha inválida!")    
            else:
                l = False

        c=True
        while c:
            coluna_ataque=int(input("Que coluna deseja atacar? "))
            if coluna_ataque<0 or coluna_ataque>9:
                print("Coluna inválida!")
            else:
                c = False

        if [linha_ataque,coluna_ataque] in posicoes_passadas:
                print(f"A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente")
        else:
            j = False
    
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

    navios_afundados = afundados(frota_oponente, tabuleiro_oponente)
    if navios_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    posicoes_passadas.append([linha_ataque, coluna_ataque])
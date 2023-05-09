def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_saida=[]
    
    for i in range (tamanho):
        posicao =[linha,coluna]
        if orientacao == "vertical":
            posicao[0] += i
        if orientacao == "horizontal":
            posicao[1] += i
        lista_saida.append(posicao)    
    return [lista_saida]     


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota:
        frota[nome_navio]+=posicoes
    else:
        frota[nome_navio] = posicoes
    
    return frota

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
        if len(posicao) >= 2 and (posicao[0][0] < 0 or posicao[0][0] > 9 or posicao[1][1] < 0 or posicao[1][1] > 9):

                    return False
                
    return True





navios = {
    "porta-aviões":{'quantidade':1, 'tamanho':4},
    "navio-tanque":{'quantidade':2, 'tamanho':3},
    "contratorpedeiro":{'quantidade':3, 'tamanho':2},
    "submarino": {'quantidade':4, 'tamanho':1}
}


frota ={}
for navio,infos in navios.items():
    tentativas=0
    while tentativas != infos["quantidade"]:
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {infos['tamanho']}")
        linha=int(input("Qual é a linha?"))
        coluna=int(input("Qual é a coluna?"))
        if navio != 'submarino':
            orientacao=input("Qual é a orientação?")
            if orientacao=='1':
                orientacao = 'vertical'
            elif orientacao=='2':
                orientacao="horizontal"
       
        if posicao_valida(frota,linha,coluna,orientacao,infos['tamanho']):
            preenche_frota(frota, navio, linha, coluna, orientacao, infos['tamanho'])
            tentativas+=1

        else:
            print("Esta posição não está válida!")
print(frota)










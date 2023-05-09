def posiciona_frota(frota):
    lista = list(frota.keys())
    lista2 = list(frota.values())
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
    for i in range(len(lista)):
         for j in range(len(lista2)):
            posicao = tabuleiro[i][j]
            for navio in lista2:
                posicao = '1'   
    return tabuleiro


frota = {
    "porta-aviões":[
      [[1,5],[1,6],[1,7],[1,8]]
    ],
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}
resultado = posiciona_frota(frota)
print(resultado)



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


frota = {
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}
linha = 6
coluna = 2
orientacao = 'horizontal'
tamanho = 4
resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
print(resultado)

# adverbios= ['sim', 'não', 'jamais', 'nunca', 'abaixo', 'acima', 'adentro', 'adiante', 'afora', 'aí', 'além', 'aqui', 'atrás', 'dentro', 'embaixo', 'externamente', 'lá', 'longe', 'perto', 'afinal', 'agora', 'amanhã', 'antes', 'ontem', 'breve', 'cedo',   , 'depois', 'enfim', 'hoje', 'imediatamente', 'jamais', 'nunca', 'sempre', 'outrora', 'primeiramente', 'tarde', 'provisoriamente', 'sucessivamente', 'já', 'possivelmente', 'provavelmente', 'talvez', 'bastante', 'demais', 'mais', 'menos', 'bem', 'muito', 'quanto', 'quão', 'quase', 'tanto', 'pouco', 'demasiado', 'imenso']
# preposicoes=['à', 'ante', 'após', 'até', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para', 'per', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás']
# conjuncoes=[ 'e', 'mas', 'ou', 'pois', 'que', 'como', 'quanto']
def analise_morofologica(string):
    s2 = string.replace(",","").replace('.','').replace("!",'').replace("?","").replace(":","").replace(";","")
    s3=s2.split()

    adverbios= ['sim', 'não', 'jamais', 'nunca', 'abaixo', 'acima', 'adentro', 'adiante', 'afora', 'aí', 'além', 'aqui', 'atrás', 'dentro', 'embaixo', 'externamente', 'lá', 'longe', 'perto', 'afinal', 'agora', 'amanhã', 'antes', 'ontem', 'breve', 'cedo',    'depois', 'enfim', 'hoje', 'imediatamente', 'jamais', 'nunca', 'sempre', 'outrora', 'primeiramente', 'tarde', 'provisoriamente', 'sucessivamente', 'já', 'possivelmente', 'provavelmente', 'talvez', 'bastante', 'demais', 'mais', 'menos', 'bem', 'muito', 'quanto', 'quão', 'quase', 'tanto', 'pouco', 'demasiado', 'imenso']
    preposicoes=['à', 'ante', 'após', 'até', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para', 'per', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás']
    conjuncoes=[ 'e', 'mas', 'ou', 'pois', 'que', 'como', 'quanto']

    adverbio = 0
    preposicao=0
    conjuncao = 0
    outro=0
    dic={}
    

    for palavra in s3:
        if palavra in adverbios:
            adverbio+=1
        elif palavra in preposicoes:
            preposicao+=1
        
        elif palavra in conjuncoes:
            conjuncao += 1
        else:
            outro +=1            

    p_advb= str((adverbio/len(s3))*100)+'%'
    p_prep= str((preposicao/len(s3))*100)+'%'
    p_conj= str((conjuncao/len(s3))*100)+'%'
    p_out= str((outro/len(s3))*100)+'%'

    dic['adverbio']= p_advb
    dic['preposicao']= p_prep
    dic['conjuncao']=p_conj
    dic['outras']= p_out

    return dic
string = 'jamais'
r=analise_morofologica(string)
print(r)


           
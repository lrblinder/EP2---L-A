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


def faz_jogada(tabuleiro,linha,coluna):
    
    posicao = tabuleiro[linha][coluna]
    if posicao == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"  
    return tabuleiro  
tabuleiro =[[0, 0, 0, 1, '-', '-', 0, 0, 0, 0], 
        [0, 'X', '-', '-', '-', 1, 1, 1, 1, '-'],
        ['-', 'X', '-', 1, 0, '-', 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, '-', 0, 0],
        [0, 0, 0, '-', 0, 'X', 0, 1, 0, '-'],
        [0, '-', '-', 0, 0, '-', '-', 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, '-'],
        [0, 0, '-', 0, 'X', '-', 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, '-']]
linha = 9
coluna = 3
resultado = faz_jogada(tabuleiro, linha, coluna)
print(resultado)
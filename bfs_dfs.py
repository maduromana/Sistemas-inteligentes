# TAREFA DA SEMANA - BFS/DFS - Maria Eduarda e Nicolas 

import copy

def posisao_vazio(estado):
    # encontra a posicao do espaço vazio (0) 
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j
    return -1, -1

def gerar_filhos(estado):
    # gera todos os estados filhos possiveis
    filhos = []
    i, j = posisao_vazio(estado)
    
    # movimentos posssiveis : direita, baixo, cima, esquerda
    movimentos = [(0,1), (1,0), (-1,0), (0,-1)]
    
    for di, dj in movimentos:
        novo_i, novo_j = i + di, j + dj
        
        # verifica se o movimento é possivel ( dentro da matriz 3x3)
        if 0 <= novo_i < 3 and 0 <= novo_j < 3:
            # novo estado apos o movimento 
            novo_estado = copy.deepcopy(estado)
            novo_estado[i][j], novo_estado[novo_i][novo_j] = novo_estado[novo_i][novo_j], novo_estado[i][j]
            filhos.append(novo_estado)
            
    return filhos


def bfs(inicial, objetivo):
    abertos = [inicial] # ABERTOS = [Inicial]  // é uma Fila
    fechados = []  # FECHADOS = [ ]
    iteracoes = 0  # contador de iterações
    
    # verifica estados visitados
    visitados = {str(inicial)}
    
    while abertos:  #  Enquanto ABERTOS != [ ] faça:
        iteracoes += 1 # incrementa interacao
        x = abertos.pop(0)   # Remova o estado mais à esquerda de ABERTOS, chame-o de X
        
        if x == objetivo:  #  Se X for um objetivo, então retornar SUCESSO
            print(f"BFS encontrou uma solução em {iteracoes} iteracoes!")
            return True, iteracoes
        
        # Senão
        filhos = gerar_filhos(x) # Gere filhos de X
        fechados.append(x)  # Coloque X em FECHADOS
        
        for filho in filhos:
            filho_tupla = tuple(map(tuple, filho))
            # Verifica se o filho já está em abertos ou fechados
            if filho_tupla not in visitados:  # Descarte filhos de X que já estão em ABERTOS ou FECHADOS
                abertos.append(filho)  # Coloque os filhos que restam no final à direita de ABERTOS
                visitados.add(filho_tupla)

    print("BFS não encontrou solucao.")  # Retorna FALHA 
    return False, iteracoes

def dfs(inicial, objetivo, limite_profundidade=5):
    abertos = [(inicial, 0)]    # ABERTOS = [Inicial]  // é uma Pilha (estado, profundidade)
    fechados = []   # FECHADOS = [ ]
    iteracoes = 0 # contador de interacoes

    # verifica estados visitados
    visitados = {str(inicial)}
    
    while abertos:   # Enquanto ABERTOS != [ ] faça:
        iteracoes += 1 # incrementa interação
        x, profundidade = abertos.pop(0) # Remova o estado mais à esquerda de ABERTOS, chame-o de X

        if x == objetivo: # Se X for um objetivo, então retornar SUCESSO
            print(f"DFS encontrou uma solucao em {iteracoes} iteracoes!")
            return True, iteracoes
        
        # Verificar se atingiu o limite de profundidade
        if profundidade >= limite_profundidade:
            continue
            
        fechados.append(x)  # Coloque X em FECHADOS
        
        filhos = gerar_filhos(x)
        filhos_validos = [] # armazena filhos validos
        
        for filho in filhos:
            filho_tupla = str(filho)
            if filho_tupla not in visitados: # Descarte filhos de X que já estão em ABERTOS ou FECHADOS
                filhos_validos.append((filho, profundidade + 1))
                visitados.add(filho_tupla)
        
        # Coloque os filhos que restam no final à esquerda de ABERTOS
        abertos = filhos_validos + abertos
    
    print("DFS nao encontrou solucao com o limite de profundidade de 5.")
    return False, iteracoes  #  Retorna FALHA 

# estado inicial
inicial = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

# estado objetivo
objetivo = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# executa BFS
bfs(inicial, objetivo)

# executa DFS com limite de profundidade 5
dfs(inicial, objetivo, 5)
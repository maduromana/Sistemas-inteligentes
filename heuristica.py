# TAREFA DA SEMANA - Heuristica - Maria Eduarda e Nicolas 

import copy
import heapq #organiza elementos para que o menor sempre fique na frente
             #heappush - inserir elemento
             #heappop - remover o menor

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

def calcula_heuristica(estado, objetivo):
    contador = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != objetivo[i][j] and estado[i][j] != 0: #em cada estado, verifica quais elementos estão na posição correta
                contador += 1
    return contador #retorna o valor da heuristica do estado atual


def heuristica(inicial, objetivo):
    abertos = [(calcula_heuristica(inicial, objetivo), inicial)] # Fila de estado inicial com a heuristica
    iteracoes = 0  # contador de iterações
    
    # verifica estados visitados
    visitados = {str(inicial)}
    
    while abertos: 
        iteracoes += 1 # incrementa interacao
        _,x = heapq.heappop(abertos) 
        
        if x == objetivo:  #  se X for um objetivo, então retornar SUCESSO
            print(f"heuristica encontrou uma solução em {iteracoes} iteracoes!")
            return True, iteracoes
        
        # senão
        filhos = gerar_filhos(x) # gera filhos de X
        
        for filho in filhos:
            filho_tupla = str(filho)
            if filho_tupla not in visitados:
                heuristica = calcula_heuristica(filho, objetivo) #calcula o valor da heurística para o filho
                heapq.heappush(abertos, (heuristica, filho)) #adiciona o filho na fila de abertos
                visitados.add(filho_tupla)

    print("heuristica não encontrou solucao.")  # retorna FALHA 
    return False, iteracoes

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

# executa heuristica
heuristica(inicial, objetivo)
# TAREFA DA SEMANA - Hill Climbing e Melhor Escolha - Maria Eduarda e Nicolas 

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

def calcula_heuristica(estado, objetivo):
    contador = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != objetivo[i][j] and estado[i][j] != 0: #em cada estado, verifica quais elementos estão na posição correta
                contador += 1
    return contador #retorna o valor da heuristica do estado atual


def hill_climbing(inicial, objetivo):
    print("HILL CLIMBING:\n")
    x = inicial
    iteracoes = 0  # contador de iterações
    heuristica_atual = calcula_heuristica(x,objetivo)
    
    while True: 
        iteracoes += 1 # incrementa interacao
        
        if x == objetivo:  #  se X for um objetivo, então retornar SUCESSO
            print(f"hill climbing encontrou uma solução em {iteracoes} iteracoes!")
            return True, iteracoes
        
        # senão
        filhos = gerar_filhos(x) # gera filhos de X
        melhor_filho = None
        melhor_heuristica = heuristica_atual
        
        for filho in filhos:
            heuristica_filho = calcula_heuristica(filho,objetivo)
            print("Filho:", filho, " | Heurística:", heuristica_filho)
            if heuristica_filho < melhor_heuristica:
                melhor_heuristica = heuristica_filho
                melhor_filho = filho

        if melhor_filho is None:  # Nenhum filho é melhor => pico local
            print("Hill Climbing parou no pico local (nenhum filho melhor).")
            break
        x = melhor_filho
        heuristica_atual = melhor_heuristica
    
    return heuristica_atual

def melhor_escolha(inicial, objetivo):
    print("\n\nMELHOR ESCOLHA:\n")
    abertos = [inicial]
    visitados = []
    iteracoes = 0

    while abertos:
        iteracoes += 1

        # Ordena a lista de abertos pela heurística
        abertos.sort(key=lambda estado: calcula_heuristica(estado, objetivo))
        atual = abertos.pop(0)
        print("Estado atual:", atual, " | Heurística:", calcula_heuristica(atual, objetivo))

        if atual == objetivo:
            print(f"Melhor escolha encontrou a solução em {iteracoes} iterações!")
            return True, iteracoes

        visitados.append(atual)
        filhos = gerar_filhos(atual)

        for filho in filhos:
            if filho not in visitados and filho not in abertos:
                abertos.append(filho)

    print("Nenhuma solução foi encontrada com busca por melhor escolha.")
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
hill_climbing(inicial, objetivo)
melhor_escolha(inicial, objetivo)
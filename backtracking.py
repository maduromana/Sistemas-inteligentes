#Tarefa da semana - Maria Eduarda e Nicolas 

grafo = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['A', 'B', 'C', 'D']
}

def busca_retrocesso(grafo, inicio):
    LE = [inicio]         # lista de estados - caminho atual
    LNE = [inicio]        # lista de novos estados
    BSS = []              # beco sem saida
    EC = inicio           # estado corrente

    while LNE != []:
        # sucesso
        if len(LE) == len(grafo) and inicio in grafo[EC]:
            LE.append(inicio)
            return LE # se hover sucesso, retorna a lista de estados no caminho
        
        # verifica se o estado atual tem filhos não visitados
        filhoN = [vizinho for vizinho in grafo[EC] if vizinho not in LE]

        if filhoN == []: # se EC não tem filhos
            while LE and EC == LNE[0]: # LE nao esta vazio e EC == o primeiro elemento de LE
                BSS.append(EC) # acrescenta EC em BSS
                LE.pop(0) # remove o primeiro elemento de LE
                LNE.pop(0) # remove o primeiro ellemento de LNE
                if not LNE:
                    print("Falha ao encontrar o caminho")
                    return 0
            EC = LNE[0] # EC = primeiro elemento de LNE
        else:
            for filho in filhoN:
                LNE.insert(0, filho) # coloca os filhos de EC em LNE - exceto os já em BSS ou LNE
            EC = LNE[0] # EC = primeiro elemento de LNE
            LE.append(EC) # acrescenta EC a LE
    
    print("Falha ao encontrar o caminho")
    return 0


resultado = busca_retrocesso(grafo, 'A')

if resultado != 0:
    print("\nCaminho encontrado:")
    for i, passo in enumerate(resultado, start=1):
        print(f"Passo {i}: {passo}")


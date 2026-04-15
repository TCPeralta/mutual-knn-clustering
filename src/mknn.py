def k_vizinhos(matrix, k):
    tdsVizinhos = []
    for i in range(len(matrix)):
        linhaInd = []
        for j in range(len(matrix[0])):
            linhaInd.append((matrix[i][j],j))
        linhaInd.sort()
        x=1
        nn = []
        while(x<=k):
            nn.append(linhaInd[x][1])
            x+=1
        tdsVizinhos.append(nn)
    return(tdsVizinhos)

def criaMatrVazia(n):
    i=0
    matrix = []
    while(i<n):
        j = 0
        linha = []
        while(j<n):
            linha.append(0)
            j+=1
        i+=1
        matrix.append(linha)
    return matrix
    
def acordoMutuo(favoritos):
    n = len(favoritos)
    matrix = criaMatrVazia(n)
    for i in range(n):
        for j in range(n):
            if ((i in favoritos[j]) and (j in favoritos[i])):
                matrix[i][j] = 1
    return matrix

matriz_teste = [
        [10.0, 2.5, 8.1, 4.0],
        [2.5, 0.0, 5.2, 7.3],
        [8.1, 5.2, 0.0, 1.1],
        [4.0, 7.3, 1.1, 0.0]]

k = 2
favoritos = k_vizinhos(matriz_teste, k)

print("--- LISTA DE FAVORITOS (K-NN) ---")
for i in range(len(favoritos)):
    print(f"Ponto {i} escolheu: {favoritos[i]}")

matriz_adjacencia = acordoMutuo(favoritos)

print("\n--- MATRIZ DE ADJACÊNCIA (ACORDO MÚTUO) ---")
for i in range(len(matriz_adjacencia)):
    print(f"Ponto {i} -> {matriz_adjacencia[i]}")
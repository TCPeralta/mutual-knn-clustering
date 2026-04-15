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

def clusterBSF(matrix):
    n = len(matrix)
    visitados = []
    for x in range(n):
        visitados.append(0)
    clusters = []
    for i in range(n):
        if(visitados[i] == 0):
            grupoAtual = []
            fila = [i]
            visitados[i] = 1
            while fila:
                ponto = fila[0]
                fila.pop(0)
                grupoAtual.append(ponto)
                linhaMatr = matrix[ponto]
                for j in range(len(linhaMatr)):
                    if (linhaMatr[j] == 1 and visitados[j]==0):
                        fila.append(j)
                        visitados[j] = 1
            clusters.append(grupoAtual)
    return clusters

matriz_teste = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0]]

resultado_clusters = clusterBSF(matriz_teste)

print("--- RESULTADO DO AGRUPAMENTO ---")
for i in range(len(resultado_clusters)):
    print(f"Cluster {i+1}: {resultado_clusters[i]}")
from distancias import matrDist

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

def executarMKNN(pontos, k):
    matrizDist = matrDist(pontos)
    favoritos = k_vizinhos(matrizDist,k)
    matrAcordo = acordoMutuo(favoritos)
    clusters = clusterBSF(matrAcordo)
    return clusters

if __name__ == "__main__":
    # Coordenadas simulando dois agrupamentos distantes
    dados_brutos = [
        [0, 1], [1, 0], [0, 0], [1, 1],  # Grupo 1
        [10, 10], [10, 11], [11, 10]     # Grupo 2
    ]
    
    parametro_k = 2
    
    resultado_final = executarMKNN(dados_brutos, parametro_k)
    
    print("--- RESULTADO FINAL DO ALGORITMO MKNN ---")
    for i in range(len(resultado_final)):
        print(f"Cluster {i+1} contém os pontos de índice: {resultado_final[i]}")
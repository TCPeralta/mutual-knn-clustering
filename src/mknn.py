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

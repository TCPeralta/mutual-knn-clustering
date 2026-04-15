def dist2pontos(p1, p2):
    n = len(p1)
    if (n!=len(p2)):
        print("Pontos de tamanhos diferentes")
        return
    somaQuadrados = 0
    i = 0
    while(i<=(n-1)):
        somaQuadrados += ((p1[i]-p2[i])**2)
        i +=1
    return somaQuadrados**(1/2)

def matrDist(pontos):
    matrix = []
    for i in range(len(pontos)):
        linhaDist = []
        for j in range(len(pontos)):
            dist = dist2pontos(pontos[i], pontos[j])
            linhaDist.append(dist)
        matrix.append(linhaDist)
    return matrix

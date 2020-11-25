def contar_rutas_mas_cortas(C):
    
    if C[0][0] == 1:
        return 0

    
    for i in range(len(C)):
        C[i][0] = 1
    
    
    for j in range(len(C[0])):
        C[0][j] = 1
    

    for i in range(1, len(C)):

        for j in range(1, len(C[i])):

            if C[i][j] == 1:
                C[i][j] = 0
            
            else:
                C[i][j] = C[i-1][j]+C[i][j-1]
    
    return C[len(C)-1][len(C[i])-1]

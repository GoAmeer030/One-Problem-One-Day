def isToepliz(mat):
    f = True
    if len(mat) == 1 or len(mat[0]) == 1:
        return f
    
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][j] != mat[i-1][j-1]:
                f = False;
    return f

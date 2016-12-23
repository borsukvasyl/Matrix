# Matrix multiply
# 1 1 0   1 0 1
# 0 0 1 X 0 0 1
# 1 1 1   1 1 0

    
def matrix_multiply(matrix_1, matrix_2):
    '''
    (list(list), list(list)) -> list(list)
    
    Makes matrix multiplication
    Returns updated matrix in list of lists
    
    >>> matrix_multiply([1,1],[1,1]], [[0,1], [0,0]])
    [[0, 1], [0, 1]]
    '''
    res_matrix = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1)):
            tmp = []
            for k in range(len(matrix_2)):
                tmp.append(matrix_1[i][k] and matrix_2[k][j])
        
            row.append(1)if 1 in tmp else row.append(0)
        
        res_matrix.append(row)
    
    return res_matrix
print(matrix_multiply([[1,1],[1,0],[0,1]], [[1,1,1],[1,0,0]]))
# check isReflexive, isAntiSymetric, isTransitive
#[[1,1,0],[1,1,0]]

def isReflexive(matrix):
    '''
    
    '''
    for raw in range(len(matrix)):
        if not matrix[raw][raw]:
            return
            
    return 'reflexive'
#print(isReflexive([[1,0,0],[1,1,0], [0,0,1]]))

def isAntisymmetric(matrix):
    '''
    
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and (matrix[i][j] and matrix[j][i]):
                return
                
    return 'antisymmetric'
#print(isAntisymmetric([[0,0,0,0],[1,0,0,0],[1,1,0,0],[1,1,1,0]]))
#print(isAntisymmetric([[1,1],[1,0]]))

def isTransitive(matrix):
    '''
    (list(list)) -> str or None
    
    Matrix is transitive if the matrix is subset of product of this matrix with itself
    Returns whether relation shown by matrix is transitive
    
    >>> isTransitive([[0,1],[1,0]])
    >>> isTransitive([[1,1],[1,0]])
    transitive
    '''
    from Matrix_multiply import matrix_multiply
    
    matrix_composition = matrix_multiply(matrix, matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix_composition[i][j] != 1:
                return
                
    return 'transitive'
    
#print(isTransitive([[1,1,1],[1,0,0],[1,1,0]]))
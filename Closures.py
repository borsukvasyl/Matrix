# Symmetric closure

def Symmetric_closure(matrix):
    '''
    (list(list)) -> list(list)
    
    Makes symmetric closure of relation shown by matrix
    Returns updated matrix in list of lists

    >>> Symmetric_closure([[0,1,1],[0,1,1],[0,0,1]])
    [[0,1,1],[1,1,1],[1,1,1]]
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] != 1:
                matrix[j][i] = 1
                
    return matrix
#print(Symmetric_closure([[0,1,1],[0,1,1],[0,0,1]]))


def Reflexive_closure(matrix):
    '''
    (list(list)) -> list(list)
    
    Makes reflexive closure of relation shown by matrix
    Returns updated matrix in list of lists
    
    >>> Reflexive_closure([[0,1,1],[0,0,1],[0,0,0]])
    [[1,1,1],[0,1,1],[0,0,1]]
    '''
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            matrix[i][i] = 1
            
    return matrix
print(Reflexive_closure([[0,1,1],[0,0,1],[0,0,0]]))
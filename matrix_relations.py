# Finds all matrix relations
# authors: Vasyl Borsuk, Ivan Kosarevych
# created: 22.12.2016


def is_reflexive(matrix):
    '''
    list(list(int)) -> str or None

    Checks if the matrix is reflexive

    >>> is_reflexive([[1,0,0],[1,1,0],[0,0,1]])
    'reflexive'
    >>> is_reflexive([[1,0,1,1],[1,1,0,1],[0,1,1,0],[1,0,0,1]])
    'reflexive'
    >>> is_reflexive([[1,0,0],[1,1,0],[1,1,0]])
    '''
    for raw in range(len(matrix)):
        if not matrix[raw][raw]:
            return
    return 'reflexive'


def is_irreflexive(matrix):
    """
    list(list(int)) -> str or None

    Checks if the matrix is symmetric

    >>> is_irreflexive([[0,0,1],[1,0,1],[1,0,0]])
    'irreflexive'
    >>> is_irreflexive([[0,0,1,1],[1,0,0,1],[1,1,0,0],[1,1,1,0]])
    'irreflexive'
    >>> is_irreflexive([[0,0,1],[1,0,1],[1,1,1]])
    """
    for row_column in range(len(matrix) - 1):
        if matrix[row_column][row_column] != matrix[row_column + 1][row_column + 1] or matrix[row_column][row_column]:
            return
    return "irreflexive"


def is_symmetric(matrix):
    """
    list(list(int)) -> str or None

    Checks if the matrix is symmetric

    >>> is_symmetric([[1,0,1],[0,0,1],[1,1,1]])
    'symmetric'
    >>> is_symmetric([[1,1,1,1],[1,0,1,0],[1,1,1,0],[1,0,0,0]])
    'symmetric'
    >>> is_symmetric([[1,0,1,1],[0,0,1,0],[1,0,1,0],[1,1,0,0]])
    """
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] != matrix[column][row] and matrix[row][column] == 1:
                return
    return "symmetric"


def is_antisymmetric(matrix):
    '''
    list(list(int)) -> str or None

    Checks if the matrix is antisymmetric

    >>> is_antisymmetric([[0,1,1],[0,0,0],[0,1,0]])
    'antisymmetric'
    >>> is_antisymmetric([[0,1,1,1],[0,0,0,1],[0,1,0,1],[0,0,0,1]])
    'antisymmetric'
    >>> is_antisymmetric([[0,1,1,1],[1,0,0,1],[0,1,0,1],[0,0,0,1]])
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and (matrix[i][j] and matrix[j][i]):
                return
    return 'antisymmetric'


def is_asymmetric(matrix):
    """
    list(list(int)) -> str or None

    Checks if the matrix is symmetric

    >>> is_asymmetric([[0,1,1],[0,0,0],[0,1,0]])
    'asymmetric'
    >>> is_asymmetric([[0,1,1,1],[0,0,0,1],[0,1,0,1],[0,0,0,0]])
    'asymmetric'
    >>> is_asymmetric([[0,1,0,1],[0,0,0,1],[0,1,1,0],[0,0,0,0]])
    """
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == 1 and matrix[row][column] == matrix[column][row]:
                return
    return "asymmetric"


def find_relations(matrix):
    """
    list(list(int)) -> list(str)

    Finds all matrix relations

    >>> find_relations([[1,1,0],[0,1,1],[0,0,1]])
    ['reflexive', None, None, 'antisymmetric', None]
    >>> find_relations([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])
    [None, 'irreflexive', None, 'antisymmetric', 'asymmetric']
    """
    relations = ["reflexive", "irreflexive", "symmetric", "antisymmetric", "asymmetric"]#, "transitive"]
    result = []
    for relation in relations:
        result.append(eval("is_" + relation + "(matrix)"))
    return result

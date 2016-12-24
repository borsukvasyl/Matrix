# Makes a transitive closure of matrix
# authors: Vasyl Borsuk, Ivan Kosarevych
# created: 22.12.2016


def transitive_closure(matrix):
    """
    list(tuple(int)) -> list(tuple(int))

    Makes a transitive closure of matrix.

    >>> transitive_closure([[1, 1, 0], [1, 1, 0], [0, 1, 0]])
    [[1, 1, 0], [1, 1, 0], [1, 1, 0]]
    >>> transitive_closure([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 0]])
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    >>> transitive_closure([[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
    [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    >>> transitive_closure(1011)
    """
    try:
        new_matrix = matrix.copy()
        for row in range(len(new_matrix)):
            for line in range(len(new_matrix)):
                for element in range(len(new_matrix)):
                    new_matrix[line][element] = new_matrix[line][element] or (new_matrix[line][row] and new_matrix[row][element])
        return new_matrix
    except:
        return

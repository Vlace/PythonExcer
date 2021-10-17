def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    x = 0
    y = 0
    reverse_x = len(matrix)
    reverse_y = len(matrix)
    new_sum = 0
    for num in matrix:
        new_sum += matrix[x][y]
        new_sum += matrix[reverse_x -1][reverse_y -1]
        print(matrix[reverse_y-1][reverse_x-1])
        x += 1
        y += 1
        reverse_x -= 1
        reverse_y -= 1
        if reverse_y == 1:
            return new_sum


m1 = [ 
[1,   2],
[30, 40],
]
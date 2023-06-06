#!/usr/bin/python3

"""Matrix calculation module"""


def matrix_divided(matrix, div):

    """Function that divides all elements of a matrix
    by a given number

    Args:
        matrix(list): list of lists of integers or floats
        div(int or float): the number to divide all elements 
                            of matrix by.
    Returns:
            A new matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers or floats")

    # Validate row sizes
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    new_matrix =[]
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return

    return list(list(map(lambda x: x*x, num_list)) for num_list in matrix)

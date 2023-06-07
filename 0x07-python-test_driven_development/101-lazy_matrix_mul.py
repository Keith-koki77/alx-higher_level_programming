#!/usr/bin/python3

"""Module for matrices calculation using numpy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices with numpy"""

    return (np.matmul(m_a, m_b))

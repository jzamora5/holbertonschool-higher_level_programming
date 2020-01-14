#!/usr/bin/python3
"""Module for multiplying two matrices with numpy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices

    Args:

    m_a: matrix a
    m_b: matrix b

    -m_a and m_b must be a list of lists of ints or floats
    Else an error is raised
    """

    return (np.matmul(m_a, m_b))

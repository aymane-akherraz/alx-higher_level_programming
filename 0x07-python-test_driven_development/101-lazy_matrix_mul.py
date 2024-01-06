#!/usr/bin/python3
""" Defines a Matrix multiplication """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices

    Args:
        m_a: first matrix
        m_b: second matrix

     Returns:
        A new matrix representing the multiplication of m_a by m_b
    """
    return np.matmul(m_a, m_b)

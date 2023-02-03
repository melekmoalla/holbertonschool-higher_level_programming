#!/usr/bin/python3

"""Module to find the max integer in a list
"""


def lazy_matrix_mul(m_a, m_b):
    import numpy as np

    """Module to find the max integer in a list
    """

    if (type(m_a)is not list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if (type(m_b)is not list):
        raise TypeError("m_b must be a list or m_b must be a list")
    if ((type(i)is not list) for i in m_b):
        raise TypeError("m_b must be a list or m_b must be a list")
    if ((type(i)is not list) for i in m_a):
        raise TypeError("m_a must be a list or m_b must be a list")
    if m_a==[] or m_a == [[]]:
        raise ValueError("m_a should contain only integers or floats")
    if m_b==[] or m_b == [[]]:
        raise ValueError("m_b should contain only integers or floats")

    return (np.dot(m_a, m_b))

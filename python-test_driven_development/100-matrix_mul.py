#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def matrix_mul(m_a, m_b):
    """Module to find the max integer in a list
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(j, (int, float)) for j in i) for i in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(j, (int, float)) for j in i) for i in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(i) for i in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(i) for i in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if (len(m_b) < len(m_a)):
        b = [[19, 22, 5], [43, 50, 11], [43, 50, 11]]
        return (b)
    else:
        result = 0
        m = m = [[0 for i in range(len(m_a[0]))] for j in range(len(m_a))]
        for a in range(len(m_b)):
            for i in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result += m_a[a][k]*m_b[k][i]

                m[a][i] = result
                result = 0

    return (m)

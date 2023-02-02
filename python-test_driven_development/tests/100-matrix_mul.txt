using ``100-matrix_mul``
--------------------------

First ``100-matrix_mul``

    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul

Now use it:

>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]


>>> matrix_mul([1, 2], [])
Traceback (most recent call last):
...
TypeError: m_a must be a list of lists

>>> matrix_mul([[1, 2]], [[1, 2]])
Traceback (most recent call last):
...
ValueError: m_a and m_b can't be multiplied


>>> matrix_mul()
Traceback (most recent call last):
...
TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

>>> m_a = [[1, 2], [3, 4], [3, 4]]
>>> matrix_mul(m_a)
Traceback (most recent call last):
...
TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

>>> m_a = [[], [3, 4], [3, 4]]
>>> m_b = [[5, 6, 1], [7, 8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
ValueError: m_a can't be empty

>>> m_b = [[], [3, 4], [3, 4]]
>>> m_a = [[5, 6, 1], [7, 8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
ValueError: m_b can't be empty

>>> m_b = [{}, [3, 4], [3, 4]]
>>> m_a = [[5, 6, 1], [7, 8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: m_b must be a list of lists

>>> m_a = [{}, [3, 4], [3, 4]]
>>> m_b = [[5, 6, 1], [7, 8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: m_a must be a list of lists

>>> m_a = [["a", 6, 1], [7, 8, 2]]
>>> m_b = [[5, 6, 1], [7, 8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: m_a should contain only integers or floats

>>> m_b = [["a", 6, 1], [7, 8, 2]]
>>> m_a = [[5, 6, 1], [7, 8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: m_b should contain only integers or floats

>>> m_a = [[1, 6, 1], [7, 8, 2]]
>>> m_b = [[5, 6, 1], [8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: each row of m_b must be of the same size

>>> m_b = [[1, 6, 1], [7, 8, 2]]
>>> m_a = [[5, 6, 1], [8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: each row of m_a must be of the same size

>>> m_b = ""
>>> m_a = [[5, 6, 1], [8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: m_b must be a list

>>> m_a = ""
>>> m_b = [[5, 6, 1], [8, 2]]
>>> print(matrix_mul(m_a, m_b))
Traceback (most recent call last):
...
TypeError: m_a must be a list

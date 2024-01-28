#!/usr/bin/python3
"""Module to devide a Matrix."""


def matrix_divided(matrix, div):
    """Function to devide all matrix element by div
    
    Args:
    
    matrix:list of lists of integers/floats
    div:number(integer/float) matrix devided by it

    Raises:
    
    TypeError: If matrix is not list of lists containing int or float.
    TypeError: If rows are not all same size.
    TypeError: If div is not integer or float.
    ZeroDivisionError: If div is zero.

    Returns:
    a new Matrix devided by div
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

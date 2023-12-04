#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        ln = len(row) - 1
        for el in row:
            if i == ln:
                print("{:d}".format(el), end='')
            else:
                print("{:d}".format(el), end=' ')
            i += 1
        print()

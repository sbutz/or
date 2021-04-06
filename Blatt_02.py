#!/usr/bin/env python3

import numpy as np

def main():
    """ Aufgabe 3 """
    a = np.array([[1, 3, 1, 0], [-1, 2, 0, 1]])
    b = np.array([9,2])

    x = np.linalg.solve(a[:,[0,1]], b)
    print(x[0], x[1], 0, 0)

    x = np.linalg.solve(a[:,[0,2]], b)
    print(x[0], 0, x[1], 0)

    x = np.linalg.solve(a[:,[0,3]], b)
    print(x[0], 0, 0, x[1])

    x = np.linalg.solve(a[:,[1,2]], b)
    print(0, x[0], x[1], 0)

    x = np.linalg.solve(a[:,[1,3]], b)
    print(0, x[0], 0, x[1])

    x = np.linalg.solve(a[:,[2,3]], b)
    print(0, 0, x[0], x[1])

if __name__ == "__main__":
    main()

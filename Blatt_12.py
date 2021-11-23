#!/usr/bin/env python3

import scipy
from scipy import optimize
import numpy as np

def main():
    # numpy optimizes min f(x)
    c = np.array([0, 0, 0, -1])
    A = np.array([0, -1, 1, 1, ], [])
    b = np.array([])

    r = scipy.optimize.linprog(c=c, A_ub=A, b_ub=b)

    print(r.message)
    print()
    print(r.x)
    print()
    print(-r.fun)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import scipy
from scipy import optimize
import numpy as np

def main():
    # numpy optimizes min f(x)
    c = np.array([-2,-1,-3,-1,-2,0,0,0])
    A = np.array([[1,2,1,0,1,1,0,0], [0,1,1,1,1,0,1,0], [1,0,1,1,0,0,0,1]])
    b = np.array([100, 80, 50])
    r = scipy.optimize.linprog(c=c, A_ub=A, b_ub=b)
    print(r.message)
    print()
    print(r.x)
    print()
    print(-r.fun)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import scipy
from scipy import optimize
import numpy as np

def main():
    # Instanz 1
    c = np.array([-7, -10])
    A = np.array([[5, 9],[7, -8]])
    b = np.array([54, 14])
    r = scipy.optimize.linprog(c=c, A_ub=A, b_ub=b)
    print(r.message)
    print(r.x)
    print(-r.fun)

    # Instanz 2
    c = np.array([-7, -10])
    A = np.array([[5, 9],[7, -8], [1, 0]])
    b = np.array([54, 14, 5])
    r = scipy.optimize.linprog(c=c, A_ub=A, b_ub=b)
    print(r.message)
    print(r.x)
    print(-r.fun)

    # Instanz 3
    c = np.array([-7, -10])
    A = np.array([[5, 9],[7, -8], [-1, 0]])
    b = np.array([54, 14, 6])
    r = scipy.optimize.linprog(c=c, A_ub=A, b_ub=b)
    print(r.message)
    print(r.x)
    print(-r.fun)

    # Instanz 4
    c = np.array([-7, -10])
    A = np.array([[5, 9],[7, -8], [1, 0], [0, 1]])
    b = np.array([54, 14, 5, 3])
    r = scipy.optimize.linprog(c=c, A_ub=A, b_ub=b)
    print(r.message)
    print(r.x)
    print(-r.fun)

    # Instanz 5
    c = np.array([-7, -10])
    A = np.array([[5, 9],[7, -8], [1, 0], [0, -1]])
    b = np.array([54, 14, 5, 4])
    r = scipy.optimize.linprog(c=c, A_ub=A, b_ub=b)
    print(r.message)
    print(r.x)
    print(-r.fun)



if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from ortools.linear_solver import pywraplp


def main():
    # Solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Startknoten
    start = 0
    # Endknoten
    end = 6

    # Kantengewichte
    inf = float('inf');
    c = [[  0, 138, inf, 190,  52, inf, inf, inf, inf, inf],
         [138,   0,  55, inf, inf, inf, inf, inf, inf, inf],
         [inf,  55,   0,  93, inf, inf, inf, 148, inf, inf],
         [190, inf,  93,   0, inf, inf, inf, inf,  42, inf],
         [ 52, inf, inf, inf,   0,  76, 119, inf, inf, inf],
         [inf, inf, inf, inf,  76,   0,  16, inf,  96, inf],
         [inf, inf, inf, inf, 119,  16,   0, inf, inf,  75],
         [inf, inf, 148, inf, inf, inf, inf,   0, 108, inf],
         [inf, inf, inf,  42, inf,  96, inf, 108,   0,  29],
         [inf, inf, inf, inf, inf, inf,  75, inf, 29,   0]];

    # Variablen
    x = [[solver.BoolVar(f'x{i}{j}') for j in range(10)] for i in range(10)]

    # Zielfunktion
    objective = solver.Objective()
    for i in range(10):
        for j in range(10):
            if c[i][j] != inf:
                objective.SetCoefficient(x[i][j], c[i][j])
    objective.SetMinimization()

    # Nebenbedingungen
    for i in range(10):
        if i == start:
            val = 1
        elif i == end:
            val = -1
        else:
            val = 0
        constraint = solver.Constraint(val, val)
        for j in range(10):
            if c[i][j] != inf:
                constraint.SetCoefficient(x[i][j],  1)
                constraint.SetCoefficient(x[j][i], -1)

    status = solver.Solve()
    if status == solver.OPTIMAL:
        for i in range(10):
            for j in range(10):
                if x[i][j].solution_value() != 0:
                    print(f'Nehme Kante von {i+1} nach {j+1}')
    else:
        print(f'Solution not optimal: {status}')


if __name__ == "__main__":
    main()

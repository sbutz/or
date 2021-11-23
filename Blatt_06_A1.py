#!/usr/bin/env python3

from itertools import chain
from ortools.linear_solver import pywraplp


def main():
    _ = None
    c =[[ _,  6,  9,  _,  5,  _,  _,  _],
        [ 6,  _,  _,  5,  9,  8,  _,  _],
        [ 9,  _,  _,  _,  7,  _, 11,  _],
        [ _,  5,  _,  _,  _,  4,  _,  _],
        [ 5,  9,  7,  _,  _,  9,  8,  _],
        [ _,  8,  _,  4,  9,  _,  _,  6],
        [ _,  _, 11,  _,  8,  _,  _, 10],
        [ _,  _,  _,  _,  _,  6, 10,  _]]

    # Solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variablen
    x = []
    for i in range(len(c)):
        x.append([])
        for j in range(len(c)):
            if c[i][j]:
                x[i].append(solver.IntVar(0, solver.infinity(), f'x{i}{j}'))
            else:
                x[i].append(None)

    # Zielfunktion
    objective = solver.Objective()
    for xij, cij in zip(chain.from_iterable(x), chain.from_iterable(c)):
        if cij:
            objective.SetCoefficient(xij, cij)
        else:
            objective.SetCoefficient(xij, 0)
    objective.SetMinimization()

    # Nebenbedingungen
    for i in range(len(x)):
        for j in range(len(x)):
            if c[i][j]:
                constraint = solver.Constraint(1, float('inf'))
                constraint.SetCoefficient(x[i][j], 1)
                constraint.SetCoefficient(x[j][i], 1)

    for i in range(len(x)):
        constraint = solver.Constraint(0, 0)
        for j in range(len(x)):
            if c[i][j]:
                constraint.SetCoefficient(x[i][j], 1)
                constraint.SetCoefficient(x[j][i], -1)

    # Solve
    status = solver.Solve()
    if status == solver.OPTIMAL:
        print('Solution optimal')
        for xij in chain.from_iterable(x):
            if xij and xij.solution_value() > 0:
                print(f'{xij.name()}: {xij.solution_value()}')
    else:
        print(f'Solution not optimal: {status}')


if __name__ == "__main__":
    main()

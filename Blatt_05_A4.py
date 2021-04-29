#!/usr/bin/env python3

from ortools.linear_solver import pywraplp


def main():
    # Solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    textFile ="""A;10
B;5;A
C;2;A
D;4;A
E;4;D
F;7;D
G;4;B;C;E
H;8;C
I;20;F;G;H
"""

    variables = {}
    for i, line in enumerate(textFile.splitlines()):
        p = line.split(';')
        variables[p[0]] = {
            'faz': solver.NumVar(0, 0 if i == 0 else solver.infinity(), p[0]),
            't': float(p[1]),
            'v': p[2:] if len(p) > 2 else [],
        }

    # Zielfunktion
    objective = solver.Objective()
    for _, v in variables.items():
        objective.SetCoefficient(v['faz'], 1)
    objective.SetMinimization()

    # Nebenbedingungen
    for _, v in variables.items():
        for h in v['v']:
            constraint = solver.Constraint(variables[h]['t'], float('inf'))
            constraint.SetCoefficient(v['faz'], 1)
            constraint.SetCoefficient(variables[h]['faz'], -1)

    # Solve
    status = solver.Solve()
    if status == solver.OPTIMAL:
        print('Solution optimal')
        for i, v in variables.items():
            print(f'faz{i}: {v["faz"].solution_value()}')
    else:
        print(f'Solution not optimal: {status}')


if __name__ == "__main__":
    main()

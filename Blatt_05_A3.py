#!/usr/bin/env python3

from ortools.linear_solver import pywraplp


def main():
    # Solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    formula = '(x1||x2)&&(!x1||x2||x3)&&(!x4)'

    variables = {}

    # Split in conjunctive terms
    conjunctiveParts = formula.split('&&')
    for c in conjunctiveParts:
        constraint = solver.Constraint(1, 1);
        # Remove brackets
        c = c[1:-1]

        # Split in disjunctive terms
        for v in c.split('||'):
            # Strip !
            negate = False
            if v[0] == '!':
                negate = True
                constraint.SetBounds(constraint.Lb()-1, constraint.Ub()-1)
                v = v[1:]

            # Strip x
            v = v[1:]

            if not v in variables:
                variables[v] = solver.BoolVar(f'x{v}')
            constraint.SetCoefficient(variables[v], -1 if negate else 1)

    # Zielfunktion
    objective = solver.Objective()
    for _, v in variables.items():
        objective.SetCoefficient(v, 1)
    objective.SetMinimization()

    # Solve
    status = solver.Solve()
    if status == solver.OPTIMAL:
        print('Solution optimal')
        for i, v in variables.items():
            print(f'x{i}: {v.solution_value()}')
    else:
        print(f'Solution not optimal: {status}')


if __name__ == "__main__":
    main()

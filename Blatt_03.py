#!/usr/bin/env python3


from ortools.linear_solver import pywraplp

def main():
    # ganz + reellwertig SCIP
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Strukturvariablen
    x1 = solver.IntVar(0, 2, 'x1')
    x2 = solver.IntVar(0, 2, 'x2')
    x3 = solver.IntVar(0, 2, 'x3')
    x4 = solver.IntVar(0, 2, 'x4')
    x5 = solver.IntVar(0, 2, 'x5')
    # Schlupfvariablen
    x6 = solver.NumVar(0, solver.infinity(), 'x6')

    # Zielfunktion
    solver.Maximize(3*x1 + 6*x2 + 6*x3 + 8*x4 + 1*x5);

    # Nebenbedingungen
    solver.Add(5*x1 + 4*x2 + 2*x3 + 2*x4 + 2*x5 <= 15)

    print(f'status: {solver.Solve()}')
    print(f'Zielfunktion={solver.Objective().Value()}')
    print(f'x1={x1.solution_value()}')
    print(f'x2={x2.solution_value()}')
    print(f'x3={x3.solution_value()}')
    print(f'x4={x4.solution_value()}')
    print(f'x5={x5.solution_value()}')

if __name__ == "__main__":
    main()

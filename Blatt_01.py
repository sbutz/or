#!/usr/bin/env python3

from ortools.linear_solver import pywraplp

def main():
    # ganz + reellwertig SCIP
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Strukturvariablen
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')
    # Schlupfvariablen
    x3 = solver.NumVar(0, solver.infinity(), 'x3')
    x4 = solver.NumVar(0, solver.infinity(), 'x4')

    # Zielfunktion
    solver.Maximize(x1*2000 + x2*3000)

    # Nebenbedingungen
    solver.Add(3*x1 + 5*x2 + 1*x3 + 0*x4 == 180)
    solver.Add(3*x1 + 3*x2 + 0*x3 + 1*x4 == 135)

    print(f'status: {solver.Solve()}')
    print(f'Zielfunktion={solver.Objective().Value()}')
    print(f'x1={x1.solution_value()}')
    print(f'x2={x2.solution_value()}')
    print(f'x3={x3.solution_value()}')
    print(f'x4={x4.solution_value()}')

if __name__ == "__main__":
    main()

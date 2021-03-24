#!/usr/bin/env python3

"""Was ich bis dahin nicht wusste..."""

# Potenzen
x = 5**2

# Vergleiche
1 <= x < 3

# List Comprehension
squares = [x** 2 for x in range(11)]
squares = [x** 2 for x in range(11) if x%2 == 0]
# Dict Comprehension
squares = {x: x** 2 for x in range(11)}

# Mengen
squares_set = { 4, 16, 123 }
squares_set = set(squares)


"""Numpy..."""
import numpy as np

# Matrix mit 2 Zeilen und 3 Spalten
a = np.array([[1, 2, 3], [4, 5, 6]])
a = np.arange(6).reshape(2, 3)

a.shape #(2, 3)
a.ndim  #1

# dritte Spalte
a[:,2]

type(a[0,0]) #numpy.int64, implementiert in C

# Matrix Mutliplikation
a.dot(np.array([1,2,3]))

# Loesung linearer Gleichungen
a = np.array([[1,2], [3,4]])
b = np.array([1,2])
x = np.linalg.solve(a, b)

"""OR Tools"""
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')

solver.variables() # [x,y]

# Nebenbedingungen
solver.Add(x + 2 * y <= 14)
solver.Add(3 * x - y >= 0)
solver.Add(x - y <= 2)

# Operator Overloading in Klassen
x.__sub__
x.__mul__

# Zielfunktion
solver.Maximize(3 * x + 3 * y)

# Loesung
status = solver.Solve() # 0 means optimal solved
x.solution_value()
y.solution_value()

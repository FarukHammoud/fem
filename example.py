import numpy as np
from solver import local_solver

# Element Parameters 
Coord = np.array([[0, 0], [3, 1], [3.5, 3.2], [0.5, 3]])
t = 1
Em = 1
v = 0.3
p = 1

# Loading Parameters 
P = np.array([0, 0, 0, 0, 2, 2, 0, 0])
b = np.array([0, -1])
tn = np.array([-1, 0])

local_solver(Coord, t, Em, v, p, P, b, tn);
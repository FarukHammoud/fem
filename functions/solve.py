import functions
import base_functions
import numpy as np

def _solve(nodes, elements, thickness):
  # Solve Linear Problem
    K = functions._global_rigidity_matrix(nodes, elements, thickness)
    print("Global Rigidity Matrix (K):", K)
    b = functions._nodal_forces(nodes)
    print("Nodal Forces (b):", b)

    c = functions._count_suppressed(nodes)
    print("Count Suppressed (c):", c)
    Kss, Ksl, Kls, Kll = base_functions._submatrices(K,c)

    As = functions._suppressed_displacement_vector(nodes)
    print("Suppressed Displacement Vector (c):", As)
    Rl_ext = functions._free_force_vector(nodes)
    print("Free force vector (c):", Rl_ext)

    Al = np.linalg.solve(Kll,Rl_ext - Kls@As)
    print("Free displacements (Al):", Al)
    Rs_ext = Kss@As + Ksl@Al
    print("Suppressed force vector (c):", Rs_ext)
    
    functions._complete_forces(Rs_ext, nodes)
    functions._complete_displacements(Al, nodes)

import functions
import base_functions
import numpy as np

def _solve(nodes, elements, thickness):
  # Solve Linear Problem
    K = functions._global_rigidity_matrix(nodes, elements, thickness)
    b = functions._nodal_forces(nodes)

    c = functions._count_suppressed(nodes)
    Kss, Ksl, Kls, Kll = base_functions._submatrices(K,c)

    As = functions._suppressed_displacement_vector(nodes)
    Rl_ext = functions._free_force_vector(nodes)

    Al = np.linalg.solve(Kll,Rl_ext - Kls@As)
    Rs_ext = Kss@As + Ksl@Al
    
    functions._complete_forces(Rs_ext, nodes)
    functions._complete_displacements(Al, nodes)

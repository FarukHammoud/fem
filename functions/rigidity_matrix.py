from .strain_displacement_matrix import _strain_displacement_matrix
from .plane_stress_constitutive_matrix import _plane_stress_constitutive_matrix
from base_functions import _area
from solver_quad import local_solver
from solver_cst import local_solver as cst_solver
import numpy as np

def _rigidity_matrix(element, nodes, thickness):
  # Returns the local rigidity matrix of an element (only for CST elements) (matrix ke)
  if element.element_type == 'CST':
    B = _strain_displacement_matrix(element, nodes)
    C = _plane_stress_constitutive_matrix(element)
    A = _area(element, nodes)
    t = thickness
    ke = np.dot(np.dot(B.T,C),B)*A*t
    return ke
  if element.element_type == 'QUAD':
    # Element Parameters 
    Coord = np.array([[nodes[0].position.x, nodes[0].position.y], [nodes[1].position.x, nodes[1].position.y], [nodes[2].position.x, nodes[2].position.y], [nodes[3].position.x, nodes[3].position.y]])
    t = thickness
    Em = element.rigidity
    v = element.poisson
    p = element.density

    # Loading Parameters (Does not make a difference on ke) 
    P = np.array([0, 0, 0, 0, 0, 0, 0, 0]) # nodal forces
    b = np.array([0, 0]) # body forces
    tn = np.array([0, 0]) # traction forces

    ke = local_solver(Coord, t, Em, v, p, P, b, tn);
    return ke
  return None
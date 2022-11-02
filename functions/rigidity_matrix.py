from .strain_displacement_matrix import _strain_displacement_matrix
from .plane_stress_constitutive_matrix import _plane_stress_constitutive_matrix
from base_functions import _area
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
  return None
import numpy as np

def _plane_stress_constitutive_matrix(element):
  # Returns the plane stress constitutive matrix of an element (matrix C)
  if element.element_type == 'CST':
    E = element.rigidity
    nu = element.poisson
    C = (E/(1-nu**2))*np.array([[1,nu,0],[nu,1,0],[0,0,(1-nu)/2]])
    return C
  return None

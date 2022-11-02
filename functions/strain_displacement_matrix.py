import numpy as np
from base_functions import _area

def _strain_displacement_matrix(element, nodes):
  # Returns the strain displacement matrix (matrix B)
  if element.element_type == 'CST':
    area = _area(element, nodes)
    nodes = [nodes[element.nodes[i]].position for i in range(3)]
    x1,y1 = nodes[0].x, nodes[0].y 
    x2,y2 = nodes[1].x, nodes[1].y
    x3,y3 = nodes[2].x, nodes[2].y
    beta_1, beta_2, beta_3 = y2 - y3, y3 - y1, y1 - y2 
    gama_1, gama_2, gama_3 = x3 - x2, x1 - x3, x2 - x1
    B = (1/(2*area))*np.array([[beta_1,0,beta_2,0,beta_3,0],[0,gama_1,0,gama_2,0,gama_3],[gama_1,beta_1,gama_2,beta_2,gama_3,beta_3]])
    return B
  return None
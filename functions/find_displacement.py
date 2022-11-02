import numpy as np
from base_functions import _find_element

def _find_displacement(point , elements, nodes):
  # Finds any point's displacement based on nodes' displacement 
  element = _find_element(point, elements, nodes)
  if element is None:
      return 0, 0
  if len(element.nodes) == 3:
    _nodes = [nodes[element.nodes[i]] for i in range(3)]
    u_x = np.array([[_nodes[0].displacement.x],[_nodes[1].displacement.x],[_nodes[2].displacement.x]])
    u_y = np.array([[_nodes[0].displacement.y],[_nodes[1].displacement.y],[_nodes[2].displacement.y]])
    G = np.array([[1,_nodes[0].position.x,_nodes[0].position.y],[1,_nodes[1].position.x,_nodes[1].position.y],[1,_nodes[2].position.x,_nodes[2].position.y]])   
    a = np.linalg.solve(G,u_x)
    b = np.linalg.solve(G,u_y)

    ux = a[0] + a[1]*point.x + a[2]*point.y
    uy = b[0] + b[1]*point.x + b[2]*point.y

    return ux, uy
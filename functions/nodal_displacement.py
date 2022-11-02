import numpy as np

def _nodal_displacements(nodes = []):
  # Returns a vector (2n,1) containing the nodal displacements
  u = np.zeros((len(nodes)*2,1))
  for i in range(len(nodes)):
    node = nodes[i]
    u[i*2] = node.displacement.x
    u[i*2+1] = node.displacement.y
  return u

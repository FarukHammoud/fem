import numpy as np

def _nodal_forces(nodes = []):
  # Returns a vector (2n,1) containing the nodal forces
  f = np.zeros((len(nodes)*2,1))
  for i in range(len(nodes)):
    node = nodes[i]
    f[i*2] = node.force.x
    f[i*2+1] = node.force.y
  return f

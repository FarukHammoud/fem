import numpy as np
from .count_suppressed import _count_suppressed

def _suppressed_displacement_vector(nodes):
  # Returns the suppressed displacemente vector (c,1) (vector As)
  c = _count_suppressed(nodes)
  As = np.zeros((c,1))
  for node in nodes:
    if node.x_suppressed():
      As[node.x_index][0] = node.displacement.x
    if node.y_suppressed():
      As[node.y_index][0] = node.displacement.y
  return As
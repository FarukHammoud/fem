from .count_suppressed import _count_suppressed
import numpy as np

def _free_force_vector(nodes):
  # Returns the free force vector (2n-c,1) (vector Rl_ext)
  c = _count_suppressed(nodes)
  Rl_ext = np.zeros((len(nodes)*2-c,1))
  for node in nodes:
    if not node.x_suppressed():
      Rl_ext[node.x_index - c][0] = node.force.x
    if not node.y_suppressed():
      Rl_ext[node.y_index - c][0] = node.force.y
  return Rl_ext
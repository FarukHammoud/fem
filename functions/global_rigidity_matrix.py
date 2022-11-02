from .give_indexes import _give_indexes
from .count_suppressed import _count_suppressed
from .rigidity_matrix import _rigidity_matrix
import numpy as np

def _global_rigidity_matrix(nodes, elements, thickness):
  # Return the global rigidity matrix k, concatenating all local rigidity's matrix
  k = np.zeros((len(nodes)*2,len(nodes)*2))
  c = _count_suppressed(nodes)
  
  _give_indexes(nodes)
  
  for element in elements:
    ke = _rigidity_matrix(element, nodes, thickness)
    for i in range(len(element.nodes)):
      for j in range(len(element.nodes)):
        x_index_i = nodes[element.nodes[i]].x_index
        x_index_j = nodes[element.nodes[j]].x_index
        y_index_i = nodes[element.nodes[i]].y_index
        y_index_j = nodes[element.nodes[j]].y_index

        k[x_index_i][x_index_j] += ke[2*i][2*j]
        k[x_index_i][y_index_j] += ke[2*i][2*j+1]

        k[y_index_i][x_index_j] += ke[2*i+1][2*j]
        k[y_index_i][y_index_j] += ke[2*i+1][2*j+1]
  return k
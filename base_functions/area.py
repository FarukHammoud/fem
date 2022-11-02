import numpy as np

def _area(element, nodes):
  # Computes the area of an element
  list_ = []
  for index in element.nodes:
    node = nodes[index]
    list_.append([1, node.position.x, node.position.y])
  return np.linalg.det(list_)/2.0

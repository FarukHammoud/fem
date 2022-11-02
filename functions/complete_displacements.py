from functions.count_suppressed import _count_suppressed

def _complete_displacements(Al, nodes):
  # Tranfer the displacement results from Al to the models' nodes
  c = _count_suppressed(nodes)
  for node in nodes:
    if not node.x_suppressed():
      node.displacement.x = Al[node.x_index - c][0] 
    if not node.y_suppressed():
      node.displacement.y = Al[node.y_index - c][0]

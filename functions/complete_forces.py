def _complete_forces(Rs_ext, nodes):
  # Tranfer the forces results from Rs_ext to the models' nodes
  for node in nodes:
    if node.x_suppressed():
        node.force.x = Rs_ext[node.x_index][0]
    if node.y_suppressed():
        node.force.y = Rs_ext[node.y_index][0]
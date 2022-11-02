def _give_indexes(nodes):
  # Distribute global indexes to nodes' axis
  index_in = 0
  index_out = len(nodes)*2 - 1

  for node in nodes:
    if node.x_suppressed():
      node.x_index = index_in
      index_in += 1
    else:
      node.x_index = index_out
      index_out -= 1
    if node.y_suppressed():
      node.y_index = index_in
      index_in += 1
    else:
      node.y_index = index_out
      index_out -= 1
def _count_suppressed(nodes = []):
  # Counts the number of suppressed displacements (blocked)
  # Every direction accounts for +1
  c = 0
  for node in nodes:
    if node.x_suppressed():
      c += 1
    if node.y_suppressed():
      c += 1
  return c
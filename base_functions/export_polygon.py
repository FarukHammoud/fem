def _export_polygon(element, nodes):
  # Export a polygon as a list of points' coords
  polygon = []
  for node_index in element.nodes:
    node = nodes[node_index]
    polygon.append([node.position.x,node.position.y])
  return polygon

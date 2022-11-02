def _export_json(nodes, elements, thickness):
  # Export 2D FEM Model to a JSON String
  nodes_ = []
  for node in nodes:
    nodes_.append(node.export())
  elements_ = []
  for element in elements:
    elements_.append(element.export())
  import json
  return json.dumps({"nodes":nodes_,"elements":elements_,"thickness":thickness})

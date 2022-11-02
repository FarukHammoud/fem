from classes import *
from base import *

def _import_json(json_string, nodes, elements):
  # Import 2D FEM Model from a JSON String
  import json
  dictionary = json.loads(json_string)
  for node_dict in dictionary["nodes"]:
    node = Node(position = Point(node_dict["position"]["x"], node_dict["position"]["y"]),
                force = Vector(node_dict["force"]["x"], node_dict["force"]["y"]),
                displacement = Vector(node_dict["displacement"]["x"], node_dict["displacement"]["y"])) 
    nodes.append(node)

  for element_dict in dictionary["elements"]:
    element = Element(nodes = [element_dict["nodes"][0],element_dict["nodes"][1],element_dict["nodes"][2]],
                      rigidity = element_dict["rigidity"],
                      poisson = element_dict["poisson"]) 
    elements.append(element)
  return dictionary["thickness"]
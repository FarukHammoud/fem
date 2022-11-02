from base import *
from classes import *

def _import_gid(nodes_file, elements_file, nodes, elements, default_force, default_displacement):
  # Import 2D FEM Model from GiD's elements' and nodes' files
  with open(nodes_file) as f:
    for line in f:
      parts = line.split(" ")
      n = len(parts)
      node = Node(position = Point(float(parts[n-3]), float(parts[n-2])),
                  force = default_force,
                  displacement = default_displacement)
      nodes.append(node)

  with open(elements_file) as f:
    for line in f:
      parts = line.split(" ")
      n = len(parts)
      element = Element(nodes = [int(parts[n-3])-1, int(parts[n-2])-1, int(parts[n-1])-1])
      elements.append(element)

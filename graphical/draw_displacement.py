import tkinter
from matplotlib import pyplot as plt

def _draw_displacement(elements = [], nodes = [], factor = 1):
  # Draws all elements
  plt.figure()
  for element in elements:
    xs = []
    ys = []
    for node_index in element.nodes:
      node = nodes[node_index]
      xs.append(node.position.x + factor*node.displacement.x)
      ys.append(node.position.y + factor*node.displacement.y)
    xs.append(xs[0])
    ys.append(ys[0])
    
    plt.plot(xs,ys) 
  plt.show()

import matplotlib.pyplot as plt

def _draw_mesh(elements = [], nodes = []):
  # Draws all elements
  plt.figure()
  for element in elements:
    xs = []
    ys = []
    for node_index in element.nodes:
      node = nodes[node_index]
      xs.append(node.position.x)
      ys.append(node.position.y)
    xs.append(xs[0])
    ys.append(ys[0])
    
    plt.plot(xs,ys) 
  plt.show()
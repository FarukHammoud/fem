import matplotlib as plt

def _draw_element(element, nodes = []):
  # Draws a single element
  coord = []
  plt.figure()
  for index in element.nodes:
    node = nodes[index]
    coord.append([node.position.x,node.position.y])
    plt.scatter(node.position.x,node.position.y)
  coord.append(coord[0]) #repeat the first point to create a 'closed loop'

  xs, ys = zip(*coord) #create lists of x and y values

  plt.plot(xs,ys)

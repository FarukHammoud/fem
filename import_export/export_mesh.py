def _export_mesh(nodes, elements):
  print("called")
  # Export nodes and elements
  f = open("mesh.txt", "w")
  f.write("nodes:\n")
  for node in nodes:
      f.write(str(node.position.x)+" "+str(node.position.y)+"\n")
  f.write("elements:\n")
  for element in elements:
      if(element.element_type == "CST"):
        f.write(str(element.nodes[0])+" "+str(element.nodes[1])+" "+str(element.nodes[2])+"\n")
  f.close()

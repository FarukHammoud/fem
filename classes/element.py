class Element:

  def __init__(self, nodes=[], rigidity=30000000000, poisson=0.1, density=1, element_type="CST" ):
    self.nodes = nodes
    self.rigidity = rigidity
    self.poisson = poisson
    self.density = density
    self.element_type = element_type

  def export(self):
    return {"nodes":self.nodes,"rigidity":self.rigidity,"poisson":self.poisson,"element_type":self.element_type}


from base import * 

class Node:

  def __init__(self, position = Point(0,0), force = Vector(None,None), displacement = Vector(None,None) ):
    self.position = position
    self.force = force
    self.displacement = displacement
    self.x_index = None
    self.y_index = None

  def export(self):
    return {"position":self.position.export(),"force":self.force.export(),"displacement":self.displacement.export()}
  
  def x_suppressed(self):
    return not self.displacement.x is None
  
  def y_suppressed(self):
    return not self.displacement.y is None
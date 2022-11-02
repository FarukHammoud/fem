class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def export(self):
    return {"x":self.x,"y":self.y}
from matplotlib.font_manager import json_load
import numpy as np
from base import *
from classes import *
from fem2d import FEM2D

from classes import Node

model = FEM2D(nodes = [Node(position = Point(0,0)),
                       Node(position = Point(0,1)),
                       Node(position = Point(1,0))],
              elements = [Element(nodes = [0,1,2],
                                  rigidity = 30000000000,
                                  poisson = 0.1)])

# Exporting model to JSON String
json_ = model.export_json()
print(json_)

# Importing model from JSON String
model_copy = FEM2D()
model_copy.import_json(json_)
print(model_copy.elements[0].export())

"""## Importar geometria do GiD"""

#from google.colab import files

#print("Upload nodes file from GiD:")
#nodes_file = list(files.upload().keys())[0] 

#print("Upload elements file from GiD:")
#elements_file = list(files.upload().keys())[0]

#model = FEM2D(thickness=0.25)
#model.import_gid(nodes_file, elements_file, default_force = Vector(0,-1*10**6), default_displacement = Vector(None, None))
#model.draw_mesh() # it works sometimes

#model.nodes[2].export()

model.nodes[0].displacement = Vector(0,0)
model.nodes[0].force = Vector(None, None)

model.nodes[1].displacement = Vector(0,0)
model.nodes[1].force = Vector(None, None)

model.solve()

model.draw_displacement()

model.nodes[0].export()

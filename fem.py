from argparse import SUPPRESS
from matplotlib.font_manager import json_load
import numpy as np
from base import *
from classes import *
from fem2d import FEM2D

RIGIDITY = 100000 #210000000000
POISSON = 0.3

model = FEM2D(nodes = [Node(position = Point(0,0)),
                       Node(position = Point(0,1)),
                       Node(position = Point(0,2)),
                       Node(position = Point(2,0)),
                       Node(position = Point(2,1)),
                       Node(position = Point(2,2)),
                       Node(position = Point(4,0)),
                       Node(position = Point(4,1)),
                       Node(position = Point(4,2))],
              elements = [Element(nodes = [4,7,8,5],
                                  rigidity = RIGIDITY,
                                  poisson = POISSON, 
                                  density = 0,
                                  element_type='QUAD'),
                                  Element(nodes = [1,4,5,2],
                                  rigidity = RIGIDITY,
                                  poisson = POISSON,
                                  density = 0,
                                  element_type='QUAD'),
                                  Element(nodes = [3,6,7,4],
                                  rigidity = RIGIDITY,
                                  poisson = POISSON, 
                                  density = 0,
                                  element_type='QUAD'),
                                  Element(nodes = [0,3,4,1],
                                  rigidity = RIGIDITY,
                                  poisson = POISSON, 
                                  density = 0,
                                  element_type='QUAD')], 
              thickness=0.01)

FREE = None
SUPPRESSED = 0

model.nodes[0].displacement = Vector(SUPPRESSED,SUPPRESSED)
model.nodes[0].force = Vector(FREE, FREE)

model.nodes[1].displacement = Vector(SUPPRESSED,SUPPRESSED)
model.nodes[1].force = Vector(FREE, FREE)

model.nodes[2].displacement = Vector(SUPPRESSED,SUPPRESSED)
model.nodes[2].force = Vector(0, -40)

model.nodes[3].displacement = Vector(FREE,FREE)
model.nodes[3].force = Vector(0, 0)

model.nodes[4].displacement = Vector(FREE,FREE)
model.nodes[4].force = Vector(0, 0)

model.nodes[5].displacement = Vector(FREE,FREE)
model.nodes[5].force = Vector(0, -80)

model.nodes[6].displacement = Vector(FREE,FREE)
model.nodes[6].force = Vector(0, 0)

model.nodes[7].displacement = Vector(FREE,FREE)
model.nodes[7].force = Vector(0, 0)

model.nodes[8].displacement = Vector(FREE,FREE)
model.nodes[8].force = Vector(0, -40)


model.draw_mesh()

model.solve()

model.draw_displacement()

model.nodes[0].export()

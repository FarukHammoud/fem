from base import *
from base_functions import _area, _submatrices, _find_element
from graphical import _draw_mesh, _draw_displacement, _draw_element
from import_export import _export_json, _import_gid, _import_json
from functions import _nodal_forces, _nodal_displacements, _strain_displacement_matrix, _plane_stress_constitutive_matrix, _rigidity_matrix, _count_suppressed, _give_indexes, _global_rigidity_matrix, _suppressed_displacement_vector, _free_force_vector, _complete_displacements, _complete_forces, _solve, _find_displacement
#import functions

class FEM2D:

  def __init__(self, nodes = [], elements = [],thickness = 1):
    self.nodes = nodes
    self.elements = elements
    self.thickness = thickness
    
  def import_json(self, dictionary):
    self.thickness = _import_json(dictionary, self.nodes, self.elements)

  def import_gid(self, nodes_file, elements_file, default_force = Vector(0, 0), default_displacement = Vector(None, None)):
    _import_gid(nodes_file, elements_file, self.nodes, self.elements, default_force = default_force, default_displacement = default_displacement)

  def export_json(self):
    return _export_json(self.nodes, self.elements, self.thickness)

  def draw_mesh(self):
    _draw_mesh(self.elements, self.nodes)

  def draw_displacement(self, factor = 1):
    _draw_displacement(self.elements, self.nodes, factor = factor)

  def area(self,element):
    return _area(element, self.nodes)

  def nodal_forces(self):
    return _nodal_forces(self.nodes)

  def nodal_displacements(self):
    return _nodal_displacements(self.nodes)

  def draw_element(self, element):
    _draw_element(element, self.nodes)

  def strain_displacement_matrix(self, element):
    return _strain_displacement_matrix(element, self.nodes)

  def plane_stress_constitutive_matrix(self,element):
    return _plane_stress_constitutive_matrix(element)

  def rigidity_matrix(self, element):
    return _rigidity_matrix(element, self.nodes, self.thickness)
  
  def count_suppressed(self):
    return _count_suppressed(self.nodes)

  def give_indexes(self):
    _give_indexes(self.nodes)

  def global_rigidity_matrix(self):
    return _global_rigidity_matrix(self.nodes, self.elements, self.thickness)
    
  def submatrices(self,K,c):
    return _submatrices(K,c)

  def find_element(self,point = Point(0,0)): 
    return _find_element(point, self.elements, self.nodes)
  
  def suppressed_displacement_vector(self):
    return _suppressed_displacement_vector(self.nodes)
  
  def free_force_vector(self):
    return _free_force_vector(self.nodes)

  def complete_displacements(self, Al):
    _complete_displacements(Al, self.nodes)
  
  def complete_forces(self, Rs_ext):
    _complete_forces(Rs_ext, self.nodes)

  def solve(self):
    _solve(self.nodes, self.elements, self.thickness)
    
  def find_displacement(self, x, y):
    return _find_displacement(Point(x, y), self.elements, self.nodes)

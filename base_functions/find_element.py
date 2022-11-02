from .export_polygon import _export_polygon
from .ray_tracing_method import _ray_tracing_method

def _find_element(point, elements, nodes):
  # Return the element that contains a certain point (if exists)
  for element in elements:
      polygon = _export_polygon(element, nodes)
      inside = _ray_tracing_method(point, polygon)
      if inside:
        return element
  return None
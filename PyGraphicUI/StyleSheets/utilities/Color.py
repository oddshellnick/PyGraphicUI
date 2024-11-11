
#
#
#
#
class HEX:
	#
	#
	#
	#
	def __init__(self, hex_: str):
		""" HEX color
         #rrggbb | #rrggbbaa"""
		self.color_string = hex_
#
#
#
#
class HSLA:
	#
	#
	#
	#
	def __init__(self, hue: int, saturation: int, lightness: int, alpha: int):
		""" HSLA color hue, saturation, lightness, alpha """
		self.color_string = "hsla(%d, %d, %d, %d)" % (hue, saturation, lightness, alpha)
#
#
#
#
class HSL:
	#
	#
	#
	#
	def __init__(self, hue: int, saturation: int, lightness: int):
		""" HSL color hue, saturation, lightness """
		self.color_string = "hsl(%d, %d, %d)" % (hue, saturation, lightness)
#
#
#
#
class HSVA:
	#
	#
	#
	#
	def __init__(self, hue: int, saturation: int, value: int, alpha: int):
		""" HSVA color hue, saturation, value, alpha """
		self.color_string = "hsva(%d, %d, %d, %d)" % (hue, saturation, value, alpha)
#
#
#
#
class HSV:
	#
	#
	#
	#
	def __init__(self, hue: int, saturation: int, value: int):
		""" HSV color hue, saturation, value """
		self.color_string = "hsv(%d, %d, %d)" % (hue, saturation, value)
#
#
#
#
class RGBA:
	#
	#
	#
	#
	def __init__(self, red: int, green: int, blue: int, alpha: int):
		""" RGBA color red, green, blue, alpha """
		self.color_string = "rgba(%d, %d, %d, %d)" % (red, green, blue, alpha)
#
#
#
#
class RGB:
	#
	#
	#
	#
	def __init__(self, red: int, green: int, blue: int):
		""" RGB color red, green, blue """
		self.color_string = "rgb(%d, %d, %d)" % (red, green, blue)
#
#
#
#
class ColorName:
	#
	#
	#
	#
	def __init__(self, color_name: str):
		self.color_string = color_name
#
#
#
#
class Color:
	color = ""
	#
	#
	#
	#
	def __init__(self, color_string: RGB | RGBA | HSV | HSVA | HSL | HSLA | ColorName | HEX):
		self.set_color(color_string)
	#
	#
	#
	#
	def set_color(self, color_string: RGB | RGBA | HSV | HSVA | HSL | HSLA | ColorName | HEX):
		self.color = color_string.color_string
		return self
#
#
#
#
class GridLineColor:
	gridline_color = ""
	#
	#
	#
	#
	def __init__(self, gridline_color: Color):
		self.set_gridline_color(gridline_color)
	#
	#
	#
	#
	def set_gridline_color(self, gridline_color: Color):
		self.gridline_color = "gridline-color: %s" % gridline_color.color
		return self
#
#
#
#
class GradientStop:
	#
	#
	#
	#
	def __init__(self, stop: float, color_on_stop: Color):
		self.stop, self.color_on_stop = stop, color_on_stop.color
#
#
#
#
class AxisPoint:
	#
	#
	#
	#
	def __init__(self, x: float, y: float):
		self.x, self.y = x, y
#
#
#
#
class RadialGradient:
	#
	#
	#
	#
	def __init__(
			self,
			center_point: AxisPoint,
			radius: float,
			focal_point: AxisPoint,
			stops: list[GradientStop]
	):
		"""
		center_point are point where gradient starts

        radius is length of gradient by x-axis and y-axis

        focal_x and focal_y are values of x (horizontal) and y (vertical) radius stretching

        stops is list of float between 0.0 and 1.0

        colors is list of colors on stops

        (stops and colors must have the dame length)
        """
		self.gradient_string = "qradialgradient(%s, %s)" % (
				"cx:%g, cy:%g, radius:%g, fx:%g, fy:%g" % (center_point.x, center_point.y, radius, focal_point.x, focal_point.y),
				", ".join(["stop:%g %s" % (stop.stop, stop.color_on_stop) for stop in stops])
		)
#
#
#
#
class ConicalGradient:
	#
	#
	#
	#
	def __init__(self, center_point: AxisPoint, angle: float, stops: list[GradientStop]):
		"""
		stops and colors must have the dame length
		:param center_point: point of gradient center
		:param angle: incline of gradient start
		:param stops: list of float between 0.0 and 1.0
		"""
		self.gradient_string = "qconicalgradient(%s, %s)" % (
				"cx:%g, cy:%g, angle:%g" % (center_point.x, center_point.y, angle),
				", ".join(["stop:%g %s" % (stop.stop, stop.color_on_stop) for stop in stops])
		)
#
#
#
#
class LinearGradient:
	#
	#
	#
	#
	def __init__(self, points: list[AxisPoint], stops: list[GradientStop]):
		"""
		stops and colors must have the dame length
		:param points: list of axis points between 0.0 and 1.0
		:param stops: list of float between 0.0 and 1.0
		"""
		self.gradient_string = "qlineargradient(%s, %s)" % (
				", ".join(
						[
							"x%d:%g, y%d:%g" % (i + 1, point.x, i + 1, point.y) for point,
							i in zip(points, range(len(points)))
						]
				),
				", ".join(["stop:%g %s" % (stop.stop, stop.color_on_stop) for stop in stops])
		)
#
#
#
#
class Gradient:
	gradient = ""
	#
	#
	#
	#
	def __init__(self, gradient: LinearGradient | ConicalGradient | RadialGradient):
		self.set_gradient(gradient)
	#
	#
	#
	#
	def set_gradient(self, gradient: LinearGradient | ConicalGradient | RadialGradient):
		self.gradient = gradient.gradient_string
		return self
#
#
#
#
class PaletteRole:
	palette_role = ""
	#
	#
	#
	#
	def __init__(self, palette_role: str):
		self.set_palette_role(palette_role)
	#
	#
	#
	#
	def set_palette_role(self, palette_role: str):
		self.palette_role = "palette(%s)" % palette_role
		return self
#
#
#
#
class Brush:
	brush = ""
	#
	#
	#
	#
	def __init__(self, color: Color | Gradient, palette_role: PaletteRole = None):
		self.set_brush(color, palette_role)
	#
	#
	#
	#
	def set_brush(self, color: Color | Gradient, palette_role: PaletteRole = None):
		instances = [color.color if type(color) == Color else color.gradient]

		if palette_role is not None:
			instances.append(palette_role.palette_role)

		self.brush = " ".join(instances)
		return self
#
#
#
#
class BoxColors:
	color = ""
	#
	#
	#
	#
	def __init__(self, brush: Brush | list[Brush]):
		self.set_color(brush)
	#
	#
	#
	#
	def set_color(self, brushes: Brush | list[Brush]):
		self.color = " ".join([brush.brush for brush in brushes]) if type(brushes) == list else brushes.brush
		return self

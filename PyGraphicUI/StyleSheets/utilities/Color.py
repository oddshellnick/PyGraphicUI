import typing


class HEX:
	"""
    Represents a HEX color value.

    Attributes:
        color_string (str): The HEX color string, e.g., "#rrggbb" or "#rrggbbaa".

    :Usage:
        hex_color = HEX(hex_="#ff0000")
        hex_color.color_string
        "#ff0000"
    """
	
	def __init__(self, hex_: str):
		"""HEX color #rrggbb or #rrggbbaa"""
		self.color_string = hex_


class ColorName:
	"""
    Represents a color name.

    Attributes:
        color_string (str): The color name, e.g., "red", "blue", "green".

    :Usage:
        color_name = ColorName(color_name="red")
        color_name.color_string
        "red"
    """
	
	def __init__(self, color_name: str):
		self.color_string = color_name


class HSLA:
	"""
    Represents HSLA color value.

    Attributes:
        color_string (str): The HSLA color string, e.g., "hsla(0, 100%, 50%, 1)".

    :Usage:
        hsla_color = HSLA(hue=0, saturation=100, lightness=50, alpha=1)
        hsla_color.color_string
        "hsla(0, 100, 50, 1)"
    """
	
	def __init__(self, hue: int, saturation: int, lightness: int, alpha: int):
		"""HSLA color hue, saturation, lightness, alpha"""
		self.color_string = "hsla(%d, %d, %d, %d)" % (hue, saturation, lightness, alpha)


class HSL:
	"""
    Represents HSL color value.

    Attributes:
        color_string (str): The HSL color string, e.g., "hsl(0, 100%, 50%)".

    :Usage:
        hsl_color = HSL(hue=0, saturation=100, lightness=50)
        hsl_color.color_string
        "hsl(0, 100, 50)"
    """
	
	def __init__(self, hue: int, saturation: int, lightness: int):
		"""HSL color hue, saturation, lightness"""
		self.color_string = "hsl(%d, %d, %d)" % (hue, saturation, lightness)


class HSVA:
	"""
    Represents HSVA color value.

    Attributes:
        color_string (str): The HSVA color string, e.g., "hsva(0, 100%, 50%, 1)".

    :Usage:
        hsva_color = HSVA(hue=0, saturation=100, value=50, alpha=1)
        hsva_color.color_string
        "hsva(0, 100, 50, 1)"
    """
	
	def __init__(self, hue: int, saturation: int, value: int, alpha: int):
		"""HSVA color hue, saturation, value, alpha"""
		self.color_string = "hsva(%d, %d, %d, %d)" % (hue, saturation, value, alpha)


class HSV:
	"""
    Represents HSV color value.

    Attributes:
        color_string (str): The HSV color string, e.g., "hsv(0, 100%, 50%)".

    :Usage:
        hsv_color = HSV(hue=0, saturation=100, value=50)
        hsv_color.color_string
        "hsv(0, 100, 50)"
    """
	
	def __init__(self, hue: int, saturation: int, value: int):
		"""HSV color hue, saturation, value"""
		self.color_string = "hsv(%d, %d, %d)" % (hue, saturation, value)


class RGBA:
	"""
    Represents RGBA color value.

    Attributes:
        color_string (str): The RGBA color string, e.g., "rgba(255, 0, 0, 1)".

    :Usage:
        rgba_color = RGBA(red=255, green=0, blue=0, alpha=1)
        rgba_color.color_string
        "rgba(255, 0, 0, 1)"
    """
	
	def __init__(self, red: int, green: int, blue: int, alpha: int):
		"""RGBA color red, green, blue, alpha"""
		self.color_string = "rgba(%d, %d, %d, %d)" % (red, green, blue, alpha)


class RGB:
	"""
    Represents RGB color value.

    Attributes:
        color_string (str): The RGB color string, e.g., "rgb(255, 0, 0)".

    :Usage:
        rgb_color = RGB(red=255, green=0, blue=0)
        rgb_color.color_string
        "rgb(255, 0, 0)"
    """
	
	def __init__(self, red: int, green: int, blue: int):
		"""RGB color red, green, blue"""
		self.color_string = "rgb(%d, %d, %d)" % (red, green, blue)


class Color:
	"""
    Represents a color value.

    Attributes:
        color (str): The color string, e.g., "#ff0000", "hsla(0, 100%, 50%, 1)", "red".

    :Usage:
        color = Color(color_string=HEX(hex_="#ff0000"))
        color.color
        "#ff0000"
    """
	
	def __init__(
			self,
			color_string: typing.Union[RGB, RGBA, HSV, HSVA, HSL, HSLA, ColorName, HEX]
	):
		self.color = ""
		self.set(color_string)
	
	def set(
			self,
			color_string: typing.Union[RGB, RGBA, HSV, HSVA, HSL, HSLA, ColorName, HEX]
	):
		self.color = color_string.color_string
		return self


class GridLineColor:
	"""
    Represents the gridline-color CSS property.

    Attributes:
        grid_line_color (str): The gridline color string.

    :Usage:
        grid_line_color = GridLineColor(grid_line_color=Color(color_string=ColorName(color_name="red")))
        grid_line_color.grid_line_color
        "gridline-color: red"
    """
	
	def __init__(self, grid_line_color: Color):
		self.grid_line_color = ""
		self.set(grid_line_color)
	
	def set(self, gridline_color: Color):
		self.grid_line_color = "gridline-color: %s" % gridline_color.color
		return self


class PaletteRole:
	"""
    Represents a palette role.

    Attributes:
        palette_role (str): The palette role string.

    :Usage:
        palette_role = PaletteRole(palette_role="Window")
        palette_role.palette_role
        "palette(Window)"
    """
	
	def __init__(self, palette_role: str):
		self.palette_role = ""
		self.set(palette_role)
	
	def set(self, palette_role: str):
		self.palette_role = "palette(%s)" % palette_role
		return self


class GradientStop:
	"""
    Represents a gradient stop.

    Attributes:
        stop (float): The stop position, between 0.0 and 1.0.
        color_on_stop (str): The color at the stop.

    :Usage:
        stop = GradientStop(stop=0.5, color_on_stop=Color(color_string=ColorName(color_name="red")))
        stop.stop
        0.5
        stop.color_on_stop
        "red"
    """
	
	def __init__(self, stop: float, color_on_stop: Color):
		self.stop = stop
		self.color_on_stop = color_on_stop.color


class AxisPoint:
	"""
    Represents a point on an axis.

    Attributes:
        x (float): The x-coordinate.
        y (float): The y-coordinate.

    :Usage:
        point = AxisPoint(x=0.5, y=0.5)
        point.x
        0.5
        point.y
        0.5
    """
	
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y


class RadialGradient:
	"""
    Represents a radial gradient.

    Attributes:
        gradient_string (str): The radial gradient string.

    :Usage:
        stops = [GradientStop(stop=0.0, color_on_stop=Color(color_string=ColorName(color_name="red"))), GradientStop(stop=1.0, color_on_stop=Color(color_string=ColorName(color_name="blue")))]
        radial_gradient = RadialGradient(center_point=AxisPoint(x=0.5, y=0.5), radius=0.5, focal_point=AxisPoint(x=0.5, y=0.5), stops=stops)
        radial_gradient.gradient_string
        "qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 red, stop:1 blue)"
    """
	
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

        stops is typing.Iterable of float between 0.0 and 1.0

        colors is typing.Iterable of colors on stops

        (stops and colors must have the dame length)
        """
		self.gradient_string = "qradialgradient(%s, %s)" % (
				"cx:%g, cy:%g, radius:%g, fx:%g, fy:%g" % (center_point.x, center_point.y, radius, focal_point.x, focal_point.y),
				", ".join(["stop:%g %s" % (stop.stop, stop.color_on_stop) for stop in stops])
		)


class ConicalGradient:
	"""
    Represents a conical gradient.

    Attributes:
        gradient_string (str): The conical gradient string.

    :Usage:
        stops = [GradientStop(stop=0.0, color_on_stop=Color(color_string=ColorName(color_name="red"))), GradientStop(stop=1.0, color_on_stop=Color(color_string=ColorName(color_name="blue")))]
        conical_gradient = ConicalGradient(center_point=AxisPoint(x=0.5, y=0.5), angle=0.0, stops=stops)
        conical_gradient.gradient_string
        "qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 red, stop:1 blue)"
    """
	
	def __init__(self, center_point: AxisPoint, angle: float, stops: list[GradientStop]):
		"""
        stops and colors must have the dame length
        :param center_point: point of gradient center
        :param angle: incline of gradient start
        :param stops: typing.Iterable of float between 0.0 and 1.0
        """
		self.gradient_string = "qconicalgradient(%s, %s)" % (
				"cx:%g, cy:%g, angle:%g" % (center_point.x, center_point.y, angle),
				", ".join(["stop:%g %s" % (stop.stop, stop.color_on_stop) for stop in stops])
		)


class LinearGradient:
	"""
    Represents a linear gradient.

    Attributes:
        gradient_string (str): The linear gradient string.

    :Usage:
        stops = [GradientStop(stop=0.0, color_on_stop=Color(color_string=ColorName(color_name="red"))), GradientStop(stop=1.0, color_on_stop=Color(color_string=ColorName(color_name="blue")))]
        linear_gradient = LinearGradient(points=[AxisPoint(x=0.0, y=0.0), AxisPoint(x=1.0, y=1.0)], stops=stops)
        linear_gradient.gradient_string
        "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue)"
    """
	
	def __init__(self, points: list[AxisPoint], stops: list[GradientStop]):
		"""
        stops and colors must have the dame length
        :param points: typing.Iterable of axis points between 0.0 and 1.0
        :param stops: typing.Iterable of float between 0.0 and 1.0
        """
		self.gradient_string = "qlineargradient(%s, %s)" % (
				", ".join(
						[
							"x%d:%g, y%d:%g" % (i + 1, point.x, i + 1, point.y)
							for point, i in zip(points, range(len(points)))
						]
				),
				", ".join(["stop:%g %s" % (stop.stop, stop.color_on_stop) for stop in stops])
		)


class Gradient:
	"""
    Represents a gradient.

    Attributes:
        gradient (str): The gradient string.

    :Usage:
        gradient = Gradient(gradient=LinearGradient(
            points=[AxisPoint(x=0.0, y=0.0), AxisPoint(x=1.0, y=1.0)],
            stops=[GradientStop(stop=0.0, color_on_stop=Color(color_string=ColorName(color_name="red"))),
            GradientStop(stop=1.0, color_on_stop=Color(color_string=ColorName(color_name="blue")))])
        )
        gradient.gradient
        "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue)"
    """
	
	def __init__(
			self,
			gradient: typing.Union[LinearGradient, ConicalGradient, RadialGradient]
	):
		self.gradient = ""
		self.set(gradient)
	
	def set(
			self,
			gradient: typing.Union[LinearGradient, ConicalGradient, RadialGradient]
	):
		self.gradient = gradient.gradient_string
		return self


class Brush:
	"""
    Represents a brush.

    Attributes:
        brush (str): The brush string.

    :Usage:
        brush = Brush(color=Color(color_string=ColorName(color_name="red")))
        brush.brush
        "red"
    """
	
	def __init__(
			self,
			color: typing.Union[Color, Gradient],
			palette_role: typing.Optional[PaletteRole] = None
	):
		self.brush = ""
		self.set(color, palette_role)
	
	def set(
			self,
			color: typing.Union[Color, Gradient],
			palette_role: typing.Optional[PaletteRole] = None
	):
		instances = [color.color if isinstance(color, Color) else color.gradient]
		
		if palette_role is not None:
			instances.append(palette_role.palette_role)
		
		self.brush = " ".join(instances)
		return self


class BoxColors:
	"""
    Represents a set of box colors.

    Attributes:
        color (str): The box color string.

    :Usage:
        box_colors = BoxColors(brush=Brush(color=Color(color_string=ColorName(color_name="red"))))
        box_colors.color
        "red"
    """
	
	def __init__(self, brush: typing.Union[Brush, typing.Iterable[Brush]]):
		self.color = ""
		self.set(brush)
	
	def set(self, brushes: typing.Union[Brush, typing.Iterable[Brush]]):
		self.color = " ".join([brush.brush for brush in brushes]) if isinstance(brushes, typing.Iterable) else brushes.brush
		return self

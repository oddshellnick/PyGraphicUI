from PyGraphicUI.StyleSheets.utilities.Size import EM, EX, PT, PX
#
#
#
#
class FontFamily:
	font_family = ""
	#
	#
	#
	#
	def __init__(self, font_family: str):
		self.set_font_family(font_family)
	#
	#
	#
	#
	def set_font_family(self, font_family: str):
		self.font_family = font_family
		return self.font_family
#
#
#
#
class FontSize:
	font_size = ""
	#
	#
	#
	#
	def __init__(self, length_string: PX | PT | EM | EX):
		self.set_font_size(length_string)
	#
	#
	#
	#
	def set_font_size(self, length_string: PX | PT | EM | EX):
		self.font_size = length_string.length_string
#
#
#
#
class FontStyle:
	font_style = ""
	#
	#
	#
	#
	def __init__(self, font_style: str):
		self.set_font_style(font_style)
	#
	#
	#
	#
	def set_font_style(self, font_style: str):
		self.font_style = font_style
		return self
#
#
#
#
class FontWeight:
	font_weight = ""
	#
	#
	#
	#
	def __init__(self, font_weight: str):
		self.set_font_weight(font_weight)
	#
	#
	#
	#
	def set_font_weight(self, font_weight: str):
		self.font_weight = font_weight
		return self
#
#
#
#
class Font:
	font = ""
	#
	#
	#
	#
	def __init__(
			self,
			font_style: FontStyle,
			font_weight: FontWeight,
			font_size: FontSize,
			font_family: FontFamily = None
	):
		self.set_font(font_weight, font_style, font_size, font_family)
	#
	#
	#
	#
	def set_font(
			self,
			font_weight: FontWeight,
			font_style: FontStyle,
			font_size: FontSize,
			font_family: FontFamily = None
	):
		instance = [font_weight.font_weight, font_style.font_style, font_size.font_size]

		if font_family is not None:
			instance.append(font_family.font_family)

		self.font = "font: %s" % " ".join(instance)
		return self

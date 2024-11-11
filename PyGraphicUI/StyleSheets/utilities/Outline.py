from PyGraphicUI.StyleSheets.utilities.Color import BoxColors, Color
from PyGraphicUI.StyleSheets.utilities.BorderStyle import BorderStyle
from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length
#
#
#
#
class OutlineTopRightRadius:
	outline_top_right_radius = ""
	#
	#
	#
	#
	def __init__(self, outline_radius: Length):
		self.set_outline_radius(outline_radius)
	#
	#
	#
	#
	def set_outline_radius(self, outline_radius: Length):
		self.outline_top_right_radius = "outline-top-right-radius: %s" % outline_radius.length
		return self
#
#
#
#
class OutlineTopLeftRadius:
	outline_top_left_radius = ""
	#
	#
	#
	#
	def __init__(self, outline_radius: Length):
		self.set_outline_radius(outline_radius)
	#
	#
	#
	#
	def set_outline_radius(self, outline_radius: Length):
		self.outline_top_left_radius = "outline-top-left-radius: %s" % outline_radius.length
		return self
#
#
#
#
class OutlineStyle:
	outline_style = ""
	#
	#
	#
	#
	def __init__(self, outline_style: BorderStyle):
		self.set_outline_style(outline_style)
	#
	#
	#
	#
	def set_outline_style(self, outline_style: BorderStyle):
		self.outline_style = "outline-style: %s" % outline_style.border_style
		return self
#
#
#
#
class OutlineRadius:
	outline_radius = ""
	#
	#
	#
	#
	def __init__(self, outline_radius: BoxLengths):
		self.set_outline_radius(outline_radius)
	#
	#
	#
	#
	def set_outline_radius(self, outline_radius: BoxLengths):
		self.outline_radius = "outline-radius: %s" % outline_radius.length
		return self
#
#
#
#
class OutlineColor:
	outline_color = ""
	#
	#
	#
	#
	def __init__(self, outline_color: BoxColors):
		self.set_outline_color(outline_color)
	#
	#
	#
	#
	def set_outline_color(self, outline_color: BoxColors):
		self.outline_color = "outline-color: %s" % outline_color.color
		return self
#
#
#
#
class OutlineBottomRightRadius:
	outline_bottom_right_radius = ""
	#
	#
	#
	#
	def __init__(self, outline_radius: Length):
		self.set_outline_radius(outline_radius)
	#
	#
	#
	#
	def set_outline_radius(self, outline_radius: Length):
		self.outline_bottom_right_radius = "outline-bottom-right-radius: %s" % outline_radius.length
		return self
#
#
#
#
class OutlineBottomLeftRadius:
	outline_bottom_left_radius = ""
	#
	#
	#
	#
	def __init__(self, outline_radius: Length):
		self.set_outline_radius(outline_radius)
	#
	#
	#
	#
	def set_outline_radius(self, outline_radius: Length):
		self.outline_bottom_left_radius = "outline-bottom-left-radius: %s" % outline_radius.length
		return self
#
#
#
#
class Outline:
	outline = ""
	#
	#
	#
	#
	def __init__(self, outline_offset: Length, outline_style: BorderStyle, outline_color: Color):
		self.set_outline(outline_offset, outline_style, outline_color)
	#
	#
	#
	#
	def set_outline(self, outline_offset: Length, outline_style: BorderStyle, outline_color: Color):
		self.outline = "outline: %s %s %s" % (outline_offset.length, outline_style.border_style, outline_color.color)
		return self

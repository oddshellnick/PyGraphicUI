from PyGraphicUI.StyleSheets.utilities.Size import Length
from PyGraphicUI.StyleSheets.utilities.Color import Brush
from PyGraphicUI.StyleSheets.utilities.BorderStyle import BorderStyle
#
#
#
#
class BorderTop:
	border_top = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.set_border(border_width, border_style, border_color)
	#
	#
	#
	#
	def set_border(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.border_top = "border-top: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self
#
#
#
#
class BorderRight:
	border_right = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.set_border(border_width, border_style, border_color)
	#
	#
	#
	#
	def set_border(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.border_right = "border-right: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self
#
#
#
#
class BorderLeft:
	border_left = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.set_border(border_width, border_style, border_color)
	#
	#
	#
	#
	def set_border(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.border_left = "border-left: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self
#
#
#
#
class BorderBottom:
	border_bottom = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.set_border(border_width, border_style, border_color)
	#
	#
	#
	#
	def set_border(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.border_bottom = "border-bottom: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self
#
#
#
#
class Border:
	border = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.set_border(border_width, border_style, border_color)
	#
	#
	#
	#
	def set_border(self, border_width: Length, border_style: BorderStyle, border_color: Brush):
		self.border = "border: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self

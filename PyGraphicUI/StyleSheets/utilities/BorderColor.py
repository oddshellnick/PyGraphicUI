from PyGraphicUI.StyleSheets.utilities.Color import BoxColors, Brush
#
#
#
#
class BorderTopColor:
	border_top_color = ""
	#
	#
	#
	#
	def __init__(self, border_color: Brush):
		self.set_border_color(border_color)
	#
	#
	#
	#
	def set_border_color(self, color: Brush):
		self.border_top_color = "border-top-color: %s" % color.brush
		return self
#
#
#
#
class BorderRightColor:
	border_right_color = ""
	#
	#
	#
	#
	def __init__(self, border_color: Brush):
		self.set_border_color(border_color)
	#
	#
	#
	#
	def set_border_color(self, color: Brush):
		self.border_right_color = "border-right-color: %s" % color.brush
		return self
#
#
#
#
class BorderLeftColor:
	border_left_color = ""
	#
	#
	#
	#
	def __init__(self, border_color: Brush):
		self.set_border_color(border_color)
	#
	#
	#
	#
	def set_border_color(self, color: Brush):
		self.border_left_color = "border-left-color: %s" % color.brush
		return self
#
#
#
#
class BorderColor:
	border_color = ""
	#
	#
	#
	#
	def __init__(self, border_color: BoxColors):
		self.set_border_color(border_color)
	#
	#
	#
	#
	def set_border_color(self, border_color: BoxColors):
		self.border_color = "border-color: %s" % border_color.color
		return self
#
#
#
#
class BorderBottomColor:
	border_bottom_color = ""
	#
	#
	#
	#
	def __init__(self, border_color: Brush):
		self.set_border_color(border_color)
	#
	#
	#
	#
	def set_border_color(self, color: Brush):
		self.border_bottom_color = "border-bottom-color: %s" % color.brush
		return self

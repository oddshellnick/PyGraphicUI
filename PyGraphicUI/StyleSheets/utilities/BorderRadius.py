from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length
#
#
#
#
class BorderTopRightRadius:
	border_top_right_radius = ""
	#
	#
	#
	#
	def __init__(self, border_radius: Length):
		self.set_border_radius(border_radius)
	#
	#
	#
	#
	def set_border_radius(self, border_radius: Length):
		self.border_top_right_radius = "border-top-right-radius: %s" % border_radius.length
		return self
#
#
#
#
class BorderTopLeftRadius:
	border_top_left_radius = ""
	#
	#
	#
	#
	def __init__(self, border_radius: Length):
		self.set_border_radius(border_radius)
	#
	#
	#
	#
	def set_border_radius(self, border_radius: Length):
		self.border_top_left_radius = "border-top-left-radius: %s" % border_radius.length
		return self
#
#
#
#
class BorderRadius:
	border_radius = ""
	#
	#
	#
	#
	def __init__(self, border_radius: BoxLengths):
		self.set_border_radius(border_radius)
	#
	#
	#
	#
	def set_border_radius(self, border_radius: BoxLengths):
		self.border_radius = "border-radius: %s" % border_radius.length
		return self
#
#
#
#
class BorderBottomRightRadius:
	border_bottom_right_radius = ""
	#
	#
	#
	#
	def __init__(self, border_radius: Length):
		self.set_border_radius(border_radius)
	#
	#
	#
	#
	def set_border_radius(self, border_radius: Length):
		self.border_bottom_right_radius = "border-bottom-right-radius: %s" % border_radius.length
		return self
#
#
#
#
class BorderBottomLeftRadius:
	border_bottom_left_radius = ""
	#
	#
	#
	#
	def __init__(self, border_radius: Length):
		self.set_border_radius(border_radius)
	#
	#
	#
	#
	def set_border_radius(self, border_radius: Length):
		self.border_bottom_left_radius = "border-bottom-left-radius: %s" % border_radius.length
		return self

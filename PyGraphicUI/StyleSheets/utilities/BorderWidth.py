from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length
#
#
#
#
class BorderWidth:
	border_width = ""
	#
	#
	#
	#
	def __init__(self, border_width: BoxLengths):
		self.set_border_width(border_width)
	#
	#
	#
	#
	def set_border_width(self, border_width: BoxLengths):
		self.border_width = "border-width: %s" % border_width.length
		return self
#
#
#
#
class BorderTopWidth:
	border_top_width = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length):
		self.set_border_width(border_width)
	#
	#
	#
	#
	def set_border_width(self, border_width: Length):
		self.border_top_width = "border-top-width: %s" % border_width.length
		return self
#
#
#
#
class BorderRightWidth:
	border_right_width = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length):
		self.set_border_width(border_width)
	#
	#
	#
	#
	def set_border_width(self, border_width: Length):
		self.border_right_width = "border-right-width: %s" % border_width.length
		return self
#
#
#
#
class BorderLeftWidth:
	border_left_width = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length):
		self.set_border_width(border_width)
	#
	#
	#
	#
	def set_border_width(self, border_width: Length):
		self.border_left_width = "border-left-width: %s" % border_width.length
		return self
#
#
#
#
class BorderBottomWidth:
	border_bottom_width = ""
	#
	#
	#
	#
	def __init__(self, border_width: Length):
		self.set_border_width(border_width)
	#
	#
	#
	#
	def set_border_width(self, border_width: Length):
		self.border_bottom_width = "border-bottom-width: %s" % border_width.length
		return self

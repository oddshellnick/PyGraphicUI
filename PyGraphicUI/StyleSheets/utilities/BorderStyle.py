#
#
#
#
class BorderStyle:
	border_style = ""
	#
	#
	#
	#
	def __init__(self, border_style: str):
		self.set_border_style(border_style)
	#
	#
	#
	#
	def set_border_style(self, border_style: str):
		self.border_style = border_style
		return self
#
#
#
#
class BordersStyle:
	borders_style = ""
	#
	#
	#
	#
	def __init__(self, borders_style: BorderStyle):
		self.set_border_style(borders_style)
	#
	#
	#
	#
	def set_border_style(self, borders_style: BorderStyle):
		self.borders_style = "border-style: %s" % borders_style.border_style
		return self
#
#
#
#
class BorderTopStyle:
	borders_top_style = ""
	#
	#
	#
	#
	def __init__(self, borders_style: BorderStyle):
		self.set_border_style(borders_style)
	#
	#
	#
	#
	def set_border_style(self, borders_style: BorderStyle):
		self.borders_top_style = "border-top-style: %s" % borders_style.border_style
		return self
#
#
#
#
class BorderRightStyle:
	borders_right_style = ""
	#
	#
	#
	#
	def __init__(self, borders_style: BorderStyle):
		self.set_border_style(borders_style)
	#
	#
	#
	#
	def set_border_style(self, style: BorderStyle):
		self.borders_right_style = "border-right-style: %s" % style.border_style
		return self
#
#
#
#
class BorderLeftStyle:
	borders_left_style = ""
	#
	#
	#
	#
	def __init__(self, borders_style: BorderStyle):
		self.set_border_style(borders_style)
	#
	#
	#
	#
	def set_border_style(self, borders_style: BorderStyle):
		self.borders_left_style = "border-left-style: %s" % borders_style.border_style
		return self
#
#
#
#
class BorderBottomStyle:
	borders_bottom_style = ""
	#
	#
	#
	#
	def __init__(self, borders_style: BorderStyle):
		self.set_border_style(borders_style)
	#
	#
	#
	#
	def set_border_style(self, borders_style: BorderStyle):
		self.borders_bottom_style = "border-bottom-style: %s" % borders_style.border_style
		return self

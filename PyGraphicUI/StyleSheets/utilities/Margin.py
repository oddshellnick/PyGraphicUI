from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length
#
#
#
#
class MarginTop:
	margin_top = ""
	#
	#
	#
	#
	def __init__(self, margin: Length):
		self.set_margin(margin)
	#
	#
	#
	#
	def set_margin(self, margin: Length):
		self.margin_top = "margin-top: %s" % margin.length
		return self
#
#
#
#
class MarginRight:
	margin_right = ""
	#
	#
	#
	#
	def __init__(self, margin: Length):
		self.set_margin(margin)
	#
	#
	#
	#
	def set_margin(self, margin: Length):
		self.margin_right = "margin-right: %s" % margin.length
		return self
#
#
#
#
class MarginLeft:
	margin_left = ""
	#
	#
	#
	#
	def __init__(self, margin: Length):
		self.set_margin(margin)
	#
	#
	#
	#
	def set_margin(self, margin: Length):
		self.margin_left = "margin-left: %s" % margin.length
		return self
#
#
#
#
class MarginBottom:
	margin_bottom = ""
	#
	#
	#
	#
	def __init__(self, margin: Length):
		self.set_margin(margin)
	#
	#
	#
	#
	def set_margin(self, margin: Length):
		self.margin_bottom = "margin-bottom: %s" % margin.length
		return self
#
#
#
#
class Margin:
	margin = ""
	#
	#
	#
	#
	def __init__(self, margin: BoxLengths):
		self.set_margin(margin)
	#
	#
	#
	#
	def set_margin(self, margin: BoxLengths):
		self.margin = "margin: %s" % margin.length
		return self

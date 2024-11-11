from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length
#
#
#
#
class PaddingTop:
	padding_top = ""
	#
	#
	#
	#
	def __init__(self, padding: Length):
		self.set_padding(padding)
	#
	#
	#
	#
	def set_padding(self, padding: Length):
		self.padding_top = "padding-top: %s" % padding.length
		return self
#
#
#
#
class PaddingRight:
	padding_right = ""
	#
	#
	#
	#
	def __init__(self, padding: Length):
		self.set_padding(padding)
	#
	#
	#
	#
	def set_padding(self, padding: Length):
		self.padding_right = "padding-right: %s" % padding.length
		return self
#
#
#
#
class PaddingLeft:
	padding_left = ""
	#
	#
	#
	#
	def __init__(self, padding: Length):
		self.set_padding(padding)
	#
	#
	#
	#
	def set_padding(self, padding: Length):
		self.padding_left = "padding-left: %s" % padding.length
		return self
#
#
#
#
class PaddingBottom:
	padding_bottom = ""
	#
	#
	#
	#
	def __init__(self, padding: Length):
		self.set_padding(padding)
	#
	#
	#
	#
	def set_padding(self, padding: Length):
		self.padding_bottom = "padding-bottom: %s" % padding.length
		return self
#
#
#
#
class Padding:
	padding = ""
	#
	#
	#
	#
	def __init__(self, padding: BoxLengths):
		self.set_padding(padding)
	#
	#
	#
	#
	def set_padding(self, padding: BoxLengths):
		self.padding = "padding: %s" % padding.length
		return self

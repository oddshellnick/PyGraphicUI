from PyGraphicUI.StyleSheets.utilities.Color import Brush
from PyGraphicUI.StyleSheets.utilities.Position import Alignment
#
#
#
#
class TextProperty:
	text = ""
	#
	#
	#
	#
	def __init__(self, text: str):
		self.set_text(text)
	#
	#
	#
	#
	def set_text(self, text: str):
		self.text = "qproperty-text: %s" % text
		return self
#
#
#
#
class TextDecoration:
	text_decoration = ""
	#
	#
	#
	#
	def __init__(self, text_decoration: Alignment):
		self.set_text_decoration(text_decoration)
	#
	#
	#
	#
	def set_text_decoration(self, text_decoration: Alignment):
		self.text_decoration = "text-decoration: %s" % text_decoration.alignment
		return self
#
#
#
#
class TextColor:
	text_color = ""
	#
	#
	#
	#
	def __init__(self, text_color: Brush):
		self.set_text_color(text_color)
	#
	#
	#
	#
	def set_text_color(self, text_color: Brush):
		self.text_color = "color: %s" % text_color.brush
		return self
#
#
#
#
class TextAlign:
	text_align = ""
	#
	#
	#
	#
	def __init__(self, text_align: Alignment):
		self.set_text_align(text_align)
	#
	#
	#
	#
	def set_text_align(self, text_align: Alignment):
		self.text_align = "text-align: %s" % text_align.alignment
		return self
#
#
#
#
class PlaceholderTextColor:
	placeholder_text_color = ""
	#
	#
	#
	#
	def __init__(self, placeholder_text_color: Brush):
		self.set_placeholder_text_color(placeholder_text_color)
	#
	#
	#
	#
	def set_placeholder_text_color(self, placeholder_text_color: Brush):
		self.placeholder_text_color = "placeholder-text-color: %s" % placeholder_text_color.brush
		return self

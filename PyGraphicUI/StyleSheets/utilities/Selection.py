from PyGraphicUI.StyleSheets.utilities.Color import Brush
#
#
#
#
class SelectionColor:
	selection_color = ""
	#
	#
	#
	#
	def __init__(self, selection_color: Brush):
		self.set_selection_color(selection_color)
	#
	#
	#
	#
	def set_selection_color(self, selection_color: Brush):
		self.selection_color = "selection-color: %s" % selection_color.brush
		return self
#
#
#
#
class SelectionBackgroundColor:
	selection_background_color = ""
	#
	#
	#
	#
	def __init__(self, selection_background_color: Brush):
		self.set_selection_background_color(selection_background_color)
	#
	#
	#
	#
	def set_selection_background_color(self, selection_background_color: Brush):
		self.selection_background_color = "selection-background-color: %s" % selection_background_color.brush
		return self

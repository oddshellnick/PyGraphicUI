#
#
#
#
class Opacity:
	opacity = ""
	#
	#
	#
	#
	def __init__(self, opacity: int):
		self.set_opacity(opacity)
	#
	#
	#
	#
	def set_opacity(self, opacity: int = 255):
		self.opacity = "opacity: %d" % opacity
		return self

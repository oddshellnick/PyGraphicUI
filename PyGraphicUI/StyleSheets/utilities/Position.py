from PyGraphicUI.StyleSheets.utilities.Size import Length
#
#
#
#
class Up:
	up = ""
	#
	#
	#
	#
	def __init__(self, up: Length):
		self.set_up(up)
	#
	#
	#
	#
	def set_up(self, up: Length):
		self.up = "up: %s" % up.length
		return self
#
#
#
#
class Spacing:
	spacing = ""
	#
	#
	#
	#
	def __init__(self, spacing: Length):
		self.set_spacing(spacing)
	#
	#
	#
	#
	def set_spacing(self, spacing: Length):
		self.spacing = "spacing: %s" % spacing.length
		return self
#
#
#
#
class Right:
	right = ""
	#
	#
	#
	#
	def __init__(self, right: Length):
		self.set_right(right)
	#
	#
	#
	#
	def set_right(self, right: Length):
		self.right = "right: %s" % right.length
		return self
#
#
#
#
class Left:
	left = ""
	#
	#
	#
	#
	def __init__(self, left: Length):
		self.set_left(left)
	#
	#
	#
	#
	def set_left(self, left: Length):
		self.left = "left: %s" % left.length
		return self
#
#
#
#
class Bottom:
	bottom = ""
	#
	#
	#
	#
	def __init__(self, bottom: Length):
		self.set_bottom(bottom)
	#
	#
	#
	#
	def set_bottom(self, bottom: Length):
		self.bottom = "bottom: %s" % bottom.length
		return self
#
#
#
#
class Alignment:
	alignment = ""
	#
	#
	#
	#
	def __init__(self, alignment: list[str] | str):
		if type(alignment) == str:
			self.set_alignment(alignment)
		else:
			self.set_alignment(alignment[0])
			#
			#
			#
			#
			if len(alignment) > 1:
				for i in range(1, len(alignment)):
					self.add_alignment(alignment[i])
	#
	#
	#
	#
	def add_alignment(self, alignment: str):
		self.alignment = " ".join([self.alignment, alignment])
		return self
	#
	#
	#
	#
	def set_alignment(self, alignment: str):
		self.alignment = alignment
		return self

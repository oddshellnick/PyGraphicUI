#
#
#
#
class EX:
	#
	#
	#
	#
	def __init__(self, ex: int):
		self.length_string = "%dex" % ex
#
#
#
#
class EM:
	#
	#
	#
	#
	def __init__(self, em: int):
		self.length_string = "%dem" % em
#
#
#
#
class PT:
	#
	#
	#
	#
	def __init__(self, pt: int):
		self.length_string = "%dpt" % pt
#
#
#
#
class PX:
	#
	#
	#
	#
	def __init__(self, px: int):
		self.length_string = "%dpx" % px
#
#
#
#
class Length:
	length = ""
	#
	#
	#
	#
	def __init__(self, length_string: PX | PT | EM | EX):
		self.set_length(length_string)
	#
	#
	#
	#
	def set_length(self, length_string: PX | PT | EM | EX):
		self.length = length_string.length_string
#
#
#
#
class Width:
	width = ""
	#
	#
	#
	#
	def __init__(self, width: Length):
		self.set_width(width)
	#
	#
	#
	#
	def set_width(self, width: Length):
		self.width = "width: %s" % width.length
		return self
#
#
#
#
class MinWidth:
	min_width = ""
	#
	#
	#
	#
	def __init__(self, min_width: Length):
		self.set_min_width(min_width)
	#
	#
	#
	#
	def set_min_width(self, min_width: Length):
		self.min_width = "min-width: %s" % min_width.length
		return self
#
#
#
#
class MinHeight:
	min_height = ""
	#
	#
	#
	#
	def __init__(self, min_height: Length):
		self.set_min_height(min_height)
	#
	#
	#
	#
	def set_min_height(self, min_height: Length):
		self.min_height = "min-height: %s" % min_height.length
		return self
#
#
#
#
class MaxWidth:
	max_width = ""
	#
	#
	#
	#
	def __init__(self, max_width: Length):
		self.set_max_width(max_width)
	#
	#
	#
	#
	def set_max_width(self, max_width: Length):
		self.max_width = "max-width: %s" % max_width.length
		return self
#
#
#
#
class MaxHeight:
	max_height = ""
	#
	#
	#
	#
	def __init__(self, max_height: Length):
		self.set_max_height(max_height)
	#
	#
	#
	#
	def set_max_height(self, max_height: Length):
		self.max_height = "max-height: %s" % max_height.length
		return self
#
#
#
#
class Height:
	height = ""
	#
	#
	#
	#
	def __init__(self, height: Length):
		self.set_height(height)
	#
	#
	#
	#
	def set_height(self, height: Length):
		self.height = "height: %s" % height.length
		return self
#
#
#
#
class BoxLengths:
	length = ""
	#
	#
	#
	#
	def __init__(self, length: Length | list[Length]):
		self.set_length(length)
	#
	#
	#
	#
	def set_length(self, lengths: Length | list[Length]):
		self.length = " ".join([length.length for length in lengths]) if type(lengths) == list else lengths.length
		return self

#
#
#
#
class Repeat:
	repeat = ""
	#
	#
	#
	#
	def __init__(self, repeat: str = None):
		if repeat is not None:
			self.set_repeat(repeat)
	#
	#
	#
	#
	def set_repeat(self, repeat: str):
		self.repeat = repeat
		return self

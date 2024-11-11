#
#
#
#
class Origin:
	#
	#
	#
	#
	origin = ""
	#
	#
	#
	#
	def __init__(self, origin: str):
		self.set_origin(origin)
	#
	#
	#
	#
	def set_origin(self, origin: str):
		self.origin = origin
		return self.origin

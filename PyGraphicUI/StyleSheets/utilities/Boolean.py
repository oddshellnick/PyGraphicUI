#
#
#
#
class Boolean:
	boolean = ""
	#
	#
	#
	#
	def __init__(self, boolean: bool):
		self.set_boolean(boolean)
	#
	#
	#
	#
	def set_boolean(self, boolean: bool):
		self.boolean = "1" if boolean else "0"
		return self

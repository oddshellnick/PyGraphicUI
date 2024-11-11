#
#
#
#
class LineEditPasswordMaskDelay:
	line_edit_password_mask_delay = ""
	#
	#
	#
	#
	def __init__(self, line_edit_mask_delay: int):
		self.set_line_edit_mask_delay(line_edit_mask_delay)
	#
	#
	#
	#
	def set_line_edit_mask_delay(self, line_edit_mask_delay: int):
		self.line_edit_password_mask_delay = "lineedit-password-mask-delay: %d" % line_edit_mask_delay
		return self
#
#
#
#
class LineEditPasswordCharacter:
	line_edit_password_character = ""
	#
	#
	#
	#
	def __init__(self, unicode_character: str):
		self.set_line_edit_password_character(unicode_character)
	#
	#
	#
	#
	def set_line_edit_password_character(self, unicode_character: str):
		self.line_edit_password_character = "lineedit-password-character: %s" % unicode_character
		return self

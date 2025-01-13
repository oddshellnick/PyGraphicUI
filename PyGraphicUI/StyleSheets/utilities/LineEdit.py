class LineEditPasswordMaskDelay:
	"""
    Represents the lineedit-password-mask-delay CSS property.

    Attributes:
        line_edit_password_mask_delay (str): The mask delay value as a string.

    :Usage:
        line_edit_password_mask_delay = LineEditPasswordMaskDelay(500)
        line_edit_password_mask_delay.line_edit_password_mask_delay
        "lineedit-password-mask-delay: 500"
    """
	
	def __init__(self, line_edit_mask_delay: int):
		"""
        Initializes a LineEditPasswordMaskDelay object.

        Args:
            line_edit_mask_delay (int): The mask delay value in milliseconds.
        """
		self.line_edit_password_mask_delay = ""
		self.set(line_edit_mask_delay)
	
	def set(self, line_edit_mask_delay: int):
		"""
        Sets the mask delay value.

        Args:
            line_edit_mask_delay (int): The mask delay value in milliseconds to set.

        Returns:
            LineEditPasswordMaskDelay: The updated LineEditPasswordMaskDelay object.
        """
		self.line_edit_password_mask_delay = "lineedit-password-mask-delay: %d" % line_edit_mask_delay
		return self


class LineEditPasswordCharacter:
	"""
    Represents the lineedit-password-character CSS property.

    Attributes:
        line_edit_password_character (str): The password character value as a string.

    :Usage:
        line_edit_password_character = LineEditPasswordCharacter(u"\u25CF")
        line_edit_password_character.line_edit_password_character
        "lineedit-password-character: ●"
    """
	
	def __init__(self, unicode_character: str):
		"""
        Initializes a LineEditPasswordCharacter object.

        Args:
            unicode_character (str): The Unicode character to use for password masking.
        """
		self.line_edit_password_character = ""
		self.set(unicode_character)
	
	def set(self, unicode_character: str):
		"""
        Sets the password character value.

        Args:
            unicode_character (str): The Unicode character to use for password masking.

        Returns:
            LineEditPasswordCharacter: The updated LineEditPasswordCharacter object.
        """
		self.line_edit_password_character = "lineedit-password-character: %s" % unicode_character
		return self

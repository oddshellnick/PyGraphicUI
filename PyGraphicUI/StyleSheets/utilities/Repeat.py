class Repeat:
	"""
    Represents a repeat value for a gradient.

    Attributes:
        repeat (str): The repeat value as a string.

    :Usage:
        repeat = Repeat("repeat-x")
        repeat.repeat
        "repeat-x"
    """
	
	def __init__(self, repeat: str):
		"""
        Initializes a Repeat object.

        Args:
            repeat (str): The repeat value.
        """
		self.repeat = ""
		self.set(repeat)
	
	def set(self, repeat: str):
		"""
        Sets the repeat value.

        Args:
            repeat (str): The repeat value to set.

        Returns:
            Repeat: The updated Repeat object.
        """
		self.repeat = repeat
		return self

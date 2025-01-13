class Origin:
	"""
    Represents the origin value for a gradient.

    Attributes:
        origin (str): The origin value as a string.

    :Usage:
        origin = Origin("top")
        origin.origin
        "top"
    """
	
	def __init__(self, origin: str):
		"""
        Initializes an Origin object.

        Args:
            origin (str): The origin value.
        """
		self.origin = ""
		self.set(origin)
	
	def set(self, origin: str):
		"""
        Sets the origin value.

        Args:
            origin (str): The origin value to set.

        Returns:
            str: The updated origin value.
        """
		self.origin = origin
		return self.origin

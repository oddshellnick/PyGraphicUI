class Boolean:
	"""
    Represents a boolean value for CSS properties.

    Attributes:
        boolean (str): The boolean value as a string ("1" or "0").

    :Usage:
        boolean = Boolean(boolean=True)
        boolean.boolean
        "1"

        boolean = Boolean(boolean=False)
        boolean.boolean
        "0"
    """
	
	def __init__(self, boolean: bool):
		"""
        Initializes a Boolean object.

        Args:
            boolean (bool): The boolean value.
        """
		self.boolean = ""
		self.set(boolean)
	
	def set(self, boolean: bool):
		"""
        Sets the boolean value.

        Args:
            boolean (bool): The boolean value to set.

        Returns:
            Boolean: The updated Boolean object.
        """
		self.boolean = "1" if boolean else "0"
		return self

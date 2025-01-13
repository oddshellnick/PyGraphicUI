class Opacity:
	"""
    Represents the opacity CSS property.

    Attributes:
        opacity (str): The opacity value as a string.

    :Usage:
        opacity = Opacity(127)
        opacity.opacity
        "opacity: 127"
    """
	
	def __init__(self, opacity: int):
		"""
        Initializes an Opacity object.

        Args:
            opacity (int): The opacity value (0-255).
        """
		self.opacity = ""
		self.set(opacity)
	
	def set(self, opacity: int = 255):
		"""
        Sets the opacity value.

        Args:
            opacity (int): The opacity value (0-255) to set.

        Returns:
            Opacity: The updated Opacity object.
        """
		self.opacity = "opacity: %d" % opacity
		return self

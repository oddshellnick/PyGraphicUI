from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length


class BorderTopRightRadius:
	"""
    Represents the border-top-right-radius CSS property.

    Attributes:
        border_top_right_radius (str): The border top right radius value.

    :Usage:
        border_top_right_radius = BorderTopRightRadius(border_radius=Length(PX(10)))
        border_top_right_radius.border_top_right_radius
        "border-top-right-radius: 10px"
    """
	
	def __init__(self, border_radius: Length):
		"""
        Initializes a BorderTopRightRadius object.

        Args:
            border_radius (Length): The border top right radius value.
        """
		self.border_top_right_radius = ""
		self.set(border_radius)
	
	def set(self, border_radius: Length):
		"""
        Sets the border top right radius value.

        Args:
            border_radius (Length): The border top right radius value.

        Returns:
            BorderTopRightRadius: The updated border top right radius object.
        """
		self.border_top_right_radius = "border-top-right-radius: %s" % border_radius.length
		return self


class BorderTopLeftRadius:
	"""
    Represents the border-top-left-radius CSS property.

    Attributes:
        border_top_left_radius (str): The border top left radius value.

    :Usage:
        border_top_left_radius = BorderTopLeftRadius(border_radius=Length(PX(10)))
        border_top_left_radius.border_top_left_radius
        "border-top-left-radius: 10px"
    """
	
	def __init__(self, border_radius: Length):
		"""
        Initializes a BorderTopLeftRadius object.

        Args:
            border_radius (Length): The border top left radius value.
        """
		self.border_top_left_radius = ""
		self.set(border_radius)
	
	def set(self, border_radius: Length):
		"""
        Sets the border top left radius value.

        Args:
            border_radius (Length): The border top left radius value.

        Returns:
            BorderTopLeftRadius: The updated border top left radius object.
        """
		self.border_top_left_radius = "border-top-left-radius: %s" % border_radius.length
		return self


class BorderRadius:
	"""
    Represents the border-radius CSS property.

    Attributes:
        border_radius (str): The border radius value.

    :Usage:
        border_radius = BorderRadius(border_radius=BoxLengths(length=[Length(PX(10)), Length(PX(20)), Length(PX(30)), Length(PX(40))]))
        border_radius.border_radius
        "border-radius: 10px 20px 30px 40px"
    """
	
	def __init__(self, border_radius: BoxLengths):
		"""
        Initializes a BorderRadius object.

        Args:
            border_radius (BoxLengths): The border radius value.
        """
		self.border_radius = ""
		self.set(border_radius)
	
	def set(self, border_radius: BoxLengths):
		"""
        Sets the border radius value.

        Args:
            border_radius (BoxLengths): The border radius value.

        Returns:
            BorderRadius: The updated border radius object.
        """
		self.border_radius = "border-radius: %s" % border_radius.length
		return self


class BorderBottomRightRadius:
	"""
    Represents the border-bottom-right-radius CSS property.

    Attributes:
        border_bottom_right_radius (str): The border bottom right radius value.

    :Usage:
        border_bottom_right_radius = BorderBottomRightRadius(border_radius=Length(PX(10)))
        border_bottom_right_radius.border_bottom_right_radius
        "border-bottom-right-radius: 10px"
    """
	
	def __init__(self, border_radius: Length):
		"""
        Initializes a BorderBottomRightRadius object.

        Args:
            border_radius (Length): The border bottom right radius value.
        """
		self.border_bottom_right_radius = ""
		self.set(border_radius)
	
	def set(self, border_radius: Length):
		"""
        Sets the border bottom right radius value.

        Args:
            border_radius (Length): The border bottom right radius value.

        Returns:
            BorderBottomRightRadius: The updated border bottom right radius object.
        """
		self.border_bottom_right_radius = "border-bottom-right-radius: %s" % border_radius.length
		return self


class BorderBottomLeftRadius:
	"""
    Represents the border-bottom-left-radius CSS property.

    Attributes:
        border_bottom_left_radius (str): The border bottom left radius value.

    :Usage:
        border_bottom_left_radius = BorderBottomLeftRadius(border_radius=Length(PX(10)))
        border_bottom_left_radius.border_bottom_left_radius
        "border-bottom-left-radius: 10px"
    """
	
	def __init__(self, border_radius: Length):
		"""
        Initializes a BorderBottomLeftRadius object.

        Args:
            border_radius (Length): The border bottom left radius value.
        """
		self.border_bottom_left_radius = ""
		self.set(border_radius)
	
	def set(self, border_radius: Length):
		"""
        Sets the border bottom left radius value.

        Args:
            border_radius (Length): The border bottom left radius value.

        Returns:
            BorderBottomLeftRadius: The updated border bottom left radius object.
        """
		self.border_bottom_left_radius = "border-bottom-left-radius: %s" % border_radius.length
		return self

class BorderStyle:
	"""
    Represents the border-style CSS property.

    Attributes:
        border_style (str): The border style value as a string.

    :Usage:
        border_style = BorderStyle("solid")
        border_style.border_style
        "solid"
    """
	
	def __init__(self, border_style: str):
		"""
        Initializes a BorderStyle object.

        Args:
            border_style (str): The border style value.
        """
		self.border_style = ""
		self.set(border_style)
	
	def set(self, border_style: str):
		"""
        Sets the border style value.

        Args:
            border_style (str): The border style value to set.

        Returns:
            BorderStyle: The updated BorderStyle object.
        """
		self.border_style = border_style
		return self


class BordersStyle:
	"""
    Represents the border-style CSS property for all sides of the border.

    Attributes:
        borders_style (str): The border style value as a string.

    :Usage:
        borders_style = BordersStyle(BorderStyle("solid"))
        borders_style.borders_style
        "border-style: solid"
    """
	
	def __init__(self, borders_style: BorderStyle):
		"""
        Initializes a BordersStyle object.

        Args:
            borders_style (BorderStyle): The border style value.
        """
		self.borders_style = ""
		self.set(borders_style)
	
	def set(self, borders_style: BorderStyle):
		"""
        Sets the border style value for all sides of the border.

        Args:
            borders_style (BorderStyle): The border style value to set.

        Returns:
            BordersStyle: The updated BordersStyle object.
        """
		self.borders_style = "border-style: %s" % borders_style.border_style
		return self


class BorderTopStyle:
	"""
    Represents the border-top-style CSS property.

    Attributes:
        borders_top_style (str): The border top style value as a string.

    :Usage:
        border_top_style = BorderTopStyle(BorderStyle("solid"))
        border_top_style.borders_top_style
        "border-top-style: solid"
    """
	
	def __init__(self, borders_style: BorderStyle):
		"""
        Initializes a BorderTopStyle object.

        Args:
            borders_style (BorderStyle): The border top style value.
        """
		self.borders_top_style = ""
		self.set(borders_style)
	
	def set(self, borders_style: BorderStyle):
		"""
        Sets the border top style value.

        Args:
            borders_style (BorderStyle): The border top style value to set.

        Returns:
            BorderTopStyle: The updated BorderTopStyle object.
        """
		self.borders_top_style = "border-top-style: %s" % borders_style.border_style
		return self


class BorderRightStyle:
	"""
    Represents the border-right-style CSS property.

    Attributes:
        borders_right_style (str): The border right style value as a string.

    :Usage:
        border_right_style = BorderRightStyle(BorderStyle("solid"))
        border_right_style.borders_right_style
        "border-right-style: solid"
    """
	
	def __init__(self, borders_style: BorderStyle):
		"""
        Initializes a BorderRightStyle object.

        Args:
            borders_style (BorderStyle): The border right style value.
        """
		self.borders_right_style = ""
		self.set(borders_style)
	
	def set(self, style: BorderStyle):
		"""
        Sets the border right style value.

        Args:
            style (BorderStyle): The border right style value to set.

        Returns:
            BorderRightStyle: The updated BorderRightStyle object.
        """
		self.borders_right_style = "border-right-style: %s" % style.border_style
		return self


class BorderLeftStyle:
	"""
    Represents the border-left-style CSS property.

    Attributes:
        borders_left_style (str): The border left style value as a string.

    :Usage:
        border_left_style = BorderLeftStyle(BorderStyle("solid"))
        border_left_style.borders_left_style
        "border-left-style: solid"
    """
	
	def __init__(self, borders_style: BorderStyle):
		"""
        Initializes a BorderLeftStyle object.

        Args:
            borders_style (BorderStyle): The border left style value.
        """
		self.borders_left_style = ""
		self.set(borders_style)
	
	def set(self, borders_style: BorderStyle):
		"""
        Sets the border left style value.

        Args:
            borders_style (BorderStyle): The border left style value to set.

        Returns:
            BorderLeftStyle: The updated BorderLeftStyle object.
        """
		self.borders_left_style = "border-left-style: %s" % borders_style.border_style
		return self


class BorderBottomStyle:
	"""
    Represents the border-bottom-style CSS property.

    Attributes:
        borders_bottom_style (str): The border bottom style value as a string.

    :Usage:
        border_bottom_style = BorderBottomStyle(BorderStyle("solid"))
        border_bottom_style.borders_bottom_style
        "border-bottom-style: solid"
    """
	
	def __init__(self, borders_style: BorderStyle):
		"""
        Initializes a BorderBottomStyle object.

        Args:
            borders_style (BorderStyle): The border bottom style value.
        """
		self.borders_bottom_style = ""
		self.set(borders_style)
	
	def set(self, borders_style: BorderStyle):
		"""
        Sets the border bottom style value.

        Args:
            borders_style (BorderStyle): The border bottom style value to set.

        Returns:
            BorderBottomStyle: The updated BorderBottomStyle object.
        """
		self.borders_bottom_style = "border-bottom-style: %s" % borders_style.border_style
		return self

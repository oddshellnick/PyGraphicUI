from PyGraphicUI.StyleSheets.utilities.Color import BoxColors, Brush


class BorderTopColor:
	"""
    Represents the border-top-color CSS property.

    Attributes:
        border_top_color (str): The border top color value.

    :Usage:
        color = Brush(color_string="#FF0000") # Red color
        border_top_color = BorderTopColor(border_color=color)
        border_top_color.border_top_color
        "border-top-color: #FF0000"
    """
	
	def __init__(self, border_color: Brush):
		"""
        Initializes a BorderTopColor object.

        Args:
            border_color (Brush): The border top color value.
        """
		self.border_top_color = ""
		self.set(border_color)
	
	def set(self, color: Brush):
		"""
        Sets the border top color value.

        Args:
            color (Brush): The border top color value.

        Returns:
            BorderTopColor: The updated border top color object.
        """
		self.border_top_color = "border-top-color: %s" % color.brush
		return self


class BorderRightColor:
	"""
    Represents the border-right-color CSS property.

    Attributes:
        border_right_color (str): The border right color value.

    :Usage:
        color = Brush(color_string="#00FF00") # Green color
        border_right_color = BorderRightColor(border_color=color)
        border_right_color.border_right_color
        "border-right-color: #00FF00"
    """
	
	def __init__(self, border_color: Brush):
		"""
        Initializes a BorderRightColor object.

        Args:
            border_color (Brush): The border right color value.
        """
		self.border_right_color = ""
		self.set(border_color)
	
	def set(self, color: Brush):
		"""
        Sets the border right color value.

        Args:
            color (Brush): The border right color value.

        Returns:
            BorderRightColor: The updated border right color object.
        """
		self.border_right_color = "border-right-color: %s" % color.brush
		return self


class BorderLeftColor:
	"""
    Represents the border-left-color CSS property.

    Attributes:
        border_left_color (str): The border left color value.

    :Usage:
        color = Brush(color_string="#0000FF") # Blue color
        border_left_color = BorderLeftColor(border_color=color)
        border_left_color.border_left_color
        "border-left-color: #0000FF"
    """
	
	def __init__(self, border_color: Brush):
		"""
        Initializes a BorderLeftColor object.

        Args:
            border_color (Brush): The border left color value.
        """
		self.border_left_color = ""
		self.set(border_color)
	
	def set(self, color: Brush):
		"""
        Sets the border left color value.

        Args:
            color (Brush): The border left color value.

        Returns:
            BorderLeftColor: The updated border left color object.
        """
		self.border_left_color = "border-left-color: %s" % color.brush
		return self


class BorderColor:
	"""
    Represents the border-color CSS property.

    Attributes:
        border_color (str): The border color value.

    :Usage:
        colors = BoxColors(
        ...    border_color=[
        ...        Brush(color_string="#FF0000"), # Red
        ...        Brush(color_string="#00FF00"), # Green
        ...        Brush(color_string="#0000FF"), # Blue
        ...        Brush(color_string="#000000")  # Black
        ...    ]
        ... )
        border_color = BorderColor(border_color=colors)
        border_color.border_color
        "border-color: #FF0000 #00FF00 #0000FF #000000"
    """
	
	def __init__(self, border_color: BoxColors):
		"""
        Initializes a BorderColor object.

        Args:
            border_color (BoxColors): The border color value.
        """
		self.border_color = ""
		self.set(border_color)
	
	def set(self, border_color: BoxColors):
		"""
        Sets the border color value.

        Args:
            border_color (BoxColors): The border color value.

        Returns:
            BorderColor: The updated border color object.
        """
		self.border_color = "border-color: %s" % border_color.color
		return self


class BorderBottomColor:
	"""
    Represents the border-bottom-color CSS property.

    Attributes:
        border_bottom_color (str): The border bottom color value.

    :Usage:
        color = Brush(color_string="#FFFF00") # Yellow color
        border_bottom_color = BorderBottomColor(border_color=color)
        border_bottom_color.border_bottom_color
        "border-bottom-color: #FFFF00"
    """
	
	def __init__(self, border_color: Brush):
		"""
        Initializes a BorderBottomColor object.

        Args:
            border_color (Brush): The border bottom color value.
        """
		self.border_bottom_color = ""
		self.set(border_color)
	
	def set(self, color: Brush):
		"""
        Sets the border bottom color value.

        Args:
            color (Brush): The border bottom color value.

        Returns:
            BorderBottomColor: The updated border bottom color object.
        """
		self.border_bottom_color = "border-bottom-color: %s" % color.brush
		return self

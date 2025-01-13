from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length


class BorderWidth:
	"""
    Represents the border-width CSS property.

    Attributes:
        border_width (str): The border width value as a string.

    :Usage:
        border_width = BorderWidth(BoxLengths(length=[Length(PX(1)), Length(PX(2)), Length(PX(3)), Length(PX(4))]))
        border_width.border_width
        "border-width: 1px 2px 3px 4px"
    """
	
	def __init__(self, border_width: BoxLengths):
		"""
        Initializes a BorderWidth object.

        Args:
            border_width (BoxLengths): The border width value.
        """
		self.border_width = ""
		self.set(border_width)
	
	def set(self, border_width: BoxLengths):
		"""
        Sets the border width value.

        Args:
            border_width (BoxLengths): The border width value to set.

        Returns:
            BorderWidth: The updated BorderWidth object.
        """
		self.border_width = "border-width: %s" % border_width.length
		return self


class BorderTopWidth:
	"""
    Represents the border-top-width CSS property.

    Attributes:
        border_top_width (str): The border top width value as a string.

    :Usage:
        border_top_width = BorderTopWidth(Length(PX(1)))
        border_top_width.border_top_width
        "border-top-width: 1px"
    """
	
	def __init__(self, border_width: Length):
		"""
        Initializes a BorderTopWidth object.

        Args:
            border_width (Length): The border top width value.
        """
		self.border_top_width = ""
		self.set(border_width)
	
	def set(self, border_width: Length):
		"""
        Sets the border top width value.

        Args:
            border_width (Length): The border top width value to set.

        Returns:
            BorderTopWidth: The updated BorderTopWidth object.
        """
		self.border_top_width = "border-top-width: %s" % border_width.length
		return self


class BorderRightWidth:
	"""
    Represents the border-right-width CSS property.

    Attributes:
        border_right_width (str): The border right width value as a string.

    :Usage:
        border_right_width = BorderRightWidth(Length(PX(1)))
        border_right_width.border_right_width
        "border-right-width: 1px"
    """
	
	def __init__(self, border_width: Length):
		"""
        Initializes a BorderRightWidth object.

        Args:
            border_width (Length): The border right width value.
        """
		self.border_right_width = ""
		self.set(border_width)
	
	def set(self, border_width: Length):
		"""
        Sets the border right width value.

        Args:
            border_width (Length): The border right width value to set.

        Returns:
            BorderRightWidth: The updated BorderRightWidth object.
        """
		self.border_right_width = "border-right-width: %s" % border_width.length
		return self


class BorderLeftWidth:
	"""
    Represents the border-left-width CSS property.

    Attributes:
        border_left_width (str): The border left width value as a string.

    :Usage:
        border_left_width = BorderLeftWidth(Length(PX(1)))
        border_left_width.border_left_width
        "border-left-width: 1px"
    """
	
	def __init__(self, border_width: Length):
		"""
        Initializes a BorderLeftWidth object.

        Args:
            border_width (Length): The border left width value.
        """
		self.border_left_width = ""
		self.set(border_width)
	
	def set(self, border_width: Length):
		"""
        Sets the border left width value.

        Args:
            border_width (Length): The border left width value to set.

        Returns:
            BorderLeftWidth: The updated BorderLeftWidth object.
        """
		self.border_left_width = "border-left-width: %s" % border_width.length
		return self


class BorderBottomWidth:
	"""
    Represents the border-bottom-width CSS property.

    Attributes:
        border_bottom_width (str): The border bottom width value as a string.

    :Usage:
        border_bottom_width = BorderBottomWidth(Length(PX(1)))
        border_bottom_width.border_bottom_width
        "border-bottom-width: 1px"
    """
	
	def __init__(self, border_width: Length):
		"""
        Initializes a BorderBottomWidth object.

        Args:
            border_width (Length): The border bottom width value.
        """
		self.border_bottom_width = ""
		self.set(border_width)
	
	def set(self, border_width: Length):
		"""
        Sets the border bottom width value.

        Args:
            border_width (Length): The border bottom width value to set.

        Returns:
            BorderBottomWidth: The updated BorderBottomWidth object.
        """
		self.border_bottom_width = "border-bottom-width: %s" % border_width.length
		return self

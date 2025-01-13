from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length


class MarginTop:
	"""
    Represents the margin-top CSS property.

    Attributes:
        margin_top (str): The margin top value as a string.

    :Usage:
        margin_top = MarginTop(Length(PX(10)))
        margin_top.margin_top
        "margin-top: 10px"
    """
	
	def __init__(self, margin: Length):
		"""
        Initializes a MarginTop object.

        Args:
            margin (Length): The margin top value.
        """
		self.margin_top = ""
		self.set(margin)
	
	def set(self, margin: Length):
		"""
        Sets the margin top value.

        Args:
            margin (Length): The margin top value to set.

        Returns:
            MarginTop: The updated MarginTop object.
        """
		self.margin_top = "margin-top: %s" % margin.length
		return self


class MarginRight:
	"""
    Represents the margin-right CSS property.

    Attributes:
        margin_right (str): The margin right value as a string.

    :Usage:
        margin_right = MarginRight(Length(PX(10)))
        margin_right.margin_right
        "margin-right: 10px"
    """
	
	def __init__(self, margin: Length):
		"""
        Initializes a MarginRight object.

        Args:
            margin (Length): The margin right value.
        """
		self.margin_right = ""
		self.set(margin)
	
	def set(self, margin: Length):
		"""
        Sets the margin right value.

        Args:
            margin (Length): The margin right value to set.

        Returns:
            MarginRight: The updated MarginRight object.
        """
		self.margin_right = "margin-right: %s" % margin.length
		return self


class MarginLeft:
	"""
    Represents the margin-left CSS property.

    Attributes:
        margin_left (str): The margin left value as a string.

    :Usage:
        margin_left = MarginLeft(Length(PX(10)))
        margin_left.margin_left
        "margin-left: 10px"
    """
	
	def __init__(self, margin: Length):
		"""
        Initializes a MarginLeft object.

        Args:
            margin (Length): The margin left value.
        """
		self.margin_left = ""
		self.set(margin)
	
	def set(self, margin: Length):
		"""
        Sets the margin left value.

        Args:
            margin (Length): The margin left value to set.

        Returns:
            MarginLeft: The updated MarginLeft object.
        """
		self.margin_left = "margin-left: %s" % margin.length
		return self


class MarginBottom:
	"""
    Represents the margin-bottom CSS property.

    Attributes:
        margin_bottom (str): The margin bottom value as a string.

    :Usage:
        margin_bottom = MarginBottom(Length(PX(10)))
        margin_bottom.margin_bottom
        "margin-bottom: 10px"
    """
	
	def __init__(self, margin: Length):
		"""
        Initializes a MarginBottom object.

        Args:
            margin (Length): The margin bottom value.
        """
		self.margin_bottom = ""
		self.set(margin)
	
	def set(self, margin: Length):
		"""
        Sets the margin bottom value.

        Args:
            margin (Length): The margin bottom value to set.

        Returns:
            MarginBottom: The updated MarginBottom object.
        """
		self.margin_bottom = "margin-bottom: %s" % margin.length
		return self


class Margin:
	"""
    Represents the margin CSS property.

    Attributes:
        margin (str): The margin value as a string.

    :Usage:
        margin = Margin(BoxLengths(length=[Length(PX(10)), Length(PX(20)), Length(PX(30)), Length(PX(40))]))
        margin.margin
        "margin: 10px 20px 30px 40px"
    """
	
	def __init__(self, margin: BoxLengths):
		"""
        Initializes a Margin object.

        Args:
            margin (BoxLengths): The margin value.
        """
		self.margin = ""
		self.set(margin)
	
	def set(self, margin: BoxLengths):
		"""
        Sets the margin value.

        Args:
            margin (BoxLengths): The margin value to set.

        Returns:
            Margin: The updated Margin object.
        """
		self.margin = "margin: %s" % margin.length
		return self

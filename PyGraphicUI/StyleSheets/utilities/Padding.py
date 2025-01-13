from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length


class PaddingTop:
	"""
    Represents the padding-top CSS property.

    Attributes:
        padding_top (str): The padding top value as a string.

    :Usage:
        padding_top = PaddingTop(Length(PX(10)))
        padding_top.padding_top
        "padding-top: 10px"
    """
	
	def __init__(self, padding: Length):
		"""
        Initializes a PaddingTop object.

        Args:
            padding (Length): The padding top value.
        """
		self.padding_top = ""
		self.set(padding)
	
	def set(self, padding: Length):
		"""
        Sets the padding top value.

        Args:
            padding (Length): The padding top value to set.

        Returns:
            PaddingTop: The updated PaddingTop object.
        """
		self.padding_top = "padding-top: %s" % padding.length
		return self


class PaddingRight:
	"""
    Represents the padding-right CSS property.

    Attributes:
        padding_right (str): The padding right value as a string.

    :Usage:
        padding_right = PaddingRight(Length(PX(10)))
        padding_right.padding_right
        "padding-right: 10px"
    """
	
	def __init__(self, padding: Length):
		"""
        Initializes a PaddingRight object.

        Args:
            padding (Length): The padding right value.
        """
		self.padding_right = ""
		self.set(padding)
	
	def set(self, padding: Length):
		"""
        Sets the padding right value.

        Args:
            padding (Length): The padding right value to set.

        Returns:
            PaddingRight: The updated PaddingRight object.
        """
		self.padding_right = "padding-right: %s" % padding.length
		return self


class PaddingLeft:
	"""
    Represents the padding-left CSS property.

    Attributes:
        padding_left (str): The padding left value as a string.

    :Usage:
        padding_left = PaddingLeft(Length(PX(10)))
        padding_left.padding_left
        "padding-left: 10px"
    """
	
	def __init__(self, padding: Length):
		"""
        Initializes a PaddingLeft object.

        Args:
            padding (Length): The padding left value.
        """
		self.padding_left = ""
		self.set(padding)
	
	def set(self, padding: Length):
		"""
        Sets the padding left value.

        Args:
            padding (Length): The padding left value to set.

        Returns:
            PaddingLeft: The updated PaddingLeft object.
        """
		self.padding_left = "padding-left: %s" % padding.length
		return self


class PaddingBottom:
	"""
    Represents the padding-bottom CSS property.

    Attributes:
        padding_bottom (str): The padding bottom value as a string.

    :Usage:
        padding_bottom = PaddingBottom(Length(PX(10)))
        padding_bottom.padding_bottom
        "padding-bottom: 10px"
    """
	
	def __init__(self, padding: Length):
		"""
        Initializes a PaddingBottom object.

        Args:
            padding (Length): The padding bottom value.
        """
		self.padding_bottom = ""
		self.set(padding)
	
	def set(self, padding: Length):
		"""
        Sets the padding bottom value.

        Args:
            padding (Length): The padding bottom value to set.

        Returns:
            PaddingBottom: The updated PaddingBottom object.
        """
		self.padding_bottom = "padding-bottom: %s" % padding.length
		return self


class Padding:
	"""
    Represents the padding CSS property.

    Attributes:
        padding (str): The padding value as a string.

    :Usage:
        padding = Padding(BoxLengths(length=[Length(PX(10)), Length(PX(20)), Length(PX(30)), Length(PX(40))]))
        padding.padding
        "padding: 10px 20px 30px 40px"
    """
	
	def __init__(self, padding: BoxLengths):
		"""
        Initializes a Padding object.

        Args:
            padding (BoxLengths): The padding value.
        """
		self.padding = ""
		self.set(padding)
	
	def set(self, padding: BoxLengths):
		"""
        Sets the padding value.

        Args:
            padding (BoxLengths): The padding value to set.

        Returns:
            Padding: The updated Padding object.
        """
		self.padding = "padding: %s" % padding.length
		return self

from PyGraphicUI.StyleSheets.utilities.Color import Brush
from PyGraphicUI.StyleSheets.utilities.Size import Length
from PyGraphicUI.StyleSheets.utilities.BorderStyle import BorderStyle


class BorderTop:
	"""
    Represents the border-top CSS property.

    Attributes:
        border_top (str): The border top value.

    :Usage:
        border_top = BorderTop(
            border_width=Length(length="1px"),
            border_style=BorderStyle(border_style="solid"),
            border_color=Brush(color_string="#FF0000") # Red color
        )
        border_top.border_top
        "border-top: 1px solid #FF0000"
    """
	
	def __init__(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Initializes a BorderTop object.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.
        """
		self.border_top = ""
		self.set(border_width, border_style, border_color)
	
	def set(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Sets the border top value.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.

        Returns:
            BorderTop: The updated border top object.
        """
		self.border_top = "border-top: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self


class BorderRight:
	"""
    Represents the border-right CSS property.

    Attributes:
        border_right (str): The border right value.

    :Usage:
        border_right = BorderRight(
            border_width=Length(length="1px"),
            border_style=BorderStyle(border_style="solid"),
            border_color=Brush(color_string="#00FF00") # Green color
        )
        border_right.border_right
        "border-right: 1px solid #00FF00"
    """
	
	def __init__(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Initializes a BorderRight object.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.
        """
		self.border_right = ""
		self.set(border_width, border_style, border_color)
	
	def set(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Sets the border right value.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.

        Returns:
            BorderRight: The updated border right object.
        """
		self.border_right = "border-right: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self


class BorderLeft:
	"""
    Represents the border-left CSS property.

    Attributes:
        border_left (str): The border left value.

    :Usage:
        border_left = BorderLeft(
            border_width=Length(length="1px"),
            border_style=BorderStyle(border_style="solid"),
            border_color=Brush(color_string="#0000FF") # Blue color
        )
        border_left.border_left
        "border-left: 1px solid #0000FF"
    """
	
	def __init__(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Initializes a BorderLeft object.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.
        """
		self.border_left = ""
		self.set(border_width, border_style, border_color)
	
	def set(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Sets the border left value.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.

        Returns:
            BorderLeft: The updated border left object.
        """
		self.border_left = "border-left: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self


class BorderBottom:
	"""
    Represents the border-bottom CSS property.

    Attributes:
        border_bottom (str): The border bottom value.

    :Usage:
        border_bottom = BorderBottom(
            border_width=Length(length="1px"),
            border_style=BorderStyle(border_style="solid"),
            border_color=Brush(color_string="#FFFF00") # Yellow color
        )
        border_bottom.border_bottom
        "border-bottom: 1px solid #FFFF00"
    """
	
	def __init__(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Initializes a BorderBottom object.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.
        """
		self.border_bottom = ""
		self.set(border_width, border_style, border_color)
	
	def set(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Sets the border bottom value.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.

        Returns:
            BorderBottom: The updated border bottom object.
        """
		self.border_bottom = "border-bottom: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self


class Border:
	"""
    Represents the border shorthand CSS property.

    Attributes:
        border (str): The border value.

    :Usage:
        border = Border(
            border_width=Length(length="1px"),
            border_style=BorderStyle(border_style="solid"),
            border_color=Brush(color_string="#FF0000") # Red color
        )
        border.border
        "border: 1px solid #FF0000"
    """
	
	def __init__(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Initializes a Border object.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.
        """
		self.border = ""
		self.set(border_width, border_style, border_color)
	
	def set(
			self,
			border_width: Length,
			border_style: BorderStyle,
			border_color: Brush
	):
		"""
        Sets the border value.

        Args:
            border_width (Length): The border width value.
            border_style (BorderStyle): The border style value.
            border_color (Brush): The border color value.

        Returns:
            Border: The updated border object.
        """
		self.border = "border: %s" % " ".join([border_width.length, border_style.border_style, border_color.brush])
		return self

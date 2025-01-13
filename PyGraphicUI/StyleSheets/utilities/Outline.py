from PyGraphicUI.StyleSheets.utilities.Color import BoxColors, Color
from PyGraphicUI.StyleSheets.utilities.BorderStyle import BorderStyle
from PyGraphicUI.StyleSheets.utilities.Size import BoxLengths, Length


class OutlineTopRightRadius:
	"""
    Represents the outline-top-right-radius CSS property.

    Attributes:
        outline_top_right_radius (str): The outline top right radius value.

    :Usage:
        outline_top_right_radius = OutlineTopRightRadius(outline_radius=Length(length="10px"))
        outline_top_right_radius.outline_top_right_radius
        "outline-top-right-radius: 10px"
    """
	
	def __init__(self, outline_radius: Length):
		"""
        Initializes an OutlineTopRightRadius object.

        Args:
            outline_radius (Length): The outline top right radius value.
        """
		self.outline_top_right_radius = ""
		self.set(outline_radius)
	
	def set(self, outline_radius: Length):
		"""
        Sets the outline top right radius value.

        Args:
            outline_radius (Length): The outline top right radius value.

        Returns:
            OutlineTopRightRadius: The updated outline top right radius object.
        """
		self.outline_top_right_radius = "outline-top-right-radius: %s" % outline_radius.length
		return self


class OutlineTopLeftRadius:
	"""
    Represents the outline-top-left-radius CSS property.

    Attributes:
        outline_top_left_radius (str): The outline top left radius value.

    :Usage:
        outline_top_left_radius = OutlineTopLeftRadius(outline_radius=Length(length="10px"))
        outline_top_left_radius.outline_top_left_radius
        "outline-top-left-radius: 10px"
    """
	
	def __init__(self, outline_radius: Length):
		"""
        Initializes an OutlineTopLeftRadius object.

        Args:
            outline_radius (Length): The outline top left radius value.
        """
		self.outline_top_left_radius = ""
		self.set(outline_radius)
	
	def set(self, outline_radius: Length):
		"""
        Sets the outline top left radius value.

        Args:
            outline_radius (Length): The outline top left radius value.

        Returns:
            OutlineTopLeftRadius: The updated outline top left radius object.
        """
		self.outline_top_left_radius = "outline-top-left-radius: %s" % outline_radius.length
		return self


class OutlineStyle:
	"""
    Represents the outline-style CSS property.

    Attributes:
        outline_style (str): The outline style value.

    :Usage:
        outline_style = OutlineStyle(outline_style=BorderStyle(border_style="solid"))
        outline_style.outline_style
        "outline-style: solid"
    """
	
	def __init__(self, outline_style: BorderStyle):
		"""
        Initializes an OutlineStyle object.

        Args:
            outline_style (BorderStyle): The outline style value.
        """
		self.outline_style = ""
		self.set(outline_style)
	
	def set(self, outline_style: BorderStyle):
		"""
        Sets the outline style value.

        Args:
            outline_style (BorderStyle): The outline style value.

        Returns:
            OutlineStyle: The updated outline style object.
        """
		self.outline_style = "outline-style: %s" % outline_style.border_style
		return self


class OutlineRadius:
	"""
    Represents the outline-radius CSS property.

    Attributes:
        outline_radius (str): The outline radius value.

    :Usage:
        outline_radius = OutlineRadius(outline_radius=BoxLengths(length=[Length(length="10px"), Length(length="20px"), Length(length="30px"), Length(length="40px")]))
        outline_radius.outline_radius
        "outline-radius: 10px 20px 30px 40px"
    """
	
	def __init__(self, outline_radius: BoxLengths):
		"""
        Initializes an OutlineRadius object.

        Args:
            outline_radius (BoxLengths): The outline radius value.
        """
		self.outline_radius = ""
		self.set(outline_radius)
	
	def set(self, outline_radius: BoxLengths):
		"""
        Sets the outline radius value.

        Args:
            outline_radius (BoxLengths): The outline radius value.

        Returns:
            OutlineRadius: The updated outline radius object.
        """
		self.outline_radius = "outline-radius: %s" % outline_radius.length
		return self


class OutlineColor:
	"""
    Represents the outline-color CSS property.

    Attributes:
        outline_color (str): The outline color value.

    :Usage:
        outline_color = OutlineColor(outline_color=BoxColors(color_string="#FF0000")) # Red color
        outline_color.outline_color
        "outline-color: #FF0000"
    """
	
	def __init__(self, outline_color: BoxColors):
		"""
        Initializes an OutlineColor object.

        Args:
            outline_color (BoxColors): The outline color value.
        """
		self.outline_color = ""
		self.set(outline_color)
	
	def set(self, outline_color: BoxColors):
		"""
        Sets the outline color value.

        Args:
            outline_color (BoxColors): The outline color value.

        Returns:
            OutlineColor: The updated outline color object.
        """
		self.outline_color = "outline-color: %s" % outline_color.color
		return self


class OutlineBottomRightRadius:
	"""
    Represents the outline-bottom-right-radius CSS property.

    Attributes:
        outline_bottom_right_radius (str): The outline bottom right radius value.

    :Usage:
        outline_bottom_right_radius = OutlineBottomRightRadius(outline_radius=Length(length="10px"))
        outline_bottom_right_radius.outline_bottom_right_radius
        "outline-bottom-right-radius: 10px"
    """
	
	def __init__(self, outline_radius: Length):
		"""
        Initializes an OutlineBottomRightRadius object.

        Args:
            outline_radius (Length): The outline bottom right radius value.
        """
		self.outline_bottom_right_radius = ""
		self.set(outline_radius)
	
	def set(self, outline_radius: Length):
		"""
        Sets the outline bottom right radius value.

        Args:
            outline_radius (Length): The outline bottom right radius value.

        Returns:
            OutlineBottomRightRadius: The updated outline bottom right radius object.
        """
		self.outline_bottom_right_radius = "outline-bottom-right-radius: %s" % outline_radius.length
		return self


class OutlineBottomLeftRadius:
	"""
    Represents the outline-bottom-left-radius CSS property.

    Attributes:
        outline_bottom_left_radius (str): The outline bottom left radius value.

    :Usage:
        outline_bottom_left_radius = OutlineBottomLeftRadius(outline_radius=Length(length="10px"))
        outline_bottom_left_radius.outline_bottom_left_radius
        "outline-bottom-left-radius: 10px"
    """
	
	def __init__(self, outline_radius: Length):
		"""
        Initializes an OutlineBottomLeftRadius object.

        Args:
            outline_radius (Length): The outline bottom left radius value.
        """
		self.outline_bottom_left_radius = ""
		self.set(outline_radius)
	
	def set(self, outline_radius: Length):
		"""
        Sets the outline bottom left radius value.

        Args:
            outline_radius (Length): The outline bottom left radius value.

        Returns:
            OutlineBottomLeftRadius: The updated outline bottom left radius object.
        """
		self.outline_bottom_left_radius = "outline-bottom-left-radius: %s" % outline_radius.length
		return self


class Outline:
	"""
    Represents the outline CSS property.

    Attributes:
        outline (str): The outline value.

    :Usage:
        outline = Outline(
            outline_offset=Length(length="10px"),
            outline_style=BorderStyle(border_style="solid"),
            outline_color=Color(color_string="#FF0000") # Red color
        )
        outline.outline
        "outline: 10px solid #FF0000"
    """
	
	def __init__(
			self,
			outline_offset: Length,
			outline_style: BorderStyle,
			outline_color: Color
	):
		"""
        Initializes an Outline object.

        Args:
            outline_offset (Length): The outline offset value.
            outline_style (BorderStyle): The outline style value.
            outline_color (Color): The outline color value.
        """
		self.outline = ""
		self.set(outline_offset, outline_style, outline_color)
	
	def set(
			self,
			outline_offset: Length,
			outline_style: BorderStyle,
			outline_color: Color
	):
		"""
        Sets the outline value.

        Args:
            outline_offset (Length): The outline offset value.
            outline_style (BorderStyle): The outline style value.
            outline_color (Color): The outline color value.

        Returns:
            Outline: The updated outline object.
        """
		self.outline = "outline: %s %s %s" % (outline_offset.length, outline_style.border_style, outline_color.color)
		return self

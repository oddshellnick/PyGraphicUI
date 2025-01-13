import typing
from PyGraphicUI.StyleSheets.utilities.Size import EM, EX, PT, PX


class FontFamily:
	"""
    Represents the font-family CSS property.

    Attributes:
        font_family (str): The font family value as a string.

    :Usage:
        font_family = FontFamily("Arial")
        font_family.font_family
        "Arial"
    """
	
	def __init__(self, font_family: str):
		"""
        Initializes a FontFamily object.

        Args:
            font_family (str): The font family value.
        """
		self.font_family = ""
		self.set(font_family)
	
	def set(self, font_family: str):
		"""
        Sets the font family value.

        Args:
            font_family (str): The font family value to set.

        Returns:
            FontFamily: The updated FontFamily object.
        """
		self.font_family = font_family
		return self.font_family


class FontSize:
	"""
    Represents the font-size CSS property.

    Attributes:
        font_size (str): The font size value as a string.

    :Usage:
        font_size = FontSize(PX(12))
        font_size.font_size
        "12px"
    """
	
	def __init__(self, length_string: typing.Union[PX, PT, EM, EX]):
		"""
        Initializes a FontSize object.

        Args:
            length_string (typing.Union[PX, PT, EM, EX]): The font size value.
        """
		self.font_size = ""
		self.set(length_string)
	
	def set(self, length_string: typing.Union[PX, PT, EM, EX]):
		"""
        Sets the font size value.

        Args:
            length_string (typing.Union[PX, PT, EM, EX]): The font size value to set.

        Returns:
            FontSize: The updated FontSize object.
        """
		self.font_size = length_string.length_string


class FontStyle:
	"""
    Represents the font-style CSS property.

    Attributes:
        font_style (str): The font style value as a string.

    :Usage:
        font_style = FontStyle("italic")
        font_style.font_style
        "italic"
    """
	
	def __init__(self, font_style: str):
		"""
        Initializes a FontStyle object.

        Args:
            font_style (str): The font style value.
        """
		self.font_style = ""
		self.set(font_style)
	
	def set(self, font_style: str):
		"""
        Sets the font style value.

        Args:
            font_style (str): The font style value to set.

        Returns:
            FontStyle: The updated FontStyle object.
        """
		self.font_style = font_style
		return self


class FontWeight:
	"""
    Represents the font-weight CSS property.

    Attributes:
        font_weight (str): The font weight value as a string.

    :Usage:
        font_weight = FontWeight("bold")
        font_weight.font_weight
        "bold"
    """
	
	def __init__(self, font_weight: str):
		"""
        Initializes a FontWeight object.

        Args:
            font_weight (str): The font weight value.
        """
		self.font_weight = ""
		self.set(font_weight)
	
	def set(self, font_weight: str):
		"""
        Sets the font weight value.

        Args:
            font_weight (str): The font weight value to set.

        Returns:
            FontWeight: The updated FontWeight object.
        """
		self.font_weight = font_weight
		return self


class Font:
	"""
    Represents the font CSS property.

    Attributes:
        font (str): The font value as a string.

    :Usage:
        font = Font(FontStyle("italic"), FontWeight("bold"), FontSize(PX(12)), FontFamily("Arial"))
        font.font
        "font: bold italic 12px Arial"
    """
	
	def __init__(
			self,
			font_style: FontStyle,
			font_weight: FontWeight,
			font_size: FontSize,
			font_family: typing.Optional[FontFamily] = None
	):
		"""
        Initializes a Font object.

        Args:
            font_style (FontStyle): The font style value.
            font_weight (FontWeight): The font weight value.
            font_size (FontSize): The font size value.
            font_family (typing.Optional[FontFamily]): The font family value (optional).
        """
		self.font = ""
		self.set(font_weight, font_style, font_size, font_family)
	
	def set(
			self,
			font_weight: FontWeight,
			font_style: FontStyle,
			font_size: FontSize,
			font_family: typing.Optional[FontFamily] = None
	):
		"""
        Sets the font value.

        Args:
            font_weight (FontWeight): The font weight value.
            font_style (FontStyle): The font style value.
            font_size (FontSize): The font size value.
            font_family (typing.Optional[FontFamily]): The font family value (optional).

        Returns:
            Font: The updated Font object.
        """
		instance = [font_weight.font_weight, font_style.font_style, font_size.font_size]
		
		if font_family is not None:
			instance.append(font_family.font_family)
		
		self.font = "font: %s" % " ".join(instance)
		return self

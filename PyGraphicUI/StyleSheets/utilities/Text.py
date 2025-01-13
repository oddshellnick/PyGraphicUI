from PyGraphicUI.StyleSheets.utilities.Color import Brush
from PyGraphicUI.StyleSheets.utilities.Position import Alignment


class TextProperty:
	"""
    Represents the qproperty-text CSS property.

    Attributes:
        text (str): The text value as a string.

    :Usage:
        text_property = TextProperty("Hello, world!")
        text_property.text
        "qproperty-text: Hello, world!"
    """
	
	def __init__(self, text: str):
		"""
        Initializes a TextProperty object.

        Args:
            text (str): The text value.
        """
		self.text = ""
		self.set(text)
	
	def set(self, text: str):
		"""
        Sets the text value.

        Args:
            text (str): The text value to set.

        Returns:
            TextProperty: The updated TextProperty object.
        """
		self.text = "qproperty-text: %s" % text
		return self


class TextDecoration:
	"""
    Represents the text-decoration CSS property.

    Attributes:
        text_decoration (str): The text decoration value as a string.

    :Usage:
        text_decoration = TextDecoration(Alignment("underline"))
        text_decoration.text_decoration
        "text-decoration: underline"
    """
	
	def __init__(self, text_decoration: Alignment):
		"""
        Initializes a TextDecoration object.

        Args:
            text_decoration (Alignment): The text decoration value.
        """
		self.text_decoration = ""
		self.set(text_decoration)
	
	def set(self, text_decoration: Alignment):
		"""
        Sets the text decoration value.

        Args:
            text_decoration (Alignment): The text decoration value to set.

        Returns:
            TextDecoration: The updated TextDecoration object.
        """
		self.text_decoration = "text-decoration: %s" % text_decoration.alignment
		return self


class TextColor:
	"""
    Represents the color CSS property.

    Attributes:
        text_color (str): The text color value as a string.

    :Usage:
        text_color = TextColor(Brush("#000000"))
        text_color.text_color
        "color: #000000"
    """
	
	def __init__(self, text_color: Brush):
		"""
        Initializes a TextColor object.

        Args:
            text_color (Brush): The text color value.
        """
		self.text_color = ""
		self.set(text_color)
	
	def set(self, text_color: Brush):
		"""
        Sets the text color value.

        Args:
            text_color (Brush): The text color value to set.

        Returns:
            TextColor: The updated TextColor object.
        """
		self.text_color = "color: %s" % text_color.brush
		return self


class TextAlign:
	"""
    Represents the text-align CSS property.

    Attributes:
        text_align (str): The text align value as a string.

    :Usage:
        text_align = TextAlign(Alignment("center"))
        text_align.text_align
        "text-align: center"
    """
	
	def __init__(self, text_align: Alignment):
		"""
        Initializes a TextAlign object.

        Args:
            text_align (Alignment): The text align value.
        """
		self.text_align = ""
		self.set(text_align)
	
	def set(self, text_align: Alignment):
		"""
        Sets the text align value.

        Args:
            text_align (Alignment): The text align value to set.

        Returns:
            TextAlign: The updated TextAlign object.
        """
		self.text_align = "text-align: %s" % text_align.alignment
		return self


class PlaceholderTextColor:
	"""
    Represents the placeholder-text-color CSS property.

    Attributes:
        placeholder_text_color (str): The placeholder text color value as a string.

    :Usage:
        placeholder_text_color = PlaceholderTextColor(Brush("#AAAAAA"))
        placeholder_text_color.placeholder_text_color
        "placeholder-text-color: #AAAAAA"
    """
	
	def __init__(self, placeholder_text_color: Brush):
		"""
        Initializes a PlaceholderTextColor object.

        Args:
            placeholder_text_color (Brush): The placeholder text color value.
        """
		self.placeholder_text_color = ""
		self.set(placeholder_text_color)
	
	def set(self, placeholder_text_color: Brush):
		"""
        Sets the placeholder text color value.

        Args:
            placeholder_text_color (Brush): The placeholder text color value to set.

        Returns:
            PlaceholderTextColor: The updated PlaceholderTextColor object.
        """
		self.placeholder_text_color = "placeholder-text-color: %s" % placeholder_text_color.brush
		return self

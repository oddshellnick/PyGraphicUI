import typing


class EX:
	"""
    Represents a length in ex units.

    Attributes:
        length_string (str): The length in ex units as a string.

    :Usage:
        ex = EX(10)
        ex.length_string
        "10ex"
    """
	
	def __init__(self, ex: int):
		"""
        Initializes an EX object.

        Args:
            ex (int): The length in ex units.
        """
		self.length_string = "%dex" % ex


class EM:
	"""
    Represents a length in em units.

    Attributes:
        length_string (str): The length in em units as a string.

    :Usage:
        em = EM(10)
        em.length_string
        "10em"
    """
	
	def __init__(self, em: int):
		"""
        Initializes an EM object.

        Args:
            em (int): The length in em units.
        """
		self.length_string = "%dem" % em


class PT:
	"""
    Represents a length in pt units.

    Attributes:
        length_string (str): The length in pt units as a string.

    :Usage:
        pt = PT(10)
        pt.length_string
        "10pt"
    """
	
	def __init__(self, pt: int):
		"""
        Initializes a PT object.

        Args:
            pt (int): The length in pt units.
        """
		self.length_string = "%dpt" % pt


class PX:
	"""
    Represents a length in px units.

    Attributes:
        length_string (str): The length in px units as a string.

    :Usage:
        px = PX(10)
        px.length_string
        "10px"
    """
	
	def __init__(self, px: int):
		"""
        Initializes a PX object.

        Args:
            px (int): The length in px units.
        """
		self.length_string = "%dpx" % px


class Length:
	"""
    Represents a length in different units.

    Attributes:
        length (str): The length in string format.

    :Usage:
        length = Length(PX(10))
        length.length
        "10px"
    """
	
	def __init__(self, length_string: typing.Union[PX, PT, EM, EX]):
		"""
        Initializes a Length object.

        Args:
            length_string (typing.Union[PX, PT, EM, EX]): The length in different units.
        """
		self.length = ""
		self.set(length_string)
	
	def set(self, length_string: typing.Union[PX, PT, EM, EX]):
		"""
        Sets the length attribute.

        Args:
            length_string (typing.Union[PX, PT, EM, EX]): The length in different units.
        """
		self.length = length_string.length_string


class Width:
	"""
    Represents the width of an element.

    Attributes:
        width (str): The width of the element as a string.

    :Usage:
        width = Width(Length(PX(100)))
        width.width
        "width: 100px"
    """
	
	def __init__(self, width: Length):
		"""
        Initializes a Width object.

        Args:
            width (Length): The width of the element.
        """
		self.width = ""
		self.set(width)
	
	def set(self, width: Length):
		"""
        Sets the width attribute.

        Args:
            width (Length): The width of the element.

        Returns:
            Width: The Width object.
        """
		self.width = "width: %s" % width.length
		return self


class MinWidth:
	"""
    Represents the minimum width of an element.

    Attributes:
        min_width (str): The minimum width of the element as a string.

    :Usage:
        min_width = MinWidth(Length(PX(100)))
        min_width.min_width
        "min-width: 100px"
    """
	
	def __init__(self, min_width: Length):
		"""
        Initializes a MinWidth object.

        Args:
            min_width (Length): The minimum width of the element.
        """
		self.min_width = ""
		self.set(min_width)
	
	def set(self, min_width: Length):
		"""
        Sets the min_width attribute.

        Args:
            min_width (Length): The minimum width of the element.

        Returns:
            MinWidth: The MinWidth object.
        """
		self.min_width = "min-width: %s" % min_width.length
		return self


class MinHeight:
	"""
    Represents the minimum height of an element.

    Attributes:
        min_height (str): The minimum height of the element as a string.

    :Usage:
        min_height = MinHeight(Length(PX(100)))
        min_height.min_height
        "min-height: 100px"
    """
	
	def __init__(self, min_height: Length):
		"""
        Initializes a MinHeight object.

        Args:
            min_height (Length): The minimum height of the element.
        """
		self.min_height = ""
		self.set(min_height)
	
	def set(self, min_height: Length):
		"""
        Sets the min_height attribute.

        Args:
            min_height (Length): The minimum height of the element.

        Returns:
            MinHeight: The MinHeight object.
        """
		self.min_height = "min-height: %s" % min_height.length
		return self


class MaxWidth:
	"""
    Represents the maximum width of an element.

    Attributes:
        max_width (str): The maximum width of the element as a string.

    :Usage:
        max_width = MaxWidth(Length(PX(100)))
        max_width.max_width
        "max-width: 100px"
    """
	
	def __init__(self, max_width: Length):
		"""
        Initializes a MaxWidth object.

        Args:
            max_width (Length): The maximum width of the element.
        """
		self.max_width = ""
		self.set(max_width)
	
	def set(self, max_width: Length):
		"""
        Sets the max_width attribute.

        Args:
            max_width (Length): The maximum width of the element.

        Returns:
            MaxWidth: The MaxWidth object.
        """
		self.max_width = "max-width: %s" % max_width.length
		return self


class MaxHeight:
	"""
    Represents the maximum height of an element.

    Attributes:
        max_height (str): The maximum height of the element as a string.

    :Usage:
        max_height = MaxHeight(Length(PX(100)))
        max_height.max_height
        "max-height: 100px"
    """
	
	def __init__(self, max_height: Length):
		"""
        Initializes a MaxHeight object.

        Args:
            max_height (Length): The maximum height of the element.
        """
		self.max_height = ""
		self.set(max_height)
	
	def set(self, max_height: Length):
		"""
        Sets the max_height attribute.

        Args:
            max_height (Length): The maximum height of the element.

        Returns:
            MaxHeight: The MaxHeight object.
        """
		self.max_height = "max-height: %s" % max_height.length
		return self


class Height:
	"""
    Represents the height of an element.

    Attributes:
        height (str): The height of the element as a string.

    :Usage:
        height = Height(Length(PX(100)))
        height.height
        "height: 100px"
    """
	
	def __init__(self, height: Length):
		"""
        Initializes a Height object.

        Args:
            height (Length): The height of the element.
        """
		self.height = ""
		self.set(height)
	
	def set(self, height: Length):
		"""
        Sets the height attribute.

        Args:
            height (Length): The height of the element.

        Returns:
            Height: The Height object.
        """
		self.height = "height: %s" % height.length
		return self


class BoxLengths:
	"""
    Represents lengths for a box model.

    Attributes:
        length (str): The lengths for the box model as a string.

    :Usage:
        box_lengths = BoxLengths(Length(PX(100)))
        box_lengths.length
        "100px"
        box_lengths = BoxLengths([Length(PX(100)), Length(PX(200))])
        box_lengths.length
        "100px 200px"
    """
	
	def __init__(self, length: typing.Union[Length, typing.Iterable[Length]]):
		"""
        Initializes a BoxLengths object.

        Args:
            length (typing.Union[Length, typing.Iterable[Length]]): The lengths for the box model.
        """
		self.length = ""
		self.set(length)
	
	def set(self, lengths: typing.Union[Length, typing.Iterable[Length]]):
		"""
        Sets the length attribute.

        Args:
            lengths (typing.Union[Length, typing.Iterable[Length]]): The lengths for the box model.

        Returns:
            BoxLengths: The BoxLengths object.
        """
		self.length = " ".join([length.length for length in lengths]) if isinstance(lengths, typing.Iterable) else lengths.length
		return self

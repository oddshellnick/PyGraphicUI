import array
import typing
import collections
from PyGraphicUI.StyleSheets.utilities.Size import Length


class Up:
	"""
    Represents the up value for alignment in a layout.

    Attributes:
        up (str): The up value as a string.

    :Usage:
        up = Up(Length(PX(10)))
        up.up
        "up: 10px"
    """
	
	def __init__(self, up: Length):
		"""
        Initializes an Up object.

        Args:
            up (Length): The up value.
        """
		self.up = ""
		self.set(up)
	
	def set(self, up: Length):
		"""
        Sets the up value.

        Args:
            up (Length): The up value to set.

        Returns:
            Up: The updated Up object.
        """
		self.up = "up: %s" % up.length
		return self


class Spacing:
	"""
    Represents the spacing value for alignment in a layout.

    Attributes:
        spacing (str): The spacing value as a string.

    :Usage:
        spacing = Spacing(Length(PX(10)))
        spacing.spacing
        "spacing: 10px"
    """
	
	def __init__(self, spacing: Length):
		"""
        Initializes a Spacing object.

        Args:
            spacing (Length): The spacing value.
        """
		self.spacing = ""
		self.set(spacing)
	
	def set(self, spacing: Length):
		"""
        Sets the spacing value.

        Args:
            spacing (Length): The spacing value to set.

        Returns:
            Spacing: The updated Spacing object.
        """
		self.spacing = "spacing: %s" % spacing.length
		return self


class Right:
	"""
    Represents the right value for alignment in a layout.

    Attributes:
        right (str): The right value as a string.

    :Usage:
        right = Right(Length(PX(10)))
        right.right
        "right: 10px"
    """
	
	def __init__(self, right: Length):
		"""
        Initializes a Right object.

        Args:
            right (Length): The right value.
        """
		self.right = ""
		self.set(right)
	
	def set(self, right: Length):
		"""
        Sets the right value.

        Args:
            right (Length): The right value to set.

        Returns:
            Right: The updated Right object.
        """
		self.right = "right: %s" % right.length
		return self


class Left:
	"""
    Represents the left value for alignment in a layout.

    Attributes:
        left (str): The left value as a string.

    :Usage:
        left = Left(Length(PX(10)))
        left.left
        "left: 10px"
    """
	
	def __init__(self, left: Length):
		"""
        Initializes a Left object.

        Args:
            left (Length): The left value.
        """
		self.left = ""
		self.set(left)
	
	def set(self, left: Length):
		"""
        Sets the left value.

        Args:
            left (Length): The left value to set.

        Returns:
            Left: The updated Left object.
        """
		self.left = "left: %s" % left.length
		return self


class Bottom:
	"""
    Represents the bottom value for alignment in a layout.

    Attributes:
        bottom (str): The bottom value as a string.

    :Usage:
        bottom = Bottom(Length(PX(10)))
        bottom.bottom
        "bottom: 10px"
    """
	
	def __init__(self, bottom: Length):
		"""
        Initializes a Bottom object.

        Args:
            bottom (Length): The bottom value.
        """
		self.bottom = ""
		self.set(bottom)
	
	def set(self, bottom: Length):
		"""
        Sets the bottom value.

        Args:
            bottom (Length): The bottom value to set.

        Returns:
            Bottom: The updated Bottom object.
        """
		self.bottom = "bottom: %s" % bottom.length
		return self


class Alignment:
	"""
    Represents the alignment values for alignment in a layout.

    Attributes:
        alignment (str): The alignment values as a string.

    :Usage:
        alignment = Alignment("center")
        alignment.alignment
        "center"
        alignment = Alignment(["center", "space-around"])
        alignment.alignment
        "center space-around"
    """
	
	def __init__(
			self,
			alignment: typing.Union[str, list[str], tuple[str], array.array[str], collections.deque[str]]
	):
		"""
        Initializes an Alignment object.

        Args:
            alignment (typing.Union[str, list[str], tuple[str], array.array[str], collections.deque[str]]): The alignment value(s).
        """
		self.alignment = ""
		
		if isinstance(alignment, str):
			self.set(alignment)
		elif isinstance(alignment, (list, tuple, array.array, collections.deque)) and len(alignment) > 0:
			self.set(alignment[0])
			
			
			if len(alignment) > 1:
				for i in range(1, len(alignment)):
					self.add_alignment(alignment[i])
	
	def add_alignment(self, alignment: str):
		"""
        Adds an alignment value to the existing alignment values.

        Args:
            alignment (str): The alignment value to add.

        Returns:
            Alignment: The updated Alignment object.
        """
		self.alignment = " ".join([self.alignment, alignment])
		return self
	
	def set(self, alignment: str):
		"""
        Sets the alignment value.

        Args:
            alignment (str): The alignment value to set.

        Returns:
            Alignment: The updated Alignment object.
        """
		self.alignment = alignment
		return self

from PyGraphicUI.StyleSheets.utilities.Color import Brush


class SelectionColor:
	"""
    Represents the selection-color CSS property.

    Attributes:
        selection_color (str): The selection color value.

    :Usage:
        selection_color = SelectionColor(selection_color=Brush(brush="#FFFF00")) # Yellow color
        selection_color.selection_color
        "selection-color: #FFFF00"
    """
	
	def __init__(self, selection_color: Brush):
		"""
        Initializes a SelectionColor object.

        Args:
            selection_color (Brush): The selection color value.
        """
		self.selection_color = ""
		self.set(selection_color)
	
	def set(self, selection_color: Brush):
		"""
        Sets the selection color value.

        Args:
            selection_color (Brush): The selection color value.

        Returns:
            SelectionColor: The updated selection color object.
        """
		self.selection_color = "selection-color: %s" % selection_color.brush
		return self


class SelectionBackgroundColor:
	"""
    Represents the selection-background-color CSS property.

    Attributes:
        selection_background_color (str): The selection background color value.

    :Usage:
        selection_background_color = SelectionBackgroundColor(
            selection_background_color=Brush(brush="#0000FF") # Blue color
        )
        selection_background_color.selection_background_color
        "selection-background-color: #0000FF"
    """
	
	def __init__(self, selection_background_color: Brush):
		"""
        Initializes a SelectionBackgroundColor object.

        Args:
            selection_background_color (Brush): The selection background color value.
        """
		self.selection_background_color = ""
		self.set(selection_background_color)
	
	def set(self, selection_background_color: Brush):
		"""
        Sets the selection background color value.

        Args:
            selection_background_color (Brush): The selection background color value.

        Returns:
            SelectionBackgroundColor: The updated selection background color object.
        """
		self.selection_background_color = "selection-background-color: %s" % selection_background_color.brush
		return self

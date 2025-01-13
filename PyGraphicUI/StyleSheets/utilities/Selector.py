import typing


class Selector:
	"""
    Represents a CSS selector.

    Attributes:
        selector_type (str): The type of selector.
        selector (str): The formatted selector string.

    :Usage:
        selector = Selector(SelectorFlag.Type)
        selector.set_selector_type(SelectorFlag.Class)
        selector.selector
        ".%s"
    """
	
	def __init__(self, selector_type: str):
		"""
        Initializes a Selector object.

        Args:
            selector_type (str): The type of selector.
        """
		self.selector_type = ""
		self.selector = ""
		self.set(selector_type)
	
	def set(self, selector_type: str):
		"""
        Sets the selector type and formats the selector string.

        Args:
            selector_type (str): The type of selector.

        Returns:
            Selector: The updated Selector object.
        """
		self.selector_type = selector_type
		self.selector = {
			"universal": "*",
			"type": "%s",
			"property": "%s[%s]",
			"class": ".%s",
			"id": "%s#%s",
			"descendant": "%s %s",
			"child": "%s > %s"
		}[selector_type]
		
		return self


class WidgetSelector:
	"""
    Represents a CSS selector for a specific widget.

    Attributes:
        widget_selector (str): The formatted widget selector string.

    :Usage:
        selector = Selector(SelectorFlag.Type)
        widget_selector = WidgetSelector(selector, widget_name="QPushButton")
        widget_selector.widget_selector
        "QPushButton"
    """
	
	def __init__(
			self,
			selector: Selector,
			widget_name: typing.Optional[str] = None,
			object_name: typing.Optional[str] = None
	):
		"""
        Initializes a WidgetSelector object.

        Args:
            selector (Selector): The CSS selector.
            widget_name (typing.Optional[str]): The name of the widget.
            object_name (typing.Optional[str]): The object name of the widget.
        """
		self.widget_selector = ""
		self.set(selector, widget_name, object_name)
	
	def set(
			self,
			selector: Selector,
			widget_name: typing.Optional[str] = None,
			object_name: typing.Optional[str] = None
	):
		"""
        Formats the widget selector string based on the selector type and arguments.

        Args:
            selector (Selector): The CSS selector.
            widget_name (typing.Optional[str]): The name of the widget.
            object_name (typing.Optional[str]): The object name of the widget.
        """
		if selector.selector_type == "universal":
			self.widget_selector = "*"
		elif selector.selector_type == "type":
			if widget_name is not None:
				self.widget_selector = widget_name
			else:
				raise ValueError('"widget_name" must be specified.')
		elif selector.selector_type == "class":
			if widget_name is not None:
				self.widget_selector = ".%s" % widget_name
			else:
				raise ValueError('"widget_name" must be specified.')
		elif selector.selector_type == "property":
			if widget_name is not None and object_name is not None:
				self.widget_selector = "%s[%s]" % (widget_name, object_name)
			else:
				raise ValueError('"widget_name" and "object_name" must be specified.')
		elif selector.selector_type == "id":
			if widget_name is not None and object_name is not None:
				self.widget_selector = "%s#%s" % (widget_name, object_name)
			else:
				raise ValueError('"widget_name" and "object_name" must be specified.')
		elif selector.selector_type == "descendant":
			if widget_name is not None and object_name is not None:
				self.widget_selector = "%s %s" % (widget_name, object_name)
			else:
				raise ValueError('"widget_name" and "object_name" must be specified.')
		elif selector.selector_type == "child":
			if widget_name is not None and object_name is not None:
				self.widget_selector = "%s > %s" % (widget_name, object_name)
			else:
				raise ValueError('"widget_name" and "object_name" must be specified.')


class SelectorFlag:
	"""
    Constants representing different types of CSS selectors.
    """
	
	Universal = "universal"
	Type = "type"
	Property = "property"
	Class = "class"
	ID = "id"
	Descendant = "descendant"
	Child = "child"

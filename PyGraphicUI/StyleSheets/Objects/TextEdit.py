import typing
from PyGraphicUI.StyleSheets.utilities.Text import PlaceholderTextColor
from PyGraphicUI.StyleSheets.Objects.Base import (
	BaseStyle,
	BaseStyleSheet
)
from PyGraphicUI.StyleSheets.utilities.Selector import (
	Selector,
	SelectorFlag
)
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import (
	CssObject,
	ObjectOfStyle
)
from PyGraphicUI.StyleSheets.utilities.utils import (
	get_kwargs_without_arguments,
	get_new_parent_objects
)


class TextEditStyle(BaseStyle):
	"""
    A style class used to style QTextEdit.

    :Usage:
        TextEditStyle(placeholder_text_color=PlaceholderTextColor(Color(RGB(100, 100, 100))))
    """
	
	def __init__(
			self,
			placeholder_text_color: typing.Optional[PlaceholderTextColor] = None,
			**kwargs
	):
		"""
        Initializes a TextEditStyle object.

        Args:
            placeholder_text_color (typing.Optional[PlaceholderTextColor]): A PlaceholderTextColor object representing the color to be used for the placeholder text.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QTextEdit")))
		else:
			self.style_sheet_object.add_css_object("QTextEdit")
		
		if placeholder_text_color is not None:
			self.add_placeholder_text_color(placeholder_text_color)
		
		self.update_style()
	
	def add_placeholder_text_color(self, placeholder_text_color: PlaceholderTextColor):
		"""
        Adds a placeholder text color to the style.

        Args:
            placeholder_text_color (PlaceholderTextColor): A PlaceholderTextColor object representing the color to be used for the placeholder text.

        Returns:
            TextEditStyle: The current TextEditStyle object for method chaining.
        """
		self.instances["placeholder_text_color"] = placeholder_text_color.placeholder_text_color
		return self.update_style()


class TextEditStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QTextEdit objects.

    :Usage:
        TextEditStyleSheet(text_edit_style=[TextEditStyle(placeholder_text_color=PlaceholderTextColor(Color(RGB(100, 100, 100)))), TextEditStyle()])
    """
	
	def __init__(
			self,
			text_edit_style: typing.Optional[typing.Union[TextEditStyle, typing.Iterable[TextEditStyle]]] = None
	):
		"""
        Initializes a TextEditStyleSheet object.

        Args:
            text_edit_style (typing.Optional[typing.Union[TextEditStyle, typing.Iterable[TextEditStyle]]]): A TextEditStyle object or typing.Iterable of TextEditStyle objects representing the styles to be applied to the QTextEdit objects.
        """
		super().__init__()
		
		if text_edit_style is not None:
			if isinstance(text_edit_style, TextEditStyle):
				self.add_style(text_edit_style)
			else:
				for style in text_edit_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainTextEditStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QTextEdit.

    :Usage:
        ChainTextEditStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			placeholder_text_color: typing.Optional[PlaceholderTextColor] = None,
			**kwargs
	):
		"""
        Initializes a ChainTextEditStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QTextEdit will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            placeholder_text_color (typing.Optional[PlaceholderTextColor]): A PlaceholderTextColor object representing the color to be used for the placeholder text.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QTextEdit", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)
		
		if placeholder_text_color is not None:
			self.add_placeholder_text_color(placeholder_text_color)
		
		self.update_style()
	
	def add_placeholder_text_color(self, placeholder_text_color: PlaceholderTextColor):
		"""
        Adds a placeholder text color to the style.

        Args:
            placeholder_text_color (PlaceholderTextColor): A PlaceholderTextColor object representing the color to be used for the placeholder text.

        Returns:
            ChainTextEditStyle: The current ChainTextEditStyle object for method chaining.
        """
		self.instances["placeholder_text_color"] = placeholder_text_color.placeholder_text_color
		return self.update_style()

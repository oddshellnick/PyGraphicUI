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
from PyGraphicUI.StyleSheets.utilities.LineEdit import (
	LineEditPasswordCharacter,
	LineEditPasswordMaskDelay
)


class LineEditStyle(BaseStyle):
	"""
    A style class used to style QLineEdit.

    :Usage:
        LineEditStyle(placeholder_text_color=PlaceholderTextColor(Color(RGB(100, 100, 100))), line_edit_password_character=LineEditPasswordCharacter("*"), line_edit_password_mask_delay=LineEditPasswordMaskDelay(1000))
    """
	
	def __init__(
			self,
			placeholder_text_color: typing.Optional[PlaceholderTextColor] = None,
			line_edit_password_character: typing.Optional[LineEditPasswordCharacter] = None,
			line_edit_password_mask_delay: typing.Optional[LineEditPasswordMaskDelay] = None,
			**kwargs
	):
		"""
        Initializes a LineEditStyle object.

        Args:
            placeholder_text_color (typing.Optional[PlaceholderTextColor]): A PlaceholderTextColor object representing the color to be used for the placeholder text.
            line_edit_password_character (typing.Optional[LineEditPasswordCharacter]): A LineEditPasswordCharacter object representing the character to be used to mask the text in a password line edit.
            line_edit_password_mask_delay (typing.Optional[LineEditPasswordMaskDelay]): A LineEditPasswordMaskDelay object representing the delay (in milliseconds) before the password mask is applied.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QLineEdit")))
		else:
			self.style_sheet_object.add_css_object("QLineEdit")
		
		if placeholder_text_color is not None:
			self.add_placeholder_text_color(placeholder_text_color)
		
		if line_edit_password_character is not None:
			self.add_line_edit_password_character(line_edit_password_character)
		
		if line_edit_password_mask_delay is not None:
			self.add_line_edit_password_mask_delay(line_edit_password_mask_delay)
		
		self.update_style()
	
	def add_line_edit_password_mask_delay(self, line_edit_password_mask_delay: LineEditPasswordMaskDelay):
		"""
        Adds a password mask delay to the style.

        Args:
            line_edit_password_mask_delay (LineEditPasswordMaskDelay): A LineEditPasswordMaskDelay object representing the delay (in milliseconds) before the password mask is applied.

        Returns:
            LineEditStyle: The current LineEditStyle object for method chaining.
        """
		self.instances["line_edit_password_mask_delay"] = line_edit_password_mask_delay.line_edit_password_mask_delay
		return self.update_style()
	
	def add_line_edit_password_character(self, line_edit_password_character: LineEditPasswordCharacter):
		"""
        Adds a password character to the style.

        Args:
            line_edit_password_character (LineEditPasswordCharacter): A LineEditPasswordCharacter object representing the character to be used to mask the text in a password line edit.

        Returns:
            LineEditStyle: The current LineEditStyle object for method chaining.
        """
		self.instances["line_edit_password_character"] = line_edit_password_character.line_edit_password_character
		return self.update_style()
	
	def add_placeholder_text_color(self, placeholder_text_color: PlaceholderTextColor):
		"""
        Adds a placeholder text color to the style.

        Args:
            placeholder_text_color (PlaceholderTextColor): A PlaceholderTextColor object representing the color to be used for the placeholder text.

        Returns:
            LineEditStyle: The current LineEditStyle object for method chaining.
        """
		self.instances["placeholder_text_color"] = placeholder_text_color.placeholder_text_color
		return self.update_style()


class LineEditStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QLineEdit objects.

    :Usage:
        LineEditStyleSheet(line_edit_style=[LineEditStyle(placeholder_text_color=PlaceholderTextColor(Color(RGB(100, 100, 100)))), LineEditStyle()])
    """
	
	def __init__(
			self,
			line_edit_style: typing.Optional[typing.Union[LineEditStyle, typing.Iterable[LineEditStyle]]] = None
	):
		"""
        Initializes a LineEditStyleSheet object.

        Args:
            line_edit_style (typing.Optional[typing.Union[LineEditStyle, typing.Iterable[LineEditStyle]]]): A LineEditStyle object or typing.Iterable of LineEditStyle objects representing the styles to be applied to the QLineEdit objects.
        """
		super().__init__()
		
		if line_edit_style is not None:
			if isinstance(line_edit_style, LineEditStyle):
				self.add_style(line_edit_style)
			else:
				for style in line_edit_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainLineEditStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QLineEdit.

    :Usage:
        ChainLineEditStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			placeholder_text_color: typing.Optional[PlaceholderTextColor] = None,
			line_edit_password_character: typing.Optional[LineEditPasswordCharacter] = None,
			line_edit_password_mask_delay: typing.Optional[LineEditPasswordMaskDelay] = None,
			**kwargs
	):
		"""
        Initializes a ChainLineEditStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QLineEdit will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            placeholder_text_color (typing.Optional[PlaceholderTextColor]): A PlaceholderTextColor object representing the color to be used for the placeholder text.
            line_edit_password_character (typing.Optional[LineEditPasswordCharacter]): A LineEditPasswordCharacter object representing the character to be used to mask the text in a password line edit.
            line_edit_password_mask_delay (typing.Optional[LineEditPasswordMaskDelay]): A LineEditPasswordMaskDelay object representing the delay (in milliseconds) before the password mask is applied.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QLineEdit", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)
		
		if placeholder_text_color is not None:
			self.add_placeholder_text_color(placeholder_text_color)
		
		if line_edit_password_character is not None:
			self.add_line_edit_password_character(line_edit_password_character)
		
		if line_edit_password_mask_delay is not None:
			self.add_line_edit_password_mask_delay(line_edit_password_mask_delay)
		
		self.update_style()
	
	def add_line_edit_password_mask_delay(self, line_edit_password_mask_delay: LineEditPasswordMaskDelay):
		"""
        Adds a password mask delay to the style.

        Args:
            line_edit_password_mask_delay (LineEditPasswordMaskDelay): A LineEditPasswordMaskDelay object representing the delay (in milliseconds) before the password mask is applied.

        Returns:
            ChainLineEditStyle: The current ChainLineEditStyle object for method chaining.
        """
		self.instances["line_edit_password_mask_delay"] = line_edit_password_mask_delay.line_edit_password_mask_delay
		return self.update_style()
	
	def add_line_edit_password_character(self, line_edit_password_character: LineEditPasswordCharacter):
		"""
        Adds a password character to the style.

        Args:
            line_edit_password_character (LineEditPasswordCharacter): A LineEditPasswordCharacter object representing the character to be used to mask the text in a password line edit.

        Returns:
            ChainLineEditStyle: The current ChainLineEditStyle object for method chaining.
        """
		self.instances["line_edit_password_character"] = line_edit_password_character.line_edit_password_character
		return self.update_style()
	
	def add_placeholder_text_color(self, placeholder_text_color: PlaceholderTextColor):
		"""
        Adds a placeholder text color to the style.

        Args:
            placeholder_text_color (PlaceholderTextColor): A PlaceholderTextColor object representing the color to be used for the placeholder text.

        Returns:
            ChainLineEditStyle: The current ChainLineEditStyle object for method chaining.
        """
		self.instances["placeholder_text_color"] = placeholder_text_color.placeholder_text_color
		return self.update_style()

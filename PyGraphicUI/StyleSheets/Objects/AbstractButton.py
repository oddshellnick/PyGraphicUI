import typing
from PyGraphicUI.StyleSheets.utilities.Icon import IconProperty
from PyGraphicUI.StyleSheets.utilities.Text import TextProperty
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


class ChainAbstractButtonStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QAbstractButton.

    :Usage:
        ChainAbstractButtonStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")), button_type="QPushButton", text="Button", icon=IconProperty("path/to/icon.png"))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			button_type: str = "QAbstractButton",
			widget_selector: tuple[str, Selector] = None,
			icon: typing.Optional[IconProperty] = None,
			text: typing.Optional[TextProperty] = None,
			**kwargs
	):
		"""
        Initializes a ChainAbstractButtonStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the button will inherit styles.
            button_type (str): The type of button to style (e.g., 'QPushButton', 'QRadioButton'). Defaults to 'QAbstractButton'.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            icon (typing.Optional[IconProperty]): An IconProperty object representing the icon to be used for the button.
            text (typing.Optional[TextProperty]): A TextProperty object representing the text to be displayed on the button.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				(button_type, Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)
		
		if icon is not None:
			self.add_icon(icon)
		
		if text is not None:
			self.add_text(text)
		
		self.update_style()
	
	def add_text(self, text: TextProperty):
		"""
        Adds text to the button style.

        Args:
            text (TextProperty): A TextProperty object representing the text to be displayed on the button.

        Returns:
            ChainAbstractButtonStyle: The current ChainAbstractButtonStyle object for method chaining.
        """
		self.instances["text"] = text.text
		return self.update_style()
	
	def add_icon(self, icon: IconProperty):
		"""
        Adds an icon to the button style.

        Args:
            icon (IconProperty): An IconProperty object representing the icon to be used for the button.

        Returns:
            ChainAbstractButtonStyle: The current ChainAbstractButtonStyle object for method chaining.
        """
		self.instances["icon"] = icon.icon_property
		return self.update_style()


class AbstractButtonStyle(BaseStyle):
	"""
    A style class used to style any subclass of QAbstractButton.

    :Usage:
        AbstractButtonStyle(button_type="QPushButton", text="Button", icon=IconProperty("path/to/icon.png"))
    """
	
	def __init__(
			self,
			button_type: str = "QAbstractButton",
			icon: typing.Optional[IconProperty] = None,
			text: typing.Optional[TextProperty] = None,
			**kwargs
	):
		"""
        Initializes an AbstractButtonStyle object.

        Args:
            button_type (str): The type of button to style (e.g., 'QPushButton', 'QRadioButton'). Defaults to 'QAbstractButton'.
            icon (typing.Optional[IconProperty]): An IconProperty object representing the icon to be used for the button.
            text (typing.Optional[TextProperty]): A TextProperty object representing the text to be displayed on the button.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject(button_type)))
		else:
			self.style_sheet_object.add_css_object(button_type)
		
		if icon is not None:
			self.add_icon(icon)
		
		if text is not None:
			self.add_text(text)
		
		self.update_style()
	
	def add_text(self, text: TextProperty):
		"""
        Adds text to the button style.

        Args:
            text (TextProperty): A TextProperty object representing the text to be displayed on the button.

        Returns:
            AbstractButtonStyle: The current AbstractButtonStyle object for method chaining.
        """
		self.instances["text"] = text.text
		return self.update_style()
	
	def add_icon(self, icon: IconProperty):
		"""
        Adds an icon to the button style.

        Args:
            icon (IconProperty): An IconProperty object representing the icon to be used for the button.

        Returns:
            AbstractButtonStyle: The current AbstractButtonStyle object for method chaining.
        """
		self.instances["icon"] = icon.icon_property
		return self.update_style()


class AbstractButtonStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple AbstractButton objects.

    :Usage:
        AbstractButtonStyleSheet(button_style=[AbstractButtonStyle(button_type="QPushButton", text="Button 1"), AbstractButtonStyle(button_type="QRadioButton", text="Radio 1")])
    """
	
	def __init__(
			self,
			button_style: typing.Optional[typing.Union[AbstractButtonStyle, typing.Iterable[AbstractButtonStyle]]] = None
	):
		"""
        Initializes an AbstractButtonStyleSheet object.

        Args:
            button_style (typing.Optional[typing.Union[AbstractButtonStyle, typing.Iterable[AbstractButtonStyle]]]): An AbstractButtonStyle object or typing.Iterable of AbstractButtonStyle objects representing the styles to be applied to the buttons.
        """
		super().__init__()
		
		if button_style is not None:
			if isinstance(button_style, AbstractButtonStyle):
				self.add_style(button_style)
			else:
				for style in button_style:
					self.add_style(style)
		
		self.update_style_sheet()

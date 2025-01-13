import typing
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import ObjectOfStyle
from PyGraphicUI.StyleSheets.Objects.AbstractButton import (
	AbstractButtonStyle,
	ChainAbstractButtonStyle
)


class PushButtonStyle(AbstractButtonStyle):
	"""
    A style class used to style QPushButton.

    :Usage:
        PushButtonStyle(text="Button", icon=IconProperty("path/to/icon.png"))
    """
	
	def __init__(self, *args, **kwargs):
		"""
        Initializes a PushButtonStyle object.

        Args:
            *args: Additional arguments passed to the AbstractButtonStyle constructor.
            **kwargs: Additional keyword arguments passed to the AbstractButtonStyle constructor.
        """
		super().__init__(button_type="QPushButton", *args, **kwargs)


class PushButtonStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QPushButton objects.

    :Usage:
        PushButtonStyleSheet(button_style=[PushButtonStyle(text="Button 1"), PushButtonStyle(text="Button 2")])
    """
	
	def __init__(
			self,
			button_style: typing.Optional[typing.Union[PushButtonStyle, typing.Iterable[PushButtonStyle]]] = None
	):
		"""
        Initializes a PushButtonStyleSheet object.

        Args:
            button_style (typing.Optional[typing.Union[PushButtonStyle, typing.Iterable[PushButtonStyle]]]): A PushButtonStyle object or typing.Iterable of PushButtonStyle objects representing the styles to be applied to the QPushButton objects.
        """
		super().__init__()
		
		if button_style is not None:
			if isinstance(button_style, PushButtonStyle):
				self.add_style(button_style)
			else:
				for style in button_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainPushButtonStyle(ChainAbstractButtonStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QPushButton.

    :Usage:
        ChainPushButtonStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			*args,
			**kwargs
	):
		"""
        Initializes a ChainPushButtonStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QPushButton will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            *args: Additional arguments passed to the ChainAbstractButtonStyle constructor.
            **kwargs: Additional keyword arguments passed to the ChainAbstractButtonStyle constructor.
        """
		super().__init__(
				parent_css_object=parent_css_object,
				button_type="QPushButton",
				widget_selector=widget_selector,
				*args,
				**kwargs
		)

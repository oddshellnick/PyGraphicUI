import typing
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import ObjectOfStyle
from PyGraphicUI.StyleSheets.Objects.AbstractButton import (
	AbstractButtonStyle,
	ChainAbstractButtonStyle
)


class TableCornerButtonStyle(AbstractButtonStyle):
	"""
    A style class used to style QTableCornerButton.

    Example:
        TableCornerButtonStyle(text="Corner")
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a TableCornerButtonStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the AbstractButtonStyle constructor.
        """
		super().__init__(button_type="QTableCornerButton", **kwargs)


class TableCornerButtonStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QTableCornerButton objects.

    Example:
        TableCornerButtonStyleSheet(button_style=[TableCornerButtonStyle(text="Corner 1"), TableCornerButtonStyle(text="Corner 2")])
    """
	
	def __init__(
			self,
			button_style: typing.Optional[
				typing.Union[TableCornerButtonStyle, typing.Iterable[TableCornerButtonStyle]]
			] = None
	):
		"""
        Initializes a TableCornerButtonStyleSheet object.

        Args:
            button_style (typing.Optional[typing.Union[TableCornerButtonStyle, typing.Iterable[TableCornerButtonStyle]]]): A TableCornerButtonStyle object or typing.Iterable of TableCornerButtonStyle objects representing the styles to be applied to the QTableCornerButton objects.
        """
		super().__init__()
		
		if button_style is not None:
			if isinstance(button_style, TableCornerButtonStyle):
				self.add_style(button_style)
			else:
				for style in button_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainTableCornerButtonStyle(ChainAbstractButtonStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QTableCornerButton.

    Example:
        ChainTableCornerButtonStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			*args,
			**kwargs
	):
		"""
        Initializes a ChainTableCornerButtonStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QTableCornerButton will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            *args: Additional arguments passed to the ChainAbstractButtonStyle constructor.
            **kwargs: Additional keyword arguments passed to the ChainAbstractButtonStyle constructor.
        """
		super().__init__(
				parent_css_object=parent_css_object,
				button_type="QTableCornerButton",
				widget_selector=widget_selector,
				*args,
				**kwargs
		)

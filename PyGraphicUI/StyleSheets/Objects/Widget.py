import typing
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


class WidgetStyle(BaseStyle):
	"""
    A style class used to style QWidget.

    :Usage:
        WidgetStyle()
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a WidgetStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QWidget")))
		else:
			self.style_sheet_object.add_css_object("QWidget")
		
		self.update_style()


class WidgetStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QWidget objects.

    :Usage:
        WidgetStyleSheet(widget_style=[WidgetStyle(), WidgetStyle()])
    """
	
	def __init__(
			self,
			widget_style: typing.Optional[typing.Union[WidgetStyle, typing.Iterable[WidgetStyle]]] = None
	):
		"""
        Initializes a WidgetStyleSheet object.

        Args:
            widget_style (typing.Optional[typing.Union[WidgetStyle, typing.Iterable[WidgetStyle]]]): A WidgetStyle object or typing.Iterable of WidgetStyle objects representing the styles to be applied to the QWidget objects.
        """
		super().__init__()
		
		if widget_style is not None:
			if isinstance(widget_style, WidgetStyle):
				self.add_style(widget_style)
			else:
				for style in widget_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainWidgetStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QWidget.

    :Usage:
        ChainWidgetStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			**kwargs
	):
		"""
        Initializes a ChainWidgetStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QWidget will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QWidget", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)

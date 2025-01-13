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


class LabelStyle(BaseStyle):
	"""
    A style class used to style QLabel.

    :Usage:
        LabelStyle()
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a LabelStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QLabel")))
		else:
			self.style_sheet_object.add_css_object("QLabel")
		
		self.update_style()


class LabelStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QLabel objects.

    :Usage:
        LabelStyleSheet(label_style=[LabelStyle(), LabelStyle()])
    """
	
	def __init__(
			self,
			label_style: typing.Optional[typing.Union[LabelStyle, typing.Iterable[LabelStyle]]] = None
	):
		"""
        Initializes a LabelStyleSheet object.

        Args:
            label_style (typing.Optional[typing.Union[LabelStyle, typing.Iterable[LabelStyle]]]): A LabelStyle object or typing.Iterable of LabelStyle objects representing the styles to be applied to the QLabel objects.
        """
		super().__init__()
		
		if label_style is not None:
			if isinstance(label_style, LabelStyle):
				self.add_style(label_style)
			else:
				for style in label_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainLabelStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QLabel.

    :Usage:
        ChainLabelStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			**kwargs
	):
		"""
        Initializes a ChainLabelStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QLabel will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QLabel", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)

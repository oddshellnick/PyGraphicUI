import typing
from PyGraphicUI.StyleSheets.Objects.ScrollBar import ChainScrollBarStyle
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
	get_new_parent_objects,
	get_objects_of_style
)


class ChainAbstractItemViewStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QAbstractItemView.

    :Usage:
        ChainAbstractItemViewStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")), widget_selector=("QListView", Selector(SelectorFlag.Descendant)))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			**kwargs
	):
		"""
        Initializes a ChainAbstractItemViewStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QAbstractItemView will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QAbstractItemView", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)


class AbstractItemViewStyle(BaseStyle):
	"""
    A style class used to style any subclass of QAbstractItemView.

    :Usage:
        AbstractItemViewStyle()
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes an AbstractItemViewStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QAbstractItemView")))
		else:
			self.style_sheet_object.add_css_object("QAbstractItemView")
		
		self.update_style()
	
	class ScrollBar(ChainScrollBarStyle):
		"""
        A nested class to apply scrollbar styles specifically to QAbstractItemView.
        """
		
		def __init__(self, **kwargs):
			"""
            Initializes a ScrollBar object.

            Args:
                **kwargs: Additional keyword arguments passed to the ChainScrollBarStyle constructor.
            """
			parent_objects, kwargs = get_objects_of_style(("QAbstractItemView", Selector(SelectorFlag.Type)), **kwargs)
			
			super().__init__(parent_css_object=parent_objects, widget_selector=None, **kwargs)


class AbstractItemViewStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple AbstractItemView objects.

    :Usage:
        AbstractItemViewStyleSheet(AbstractItemView_style=[AbstractItemViewStyle(), AbstractItemViewStyle()])
    """
	
	def __init__(
			self,
			AbstractItemView_style: typing.Optional[
				typing.Union[AbstractItemViewStyle, typing.Iterable[AbstractItemViewStyle]]
			] = None
	):
		"""
        Initializes an AbstractItemViewStyleSheet object.

        Args:
            AbstractItemView_style (typing.Optional[typing.Union[AbstractItemViewStyle, typing.Iterable[AbstractItemViewStyle]]]): An AbstractItemViewStyle object or typing.Iterable of AbstractItemViewStyle objects representing the styles to be applied to the QAbstractItemView objects.
        """
		super().__init__()
		
		if AbstractItemView_style is not None:
			if isinstance(
					AbstractItemView_style,
					(AbstractItemViewStyle, AbstractItemViewStyle.ScrollBar)
			):
				self.add_style(AbstractItemView_style)
			else:
				for style in AbstractItemView_style:
					self.add_style(style)
		
		self.update_style_sheet()

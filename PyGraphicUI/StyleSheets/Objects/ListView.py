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


class ListViewStyle(BaseStyle):
	"""
    A style class used to style QListView.

    :Usage:
        ListViewStyle()
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a ListViewStyle object.

        Args:
            *args: Additional arguments passed to the BaseStyle constructor.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QListView")))
		else:
			self.style_sheet_object.add_css_object("QListView")
		
		self.update_style()
	
	class ScrollBar(ChainScrollBarStyle):
		"""
        A nested class to apply styles specifically to the scroll bar of QListView.
        """
		
		def __init__(self, **kwargs):
			"""
            Initializes a ScrollBar object.

            Args:
                *args: Additional arguments passed to the ChainScrollBarStyle constructor.
                **kwargs: Additional keyword arguments passed to the ChainScrollBarStyle constructor.
            """
			parent_objects, kwargs = get_objects_of_style(("QListView", Selector(SelectorFlag.Type)), **kwargs)
			
			super().__init__(parent_css_object=parent_objects, widget_selector=None, **kwargs)


class ListViewStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QListView objects.

    :Usage:
        ListViewStyleSheet(list_view_style=[ListViewStyle(), ListViewStyle()])
    """
	
	def __init__(
			self,
			list_view_style: typing.Optional[typing.Union[ListViewStyle, typing.Iterable[ListViewStyle]]] = None
	):
		"""
        Initializes a ListViewStyleSheet object.

        Args:
            list_view_style (typing.Optional[typing.Union[ListViewStyle, typing.Iterable[ListViewStyle]]]): A ListViewStyle object or typing.Iterable of ListViewStyle objects representing the styles to be applied to the QListView objects.
        """
		super().__init__()
		
		if list_view_style is not None:
			if isinstance(list_view_style, (ListViewStyle, ListViewStyle.ScrollBar)):
				self.add_style(list_view_style)
			else:
				for style in list_view_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainListViewStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QListView.

    :Usage:
        ChainListViewStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			**kwargs
	):
		"""
        Initializes a ChainListViewStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QListView will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QListView", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)

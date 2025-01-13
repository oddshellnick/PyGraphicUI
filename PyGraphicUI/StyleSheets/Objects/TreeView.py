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


class TreeViewStyle(BaseStyle):
	"""
    A style class used to style QTreeView.

    :Usage:
        TreeViewStyle()
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a TreeViewStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QTreeView")))
		else:
			self.style_sheet_object.add_css_object("QTreeView")
		
		self.update_style()


class TreeViewStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QTreeView objects.

    :Usage:
        TreeViewStyleSheet(tree_view_style=[TreeViewStyle(), TreeViewStyle()])
    """
	
	def __init__(
			self,
			tree_view_style: typing.Optional[typing.Union[TreeViewStyle, typing.Iterable[TreeViewStyle]]] = None
	):
		"""
        Initializes a TreeViewStyleSheet object.

        Args:
            tree_view_style (typing.Optional[typing.Union[TreeViewStyle, typing.Iterable[TreeViewStyle]]]): A TreeViewStyle object or typing.Iterable of TreeViewStyle objects representing the styles to be applied to the QTreeView objects.
        """
		super().__init__()
		
		if tree_view_style is not None:
			if isinstance(tree_view_style, TreeViewStyle):
				self.add_style(tree_view_style)
			else:
				for style in tree_view_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainTreeViewStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QTreeView.

    :Usage:
        ChainTreeViewStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			**kwargs
	):
		"""
        Initializes a ChainTreeViewStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QTreeView will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QTreeView", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)

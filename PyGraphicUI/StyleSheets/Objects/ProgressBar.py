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


class ProgressBarStyle(BaseStyle):
	"""
    A class that represents a style for a progress bar.

    :Usage:
        This class is used within a "ProgressBarStyleSheet" or can be directly inherited to create custom styles.
    """
	
	def __init__(self, **kwargs):
		"""
        Initialize a new ProgressBarStyle instance.

        Args:
            **kwargs: Keyword arguments, passed to the parent class constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QProgressBar")))
		else:
			self.style_sheet_object.add_css_object("QProgressBar")
		
		self.update_style()


class ProgressBarStyleSheet(BaseStyleSheet):
	"""
    A class that represents a style sheet for a progress bar.

    :Usage:
        This class is used to create a style sheet for a progress bar.
    """
	
	def __init__(
			self,
			progress_bar_style: typing.Optional[typing.Union[ProgressBarStyle, typing.Iterable[ProgressBarStyle]]] = None
	):
		"""
        Initialize a new ProgressBarStyleSheet instance.

        Args:
            progress_bar_style (typing.Optional[typing.Union[ProgressBarStyle, typing.Iterable[ProgressBarStyle]]]): The style(s) to add to the style sheet. Defaults to None.
        """
		super().__init__()
		
		if progress_bar_style is not None:
			if isinstance(progress_bar_style, ProgressBarStyle):
				self.add_style(progress_bar_style)
			else:
				for style in progress_bar_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainProgressBarStyle(BaseStyle):
	"""
    A class that represents a style for a progress bar that is chained to a parent widget/object.

    :Usage:
        This class can be used to create styles for progress bars that are inside of a widget/object.
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: tuple[str, Selector] = None,
			**kwargs
	):
		"""
        Initialize a new ChainProgressBarStyle instance.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The object of style for the parent widget.
            widget_selector (tuple[str, Selector], optional): The selector for the widget. Defaults to None.
            **kwargs: Keyword arguments, passed to the parent class constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QProgressBar", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)

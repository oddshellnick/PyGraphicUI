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
from PyGraphicUI.StyleSheets.utilities.Subcontrol import (
	SubcontrolOrigin,
	SubcontrolPosition
)
from PyGraphicUI.StyleSheets.utilities.utils import (
	get_kwargs_without_arguments,
	get_new_parent_objects
)


class ScrollBarStyle(BaseStyle):
	"""
    A style class used to style QScrollBar.

    :Usage:
        ScrollBarStyle(subcontrol_position=SubcontrolPosition.AddLine, subcontrol_origin=SubcontrolOrigin.SubLine)
    """
	
	def __init__(
			self,
			subcontrol_position: typing.Optional[SubcontrolPosition] = None,
			subcontrol_origin: typing.Optional[SubcontrolOrigin] = None,
			**kwargs
	):
		"""
        Initializes a ScrollBarStyle object.

        Args:
            subcontrol_position (typing.Optional[SubcontrolPosition]): A SubcontrolPosition object representing the position of the subcontrol to style.
            subcontrol_origin (typing.Optional[SubcontrolOrigin]): A SubcontrolOrigin object representing the origin of the subcontrol to style.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QScrollBar")))
		else:
			self.style_sheet_object.add_css_object("QScrollBar")
		
		if subcontrol_position is not None:
			self.add_subcontrol_position(subcontrol_position)
		
		if subcontrol_origin is not None:
			self.add_subcontrol_origin(subcontrol_origin)
		
		self.update_style()
	
	def add_subcontrol_origin(self, subcontrol_origin: SubcontrolOrigin):
		"""
        Adds a subcontrol origin to the style.

        Args:
            subcontrol_origin (SubcontrolOrigin): A SubcontrolOrigin object representing the origin of the subcontrol to style.

        Returns:
            ScrollBarStyle: The current ScrollBarStyle object for method chaining.
        """
		self.instances["subcontrol_origin"] = subcontrol_origin.subcontrol_origin
		return self.update_style()
	
	def add_subcontrol_position(self, subcontrol_position: SubcontrolPosition):
		"""
        Adds a subcontrol position to the style.

        Args:
            subcontrol_position (SubcontrolPosition): A SubcontrolPosition object representing the position of the subcontrol to style.

        Returns:
            ScrollBarStyle: The current ScrollBarStyle object for method chaining.
        """
		self.instances["subcontrol_position"] = subcontrol_position.subcontrol_position
		return self.update_style()


class ScrollBarStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QScrollBar objects.

    :Usage:
        ScrollBarStyleSheet(widget_style=[ScrollBarStyle(subcontrol_position=SubcontrolPosition.AddLine), ScrollBarStyle()])
    """
	
	def __init__(
			self,
			widget_style: typing.Optional[typing.Union[ScrollBarStyle, typing.Iterable[ScrollBarStyle]]] = None
	):
		"""
        Initializes a ScrollBarStyleSheet object.

        Args:
            widget_style (typing.Optional[typing.Union[ScrollBarStyle, typing.Iterable[ScrollBarStyle]]]): A ScrollBarStyle object or typing.Iterable of ScrollBarStyle objects representing the styles to be applied to the QScrollBar objects.
        """
		super().__init__()
		
		if widget_style is not None:
			if isinstance(widget_style, ScrollBarStyle):
				self.add_style(widget_style)
			else:
				for style in widget_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainScrollBarStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QScrollBar.

    :Usage:
        ChainScrollBarStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			subcontrol_position: typing.Optional[SubcontrolPosition] = None,
			subcontrol_origin: typing.Optional[SubcontrolOrigin] = None,
			**kwargs
	):
		"""
        Initializes a ChainScrollBarStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QScrollBar will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            subcontrol_position (typing.Optional[SubcontrolPosition]): A SubcontrolPosition object representing the position of the subcontrol to style.
            subcontrol_origin (typing.Optional[SubcontrolOrigin]): A SubcontrolOrigin object representing the origin of the subcontrol to style.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QScrollBar", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)
		
		if subcontrol_position is not None:
			self.add_subcontrol_position(subcontrol_position)
		
		if subcontrol_origin is not None:
			self.add_subcontrol_origin(subcontrol_origin)
		
		self.update_style()
	
	def add_subcontrol_origin(self, subcontrol_origin: SubcontrolOrigin):
		"""
        Adds a subcontrol origin to the style.

        Args:
            subcontrol_origin (SubcontrolOrigin): A SubcontrolOrigin object representing the origin of the subcontrol to style.

        Returns:
            ChainScrollBarStyle: The current ChainScrollBarStyle object for method chaining.
        """
		self.instances["subcontrol_origin"] = subcontrol_origin.subcontrol_origin
		return self.update_style()
	
	def add_subcontrol_position(self, subcontrol_position: SubcontrolPosition):
		"""
        Adds a subcontrol position to the style.

        Args:
            subcontrol_position (SubcontrolPosition): A SubcontrolPosition object representing the position of the subcontrol to style.

        Returns:
            ChainScrollBarStyle: The current ChainScrollBarStyle object for method chaining.
        """
		self.instances["subcontrol_position"] = subcontrol_position.subcontrol_position
		return self.update_style()

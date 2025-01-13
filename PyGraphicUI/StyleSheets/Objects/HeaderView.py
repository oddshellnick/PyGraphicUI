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


class HeaderViewStyle(BaseStyle):
	"""
    A style class used to style QHeaderView.

    :Usage:
        HeaderViewStyle(subcontrol_position=SubcontrolPosition.Section, subcontrol_origin=SubcontrolOrigin.Section)
    """
	
	def __init__(
			self,
			subcontrol_position: typing.Optional[SubcontrolPosition] = None,
			subcontrol_origin: typing.Optional[SubcontrolOrigin] = None,
			**kwargs
	):
		"""
        Initializes a HeaderViewStyle object.

        Args:
            subcontrol_position (typing.Optional[SubcontrolPosition]): A SubcontrolPosition object representing the position of the subcontrol to style.
            subcontrol_origin (typing.Optional[SubcontrolOrigin]): A SubcontrolOrigin object representing the origin of the subcontrol to style.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QHeaderView")))
		else:
			self.style_sheet_object.add_css_object("QHeaderView")
		
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
            HeaderViewStyle: The current HeaderViewStyle object for method chaining.
        """
		self.instances["subcontrol_origin"] = subcontrol_origin.subcontrol_origin
		return self.update_style()
	
	def add_subcontrol_position(self, subcontrol_position: SubcontrolPosition):
		"""
        Adds a subcontrol position to the style.

        Args:
            subcontrol_position (SubcontrolPosition): A SubcontrolPosition object representing the position of the subcontrol to style.

        Returns:
            HeaderViewStyle: The current HeaderViewStyle object for method chaining.
        """
		self.instances["subcontrol_position"] = subcontrol_position.subcontrol_position
		return self.update_style()


class HeaderViewStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QHeaderView objects.

    :Usage:
        HeaderViewStyleSheet(widget_style=[HeaderViewStyle(subcontrol_position=SubcontrolPosition.Section), HeaderViewStyle()])
    """
	
	def __init__(
			self,
			widget_style: typing.Optional[typing.Union[HeaderViewStyle, typing.Iterable[HeaderViewStyle]]] = None
	):
		"""
        Initializes a HeaderViewStyleSheet object.

        Args:
            widget_style (typing.Optional[typing.Union[HeaderViewStyle, typing.Iterable[HeaderViewStyle]]]): A HeaderViewStyle object or typing.Iterable of HeaderViewStyle objects representing the styles to be applied to the QHeaderView objects.
        """
		super().__init__()
		
		if widget_style is not None:
			if isinstance(widget_style, HeaderViewStyle):
				self.add_style(widget_style)
			else:
				for style in widget_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainHeaderViewStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QHeaderView.

    :Usage:
        ChainHeaderViewStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
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
        Initializes a ChainHeaderViewStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QHeaderView will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            subcontrol_position (typing.Optional[SubcontrolPosition]): A SubcontrolPosition object representing the position of the subcontrol to style.
            subcontrol_origin (typing.Optional[SubcontrolOrigin]): A SubcontrolOrigin object representing the origin of the subcontrol to style.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QHeaderView", Selector(SelectorFlag.Descendant))
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
            ChainHeaderViewStyle: The current ChainHeaderViewStyle object for method chaining.
        """
		self.instances["subcontrol_origin"] = subcontrol_origin.subcontrol_origin
		return self.update_style()
	
	def add_subcontrol_position(self, subcontrol_position: SubcontrolPosition):
		"""
        Adds a subcontrol position to the style.

        Args:
            subcontrol_position (SubcontrolPosition): A SubcontrolPosition object representing the position of the subcontrol to style.

        Returns:
            ChainHeaderViewStyle: The current ChainHeaderViewStyle object for method chaining.
        """
		self.instances["subcontrol_position"] = subcontrol_position.subcontrol_position
		return self.update_style()

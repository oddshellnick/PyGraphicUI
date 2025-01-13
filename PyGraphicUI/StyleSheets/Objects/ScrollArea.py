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
from PyGraphicUI.StyleSheets.utilities.Subcontrol import (
	SubcontrolOrigin,
	SubcontrolPosition
)
from PyGraphicUI.StyleSheets.utilities.utils import (
	get_kwargs_without_arguments,
	get_new_parent_objects,
	get_objects_of_style
)


class ScrollAreaStyle(BaseStyle):
	"""
    A style class used to style QScrollArea.

    :Usage:
        ScrollAreaStyle()
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a ScrollAreaStyle object.

        Args:
            *args: Additional arguments passed to the BaseStyle constructor.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QScrollArea")))
		else:
			self.style_sheet_object.add_css_object("QScrollArea")
		
		self.update_style()
	
	class ScrollBar(ChainScrollBarStyle):
		"""
        A nested class to apply styles specifically to the scroll bar of QScrollArea.
        """
		
		def __init__(
				self,
				subcontrol_position: typing.Optional[SubcontrolPosition] = None,
				subcontrol_origin: typing.Optional[SubcontrolOrigin] = None,
				**kwargs
		):
			"""
            Initializes a ScrollBar object.

            Args:
                subcontrol_position (typing.Optional[SubcontrolPosition]): A SubcontrolPosition object representing the position of the subcontrol to style.
                subcontrol_origin (typing.Optional[SubcontrolOrigin]): A SubcontrolOrigin object representing the origin of the subcontrol to style.
                **kwargs: Additional keyword arguments passed to the ChainScrollBarStyle constructor.
            """
			parent_objects, kwargs = get_objects_of_style(("QScrollArea", Selector(SelectorFlag.Type)), **kwargs)
			
			super().__init__(
					parent_css_object=parent_objects,
					widget_selector=None,
					subcontrol_position=subcontrol_position,
					subcontrol_origin=subcontrol_origin,
					**kwargs
			)


class ScrollAreaStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QScrollArea objects.

    :Usage:
        ScrollAreaStyleSheet(scroll_area_style=[ScrollAreaStyle(), ScrollAreaStyle.ScrollBar(subcontrol_position=SubcontrolPosition.AddLine)])
    """
	
	def __init__(
			self,
			scroll_area_style: typing.Optional[typing.Union[ScrollAreaStyle, typing.Iterable[ScrollAreaStyle]]] = None
	):
		"""
        Initializes a ScrollAreaStyleSheet object.

        Args:
            scroll_area_style (typing.Optional[typing.Union[ScrollAreaStyle, typing.Iterable[ScrollAreaStyle]]]): A ScrollAreaStyle object, ScrollAreaStyle.ScrollBar object, or typing.Iterable of ScrollAreaStyle or ScrollAreaStyle.ScrollBar objects representing the styles to be applied to the QScrollArea objects.
        """
		super().__init__()
		
		if scroll_area_style is not None:
			if isinstance(scroll_area_style, (ScrollAreaStyle, ScrollAreaStyle.ScrollBar)):
				self.add_style(scroll_area_style)
			else:
				for style in scroll_area_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainScrollAreaStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QScrollArea.

    :Usage:
        ChainScrollAreaStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			**kwargs
	):
		"""
        Initializes a ChainScrollAreaStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QScrollArea will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QScrollArea", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)
	
	class ScrollBar(ChainScrollBarStyle):
		"""
        A nested class to apply styles specifically to the scroll bar of QScrollArea.
        """
		
		def __init__(
				self,
				parent_css_object: ObjectOfStyle,
				widget_selector: typing.Optional[tuple[str, Selector]] = None,
				subcontrol_position: typing.Optional[SubcontrolPosition] = None,
				subcontrol_origin: typing.Optional[SubcontrolOrigin] = None,
				**kwargs
		):
			"""
            Initializes a ScrollBar object.

            Args:
                parent_css_object (ObjectOfStyle): The parent style sheet object.
                widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to.
                subcontrol_position (typing.Optional[SubcontrolPosition]): A SubcontrolPosition object representing the position of the subcontrol to style.
                subcontrol_origin (typing.Optional[SubcontrolOrigin]): A SubcontrolOrigin object representing the origin of the subcontrol to style.
                **kwargs: Additional keyword arguments passed to the ChainScrollBarStyle constructor.
            """
			new_parent_objects = get_new_parent_objects(
					parent_css_object,
					widget_selector,
					("QScrollArea", Selector(SelectorFlag.Descendant))
			)
			parent_objects, kwargs = get_objects_of_style(
					(new_parent_objects.css_object.css_object, Selector(SelectorFlag.Type)),
					**kwargs
			)
			
			super().__init__(
					parent_css_object=parent_objects,
					widget_selector=None,
					subcontrol_position=subcontrol_position,
					subcontrol_origin=subcontrol_origin,
					**kwargs
			)

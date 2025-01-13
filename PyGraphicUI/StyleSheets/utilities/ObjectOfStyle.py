import typing
from PyGraphicUI.StyleSheets.utilities.PseudoState import PseudoState
from PyGraphicUI.StyleSheets.utilities.Selector import (
	Selector,
	SelectorFlag,
	WidgetSelector
)


class CssObject:
	"""
    Represents a CSS object, combining widget names and selectors.

    Attributes:
        widgets (list[str]): A typing.Iterable of widget names.
        selectors (list[Selector]): A typing.Iterable of selectors.
        css_object (str): The formatted CSS object string.

    :Usage:
        css_object = CssObject(widget="QPushButton", selector=Selector(SelectorFlag.Type))
        css_object.css_object
        'QPushButton'

        css_object = CssObject(widget=["QPushButton", "QLineEdit"], selector=Selector(SelectorFlag.Type))
        css_object.css_object
        'QPushButton QLineEdit'

        css_object = CssObject(widget="QPushButton", selector=[Selector(SelectorFlag.Type), Selector(SelectorFlag.Focus)])
        css_object.css_object
        'QPushButton:focus'
    """
	
	def __init__(
			self,
			widget: typing.Optional[typing.Union[str, typing.Iterable[str]]] = None,
			selector: typing.Union[Selector, typing.Iterable[Selector]] = Selector(SelectorFlag.Type)
	):
		"""
        Initializes a CssObject object.

        Args:
            widget (typing.Optional[typing.Union[str, typing.Iterable[str]]]): The widget name or a typing.Iterable of widget names.
            selector (typing.Union[Selector, typing.Iterable[Selector]]): The selector or a typing.Iterable of selectors.
        """
		self.widgets = [widget] if isinstance(widget, (str, None)) else widget
		self.selectors = [selector] if isinstance(selector, Selector) else selector
		self.css_object = ""
		self.update_css_objects()
	
	def update_css_objects(self):
		"""
        Updates the formatted CSS object string based on widgets and selectors.
        """
		if len(self.widgets) > 0:
			self.css_object = WidgetSelector(self.selectors[0], self.widgets[0]).widget_selector
		
			for i in range(1, len(self.widgets)):
				self.css_object = WidgetSelector(self.selectors[i], self.css_object, self.widgets[i]).widget_selector
		else:
			self.css_object = ""
	
	def add_css_object(self, widget: str, selector: Selector = Selector(SelectorFlag.Type)):
		"""
        Adds a new widget and selector to the CSS object.

        Args:
            widget (str): The widget name.
            selector (Selector): The selector.
        """
		self.widgets.append(widget)
		self.selectors.append(selector)
		self.update_css_objects()


class ObjectOfStyle:
	"""
    Represents a style object, combining a CSS object, subcontrol, and pseudo state.

    Attributes:
        css_object (CssObject): The CSS object representing the widget and selector.
        subcontrol (str): The subcontrol name.
        pseudo_state (str): The pseudo state string.

    :Usage:
        object_of_style = ObjectOfStyle(css_objects=CssObject(widget="QPushButton"), subcontrol="indicator", pseudo_state=PseudoState("hover"))
        object_of_style.css_object.css_object
        'QPushButton'
        object_of_style.subcontrol
        'indicator'
        object_of_style.pseudo_state
        ':hover'
    """
	
	def __init__(
			self,
			css_objects: typing.Optional[CssObject] = None,
			subcontrol: str = "",
			pseudo_state: typing.Optional[PseudoState] = None
	):
		"""
        Initializes an ObjectOfStyle object.

        Args:
            css_objects (typing.Optional[CssObject]): The CSS object.
            subcontrol (str): The subcontrol name.
            pseudo_state (typing.Optional[PseudoState]): The pseudo state.
        """
		self.css_object = css_objects
		self.subcontrol = subcontrol
		self.pseudo_state = pseudo_state.pseudo_state if pseudo_state is not None else ""
	
	def add_css_object(self, widget: str, selector: Selector = Selector(SelectorFlag.Type)):
		"""
        Adds a new widget and selector to the CSS object within the ObjectOfStyle.

        Args:
            widget (str): The widget name.
            selector (Selector): The selector.
        """
		if self.css_object is not None:
			self.css_object.add_css_object(widget, selector)
		else:
			self.css_object = CssObject(widget, selector)


class StyleSheetObject:
	"""
    Represents a style sheet object, combining multiple ObjectOfStyle objects.

    Attributes:
        style_sheet_object (str): The formatted style sheet object string.
        objects_of_style (list[ObjectOfStyle]): A typing.Iterable of ObjectOfStyle objects.

    :Usage:
        style_sheet_object = StyleSheetObject(objects_of_style=[
        ...    ObjectOfStyle(css_objects=CssObject(widget="QPushButton", selector=Selector(SelectorFlag.Type)), subcontrol="indicator", pseudo_state=PseudoState("hover"))
        ... ])
        style_sheet_object.style_sheet_object
        'QPushButton:hover'
    """
	
	def __init__(
			self,
			objects_of_style: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]
	):
		"""
        Initializes a StyleSheetObject object.

        Args:
            objects_of_style (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The ObjectOfStyle object or a typing.Iterable of ObjectOfStyle objects.
        """
		self.style_sheet_object = ""
		self.objects_of_style = objects_of_style if isinstance(objects_of_style, list) else [objects_of_style]
		self.update()
	
	def update(self):
		"""
        Updates the formatted style
        sheet object string based on ObjectOfStyle objects.
        """
		self.style_sheet_object = ", ".join(
				"".join(
						[
							objects_of_style.css_object.css_object,
							objects_of_style.subcontrol,
							objects_of_style.pseudo_state
						]
				)
				for objects_of_style in list(
						filter(lambda value: value.css_object is not None, self.objects_of_style)
				)
		)
	
	def add_css_object(self, widget: str, selector: Selector = Selector(SelectorFlag.Type)):
		"""
        Adds a new widget and selector to all ObjectOfStyle objects within the StyleSheetObject.

        Args:
            widget (str): The widget name.
            selector (Selector): The selector.
        """
		for i in range(len(self.objects_of_style)):
			self.objects_of_style[i].add_css_object(widget, selector)
		
		self.update()

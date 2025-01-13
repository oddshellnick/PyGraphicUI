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


class DialogStyle(BaseStyle):
	"""
    A style class used to style QDialog.

    :Usage:
        DialogStyle()
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a DialogStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QDialog")))
		else:
			self.style_sheet_object.add_css_object("QDialog")
		
		self.update_style()


class DialogStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QDialog objects.

    :Usage:
        DialogStyleSheet(dialog_style=[DialogStyle(), DialogStyle()])
    """
	
	def __init__(
			self,
			dialog_style: typing.Optional[typing.Union[DialogStyle, typing.Iterable[DialogStyle]]] = None
	):
		"""
        Initializes a DialogStyleSheet object.

        Args:
            dialog_style (typing.Optional[typing.Union[DialogStyle, typing.Iterable[DialogStyle]]]): A DialogStyle object or typing.Iterable of DialogStyle objects representing the styles to be applied to the QDialog objects.
        """
		super().__init__()
		
		if dialog_style is not None:
			if isinstance(dialog_style, DialogStyle):
				self.add_style(dialog_style)
			else:
				for style in dialog_style:
					self.add_style(style)
		
		self.update_style_sheet()


class ChainDialogStyle(BaseStyle):
	"""
    A style class that can be chained to apply styles to any subclass of QDialog.

    :Usage:
        ChainDialogStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """
	
	def __init__(
			self,
			parent_css_object: typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]],
			widget_selector: typing.Optional[tuple[str, Selector]] = None,
			**kwargs
	):
		"""
        Initializes a ChainDialogStyle object.

        Args:
            parent_css_object (typing.Union[ObjectOfStyle, typing.Iterable[ObjectOfStyle]]): The style sheet object or typing.Iterable of objects that the style is applied to, from which the QDialog will inherit styles.
            widget_selector (typing.Optional[tuple[str, Selector]]): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QDialog", Selector(SelectorFlag.Descendant))
		)
		
		kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)
		
		super().__init__(object_of_style=new_parent_objects, **kwargs)

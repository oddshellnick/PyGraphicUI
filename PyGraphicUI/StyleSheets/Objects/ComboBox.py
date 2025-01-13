import typing
from PyGraphicUI.StyleSheets.utilities.utils import get_objects_of_style
from PyGraphicUI.StyleSheets.Objects.ScrollBar import ChainScrollBarStyle
from PyGraphicUI.StyleSheets.Objects.Base import (
	BaseStyle,
	BaseStyleSheet
)
from PyGraphicUI.StyleSheets.utilities.Selector import (
	Selector,
	SelectorFlag
)
from PyGraphicUI.StyleSheets.Objects.AbstractItemView import ChainAbstractItemViewStyle
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import (
	CssObject,
	ObjectOfStyle
)


class ComboBoxStyle(BaseStyle):
	"""
    A style class used to style QComboBox.
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a ComboBoxStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QComboBox")))
		else:
			self.style_sheet_object.add_css_object("QComboBox")
		
		self.update_style()
	
	class ItemViewStyle(ChainAbstractItemViewStyle):
		"""
        A nested class to apply styles specifically to the item view of QComboBox.
        """
		
		def __init__(self, **kwargs):
			"""
            Initializes a ItemViewStyle object.

            Args:
                **kwargs: Additional keyword arguments passed to the ChainAbstractItemViewStyle constructor.
            """
			parent_objects, kwargs = get_objects_of_style(("QComboBox", Selector(SelectorFlag.Type)), **kwargs)
			
			super().__init__(parent_css_object=parent_objects, widget_selector=None, **kwargs)
	
	class ScrollBar(ChainScrollBarStyle):
		"""
        A nested class to apply styles specifically to the scroll bar of QComboBox.
        """
		
		def __init__(self, **kwargs):
			"""
            Initializes a ScrollBar object.

            Args:
                **kwargs: Additional keyword arguments passed to the ChainScrollBarStyle constructor.
            """
			parent_objects, kwargs = get_objects_of_style(("QComboBox", Selector(SelectorFlag.Type)), **kwargs)
			
			super().__init__(parent_css_object=parent_objects, widget_selector=None, **kwargs)


class ComboBoxStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QComboBox objects.
    """
	
	def __init__(
			self,
			combo_box_style: typing.Optional[typing.Union[ComboBoxStyle, typing.Iterable[ComboBoxStyle]]] = None
	):
		"""
        Initializes a ComboBoxStyleSheet object.

        Args:
            combo_box_style (typing.Optional[typing.Union[ComboBoxStyle, typing.Iterable[ComboBoxStyle]]]): A ComboBoxStyle object or typing.Iterable of ComboBoxStyle objects representing the styles to be applied to the QComboBox objects.
        """
		super().__init__()
		
		if combo_box_style is not None:
			if isinstance(
					combo_box_style,
					(ComboBoxStyle, ComboBoxStyle.ItemViewStyle, ComboBoxStyle.ScrollBar)
			):
				self.add_style(combo_box_style)
			else:
				for style in combo_box_style:
					self.add_style(style)
		
		self.update_style_sheet()

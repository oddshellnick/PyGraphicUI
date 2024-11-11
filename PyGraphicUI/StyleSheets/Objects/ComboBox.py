from PyGraphicUI.StyleSheets.utilities.utils import get_objects_of_style
from PyGraphicUI.StyleSheets.Objects.ScrollBar import ChainScrollBarStyle
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.Objects.AbstractItemView import ChainAbstractItemViewStyle
#
#
#
#
class ComboBoxStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#
		#
		#
		#
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QComboBox")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QComboBox")
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	class ScrollBar(ChainScrollBarStyle):
		#
		#
		#
		#
		def __init__(self, *args, **kwargs):
			parent_objects, args, kwargs = get_objects_of_style(("QComboBox", Selector(SelectorFlag.Type)), *args, **kwargs)
			super().__init__(parent_css_object=parent_objects, widget_selector=None, *args, **kwargs)
	#
	#
	#
	#
	class ItemViewStyle(ChainAbstractItemViewStyle):
		#
		#
		#
		#
		def __init__(self, *args, **kwargs):
			parent_objects, args, kwargs = get_objects_of_style(("QComboBox", Selector(SelectorFlag.Type)), *args, **kwargs)
			super().__init__(parent_css_object=parent_objects, widget_selector=None, *args, **kwargs)
#
#
#
#
class ComboBoxStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, combo_box_style: ComboBoxStyle | list[ComboBoxStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if combo_box_style is not None:
			if type(combo_box_style) != list:
				self.add_style(combo_box_style)
			else:
				for style in combo_box_style:
					self.add_style(style)
		#
		#
		#
		#
		self.update_style_sheet()

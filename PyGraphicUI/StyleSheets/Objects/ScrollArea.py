from PyGraphicUI.StyleSheets.Objects.ScrollBar import ChainScrollBarStyle
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.utils import get_objects_of_style
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
#
#
#
#
class ScrollAreaStyle(BaseStyle):
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
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QScrollArea")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QScrollArea")
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
			parent_objects, args, kwargs = get_objects_of_style(
					("QScrollArea", Selector(SelectorFlag.Type)),
					*args,
					**kwargs
			)
			super().__init__(parent_css_object=parent_objects, widget_selector=None, *args, **kwargs)
#
#
#
#
class ScrollAreaStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(
			self,
			scroll_area_style: ScrollAreaStyle | ScrollAreaStyle.ScrollBar | list[ScrollAreaStyle | ScrollAreaStyle.ScrollBar] = None
	):
		super().__init__()
		#
		#
		#
		#
		if scroll_area_style is not None:
			if type(scroll_area_style) != list:
				self.add_style(scroll_area_style)
			else:
				for style in scroll_area_style:
					self.add_style(style)
		#
		#
		#
		#
		self.update_style_sheet()

from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects
#
#
#
#
class WidgetStyle(BaseStyle):
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
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QWidget")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QWidget")
		#
		#
		#
		#
		self.update_style()
#
#
#
#
class WidgetStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, widget_style: WidgetStyle | list[WidgetStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if widget_style is not None:
			if type(widget_style) != list:
				self.add_style(widget_style)
			else:
				for style in widget_style:
					self.add_style(style)
		#
		#
		#
		#
		self.update_style_sheet()
#
#
#
#
class ChainWidgetStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
			widget_selector: tuple[str, Selector] = None,
			*args,
			**kwargs
	):
		new_parent_objects = get_new_parent_objects(parent_css_object, widget_selector, ("QWidget", Selector(SelectorFlag.Descendant)))
		#
		#
		#
		#
		args, kwargs = get_args_without_object_of_style(*args, **kwargs)
		#
		#
		#
		#
		super().__init__(object_of_style=new_parent_objects, *args, **kwargs)

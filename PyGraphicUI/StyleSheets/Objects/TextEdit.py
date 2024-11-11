from PyGraphicUI.StyleSheets.utilities.Text import PlaceholderTextColor
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects
#
#
#
#
class TextEditStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			placeholder_text_color: PlaceholderTextColor = None,
			*args,
			**kwargs
	):
		super().__init__(*args, **kwargs)
		#
		#
		#
		#
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QTextEdit")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QTextEdit")
		#
		#
		#
		#
		if placeholder_text_color is not None:
			self.add_placeholder_text_color(placeholder_text_color)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_placeholder_text_color(self, placeholder_text_color: PlaceholderTextColor):
		self.instances["placeholder_text_color"] = placeholder_text_color.placeholder_text_color
		return self.update_style()
#
#
#
#
class TextEditStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, text_edit_style: TextEditStyle | list[TextEditStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if text_edit_style is not None:
			if type(text_edit_style) != list:
				self.add_style(text_edit_style)
			else:
				for style in text_edit_style:
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
class ChainTextEditStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
			widget_selector: tuple[str, Selector] = None,
			placeholder_text_color: PlaceholderTextColor = None,
			*args,
			**kwargs
	):
		new_parent_objects = get_new_parent_objects(parent_css_object, widget_selector, ("QTextEdit", Selector(SelectorFlag.Descendant)))
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
		#
		#
		#
		#
		if placeholder_text_color is not None:
			self.add_placeholder_text_color(placeholder_text_color)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_placeholder_text_color(self, placeholder_text_color: PlaceholderTextColor):
		self.instances["placeholder_text_color"] = placeholder_text_color.placeholder_text_color
		return self.update_style()

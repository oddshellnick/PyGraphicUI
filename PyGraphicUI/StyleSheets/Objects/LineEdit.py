from PyGraphicUI.StyleSheets.utilities.Text import PlaceholderTextColor
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects
from PyGraphicUI.StyleSheets.utilities.LineEdit import LineEditPasswordCharacter, LineEditPasswordMaskDelay
#
#
#
#
class LineEditStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			placeholder_text_color: PlaceholderTextColor = None,
			line_edit_password_character: LineEditPasswordCharacter = None,
			line_edit_password_mask_delay: LineEditPasswordMaskDelay = None,
			*args,
			**kwargs
	):
		super().__init__(*args, **kwargs)
		#
		#
		#
		#
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QLineEdit")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QLineEdit")
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
		if line_edit_password_character is not None:
			self.add_line_edit_password_character(line_edit_password_character)
		#
		#
		#
		#
		if line_edit_password_mask_delay is not None:
			self.add_line_edit_password_mask_delay(line_edit_password_mask_delay)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_line_edit_password_mask_delay(self, line_edit_password_mask_delay: LineEditPasswordMaskDelay):
		self.instances["line_edit_password_mask_delay"] = line_edit_password_mask_delay.line_edit_password_mask_delay
		return self.update_style()
	#
	#
	#
	#
	def add_line_edit_password_character(self, line_edit_password_character: LineEditPasswordCharacter):
		self.instances["line_edit_password_character"] = line_edit_password_character.line_edit_password_character
		return self.update_style()
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
class LineEditStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, line_edit_style: LineEditStyle | list[LineEditStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if line_edit_style is not None:
			if type(line_edit_style) != list:
				self.add_style(line_edit_style)
			else:
				for style in line_edit_style:
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
class ChainLineEditStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
			widget_selector: tuple[str, Selector] = None,
			placeholder_text_color: PlaceholderTextColor = None,
			line_edit_password_character: LineEditPasswordCharacter = None,
			line_edit_password_mask_delay: LineEditPasswordMaskDelay = None,
			*args,
			**kwargs
	):
		new_parent_objects = get_new_parent_objects(parent_css_object, widget_selector, ("QLineEdit", Selector(SelectorFlag.Descendant)))
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
		if line_edit_password_character is not None:
			self.add_line_edit_password_character(line_edit_password_character)
		#
		#
		#
		#
		if line_edit_password_mask_delay is not None:
			self.add_line_edit_password_mask_delay(line_edit_password_mask_delay)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_line_edit_password_mask_delay(self, line_edit_password_mask_delay: LineEditPasswordMaskDelay):
		self.instances["line_edit_password_mask_delay"] = line_edit_password_mask_delay.line_edit_password_mask_delay
		return self.update_style()
	#
	#
	#
	#
	def add_line_edit_password_character(self, line_edit_password_character: LineEditPasswordCharacter):
		self.instances["line_edit_password_character"] = line_edit_password_character.line_edit_password_character
		return self.update_style()
	#
	#
	#
	#
	def add_placeholder_text_color(self, placeholder_text_color: PlaceholderTextColor):
		self.instances["placeholder_text_color"] = placeholder_text_color.placeholder_text_color
		return self.update_style()

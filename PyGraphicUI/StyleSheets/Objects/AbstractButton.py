from PyGraphicUI.StyleSheets.utilities.Icon import IconProperty
from PyGraphicUI.StyleSheets.utilities.Text import TextProperty
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects
#
#
#
#
class ChainAbstractButtonStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
			button_type: str = "QAbstractButton",
			widget_selector: tuple[str, Selector] = None,
			icon: IconProperty = None,
			text: TextProperty = None,
			*args,
			**kwargs
	):
		new_parent_objects = get_new_parent_objects(parent_css_object, widget_selector, (button_type, Selector(SelectorFlag.Descendant)))
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
		if icon is not None:
			self.add_icon(icon)
		#
		#
		#
		#
		if text is not None:
			self.add_text(text)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_text(self, text: TextProperty):
		self.instances["text"] = text.text
		return self.update_style()
	#
	#
	#
	#
	def add_icon(self, icon: IconProperty):
		self.instances["icon"] = icon.icon_property
		return self.update_style()
#
#
#
#
class AbstractButtonStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(self, button_type: str = "QAbstractButton", icon: IconProperty = None, text: TextProperty = None, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#
		#
		#
		#
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject(button_type)))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet(button_type)
		#
		#
		#
		#
		if icon is not None:
			self.add_icon(icon)
		#
		#
		#
		#
		if text is not None:
			self.add_text(text)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_text(self, text: TextProperty):
		self.instances["text"] = text.text
		return self.update_style()
	#
	#
	#
	#
	def add_icon(self, icon: IconProperty):
		self.instances["icon"] = icon.icon_property
		return self.update_style()
#
#
#
#
class AbstractButtonStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, button_style: AbstractButtonStyle | list[AbstractButtonStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if button_style is not None:
			if type(button_style) != list:
				self.add_style(button_style)
			else:
				for style in button_style:
					self.add_style(style)
		#
		#
		#
		#
		self.update_style_sheet()

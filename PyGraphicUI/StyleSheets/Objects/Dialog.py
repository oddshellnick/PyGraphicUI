from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects
#
#
#
#
class DialogStyle(BaseStyle):
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
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QDialog")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QDialog")
		#
		#
		#
		#
		self.update_style()
#
#
#
#
class DialogStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, dialog_style: DialogStyle | list[DialogStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if dialog_style is not None:
			if type(dialog_style) != list:
				self.add_style(dialog_style)
			else:
				for style in dialog_style:
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
class ChainDialogStyle(BaseStyle):
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
		new_parent_objects = get_new_parent_objects(parent_css_object, widget_selector, ("QDialog", Selector(SelectorFlag.Descendant)))
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

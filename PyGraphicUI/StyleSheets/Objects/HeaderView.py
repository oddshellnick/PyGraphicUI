from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects
from PyGraphicUI.StyleSheets.utilities.Subcontrol import SubcontrolOrigin, SubcontrolPosition
#
#
#
#
class HeaderViewStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			subcontrol_position: SubcontrolPosition = None,
			subcontrol_origin: SubcontrolOrigin = None,
			*args,
			**kwargs
	):
		super().__init__(*args, **kwargs)
		#
		#
		#
		#
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QHeaderView")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QHeaderView")
		#
		#
		#
		#
		if subcontrol_position is not None:
			self.add_subcontrol_position(subcontrol_position)
		#
		#
		#
		#
		if subcontrol_origin is not None:
			self.add_subcontrol_origin(subcontrol_origin)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_subcontrol_origin(self, subcontrol_origin: SubcontrolOrigin):
		self.instances["subcontrol_origin"] = subcontrol_origin.subcontrol_origin
		return self.update_style()
	#
	#
	#
	#
	def add_subcontrol_position(self, subcontrol_position: SubcontrolPosition):
		self.instances["subcontrol_position"] = subcontrol_position.subcontrol_position
		return self.update_style()
#
#
#
#
class HeaderViewStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, widget_style: HeaderViewStyle | list[HeaderViewStyle] = None):
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
class ChainHeaderViewStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
			widget_selector: tuple[str, Selector] = None,
			subcontrol_position: SubcontrolPosition = None,
			subcontrol_origin: SubcontrolOrigin = None,
			*args,
			**kwargs
	):
		new_parent_objects = get_new_parent_objects(parent_css_object, widget_selector, ("QHeaderView", Selector(SelectorFlag.Descendant)))
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
		if subcontrol_position is not None:
			self.add_subcontrol_position(subcontrol_position)
		#
		#
		#
		#
		if subcontrol_origin is not None:
			self.add_subcontrol_origin(subcontrol_origin)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_subcontrol_origin(self, subcontrol_origin: SubcontrolOrigin):
		self.instances["subcontrol_origin"] = subcontrol_origin.subcontrol_origin
		return self.update_style()
	#
	#
	#
	#
	def add_subcontrol_position(self, subcontrol_position: SubcontrolPosition):
		self.instances["subcontrol_position"] = subcontrol_position.subcontrol_position
		return self.update_style()

from PyGraphicUI.StyleSheets.Objects.ScrollBar import ChainScrollBarStyle
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects, get_objects_of_style
#
#
#
#
class ListViewStyle(BaseStyle):
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
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QListView")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QListView")
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
			parent_objects, args, kwargs = get_objects_of_style(("QListView", Selector(SelectorFlag.Type)), *args, **kwargs)
			super().__init__(parent_css_object=parent_objects, widget_selector=None, *args, **kwargs)
#
#
#
#
class ListViewStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, list_view_style: ListViewStyle | list[ListViewStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if list_view_style is not None:
			if type(list_view_style) != list:
				self.add_style(list_view_style)
			#
			#
			#
			#
			else:
				for style in list_view_style:
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
class ChainListViewStyle(BaseStyle):
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
		new_parent_objects = get_new_parent_objects(
				parent_css_object,
				widget_selector,
				("QListView", Selector(SelectorFlag.Descendant))
		)
		#
		#
		#
		#
		args, kwargs = get_args_without_object_of_style(*args, **kwargs)
		super().__init__(object_of_style=new_parent_objects, *args, **kwargs)

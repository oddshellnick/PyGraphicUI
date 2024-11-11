from PyGraphicUI.StyleSheets.utilities.Color import GridLineColor
from PyGraphicUI.StyleSheets.Objects.ScrollBar import ChainScrollBarStyle
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.Objects.HeaderView import ChainHeaderViewStyle
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import ObjectOfStyle
from PyGraphicUI.StyleSheets.Objects.TableCornerButton import ChainTableCornerButtonStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_args_without_object_of_style, get_new_parent_objects, get_objects_of_style
#
#
#
#
class TableViewStyle(BaseStyle):
	#
	#
	#
	#
	def __init__(self, gridline_color: GridLineColor = None, *args, **kwargs):
		object_of_style, args, kwargs = get_objects_of_style(("QTableView", Selector(SelectorFlag.Type)), *args, **kwargs)
		#
		#
		#
		#
		super().__init__(object_of_style=object_of_style, *args, **kwargs)
		#
		#
		#
		#
		if gridline_color is not None:
			self.add_gridline_color(gridline_color)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_gridline_color(self, gridline_color: GridLineColor):
		self.instances["gridline_color"] = gridline_color.gridline_color
		return self.update_style()
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
					("QTableView", Selector(SelectorFlag.Type)),
					*args,
					**kwargs
			)
			super().__init__(parent_css_object=parent_objects, widget_selector=None, *args, **kwargs)
	#
	#
	#
	#
	class HeaderView(ChainHeaderViewStyle):
		#
		#
		#
		#
		def __init__(self, *args, **kwargs):
			parent_objects, args, kwargs = get_objects_of_style(("QTableView", Selector(SelectorFlag.Type)), *args, **kwargs)
			super().__init__(parent_css_object=parent_objects, widget_selector=None, *args, **kwargs)
	#
	#
	#
	#
	class CornerButton(ChainTableCornerButtonStyle):
		#
		#
		#
		#
		def __init__(self, *args, **kwargs):
			parent_objects, args, kwargs = get_objects_of_style(("QTableView", Selector(SelectorFlag.Type)), *args, **kwargs)
			super().__init__(parent_css_object=parent_objects, widget_selector=None, *args, **kwargs)
#
#
#
#
class TableViewStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(
			self,
			table_view_style: TableViewStyle | TableViewStyle.HeaderView | TableViewStyle.ScrollBar | list[TableViewStyle | TableViewStyle.HeaderView | TableViewStyle.ScrollBar] = None
	):
		super().__init__()
		#
		#
		#
		#
		if table_view_style is not None:
			if type(table_view_style) != list:
				self.add_style(table_view_style)
			else:
				for style in table_view_style:
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
class ChainTableViewStyles(BaseStyle):
	#
	#
	#
	#
	def __init__(
			self,
			parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
			widget_selector: tuple[str, Selector] = None,
			gridline_color: GridLineColor = None,
			*args,
			**kwargs
	):
		new_parent_objects = get_new_parent_objects(parent_css_object, widget_selector, ("QTableView", Selector(SelectorFlag.Descendant)))
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
		if gridline_color is not None:
			self.add_gridline_color(gridline_color)
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	def add_gridline_color(self, gridline_color: GridLineColor):
		self.instances["gridline_color"] = gridline_color.gridline_color
		return self.update_style()

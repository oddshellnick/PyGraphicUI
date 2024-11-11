from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
#
#
#
#
class TreeViewStyle(BaseStyle):
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
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QTreeView")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QTreeView")
		#
		#
		#
		#
		self.update_style()
#
#
#
#
class TreeViewStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, tree_view_style: TreeViewStyle | list[TreeViewStyle] = None):
		super().__init__()
		#
		#
		#
		#
		if tree_view_style is not None:
			if type(tree_view_style) != list:
				self.add_style(tree_view_style)
			else:
				for style in tree_view_style:
					self.add_style(style)
		#
		#
		#
		#
		self.update_style_sheet()

from PyGraphicUI.StyleSheets.Objects.Base import BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.Selector import Selector
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import ObjectOfStyle
from PyGraphicUI.StyleSheets.Objects.AbstractButton import AbstractButtonStyle, ChainAbstractButtonStyle
#
#
#
#
class TableCornerButtonStyle(AbstractButtonStyle):
	#
	#
	#
	#
	def __init__(self, *args, **kwargs):
		super().__init__(button_type="QTableCornerButton", *args, **kwargs)
#
#
#
#
class TableCornerButtonStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self, button_style: TableCornerButtonStyle | list[TableCornerButtonStyle] = None):
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
#
#
#
#
class ChainTableCornerButtonStyle(ChainAbstractButtonStyle):
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
		super().__init__(
				parent_css_object=parent_css_object,
				button_type="QTableCornerButton",
				widget_selector=widget_selector,
				object_of_style=parent_css_object,
				*args,
				**kwargs
		)

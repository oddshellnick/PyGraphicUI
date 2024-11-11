from PyGraphicUI.StyleSheets.utilities.PseudoState import PseudoState
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag, WidgetSelector
#
#
#
#
class CssObject:
	#
	#
	#
	#
	def __init__(
			self,
			widget: str | list[str] = None,
			selector: Selector | list[Selector] = Selector(SelectorFlag.Type)
	):
		self.widgets = widget if type(widget) == list else [widget]
		self.selectors = selector if type(selector) == list else [selector]
		self.css_object = ""

		self.update_css_objects()

	def add_css_object(
			self,
			widget: str,
			selector: Selector = Selector(SelectorFlag.Type)
	):
		self.widgets.append(widget)
		self.selectors.append(selector)
		self.update_css_objects()

	def update_css_objects(self):
		if len(self.widgets) > 0:
			if len(self.widgets) == 1:
				self.css_object = WidgetSelector(self.selectors[0], self.widgets[0]).widget_selector
			else:
				self.css_object = WidgetSelector(self.selectors[0], self.widgets[0]).widget_selector

				for i in range(1, len(self.widgets)):
					self.css_object = WidgetSelector(self.selectors[i], self.css_object, self.widgets[i]).widget_selector
		else:
			self.css_object = ""
#
#
#
#
class ObjectOfStyle:
	#
	#
	#
	#
	def __init__(
			self,
			css_objects: CssObject = None,
			subcontrol: str = "",
			pseudo_state: PseudoState = None
	):
		self.css_object = css_objects
		self.subcontrol = subcontrol
		self.pseudo_state = pseudo_state.pseudo_state if pseudo_state is not None else ""
	#
	#
	#
	#
	def add_css_object_to_object(
			self,
			widget: str,
			selector: Selector = Selector(SelectorFlag.Type)
	):
		if self.css_object is not None:
			self.css_object.add_css_object(widget, selector)
		else:
			self.css_object = CssObject(widget, selector)
#
#
#
#
class StyleSheetObject:
	#
	#
	#
	#
	def __init__(
			self,
			objects_of_style: ObjectOfStyle | list[ObjectOfStyle]
	):
		self.style_sheet_object = ""
		self.objects_of_style = objects_of_style if type(objects_of_style) == list else [objects_of_style]
		self.update_style_sheet_object()
	#
	#
	#
	#
	def add_css_object_to_style_sheet(
			self,
			widget: str,
			selector: Selector = Selector(SelectorFlag.Type)
	):
		for i in range(len(self.objects_of_style)):
			self.objects_of_style[i].add_css_object_to_object(widget, selector)

		self.update_style_sheet_object()
	#
	#
	#
	#
	def update_style_sheet_object(self):
		self.style_sheet_object = ", ".join("".join([objects_of_style.css_object.css_object, objects_of_style.subcontrol, objects_of_style.pseudo_state]) for objects_of_style in list(filter(lambda value: value.css_object is not None, self.objects_of_style)))

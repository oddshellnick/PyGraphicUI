from PyGraphicUI.StyleSheets.Objects.Widget import ChainWidgetStyle
from PyGraphicUI.StyleSheets.Objects.SpinBox import ChainSpinBoxStyle
from PyGraphicUI.StyleSheets.Objects.LineEdit import ChainLineEditStyle
from PyGraphicUI.StyleSheets.Objects.TableView import ChainTableViewStyles
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.Objects.ToolButton import ChainToolButtonStyle
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.utils import get_objects_of_style
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
#
#
#
#
class CalendarStyle(BaseStyle):
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
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QCalendarWidget")))
		else:
			self.style_sheet_object.add_css_object_to_style_sheet("QCalendarWidget")
		#
		#
		#
		#
		self.update_style()
	#
	#
	#
	#
	class NavigationBar(ChainWidgetStyle):
		#
		#
		#
		#
		def __init__(self, *args, **kwargs):
			parent_objects, args, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), *args, **kwargs)
			super().__init__(
					parent_css_object=parent_objects,
					widget_selector=("qt_calendar_navigationbar", Selector(SelectorFlag.ID)),
					*args,
					**kwargs
			)
		#
		#
		#
		#
		class YearSpinBox(ChainSpinBoxStyle):
			#
			#
			#
			#
			def __init__(self, *args, **kwargs):
				parent_objects, args, kwargs = get_objects_of_style(
						("QCalendarWidget", Selector(SelectorFlag.Type)),
						*args,
						**kwargs
				)
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_yearedit", Selector(SelectorFlag.ID)),
						*args,
						**kwargs
				)
			#
			#
			#
			#
			class YearEdit(ChainLineEditStyle):
				#
				#
				#
				#
				def __init__(self, *args, **kwargs):
					parent_objects, args, kwargs = get_objects_of_style(
							("QCalendarWidget", Selector(SelectorFlag.Type)),
							*args,
							**kwargs
					)
					super().__init__(
							parent_css_object=parent_objects,
							widget_selector=("qt_spinbox_lineedit", Selector(SelectorFlag.ID)),
							*args,
							**kwargs
					)
		#
		#
		#
		#
		class YearButton(ChainToolButtonStyle):
			#
			#
			#
			#
			def __init__(self, *args, **kwargs):
				parent_objects, args, kwargs = get_objects_of_style(
						("QCalendarWidget", Selector(SelectorFlag.Type)),
						*args,
						**kwargs
				)
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_yearbutton", Selector(SelectorFlag.ID)),
						*args,
						**kwargs
				)
		#
		#
		#
		#
		class PreviousMonthButton(ChainToolButtonStyle):
			#
			#
			#
			#
			def __init__(self, *args, **kwargs):
				parent_objects, args, kwargs = get_objects_of_style(
						("QCalendarWidget", Selector(SelectorFlag.Type)),
						*args,
						**kwargs
				)
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_prevmonth", Selector(SelectorFlag.ID)),
						*args,
						**kwargs
				)
		#
		#
		#
		#
		class NextMonthButton(ChainToolButtonStyle):
			#
			#
			#
			#
			def __init__(self, *args, **kwargs):
				parent_objects, args, kwargs = get_objects_of_style(
						("QCalendarWidget", Selector(SelectorFlag.Type)),
						*args,
						**kwargs
				)
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_nextmonth", Selector(SelectorFlag.ID)),
						*args,
						**kwargs
				)
		#
		#
		#
		#
		class MonthButton(ChainToolButtonStyle):
			#
			#
			#
			#
			def __init__(self, *args, **kwargs):
				parent_objects, args, kwargs = get_objects_of_style(
						("QCalendarWidget", Selector(SelectorFlag.Type)),
						*args,
						**kwargs
				)
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_monthbutton", Selector(SelectorFlag.ID)),
						*args,
						**kwargs
				)
	#
	#
	#
	#
	class DatesGrid(ChainTableViewStyles):
		#
		#
		#
		#
		def __init__(self, *args, **kwargs):
			parent_objects, args, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), *args, **kwargs)
			super().__init__(
					parent_css_object=parent_objects,
					widget_selector=("qt_calendar_calendarview", Selector(SelectorFlag.ID)),
					*args,
					**kwargs
			)
#
#
#
#
class CalendarStyleSheet(BaseStyleSheet):
	#
	#
	#
	#
	def __init__(self,
	             calendar_style: CalendarStyle | CalendarStyle.DatesGrid | CalendarStyle.NavigationBar.YearSpinBox | CalendarStyle.NavigationBar.YearSpinBox.YearEdit | CalendarStyle.NavigationBar.YearButton | CalendarStyle.NavigationBar.MonthButton | CalendarStyle.NavigationBar | CalendarStyle.NavigationBar.PreviousMonthButton | CalendarStyle.NavigationBar.NextMonthButton | list[CalendarStyle | CalendarStyle.DatesGrid | CalendarStyle.NavigationBar.YearSpinBox | CalendarStyle.NavigationBar.YearSpinBox.YearEdit | CalendarStyle.NavigationBar.YearButton | CalendarStyle.NavigationBar.MonthButton | CalendarStyle.NavigationBar | CalendarStyle.NavigationBar.PreviousMonthButton | CalendarStyle.NavigationBar.NextMonthButton] = None):
		super().__init__()
		#
		#
		#
		#
		if calendar_style is not None:
			if type(calendar_style) != list:
				self.add_style(calendar_style)
			else:
				for style in calendar_style:
					self.add_style(style)
		#
		#
		#
		#
		self.update_style_sheet()

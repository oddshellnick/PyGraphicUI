import typing
from PyGraphicUI.StyleSheets.Objects.Widget import ChainWidgetStyle
from PyGraphicUI.StyleSheets.Objects.SpinBox import ChainSpinBoxStyle
from PyGraphicUI.StyleSheets.Objects.LineEdit import ChainLineEditStyle
from PyGraphicUI.StyleSheets.utilities.utils import get_objects_of_style
from PyGraphicUI.StyleSheets.Objects.TableView import ChainTableViewStyles
from PyGraphicUI.StyleSheets.Objects.ToolButton import ChainToolButtonStyle
from PyGraphicUI.StyleSheets.Objects.Base import (
	BaseStyle,
	BaseStyleSheet
)
from PyGraphicUI.StyleSheets.utilities.Selector import (
	Selector,
	SelectorFlag
)
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import (
	CssObject,
	ObjectOfStyle
)


class CalendarStyle(BaseStyle):
	"""
    A style class used to style QCalendarWidget.
    """
	
	def __init__(self, **kwargs):
		"""
        Initializes a CalendarStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
		super().__init__(**kwargs)
		
		if self.style_sheet_object is None:
			self.set_style_sheet_object(ObjectOfStyle(CssObject("QCalendarWidget")))
		else:
			self.style_sheet_object.add_css_object("QCalendarWidget")
		
		self.update_style()
	
	class DatesGrid(ChainTableViewStyles):
		"""
        A nested class to apply styles specifically to the dates grid of QCalendarWidget.
        """
		
		def __init__(self, **kwargs):
			"""
            Initializes a DatesGrid object.

            Args:
                **kwargs: Additional keyword arguments passed to the ChainTableViewStyles constructor.
            """
			parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
			
			super().__init__(
					parent_css_object=parent_objects,
					widget_selector=("qt_calendar_calendarview", Selector(SelectorFlag.ID)),
					**kwargs
			)
	
	class NavigationBar(ChainWidgetStyle):
		"""
        A nested class to apply styles specifically to the navigation bar of QCalendarWidget.
        """
		
		def __init__(self, **kwargs):
			"""
            Initializes a NavigationBar object.

            Args:
                **kwargs: Additional keyword arguments passed to the ChainWidgetStyle constructor.
            """
			parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
			
			super().__init__(
					parent_css_object=parent_objects,
					widget_selector=("qt_calendar_navigationbar", Selector(SelectorFlag.ID)),
					**kwargs
			)
		
		class MonthButton(ChainToolButtonStyle):
			"""
            A nested class to apply styles specifically to the month button in the navigation bar of QCalendarWidget.
            """
			
			def __init__(self, **kwargs):
				"""
                Initializes a MonthButton object.

                Args:
                    **kwargs: Additional keyword arguments passed to the ChainToolButtonStyle constructor.
                """
				parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
				
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_monthbutton", Selector(SelectorFlag.ID)),
						**kwargs
				)
		
		class NextMonthButton(ChainToolButtonStyle):
			"""
            A nested class to apply styles specifically to the next month button in the navigation bar of QCalendarWidget.
            """
			
			def __init__(self, **kwargs):
				"""
                Initializes a NextMonthButton object.

                Args:
                    **kwargs: Additional keyword arguments passed to the ChainToolButtonStyle constructor.
                """
				parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
				
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_nextmonth", Selector(SelectorFlag.ID)),
						**kwargs
				)
		
		class PreviousMonthButton(ChainToolButtonStyle):
			"""
            A nested class to apply styles specifically to the previous month button in the navigation bar of QCalendarWidget.
            """
			
			def __init__(self, **kwargs):
				"""
                Initializes a PreviousMonthButton object.

                Args:
                    **kwargs: Additional keyword arguments passed to the ChainToolButtonStyle constructor.
                """
				parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
				
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_prevmonth", Selector(SelectorFlag.ID)),
						**kwargs
				)
		
		class YearButton(ChainToolButtonStyle):
			"""
            A nested class to apply styles specifically to the year button in the navigation bar of QCalendarWidget.
            """
			
			def __init__(self, **kwargs):
				"""
                Initializes a YearButton object.

                Args:
                    **kwargs: Additional keyword arguments passed to the ChainToolButtonStyle constructor.
                """
				parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
				
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_yearbutton", Selector(SelectorFlag.ID)),
						**kwargs
				)
		
		class YearSpinBox(ChainSpinBoxStyle):
			"""
            A nested class to apply styles specifically to the year spin box in the navigation bar of QCalendarWidget.
            """
			
			def __init__(self, **kwargs):
				"""
                Initializes a YearSpinBox object.

                Args:
                    **kwargs: Additional keyword arguments passed to the ChainSpinBoxStyle constructor.
                """
				parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
				
				super().__init__(
						parent_css_object=parent_objects,
						widget_selector=("qt_calendar_yearedit", Selector(SelectorFlag.ID)),
						**kwargs
				)
			
			class YearEdit(ChainLineEditStyle):
				"""
                A nested class to apply styles specifically to the year edit line in the year spin box of the navigation bar of QCalendarWidget.
                """
				
				def __init__(self, **kwargs):
					"""
                    Initializes a YearEdit object.

                    Args:
                        **kwargs: Additional keyword arguments passed to the ChainLineEditStyle constructor.
                    """
					parent_objects, kwargs = get_objects_of_style(("QCalendarWidget", Selector(SelectorFlag.Type)), **kwargs)
					
					super().__init__(
							parent_css_object=parent_objects,
							widget_selector=("qt_spinbox_lineedit", Selector(SelectorFlag.ID)),
							**kwargs
					)


class CalendarStyleSheet(BaseStyleSheet):
	"""
    A style sheet class used to manage styles for multiple QCalendarWidget objects.
    """
	
	def __init__(
			self,
			calendar_style: typing.Optional[typing.Union[CalendarStyle, typing.Iterable[CalendarStyle]]] = None
	):
		"""
        Initializes a CalendarStyleSheet object.

        Args:
            calendar_style (typing.Optional[typing.Union[CalendarStyle, typing.Iterable[CalendarStyle]]]): A CalendarStyle object or typing.Iterable of CalendarStyle objects representing the styles to be applied to the QCalendarWidget objects.
        """
		super().__init__()
		
		if calendar_style is not None:
			if isinstance(
					calendar_style,
					(
							CalendarStyle,
							CalendarStyle.DatesGrid,
							CalendarStyle.NavigationBar,
							CalendarStyle.NavigationBar.MonthButton,
							CalendarStyle.NavigationBar.NextMonthButton,
							CalendarStyle.NavigationBar.PreviousMonthButton,
							CalendarStyle.NavigationBar.YearButton,
							CalendarStyle.NavigationBar.YearSpinBox,
							CalendarStyle.NavigationBar.YearSpinBox.LineEdit,
							CalendarStyle.NavigationBar.YearSpinBox.YearEdit
					)
			):
				self.add_style(calendar_style)
			else:
				for style in calendar_style:
					self.add_style(style)
		
		self.update_style_sheet()

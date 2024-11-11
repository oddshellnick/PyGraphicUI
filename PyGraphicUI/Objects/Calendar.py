from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QCalendarWidget, QGraphicsEffect, QSizePolicy, QWidget
#
#
#
#
class CalendarWidgetInit(WidgetInit):
	#
	#
	#
	#
	def __init__(
			self,
			name: str = "calendar",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			font: QFont = None,
			grid_visible: bool = True,
			vertical_header_format: QCalendarWidget.VerticalHeaderFormat = QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader,
			horizontal_header_format: QCalendarWidget.HorizontalHeaderFormat = QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader,
			cursor: Qt.CursorShape = Qt.CursorShape.PointingHandCursor
	):
		super().__init__(
				name,
				parent,
				enabled,
				visible,
				style_sheet,
				minimum_size,
				maximum_size,
				fixed_size,
				size_policy,
				graphic_effect
		)
		#
		#
		#
		#
		self.font = font
		self.grid_visible = grid_visible
		self.vertical_header_format = vertical_header_format
		self.horizontal_header_format = horizontal_header_format
		self.cursor = cursor
#
#
#
#
class PyCalendarWidget(QCalendarWidget, PyWidget):
	#
	#
	#
	#
	def __init__(self, calendar_init: CalendarWidgetInit = CalendarWidgetInit()):
		super().__init__(widget_init=calendar_init)
		#
		#
		#
		#
		self.setCursor(calendar_init.cursor)
		self.setGridVisible(calendar_init.grid_visible)
		self.setHorizontalHeaderFormat(calendar_init.horizontal_header_format)
		self.setVerticalHeaderFormat(calendar_init.vertical_header_format)
		#
		#
		#
		#
		if calendar_init.font is not None:
			self.setFont(calendar_init.font)

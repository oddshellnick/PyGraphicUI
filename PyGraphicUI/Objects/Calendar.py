import typing
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QCalendarWidget,
	QGraphicsEffect,
	QSizePolicy,
	QWidget
)


class CalendarWidgetInit(WidgetInit):
	"""
    Data class to hold initialization parameters for calendar widgets.

    Attributes:
        name (str): The object name of the calendar widget. Defaults to "calendar".
        parent (typing.Union[QWidget, None]): The parent widget. Defaults to None.
        enabled (bool): Whether the calendar widget is enabled. Defaults to True.
        visible (bool): Whether the calendar widget is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the calendar widget. Defaults to "".
        minimum_size (typing.Union[ObjectSize, None]): The minimum size of the calendar widget. Defaults to None.
        maximum_size (typing.Union[ObjectSize, None]): The maximum size of the calendar widget. Defaults to None.
        fixed_size (typing.Union[ObjectSize, None]): The fixed size of the calendar widget. Defaults to None.
        size_policy (typing.Union[QSizePolicy, None]): The size policy of the calendar widget. Defaults to None.
        graphic_effect (typing.Union[QGraphicsEffect, None]): The graphic effect to apply to the calendar widget. Defaults to None.
        font (typing.Union[QFont, None]): The font for the calendar widget. Defaults to None.
        grid_visible (bool): Whether the grid is visible. Defaults to True.
        vertical_header_format (QCalendarWidget.VerticalHeaderFormat): The vertical header format. Defaults to QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader.
        horizontal_header_format (QCalendarWidget.HorizontalHeaderFormat): The horizontal header format. Defaults to QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader.
        cursor (Qt.CursorShape): The cursor shape to use for the calendar widget. Defaults to Qt.CursorShape.PointingHandCursor.
    """
	
	def __init__(
			self,
			name: str = "calendar",
			parent: typing.Union[QWidget, None] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Union[ObjectSize, None] = None,
			maximum_size: typing.Union[ObjectSize, None] = None,
			fixed_size: typing.Union[ObjectSize, None] = None,
			size_policy: typing.Union[QSizePolicy, None] = None,
			graphic_effect: typing.Union[QGraphicsEffect, None] = None,
			font: typing.Union[QFont, None] = None,
			grid_visible: bool = True,
			vertical_header_format: QCalendarWidget.VerticalHeaderFormat = QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader, horizontal_header_format: QCalendarWidget.HorizontalHeaderFormat = QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader, cursor: Qt.CursorShape = Qt.CursorShape.PointingHandCursor
	):
		"""
        Initializes a CalendarWidgetInit object.

        Args:
            name (str): The object name.
            parent (typing.Union[QWidget, None]): The parent widget.
            enabled (bool): Whether the calendar widget is enabled.
            visible (bool): Whether the calendar widget is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Union[ObjectSize, None]): The minimum size.
            maximum_size (typing.Union[ObjectSize, None]): The maximum size.
            fixed_size (typing.Union[ObjectSize, None]): The fixed size.
            size_policy (typing.Union[QSizePolicy, None]): The size policy.
            graphic_effect (typing.Union[QGraphicsEffect, None]): The graphic effect.
            font (typing.Union[QFont, None]): The font to use.
            grid_visible (bool): Whether the grid is visible.
            vertical_header_format (QCalendarWidget.VerticalHeaderFormat): The vertical header format.
            horizontal_header_format (QCalendarWidget.HorizontalHeaderFormat): The horizontal header format.
            cursor (Qt.CursorShape): The cursor shape.
        """
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
		
		self.font = font
		self.grid_visible = grid_visible
		self.vertical_header_format = vertical_header_format
		self.horizontal_header_format = horizontal_header_format
		self.cursor = cursor


class PyCalendarWidget(QCalendarWidget, PyWidget):
	"""
    A custom calendar widget with enhanced initialization.
    """
	
	def __init__(self, calendar_init: CalendarWidgetInit = CalendarWidgetInit()):
		"""
        Initializes a PyCalendarWidget.

        Args:
            calendar_init (CalendarWidgetInit): Calendar widget initialization parameters.
        """
		super().__init__(widget_init=calendar_init)
		
		self.setCursor(calendar_init.cursor)
		self.setGridVisible(calendar_init.grid_visible)
		self.setHorizontalHeaderFormat(calendar_init.horizontal_header_format)
		self.setVerticalHeaderFormat(calendar_init.vertical_header_format)
		
		if calendar_init.font is not None:
			self.setFont(calendar_init.font)

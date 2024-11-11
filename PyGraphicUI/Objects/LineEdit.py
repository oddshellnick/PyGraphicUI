from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QGraphicsEffect, QLineEdit, QSizePolicy, QWidget
#
#
#
#
class LineEditInit(WidgetInit):
	def __init__(
			self,
			name: str = "line_edit",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
			cursor: Qt.CursorShape = Qt.CursorShape.IBeamCursor,
			placeholder_text: str = "",
			font: PyFont = PyFont(point_size=10)
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
		self.alignment = alignment
		self.cursor = cursor
		self.placeholder_text = placeholder_text
		self.font = font
#
#
#
#
class PyLineEdit(QLineEdit, PyWidget):
	def __init__(
			self,
			line_edit_init: LineEditInit = LineEditInit(),
			instance: str = ""
	):
		super().__init__(widget_init=line_edit_init)
		#
		#
		#
		#
		self.setAlignment(line_edit_init.alignment)
		self.setAutoFillBackground(False)
		self.setCursor(line_edit_init.cursor)
		self.setPlaceholderText(instance)
		self.setFont(line_edit_init.font)

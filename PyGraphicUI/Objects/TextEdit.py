from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextOption
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QGraphicsEffect, QSizePolicy, QTextEdit, QWidget
#
#
#
#
class TextEditInit(WidgetInit):
	def __init__(
			self,
			name: str = "text_edit",
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
			font: PyFont = PyFont(point_size=10),
			line_wrap_mode: QTextEdit.LineWrapMode = QTextEdit.LineWrapMode.NoWrap,
			word_wrap_mode: QTextOption.WrapMode = QTextOption.WrapMode.NoWrap,
			line_wrap_column_or_width: int = 0,
			overwrite_mode: bool = False,
			read_only: bool = False,
			contents_margins: list[int] = None,
			input_method_hints: Qt.InputMethodHint = Qt.InputMethodHint.ImhNone,
			mid_line_width: int = 0,
			vertical_scrollbar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAlwaysOff,
			horizontal_scrollbar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
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
		self.line_wrap_mode = line_wrap_mode
		self.word_wrap_mode = word_wrap_mode
		self.line_wrap_column_or_width = line_wrap_column_or_width
		self.overwrite_mode = overwrite_mode
		self.read_only = read_only
		self.contents_margins = contents_margins
		self.input_method_hints = input_method_hints
		self.mid_line_width = mid_line_width
		self.vertical_scrollbar_policy = vertical_scrollbar_policy
		self.horizontal_scrollbar_policy = horizontal_scrollbar_policy
#
#
#
#
class PyTextEdit(QTextEdit, PyWidget):
	def __init__(
			self,
			text_edit_init: TextEditInit = TextEditInit(),
			instance: str = ""
	):
		super().__init__(widget_init=text_edit_init)
		#
		#
		#
		#
		self.setAlignment(text_edit_init.alignment)
		self.setAutoFillBackground(False)
		self.setCursor(text_edit_init.cursor)
		self.setPlaceholderText(instance)
		self.setLineWrapMode(text_edit_init.line_wrap_mode)
		self.setWordWrapMode(text_edit_init.word_wrap_mode)
		self.setLineWrapColumnOrWidth(text_edit_init.line_wrap_column_or_width)
		self.setOverwriteMode(text_edit_init.overwrite_mode)
		self.setReadOnly(text_edit_init.read_only)
		self.setInputMethodHints(text_edit_init.input_method_hints)
		self.setMidLineWidth(text_edit_init.mid_line_width)
		self.setFont(text_edit_init.font)
		self.setVerticalScrollBarPolicy(text_edit_init.vertical_scrollbar_policy)
		self.setHorizontalScrollBarPolicy(text_edit_init.horizontal_scrollbar_policy)
		#
		#
		#
		#
		if text_edit_init.contents_margins is not None:
			self.setContentsMargins(*text_edit_init.contents_margins)
		else:
			self.setContentsMargins(0, 0, 0, 0)

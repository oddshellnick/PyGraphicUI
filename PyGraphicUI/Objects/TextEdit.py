import typing
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextOption
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QSizePolicy,
	QTextEdit,
	QWidget
)


class TextEditInit(WidgetInit):
	"""
    Data class to hold initialization parameters for text edits.

    Attributes:
        name (str): The object name of the text edit. Defaults to "text_edit".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the text edit is enabled. Defaults to True.
        visible (bool): Whether the text edit is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the text edit. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the text edit. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the text edit. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the text edit. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the text edit. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the text edit. Defaults to None.
        alignment (Qt.AlignmentFlag): The alignment of the text within the text edit. Defaults to Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter.
        cursor (Qt.CursorShape): The cursor shape to use for the text edit. Defaults to Qt.CursorShape.IBeamCursor.
        placeholder_text (str): The placeholder text to display when the text edit is empty. Defaults to "".
        font (PyFont): The font to use for the text edit text. Defaults to a default PyFont object.
        line_wrap_mode (QTextEdit.LineWrapMode): The line wrap mode. Defaults to QTextEdit.LineWrapMode.NoWrap.
        word_wrap_mode (QTextOption.WrapMode): The word wrap mode. Defaults to QTextOption.WrapMode.NoWrap.
        line_wrap_column_or_width (int): The line wrap column or width. Defaults to 0.
        overwrite_mode (bool): Whether overwrite mode is enabled. Defaults to False.
        read_only (bool): Whether the text edit is read-only. Defaults to False.
        contents_margins (typing.Union[tuple[int, int, int, int], None]): The margins of the text edit's content. Defaults to None.
        input_method_hints (Qt.InputMethodHint): Input method hints for the text edit. Defaults to Qt.InputMethodHint.ImhNone.
        mid_line_width (int): The width of the middle line. Defaults to 0.
        vertical_scrollbar_policy (Qt.ScrollBarPolicy): The vertical scroll bar policy. Defaults to Qt.ScrollBarPolicy.ScrollBarAlwaysOff.
        horizontal_scrollbar_policy (Qt.ScrollBarPolicy): The horizontal scroll bar policy. Defaults to Qt.ScrollBarPolicy.ScrollBarAlwaysOff.
    """
	
	def __init__(
			self,
			name: str = "text_edit",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
			cursor: Qt.CursorShape = Qt.CursorShape.IBeamCursor,
			placeholder_text: str = "",
			font: PyFont = PyFont(),
			line_wrap_mode: QTextEdit.LineWrapMode = QTextEdit.LineWrapMode.NoWrap,
			word_wrap_mode: QTextOption.WrapMode = QTextOption.WrapMode.NoWrap,
			line_wrap_column_or_width: int = 0,
			overwrite_mode: bool = False,
			read_only: bool = False,
			contents_margins: typing.Union[tuple[int, int, int, int], None] = None,
			input_method_hints: Qt.InputMethodHint = Qt.InputMethodHint.ImhNone,
			mid_line_width: int = 0,
			vertical_scrollbar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAlwaysOff,
			horizontal_scrollbar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
	):
		"""
        Initializes a TextEditInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the text edit is enabled.
            visible (bool): Whether the text edit is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            alignment (Qt.AlignmentFlag): The text alignment.
            cursor (Qt.CursorShape): The cursor shape.
            placeholder_text (str): The placeholder text.
            font (PyFont): The font to use.
            line_wrap_mode (QTextEdit.LineWrapMode): The line wrap mode.
            word_wrap_mode (QTextOption.WrapMode): The word wrap mode.
            line_wrap_column_or_width (int): The line wrap column or width.
            overwrite_mode (bool): Whether overwrite mode is enabled.
            read_only (bool): Whether the text edit is read-only.
            contents_margins (typing.Union[tuple[int, int, int, int], None]): The content margins.
            input_method_hints (Qt.InputMethodHint): Input method hints.
            mid_line_width (int): The middle line width.
            vertical_scrollbar_policy (Qt.ScrollBarPolicy): The vertical scroll bar policy.
            horizontal_scrollbar_policy (Qt.ScrollBarPolicy): The horizontal scroll bar policy.
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


class PyTextEdit(QTextEdit, PyWidget):
	"""
    A custom text edit widget.
    """
	
	def __init__(self, text_edit_init: TextEditInit = TextEditInit(), instance: str = ""):
		"""
        Initializes a PyTextEdit object.

        Args:
            text_edit_init (TextEditInit): Initialization parameters.
            instance (str): Initial text.
        """
		super().__init__(widget_init=text_edit_init)
		
		self.setAlignment(text_edit_init.alignment)
		self.setAutoFillBackground(False)
		self.setCursor(text_edit_init.cursor)
		self.setPlaceholderText(text_edit_init.placeholder_text)
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
		self.setText(instance)
		
		if text_edit_init.contents_margins is not None:
			self.setContentsMargins(*text_edit_init.contents_margins)
		else:
			self.setContentsMargins(0, 0, 0, 0)

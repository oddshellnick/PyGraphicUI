from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsEffect, QLineEdit, QSizePolicy, QWidget

from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit


class LineEditInit(WidgetInit):
    """
    Data class to hold initialization parameters for line edits.

    Attributes:
        name (str): The object name of the line edit. Defaults to "line_edit".
        parent (QWidget | None): The parent widget. Defaults to None.
        enabled (bool): Whether the line edit is enabled. Defaults to True.
        visible (bool): Whether the line edit is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the line edit. Defaults to "".
        minimum_size (ObjectSize | None): The minimum size of the line edit. Defaults to None.
        maximum_size (ObjectSize | None): The maximum size of the line edit. Defaults to None.
        fixed_size (ObjectSize | None): The fixed size of the line edit. Defaults to None.
        size_policy (QSizePolicy | None): The size policy of the line edit. Defaults to None.
        graphic_effect (QGraphicsEffect | None): The graphic effect to apply to the line edit. Defaults to None.
        alignment (Qt.AlignmentFlag): The alignment of the text within the line edit. Defaults to Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter.
        cursor (Qt.CursorShape): The cursor shape to use for the line edit. Defaults to Qt.CursorShape.IBeamCursor.
        placeholder_text (str): The placeholder text to display when the line edit is empty. Defaults to "".
        font (PyFont): The font to use for the line edit text. Defaults to a default PyFont object.
    """

    def __init__(
        self,
        name: str = "line_edit",
        parent: QWidget | None = None,
        enabled: bool = True,
        visible: bool = True,
        style_sheet: str = "",
        minimum_size: ObjectSize | None = None,
        maximum_size: ObjectSize | None = None,
        fixed_size: ObjectSize | None = None,
        size_policy: QSizePolicy | None = None,
        graphic_effect: QGraphicsEffect | None = None,
        alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        cursor: Qt.CursorShape = Qt.CursorShape.IBeamCursor,
        placeholder_text: str = "",
        font: PyFont = PyFont(),
    ):
        """Initializes a LineEditInit object.

        Args:
            name (str): The object name.
            parent (QWidget | None): The parent widget.
            enabled (bool): Whether the line edit is enabled.
            visible (bool): Whether the line edit is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (ObjectSize | None): The minimum size.
            maximum_size (ObjectSize | None): The maximum size.
            fixed_size (ObjectSize | None): The fixed size.
            size_policy (QSizePolicy | None): The size policy.
            graphic_effect (QGraphicsEffect | None): The graphic effect.
            alignment (Qt.AlignmentFlag): The text alignment.
            cursor (Qt.CursorShape): The cursor shape.
            placeholder_text (str): The placeholder text.
            font (PyFont): The font to use.
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
            graphic_effect,
        )

        self.alignment = alignment
        self.cursor = cursor
        self.placeholder_text = placeholder_text
        self.font = font


class PyLineEdit(QLineEdit, PyWidget):
    """
    A custom line edit widget.
    """

    def __init__(self, line_edit_init: LineEditInit = LineEditInit(), instance: str = ""):
        """
        Initializes a PyLineEdit object.

        Args:
            line_edit_init (LineEditInit): Initialization parameters.
            instance (str): Initial text. Defaults to "".
        """
        super().__init__(widget_init=line_edit_init)

        self.line_edit_instance = instance

        self.setAlignment(line_edit_init.alignment)
        self.setAutoFillBackground(False)
        self.setCursor(line_edit_init.cursor)
        self.setPlaceholderText(line_edit_init.placeholder_text)
        self.setFont(line_edit_init.font)
        self.setText(instance)

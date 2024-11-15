from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsEffect, QLabel, QSizePolicy, QWidget

from PyGraphicUI.Attributes import ObjectSize, PixmapInstance, PyFont, TextInstance
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit


class LabelInit(WidgetInit):
    """
    Data class to hold initialization parameters for labels.

    Attributes:
        name (str): The object name of the label. Defaults to "label".
        parent (QWidget | None): The parent widget. Defaults to None.
        enabled (bool): Whether the label is enabled. Defaults to True.
        visible (bool): Whether the label is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the label. Defaults to "".
        minimum_size (ObjectSize | None): The minimum size of the label. Defaults to None.
        maximum_size (ObjectSize | None): The maximum size of the label. Defaults to None.
        fixed_size (ObjectSize | None): The fixed size of the label. Defaults to None.
        size_policy (QSizePolicy | None): The size policy of the label. Defaults to None.
        graphic_effect (QGraphicsEffect | None): The graphic effect to apply to the label. Defaults to None.
        scaled_contents (bool): Whether the contents should be scaled to fit the label. Defaults to False.
        word_wrap (bool): Whether the text should wrap. Defaults to True.
        indent (int): The indentation of the text. Defaults to 0.
        alignment (Qt.AlignmentFlag): The alignment of the text. Defaults to Qt.AlignmentFlag.AlignCenter.
        interaction_flag (Qt.TextInteractionFlag): The text interaction flag. Defaults to Qt.TextInteractionFlag.NoTextInteraction.
        font (PyFont): The font of the text. Defaults to a default PyFont object.
        margin (int): The margin around the text. Defaults to 0.

    """

    def __init__(
        self,
        name: str = "label",
        parent: QWidget | None = None,
        enabled: bool = True,
        visible: bool = True,
        style_sheet: str = "",
        minimum_size: ObjectSize | None = None,
        maximum_size: ObjectSize | None = None,
        fixed_size: ObjectSize | None = None,
        size_policy: QSizePolicy | None = None,
        graphic_effect: QGraphicsEffect | None = None,
        scaled_contents: bool = False,
        word_wrap: bool = True,
        indent: int = 0,
        alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
        interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
        font: PyFont = PyFont(),
        margin: int = 0,
    ):
        """
        Initializes a LabelInit object.

        Args:
            name (str): The object name.
            parent (QWidget | None): The parent widget.
            enabled (bool): Whether the label is enabled.
            visible (bool): Whether the label is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (ObjectSize | None): The minimum size.
            maximum_size (ObjectSize | None): The maximum size.
            fixed_size (ObjectSize | None): The fixed size.
            size_policy (QSizePolicy | None): The size policy.
            graphic_effect (QGraphicsEffect | None): The graphic effect.
            scaled_contents (bool): Whether to scale contents.
            word_wrap (bool): Whether to wrap text.
            indent (int): Text indentation.
            alignment (Qt.AlignmentFlag): Text alignment.
            interaction_flag (Qt.TextInteractionFlag): Text interaction flags.
            font (PyFont): The font to use.
            margin (int): The margin around the text.
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

        self.scaled_contents = scaled_contents
        self.word_wrap = word_wrap
        self.indent = indent
        self.alignment = alignment
        self.interaction_flag = interaction_flag
        self.font = font
        self.margin = margin


class PyLabel(QLabel, PyWidget):
    """
    Custom label class inheriting from QLabel and PyWidget.
    """

    def __init__(self, label_init: LabelInit = LabelInit(), instance: str | PixmapInstance | None = None):
        """
        Initializes a PyLabel object.

        Args:
            label_init (LabelInit): Initialization parameters for the label.
            instance (str | PixmapInstance | None): Initial content for the label, either text or a PixmapInstance. Defaults to None.
        """
        super().__init__(widget_init=label_init)

        self.label_instance = instance

        self.setAlignment(label_init.alignment)
        self.setAutoFillBackground(False)
        self.setIndent(label_init.indent)
        self.setScaledContents(label_init.scaled_contents)
        self.setTextInteractionFlags(label_init.interaction_flag)
        self.setWordWrap(label_init.word_wrap)
        self.setFont(label_init.font)
        self.setMargin(label_init.margin)
        self.set_label_instance(instance)

    def set_label_instance(
        self,
        label_instance: str | TextInstance | PixmapInstance | None = None,
    ):
        """
        Set the content to display in label.

        Args:
            label_instance (str | TextInstance | PixmapInstance | None): The content to display. Defaults to None.
        """
        if isinstance(label_instance, TextInstance):
            self.setText(label_instance.text)
            self.setFont(label_instance.font)
        elif isinstance(label_instance, PixmapInstance):
            scaled_pixmap = label_instance.pixmap.scaled(label_instance.pixmap_size)
            self.setPixmap(scaled_pixmap)
        elif isinstance(label_instance, str):
            self.setText(label_instance)
        elif label_instance is None:
            self.setText("")

    def set_default_label_instance(self):
        """Resets the label to its initial instance."""
        self.set_label_instance(self.label_instance)

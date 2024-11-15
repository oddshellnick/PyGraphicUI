from PyQt6.QtCore import QRect, QSize, Qt
from PyQt6.QtGui import QFont, QFontMetrics
from PyQt6.QtWidgets import QGraphicsEffect, QHeaderView, QSizePolicy, QWidget

from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import WidgetInit


class HeaderViewInit(WidgetInit):
    """
    Data class to hold initialization parameters for header views.

    Attributes:
        orientation (Qt.Orientation): The orientation of the header view.
        name (str): The object name of the header view. Defaults to "header_view".
        parent (QWidget | None): The parent widget. Defaults to None.
        enabled (bool): Whether the header view is enabled. Defaults to True.
        visible (bool): Whether the header view is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the header view. Defaults to "".
        minimum_size (ObjectSize | None): The minimum size of the header view. Defaults to None.
        maximum_size (ObjectSize | None): The maximum size of the header view. Defaults to None.
        fixed_size (ObjectSize | None): The fixed size of the header view. Defaults to None.
        size_policy (QSizePolicy | None): The size policy of the header view. Defaults to None.
        graphic_effect (QGraphicsEffect | None): The graphic effect to apply to the header view. Defaults to None.
        font (QFont): The font for the header view. Defaults to a default PyFont object.
    """

    def __init__(
        self,
        orientation: Qt.Orientation,
        name: str = "header_view",
        parent: QWidget | None = None,
        enabled: bool = True,
        visible: bool = True,
        style_sheet: str = "",
        minimum_size: ObjectSize | None = None,
        maximum_size: ObjectSize | None = None,
        fixed_size: ObjectSize | None = None,
        size_policy: QSizePolicy | None = None,
        graphic_effect: QGraphicsEffect | None = None,
        font: QFont = PyFont(),
    ):
        """
        Initializes a HeaderViewInit object.

        Args:
            orientation (Qt.Orientation): The orientation of the header view.
            name (str): The object name.
            parent (QWidget | None): The parent widget.
            enabled (bool): Whether the header view is enabled.
            visible (bool): Whether the header view is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (ObjectSize | None): The minimum size.
            maximum_size (ObjectSize | None): The maximum size.
            fixed_size (ObjectSize | None): The fixed size.
            size_policy (QSizePolicy | None): The size policy.
            graphic_effect (QGraphicsEffect | None): The graphic effect.
            font (QFont): The font to use.
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

        self.orientation = orientation
        self.font = font


class PyHeaderView(QHeaderView):
    """
    A custom header view class with enhanced initialization.
    """

    def __init__(self, header_view_init: HeaderViewInit):
        """
        Initializes a PyHeaderView object.

        Args:
            header_view_init (HeaderViewInit): Initialization parameters for the header view.
        """
        if header_view_init.parent is None:
            super().__init__(header_view_init.orientation)
        else:
            super().__init__(header_view_init.orientation, header_view_init.parent)

        self.font = header_view_init.font

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setEnabled(header_view_init.enabled)
        self.setGraphicsEffect(header_view_init.graphic_effect)
        self.setObjectName(header_view_init.name)
        self.setStyleSheet(header_view_init.style_sheet)
        self.setVisible(header_view_init.visible)
        self.set_fixed_size(header_view_init.fixed_size)
        self.set_maximum_size(header_view_init.maximum_size)
        self.set_minimum_size(header_view_init.minimum_size)
        self.setFont(header_view_init.font)

        if header_view_init.size_policy is not None:
            self.setSizePolicy(header_view_init.size_policy)

    def set_minimum_size(self, minimum_size: ObjectSize | None):
        """
        Sets the minimum size of the header view.

        Args:
            minimum_size (ObjectSize | None): The minimum size to set.
        """
        if minimum_size is not None:
            if minimum_size.size is not None:
                self.setMinimumSize(minimum_size.size)
            elif minimum_size.width is not None:
                self.setMinimumWidth(minimum_size.width)
            elif minimum_size.height is not None:
                self.setMinimumHeight(minimum_size.height)

    def set_maximum_size(self, maximum_size: ObjectSize | None):
        """
        Sets the maximum size of the header view.

        Args:
            maximum_size (ObjectSize | None): The maximum size to set.
        """
        if maximum_size is not None:
            if maximum_size.size is not None:
                self.setMaximumSize(maximum_size.size)
            elif maximum_size.width is not None:
                self.setMaximumWidth(maximum_size.width)
            elif maximum_size.height is not None:
                self.setMaximumHeight(maximum_size.height)

    def set_fixed_size(self, fixed_size: ObjectSize | None):
        """
        Sets the fixed size of the header view.

        Args:
            fixed_size (ObjectSize | None): The fixed size to set.
        """
        if fixed_size is not None:
            if fixed_size.size is not None:
                self.setFixedSize(fixed_size.size)
            elif fixed_size.width is not None:
                self.setFixedWidth(fixed_size.width)
            elif fixed_size.height is not None:
                self.setFixedHeight(fixed_size.height)

    def sectionSizeFromContents(self, logicalIndex: int) -> QSize:
        """
        Calculates the size of a section based on its contents.

        Args:
            logicalIndex (int): The logical index of the section.

        Returns:
            QSize: The calculated size of the section.
        """
        if self.model():
            header_text = self.model().headerData(logicalIndex, self.orientation(), Qt.ItemDataRole.DisplayRole)

            metrics = QFontMetrics(self.font)
            max_width = self.sectionSize(logicalIndex)

            rect = metrics.boundingRect(
                QRect(0, 0, max_width, 5000),
                self.defaultAlignment() | Qt.TextFlag.TextWordWrap | Qt.TextFlag.TextExpandTabs,
                header_text,
                4,
            )
            return rect.size()
        else:
            return super().sectionSizeFromContents(logicalIndex)

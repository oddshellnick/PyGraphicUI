import typing
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QLocale, Qt
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QComboBox,
	QCompleter,
	QGraphicsEffect,
	QSizePolicy,
	QStyledItemDelegate,
	QWidget
)


class ComboBoxItemTextDelegate(QStyledItemDelegate):
	"""
    A custom item delegate for QComboBox to display prefix and suffix in items.
    """
	
	def __init__(self, prefix: str, suffix: str, parent: typing.Optional[QWidget] = None):
		"""
        Initializes the ComboBoxItemTextDelegate.

        Args:
            prefix: The prefix to add to each item's text.
            suffix: The suffix to add to each item's text.
            parent: The parent widget.
        """
		super().__init__(parent)
		
		self.prefix = prefix
		self.suffix = suffix
	
	def displayText(self, value: typing.Any, locale: QLocale) -> str:
		"""
        Returns the display text for the given value.

        Args:
            value (typing.Any): The value to display.
            locale (QLocale): The locale to use.

        Returns:
            The display text with prefix and suffix added.
        """
		text = super().displayText(value, locale)
		return f"{self.prefix}{text}{self.suffix}"


class ComboBoxInit(WidgetInit):
	"""
    Data class to hold initialization parameters for combo boxes.

    Attributes:
        name (str): The object name of the combo box. Defaults to "combo_box".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the combo box is enabled. Defaults to True.
        visible (bool): Whether the combo box is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the combo box. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the combo box. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the combo box. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the combo box. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the combo box. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the combo box. Defaults to None.
        cursor (Qt.CursorShape): The cursor shape to use for the combo box. Defaults to Qt.CursorShape.PointingHandCursor.
        font (typing.Optional[QFont]): The font to use for the combo box text. Defaults to None.
        editable (bool): Whether the combo box is editable. Defaults to False.
        insert_policy (QComboBox.InsertPolicy): The insert policy for the combo box. Defaults to QComboBox.InsertPolicy.NoInsert.
        completion_mode (QCompleter.CompletionMode): The completion mode for the combo box. Defaults to QCompleter.CompletionMode.PopupCompletion.
        filter_mode (Qt.MatchFlag): The filter mode for the combo box completer. Defaults to Qt.MatchFlag.MatchContains.
        item_prefix (str): The prefix to add to each item's text. Defaults to "".
        item_suffix (str): The suffix to add to each item's text. Defaults to "".
        completer_popup_style_sheet (str): The style sheet to apply to the completer popup. Defaults to "".
    """
	
	def __init__(
			self,
			name: str = "combo_box",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			cursor: Qt.CursorShape = Qt.CursorShape.PointingHandCursor,
			font: PyFont = PyFont(),
			editable: bool = False,
			insert_policy: QComboBox.InsertPolicy = QComboBox.InsertPolicy.NoInsert,
			completion_mode: QCompleter.CompletionMode = QCompleter.CompletionMode.PopupCompletion,
			filter_mode: Qt.MatchFlag = Qt.MatchFlag.MatchContains,
			item_prefix: str = "",
			item_suffix: str = "",
			completer_popup_stylesheet: str = ""
	):
		"""
        Initializes a ComboBoxInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the combo box is enabled.
            visible (bool): Whether the combo box is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            cursor (Qt.CursorShape): The cursor shape.
            font (PyFont): The font for the text.
            editable (bool): Whether the combo box is editable.
            insert_policy (QComboBox.InsertPolicy): The insert policy.
            completion_mode (QCompleter.CompletionMode): The completion mode.
            filter_mode (Qt.MatchFlag): The filter mode.
            item_prefix (str): The item prefix.
            item_suffix (str): The item suffix.
            completer_popup_stylesheet (str): The style sheet for completer popup.
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
		
		self.cursor = cursor
		self.font = font
		self.editable = editable
		self.insert_policy = insert_policy
		self.completion_mode = completion_mode
		self.filter_mode = filter_mode
		self.item_prefix = item_prefix
		self.item_suffix = item_suffix
		self.completer_popup_style_sheet = completer_popup_stylesheet


class PyComboBox(QComboBox, PyWidget):
	"""
    A custom combo box widget.
    """
	
	def __init__(
			self,
			combo_box_init: ComboBoxInit = ComboBoxInit(),
			instances: typing.Optional[typing.Iterable[str]] = None
	):
		"""
        Initializes a PyComboBox object.

        Args:
            combo_box_init (ComboBoxInit): The initialization parameters.
            instances (typing.Optional[typing.Iterable[str]]): A typing.Iterable of strings representing the initial items in the combo box. Defaults to None.
        """
		super().__init__(widget_init=combo_box_init)
		
		self.setCursor(combo_box_init.cursor)
		self.setEditable(combo_box_init.editable)
		self.setInsertPolicy(combo_box_init.insert_policy)
		
		if combo_box_init.item_prefix or combo_box_init.item_suffix:
			self.setItemDelegate(
					ComboBoxItemTextDelegate(combo_box_init.item_prefix, combo_box_init.item_suffix, self)
			)
		
		if combo_box_init.editable:
			self.completer().setCompletionMode(combo_box_init.completion_mode)
			
			
			self.completer().setFilterMode(combo_box_init.filter_mode)
			
			
			if self.completer().completionMode() == QCompleter.CompletionMode.PopupCompletion:
				self.completer().popup().setStyleSheet(combo_box_init.completer_popup_style_sheet)
				self.completer().popup().setFont(combo_box_init.font)
			
			
			self.lineEdit().setFont(combo_box_init.font)
		
		self.setFont(combo_box_init.font)
		
		if instances is not None:
			self.add_instances(instances)
	
	def add_instances(self, instances: typing.Iterable[str]):
		"""
        Adds a typing.Iterable of items to the combo box.

        Args:
            instances (typing.Iterable[str]): A typing.Iterable of strings to add as items to the combo box.
        """
		self.addItems(instances)
	
	def reset_instances(self, instances: typing.Iterable[str]):
		"""
        Clears existing items and sets new items in the combo box.

        Args:
            instances (typing.Iterable[str]): A typing.Iterable of strings to set as the new items in the combo box.
        """
		self.clear()
		self.add_instances(instances)

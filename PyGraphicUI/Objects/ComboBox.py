from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QComboBox, QCompleter, QGraphicsEffect, QSizePolicy, QStyledItemDelegate, QWidget
#
#
#
#
class ComboBoxItemTextDelegate(QStyledItemDelegate):
	#
	#
	#
	#
	def __init__(self, prefix, suffix, parent=None):
		super().__init__(parent)
		#
		#
		#
		#
		self.prefix = prefix
		self.suffix = suffix
	#
	#
	#
	#
	def displayText(self, value, locale):
		text = super().displayText(value, locale)
		return f"{self.prefix}{text}{self.suffix}"
#
#
#
#
class ComboBoxInit(WidgetInit):
	#
	#
	#
	#
	def __init__(
			self,
			name: str = "combo_box",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			cursor: Qt.CursorShape = Qt.CursorShape.PointingHandCursor,
			font: QFont = None,
			editable: bool = False,
			insert_policy: QComboBox.InsertPolicy = QComboBox.InsertPolicy.NoInsert,
			completion_mode: QCompleter.CompletionMode = QCompleter.CompletionMode.PopupCompletion,
			filter_mode: Qt.MatchFlag = Qt.MatchFlag.MatchContains,
			item_prefix: str = "",
			item_suffix: str = "",
			completer_popup_stylesheet: str = "",
			maximum_output_length: int = None
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
		self.cursor = cursor
		self.font = font
		self.editable = editable
		self.insert_policy = insert_policy
		self.completion_mode = completion_mode
		self.filter_mode = filter_mode
		self.item_prefix = item_prefix
		self.item_suffix = item_suffix
		self.completer_popup_style_sheet = completer_popup_stylesheet
		self.maximum_output_length = maximum_output_length
#
#
#
#
class PyComboBox(QComboBox, PyWidget):
	#
	#
	#
	#
	def __init__(self, combo_box_init: ComboBoxInit = ComboBoxInit(), instances: list[str] = None):
		super().__init__(widget_init=combo_box_init)
		#
		#
		#
		#
		self.setCursor(combo_box_init.cursor)
		self.setEditable(combo_box_init.editable)
		self.setInsertPolicy(combo_box_init.insert_policy)
		#
		#
		#
		#
		if combo_box_init.item_prefix or combo_box_init.item_suffix:
			self.setItemDelegate(
					ComboBoxItemTextDelegate(combo_box_init.item_prefix, combo_box_init.item_suffix, self)
			)
		#
		#
		#
		#
		if combo_box_init.editable:
			self.completer().setCompletionMode(combo_box_init.completion_mode)
			self.completer().setFilterMode(combo_box_init.filter_mode)
			#
			#
			#
			#
			if self.completer().completionMode() == QCompleter.CompletionMode.PopupCompletion:
				self.completer().popup().setStyleSheet(combo_box_init.completer_popup_style_sheet)
				self.completer().popup().setFont(combo_box_init.font)
			#
			#
			#
			#
			self.lineEdit().setFont(combo_box_init.font)
		#
		#
		#
		#
		if combo_box_init.font is not None:
			self.setFont(combo_box_init.font)
		#
		#
		#
		#
		if instances is not None:
			self.add_instances(instances)
	#
	#
	#
	#
	def add_instances(self, instances: list[str]):
		self.addItems(instances)
	#
	#
	#
	#
	def reset_instances(self, instances: list[str]):
		self.clear()
		self.add_instances(instances)

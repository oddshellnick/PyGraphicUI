from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QGraphicsEffect, QProgressBar, QSizePolicy, QWidget
#
#
#
#
class ProgressBarInit(WidgetInit):
	def __init__(
			self,
			name: str = "progress_bar",
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
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			minimum_value: int = 0,
			maximum_value: int = 0,
			format_: str = "%.02f %%"
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
		self.alignment = alignment
		self.minimum_value = minimum_value
		self.maximum_value = maximum_value
		self.format_ = format_
#
#
#
#
class PyProgressBar(QProgressBar, PyWidget):
	def __init__(self, progress_bar_init: ProgressBarInit = ProgressBarInit()):
		super().__init__(widget_init=progress_bar_init)
		#
		#
		#
		#
		self.progress_bar_format = progress_bar_init.format_
		#
		#
		#
		#
		self.setAlignment(progress_bar_init.alignment)
		self.setRange(
				progress_bar_init.minimum_value,
				progress_bar_init.maximum_value
		)
		self.setValue(progress_bar_init.minimum_value)
		#
		#
		#
		#
		if progress_bar_init.font is not None:
			self.setFont(progress_bar_init.font)
		#
		#
		#
		#
		self.valueChanged.connect(self.set_new_value)
		self.set_new_value()
	#
	#
	#
	#
	def set_new_value(self):
		self.setFormat(
				self.progress_bar_format % (
					((self.value() / self.maximum()) * 100) if self.maximum() != 0 else 0
				)
		)
	#
	#
	#
	#
	def reset_range(self, minimum_value: int, maximum_value: int):
		self.setRange(minimum_value, maximum_value)
		self.setValue(minimum_value)
	#
	#
	#
	#
	def update_progress(self):
		self.setValue(self.value() + 1)

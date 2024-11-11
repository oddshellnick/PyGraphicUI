from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QAbstractSpinBox, QGraphicsEffect, QSizePolicy, QSpinBox, QWidget
#
#
#
#
class SpinBoxInit(WidgetInit):
	#
	#
	#
	#
	def __init__(
			self,
			name: str = "spinbox",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			font: QFont = PyFont(),
			minimum: int = 0,
			maximum: int = 99,
			step: int = 1,
			step_type: QAbstractSpinBox.StepType = QAbstractSpinBox.StepType.DefaultStepType,
			prefix: str = "",
			suffix: str = ""
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
		self.minimum = minimum
		self.maximum = maximum
		self.step = step
		self.step_type = step_type
		self.prefix = prefix
		self.suffix = suffix
#
#
#
#
class PySpinBox(QSpinBox, PyWidget):
	#
	#
	#
	#
	def __init__(self, spinbox_init: SpinBoxInit = SpinBoxInit()):
		super().__init__(widget_init=spinbox_init)
		#
		#
		#
		#
		self.setFont(spinbox_init.font)
		self.lineEdit().setFont(spinbox_init.font)
		self.setRange(spinbox_init.minimum, spinbox_init.maximum)
		self.setSingleStep(spinbox_init.step)
		self.setStepType(spinbox_init.step_type)
		self.setPrefix(spinbox_init.prefix)
		self.setSuffix(spinbox_init.suffix)

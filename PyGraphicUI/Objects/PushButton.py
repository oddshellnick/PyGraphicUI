from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyGraphicUI.Attributes import IconInstance, ObjectSize, PyFont, TextInstance
from PyQt6.QtWidgets import QGraphicsEffect, QPushButton, QSizePolicy, QWidget
#
#
#
#
class PushButtonInit(WidgetInit):
	def __init__(
			self,
			name: str = "button",
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
		self.cursor = cursor
		self.font = font
#
#
#
#
class PyPushButton(QPushButton, PyWidget):
	doubleClicked = pyqtSignal()
	clicked = pyqtSignal()
	#
	#
	#
	#
	def __init__(
			self,
			button_init: PushButtonInit = PushButtonInit(),
			instance: str | IconInstance = ""
	):
		super().__init__(widget_init=button_init)
		#
		#
		#
		#
		self.setCursor(button_init.cursor)
		self.setFont(button_init.font)
		#
		#
		#
		#
		self.button_instance = instance
		self.set_button_instance(self.button_instance)
		#
		#
		#
		#
		self.timer = QTimer()
		self.timer.setSingleShot(True)
		self.timer.timeout.connect(self.clicked.emit)
		#
		#
		#
		#
		super().clicked.connect(self.check_double_click)
	#
	#
	#
	#
	def check_double_click(self):
		if self.timer.isActive():
			self.doubleClicked.emit()
			self.timer.stop()
		else:
			self.timer.start(250)
	#
	#
	#
	#
	def set_button_instance(
			self,
			button_instance: str | TextInstance | IconInstance = ""
	):
		if type(button_instance) == TextInstance:
			self.setText(button_instance.text)
			self.setFont(button_instance.font)

		elif type(button_instance) == IconInstance:
			self.setIcon(button_instance.icon)
			self.setIconSize(button_instance.icon_size)
		elif type(button_instance) == str:
			self.setText(button_instance)
	#
	#
	#
	#
	def set_default_button_instance(self):
		if type(self.button_instance) == TextInstance:
			self.setText(self.button_instance)
		elif type(self.button_instance) == IconInstance:
			self.setIcon(self.button_instance.icon)
			self.setIconSize(self.button_instance.icon_size)

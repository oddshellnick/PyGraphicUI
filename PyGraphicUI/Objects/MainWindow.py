from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import ObjectSize
from PyQt6.QtWidgets import QGraphicsEffect, QMainWindow, QSizePolicy, QWidget
#
#
#
#
class MainWindowInit:
	def __init__(
			self,
			name: str = "widget",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			window_flag: tuple[Qt.WindowType, bool] = (Qt.WindowType.Window, True)
	):
		self.name = name
		self.parent = parent
		self.enabled = enabled
		self.visible = visible
		self.style_sheet = style_sheet
		self.minimum_size = minimum_size
		self.maximum_size = maximum_size
		self.fixed_size = fixed_size
		self.size_policy = size_policy
		self.graphic_effect = graphic_effect
		self.window_flag = window_flag
#
#
#
#
class PyMainWindow(QMainWindow):
	def __init__(self, main_window_init: MainWindowInit = MainWindowInit()):
		super().__init__()
		#
		#
		#
		#
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		self.setEnabled(main_window_init.enabled)
		self.setGraphicsEffect(main_window_init.graphic_effect)
		self.setObjectName(main_window_init.name)
		self.setStyleSheet(main_window_init.style_sheet)
		self.setVisible(main_window_init.visible)
		self.set_fixed_size(main_window_init.fixed_size)
		self.set_maximum_size(main_window_init.maximum_size)
		self.set_minimum_size(main_window_init.minimum_size)
		self.setWindowFlag(*main_window_init.window_flag)
		#
		#
		#
		#
		if main_window_init.size_policy is not None:
			self.setSizePolicy(main_window_init.size_policy)
	#
	#
	#
	#
	def set_minimum_size(self, minimum_size: ObjectSize):
		if minimum_size is not None:
			if minimum_size.size is not None:
				self.setMinimumSize(minimum_size.size)
			elif minimum_size.width is not None:
				self.setMinimumWidth(minimum_size.width)
			elif minimum_size.height is not None:
				self.setMinimumHeight(minimum_size.height)
	#
	#
	#
	#
	def set_maximum_size(self, maximum_size: ObjectSize):
		if maximum_size is not None:
			if maximum_size.size is not None:
				self.setMaximumSize(maximum_size.size)
			elif maximum_size.width is not None:
				self.setMaximumWidth(maximum_size.width)
			elif maximum_size.height is not None:
				self.setMaximumHeight(maximum_size.height)
	#
	#
	#
	#
	def set_fixed_size(self, fixed_size: ObjectSize):
		if fixed_size is not None:
			if fixed_size.size is not None:
				self.setFixedSize(fixed_size.size)
			elif fixed_size.width is not None:
				self.setFixedWidth(fixed_size.width)
			elif fixed_size.height is not None:
				self.setFixedHeight(fixed_size.height)

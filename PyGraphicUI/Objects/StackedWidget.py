from PyGraphicUI.Attributes import ObjectSize
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QGraphicsEffect, QSizePolicy, QStackedWidget, QWidget
#
#
#
#
class StackedWidgetInit(WidgetInit):
	#
	#
	#
	#
	def __init__(
			self,
			name: str = "stacked_widget",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None
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
class PyStackedWidget(QStackedWidget, PyWidget):
	#
	#
	#
	#
	def __init__(
			self,
			stacked_widget_init: StackedWidgetInit = StackedWidgetInit(),
			stacked_widget_instances: list[QWidget] = None
	):
		super().__init__(widget_init=stacked_widget_init)
		#
		#
		#
		#
		if stacked_widget_instances is not None:
			self.add_widgets(stacked_widget_instances)
	#
	#
	#
	#
	def add_widgets(self, instances: list[QWidget] | QWidget):
		if type(instances) == list:
			for instance in instances:
				self.addWidget(instance)
		else:
			self.addWidget(instances)
	#
	#
	#
	#
	def clear_stacked_widget(self):
		for _ in range(self.count()):
			self.setCurrentIndex(0)
			self.removeWidget(self.currentWidget())

from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import GridLayoutItem, LinearLayoutItem, ObjectSize
from PyQt6.QtWidgets import QGraphicsEffect, QLayout, QLayoutItem, QSizePolicy, QWidget
from PyGraphicUI.Objects.Layouts import GridLayout, LayoutInit, PyHorizontalLayout, PyVerticalLayout
#
#
#
#
class WidgetInit:
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
			graphic_effect: QGraphicsEffect = None
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
#
#
#
#
class PyWidget(QWidget):
	def __init__(self, widget_init: WidgetInit = WidgetInit()):
		if widget_init.parent is None:
			super().__init__()
		else:
			super().__init__(widget_init.parent)
		#
		#
		#
		#
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		self.setEnabled(widget_init.enabled)
		self.setGraphicsEffect(widget_init.graphic_effect)
		self.setObjectName(widget_init.name)
		self.setStyleSheet(widget_init.style_sheet)
		self.setVisible(widget_init.visible)
		self.set_fixed_size(widget_init.fixed_size)
		self.set_maximum_size(widget_init.maximum_size)
		self.set_minimum_size(widget_init.minimum_size)
		#
		#
		#
		#
		if widget_init.size_policy is not None:
			self.setSizePolicy(widget_init.size_policy)
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
	#
	#
	#
	#
	def disable_and_hide(self):
		self.setEnabled(False)
		self.setVisible(False)
	#
	#
	#
	#
	def enable_and_show(self):
		self.setEnabled(True)
		self.setVisible(True)
#
#
#
#
class WidgetWithLayoutInit:
	def __init__(
			self,
			widget_init: WidgetInit = WidgetInit(),
			layout_init: LayoutInit = LayoutInit()
	):
		self.widget_init = widget_init
		self.layout_init = layout_init
#
#
#
#
class PyWidgetWithVerticalLayout(PyWidget):
	def __init__(
			self,
			widget_with_layout_init: WidgetWithLayoutInit = WidgetWithLayoutInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(widget_init=widget_with_layout_init.widget_init)
		#
		#
		#
		#
		widget_with_layout_init.layout_init.parent = self
		#
		#
		#
		#
		self.vertical_layout = PyVerticalLayout(
				layout_init=widget_with_layout_init.layout_init,
				instances=instances
		)
		self.setLayout(self.vertical_layout)
	#
	#
	#
	#
	def add_instance(self, instance: LinearLayoutItem):
		self.vertical_layout.add_instance(instance)
	#
	#
	#
	#
	def add_stretch(self):
		self.vertical_layout.addStretch()
	#
	#
	#
	#
	def clear_widget_layout(self):
		self.vertical_layout.clear_layout()
	#
	#
	#
	#
	def clear_widget_layout_by_type(self, type_to_clear):
		self.vertical_layout.clear_layout_by_type(type_to_clear)
	#
	#
	#
	#
	def get_all_instances(self):
		return self.vertical_layout.get_all_instances()
	#
	#
	#
	#
	def get_all_instances_of_type(self, type_to_get):
		return self.vertical_layout.get_all_instances_of_type(type_to_get)
	#
	#
	#
	#
	def get_instance(self, index: int):
		return self.vertical_layout.get_instance(index)
	#
	#
	#
	#
	def get_number_of_instances(self):
		return self.vertical_layout.get_number_of_instances()
	#
	#
	#
	#
	def get_number_of_instances_of_type(self, type_to_check):
		return self.vertical_layout.get_number_of_instances_of_type(type_to_check)
	#
	#
	#
	#
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		self.vertical_layout.insert_instance(index, instance)
	#
	#
	#
	#
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.vertical_layout.remove_instance(instance)
#
#
#
#
class PyWidgetWithHorizontalLayout(PyWidget):
	def __init__(
			self,
			widget_with_layout_init: WidgetWithLayoutInit = WidgetWithLayoutInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(widget_init=widget_with_layout_init.widget_init)
		#
		#
		#
		#
		widget_with_layout_init.layout_init.parent = self
		#
		#
		#
		#
		self.horizontal_layout = PyHorizontalLayout(
				layout_init=widget_with_layout_init.layout_init,
				instances=instances
		)
		self.setLayout(self.horizontal_layout)
	#
	#
	#
	#
	def add_instance(self, instance: LinearLayoutItem):
		self.horizontal_layout.add_instance(instance)
	#
	#
	#
	#
	def add_stretch(self):
		self.horizontal_layout.addStretch()
	#
	#
	#
	#
	def clear_widget_layout(self):
		self.horizontal_layout.clear_layout()
	#
	#
	#
	#
	def clear_widget_layout_by_type(self, type_to_clear):
		self.horizontal_layout.clear_layout_by_type(type_to_clear)
	#
	#
	#
	#
	def get_all_instances(self):
		return self.horizontal_layout.get_all_instances()
	#
	#
	#
	#
	def get_all_instances_of_type(self, type_to_get):
		return self.horizontal_layout.get_all_instances_of_type(type_to_get)
	#
	#
	#
	#
	def get_instance(self, index: int):
		return self.horizontal_layout.get_instance(index)
	#
	#
	#
	#
	def get_number_of_instances(self):
		return self.horizontal_layout.get_number_of_instances()
	#
	#
	#
	#
	def get_number_of_instances_of_type(self, type_to_check):
		return self.horizontal_layout.get_number_of_instances_of_type(type_to_check)
	#
	#
	#
	#
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		self.horizontal_layout.insert_instance(index, instance)
	#
	#
	#
	#
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.horizontal_layout.remove_instance(instance)
#
#
#
#
class PyWidgetWithGridLayout(PyWidget):
	def __init__(
			self,
			widget_with_layout_init: WidgetWithLayoutInit = WidgetWithLayoutInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(widget_init=widget_with_layout_init.widget_init)
		#
		#
		#
		#
		widget_with_layout_init.layout_init.parent = self
		#
		#
		#
		#
		self.grid_layout = GridLayout(
				layout_init=widget_with_layout_init.layout_init,
				instances=instances
		)
		self.setLayout(self.grid_layout)
	#
	#
	#
	#
	def add_instance(self, instance: GridLayoutItem):
		self.grid_layout.add_instance(instance)
	#
	#
	#
	#
	def clear_widget_layout(self):
		self.grid_layout.clear_layout()
	#
	#
	#
	#
	def clear_widget_layout_by_type(self, type_to_clear):
		self.grid_layout.clear_layout_by_type(type_to_clear)
	#
	#
	#
	#
	def get_all_instances(self):
		return self.grid_layout.get_all_instances()
	#
	#
	#
	#
	def get_all_instances_of_type(self, type_to_get):
		return self.grid_layout.get_all_instances_of_type(type_to_get)
	#
	#
	#
	#
	def get_instance(self, index: int):
		return self.grid_layout.get_instance(index)
	#
	#
	#
	#
	def get_number_of_instances(self):
		return self.grid_layout.get_number_of_instances()
	#
	#
	#
	#
	def get_number_of_instances_of_type(self, type_to_check):
		return self.grid_layout.get_number_of_instances_of_type(type_to_check)
	#
	#
	#
	#
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.grid_layout.remove_instance(instance)

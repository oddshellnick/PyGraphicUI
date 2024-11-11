from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyGraphicUI.Attributes import GridLayoutItem, LinearLayoutItem, ObjectSize
from PyQt6.QtWidgets import QDialog, QGraphicsEffect, QLayout, QLayoutItem, QSizePolicy, QWidget
from PyGraphicUI.Objects.Layouts import GridLayout, LayoutInit, PyHorizontalLayout, PyVerticalLayout
#
#
#
#
class DialogInit(WidgetInit):
	def __init__(
			self,
			title: str = "dialog",
			name: str = "dialog",
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
		self.title = title
#
#
#
#
class PyDialog(QDialog, PyWidget):
	def __init__(self, dialog_init: DialogInit = DialogInit()):
		super().__init__(widget_init=dialog_init)
		#
		#
		#
		#
		self.setWindowTitle(dialog_init.title)
#
#
#
#
class DialogWithLayoutInit:
	def __init__(
			self,
			dialog_init: DialogInit = DialogInit(),
			layout_init: LayoutInit = LayoutInit()
	):
		self.dialog_init = dialog_init
		self.layout_init = layout_init
#
#
#
#
class PyDialogWithVerticalLayout(PyDialog):
	def __init__(
			self,
			dialog_with_layout_init: DialogWithLayoutInit = DialogWithLayoutInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(dialog_init=dialog_with_layout_init.dialog_init)
		#
		#
		#
		#
		dialog_with_layout_init.layout_init.parent = self
		#
		#
		#
		#
		self.vertical_layout = PyVerticalLayout(
				layout_init=dialog_with_layout_init.layout_init,
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
	def clear_dialog_layout(self):
		self.vertical_layout.clear_layout()
	#
	#
	#
	#
	def clear_dialog_layout_by_type(self, type_to_clear):
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
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.vertical_layout.remove_instance(instance)
#
#
#
#
class PyDialogWithHorizontalLayout(PyDialog):
	def __init__(
			self,
			dialog_with_layout_init: DialogWithLayoutInit = DialogWithLayoutInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(dialog_init=dialog_with_layout_init.dialog_init)
		#
		#
		#
		#
		dialog_with_layout_init.layout_init.parent = self
		#
		#
		#
		#
		self.horizontal_layout = PyHorizontalLayout(
				layout_init=dialog_with_layout_init.layout_init,
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
	def clear_dialog_layout(self):
		self.horizontal_layout.clear_layout()
	#
	#
	#
	#
	def clear_dialog_layout_by_type(self, type_to_clear):
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
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.horizontal_layout.remove_instance(instance)
#
#
#
#
class PyDialogWithGridLayout(PyDialog):
	def __init__(
			self,
			dialog_with_layout_init: DialogWithLayoutInit = DialogWithLayoutInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(dialog_init=dialog_with_layout_init.dialog_init)
		#
		#
		#
		#
		dialog_with_layout_init.layout_init.parent = self
		#
		#
		#
		#
		self.grid_layout = GridLayout(
				layout_init=dialog_with_layout_init.layout_init,
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
	def clear_dialog_layout(self):
		self.grid_layout.clear_layout()
	#
	#
	#
	#
	def clear_dialog_layout_by_type(self, type_to_clear):
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

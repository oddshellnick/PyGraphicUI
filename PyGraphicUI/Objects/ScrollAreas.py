from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import GridLayoutItem, LinearLayoutItem, ObjectSize
from PyQt6.QtWidgets import QGraphicsEffect, QLayout, QLayoutItem, QScrollArea, QSizePolicy, QWidget
from PyGraphicUI.Objects.Widgets import PyWidget, PyWidgetWithGridLayout, PyWidgetWithHorizontalLayout, PyWidgetWithVerticalLayout, WidgetInit, WidgetWithLayoutInit
#
#
#
#
class ScrollAreaInit(WidgetInit):
	def __init__(
			self,
			name: str = "scroll_area",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			vertical_scroll_bar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAsNeeded,
			horizontal_scroll_bar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAsNeeded,
			central_widget_init: WidgetWithLayoutInit = WidgetWithLayoutInit()
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
		self.vertical_scroll_bar_policy = vertical_scroll_bar_policy
		self.horizontal_scroll_bar_policy = horizontal_scroll_bar_policy
		self.central_widget_init = central_widget_init
#
#
#
#
class PyVerticalScrollArea(QScrollArea, PyWidget):
	def __init__(
			self,
			scroll_area_init: ScrollAreaInit = ScrollAreaInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(widget_init=scroll_area_init)
		#
		#
		#
		#
		self.horizontal_scroll = PyWidgetWithHorizontalLayout(
				widget_with_layout_init=WidgetWithLayoutInit(widget_init=WidgetInit(parent=self))
		)
		scroll_area_init.central_widget_init.widget_init.parent = self.horizontal_scroll
		#
		#
		#
		#
		self.vertical_scroll = PyWidgetWithVerticalLayout(
				widget_with_layout_init=scroll_area_init.central_widget_init,
				instances=instances
		)
		self.horizontal_scroll.add_instance(LinearLayoutItem(self.vertical_scroll))
		self.setHorizontalScrollBarPolicy(scroll_area_init.horizontal_scroll_bar_policy)
		self.setVerticalScrollBarPolicy(scroll_area_init.vertical_scroll_bar_policy)
		self.setWidget(self.horizontal_scroll)
		self.setWidgetResizable(True)
	#
	#
	#
	#
	def add_instance(self, instance: LinearLayoutItem):
		self.vertical_scroll.add_instance(instance)
	#
	#
	#
	#
	def clear_scroll_area(self):
		self.vertical_scroll.clear_widget_layout()
	#
	#
	#
	#
	def clear_scroll_area_by_type(self, type_to_clear):
		self.vertical_scroll.clear_widget_layout_by_type(type_to_clear)
	#
	#
	#
	#
	def get_all_instances(self):
		return self.vertical_scroll.get_all_instances()
	#
	#
	#
	#
	def get_instance(self, index: int):
		return self.vertical_scroll.get_instance(index)
	#
	#
	#
	#
	def get_number_of_instances(self):
		return self.vertical_scroll.get_number_of_instances()
	#
	#
	#
	#
	def get_number_of_instances_of_type(self, type_to_check):
		return self.vertical_scroll.get_number_of_instances_of_type(type_to_check)
	#
	#
	#
	#
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		self.vertical_scroll.insert_instance(index, instance)
	#
	#
	#
	#
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.vertical_scroll.remove_instance(instance)
#
#
#
#
class PyHorizontalScrollArea(QScrollArea, PyWidget):
	def __init__(
			self,
			scroll_area_init: ScrollAreaInit = ScrollAreaInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(widget_init=scroll_area_init)
		#
		#
		#
		#
		self.vertical_scroll = PyWidgetWithHorizontalLayout(
				widget_with_layout_init=WidgetWithLayoutInit(widget_init=WidgetInit(parent=self))
		)
		scroll_area_init.central_widget_init.widget_init.parent = self.vertical_scroll
		#
		#
		#
		#
		self.horizontal_scroll = PyWidgetWithHorizontalLayout(
				widget_with_layout_init=scroll_area_init.central_widget_init,
				instances=instances
		)
		self.vertical_scroll.add_instance(LinearLayoutItem(self.horizontal_scroll))
		self.setHorizontalScrollBarPolicy(scroll_area_init.horizontal_scroll_bar_policy)
		self.setVerticalScrollBarPolicy(scroll_area_init.vertical_scroll_bar_policy)
		self.setWidget(self.vertical_scroll)
		self.setWidgetResizable(True)
	#
	#
	#
	#
	def add_instance(self, instance: LinearLayoutItem):
		self.horizontal_scroll.add_instance(instance)
	#
	#
	#
	#
	def clear_scroll_area(self):
		self.horizontal_scroll.clear_widget_layout()
	#
	#
	#
	#
	def clear_scroll_area_by_type(self, type_to_clear):
		self.horizontal_scroll.clear_widget_layout_by_type(type_to_clear)
	#
	#
	#
	#
	def get_all_instances(self):
		return self.horizontal_scroll.get_all_instances()
	#
	#
	#
	#
	def get_instance(self, index: int):
		return self.horizontal_scroll.get_instance(index)
	#
	#
	#
	#
	def get_number_of_instances(self):
		return self.horizontal_scroll.get_number_of_instances()
	#
	#
	#
	#
	def get_number_of_instances_of_type(self, type_to_check):
		return self.horizontal_scroll.get_number_of_instances_of_type(type_to_check)
	#
	#
	#
	#
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		self.horizontal_scroll.insert_instance(index, instance)
	#
	#
	#
	#
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.horizontal_scroll.remove_instance(instance)
#
#
#
#
class GridScrollArea(QScrollArea, PyWidget):
	def __init__(
			self,
			scroll_area_init: ScrollAreaInit = ScrollAreaInit(),
			instances: list[LinearLayoutItem] = None
	):
		super().__init__(widget_init=scroll_area_init)
		#
		#
		#
		#
		self.vertical_scroll = PyWidgetWithHorizontalLayout(
				widget_with_layout_init=WidgetWithLayoutInit(widget_init=WidgetInit(parent=self))
		)
		scroll_area_init.central_widget_init.widget_init.parent = self.vertical_scroll
		#
		#
		#
		#
		self.grid_scroll = PyWidgetWithGridLayout(
				widget_with_layout_init=scroll_area_init.central_widget_init,
				instances=instances
		)
		self.vertical_scroll.add_instance(LinearLayoutItem(self.grid_scroll))
		self.setHorizontalScrollBarPolicy(scroll_area_init.horizontal_scroll_bar_policy)
		self.setVerticalScrollBarPolicy(scroll_area_init.vertical_scroll_bar_policy)
		self.setWidget(self.vertical_scroll)
		self.setWidgetResizable(True)
	#
	#
	#
	#
	def add_instance(self, instance: GridLayoutItem):
		self.grid_scroll.add_instance(instance)
	#
	#
	#
	#
	def clear_scroll_area(self):
		self.grid_scroll.clear_widget_layout()
	#
	#
	#
	#
	def clear_scroll_area_by_type(self, type_to_clear):
		self.grid_scroll.clear_widget_layout_by_type(type_to_clear)
	#
	#
	#
	#
	def get_all_instances(self):
		return self.grid_scroll.get_all_instances()
	#
	#
	#
	#
	def get_instance(self, index: int):
		return self.grid_scroll.get_instance(index)
	#
	#
	#
	#
	def get_number_of_instances(self):
		return self.grid_scroll.get_number_of_instances()
	#
	#
	#
	#
	def get_number_of_instances_of_type(self, type_to_check):
		return self.grid_scroll.get_number_of_instances_of_type(type_to_check)
	#
	#
	#
	#
	def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
		self.grid_scroll.remove_instance(instance)

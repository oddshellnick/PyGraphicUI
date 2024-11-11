from copy import deepcopy
from PyQt6.QtCore import Qt
from pandas import DataFrame
from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyGraphicUI.Objects.AbstractTableModel import PyAbstractTableModel
from PyGraphicUI.Objects.SortFilterProxyModel import PySortFilterProxyModel
from PyQt6.QtWidgets import QGraphicsEffect, QHeaderView, QSizePolicy, QTableView, QWidget
#
#
#
#
class TableViewOptimize:
	def __init__(self, optimize_enabled: bool = False, view_length: int = 100):
		self.optimize_enabled = optimize_enabled
		self.view_length = view_length
#
#
#
#
class TableViewInit(WidgetInit):
	def __init__(
			self,
			name: str = "table_view",
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
			sorting_enabled: bool = True,
			vertical_optimize: TableViewOptimize = TableViewOptimize(),
			horizontal_optimize: TableViewOptimize = TableViewOptimize()
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
		self.sorting_enabled = sorting_enabled
		self.vertical_optimize = vertical_optimize
		self.horizontal_optimize = horizontal_optimize
#
#
#
#
class PyTableView(QTableView, PyWidget):
	def __init__(
			self,
			table_view_init: TableViewInit,
			table_model: PySortFilterProxyModel | PyAbstractTableModel
	):
		super().__init__(widget_init=table_view_init)
		#
		#
		#
		#
		self.table_model = table_model
		self.vertical_optimize = table_view_init.vertical_optimize
		self.horizontal_optimize = table_view_init.horizontal_optimize
		self.sort_order = Qt.SortOrder.AscendingOrder
		#
		#
		#
		#
		self.last_sorted_column = self.table_model.headerData(0, Qt.Orientation.Horizontal, Qt.ItemDataRole.UserRole)
		#
		#
		#
		#
		self.setModel(self.table_model)
		self.setFont(table_view_init.font)
		self.setSortingEnabled(table_view_init.sorting_enabled)
		self.horizontalHeader().sectionClicked.connect(self.h_header_clicked)
		self.resize_columns()
		#
		#
		#
		#
		if self.vertical_optimize.optimize_enabled or self.horizontal_optimize.optimize_enabled:
			if type(table_model) == PyAbstractTableModel:
				self.current_data = deepcopy(table_model.table_data)
			else:
				self.current_data = deepcopy(table_model.table_model.table_data)
	#
	#
	#
	#
	def sort_table(self, column_index: int):
		sorted_column = self.table_model.headerData(
				column_index,
				Qt.Orientation.Horizontal,
				Qt.ItemDataRole.UserRole
		)

		if self.sort_order == Qt.SortOrder.DescendingOrder or self.last_sorted_column != sorted_column:
			self.sort_order = Qt.SortOrder.AscendingOrder
		else:
			self.sort_order = Qt.SortOrder.DescendingOrder

		self.last_sorted_column = sorted_column

		self.sortByColumn(column_index, self.sort_order)
		self.reset()
	#
	#
	#
	#
	def h_header_clicked(self, column_index: int):
		self.sort_table(column_index)
	#
	#
	#
	#
	def resize_columns(self):
		for i in range(self.table_model.columnCount()):
			self.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

		for i in range(self.table_model.rowCount()):
			self.verticalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
	#
	#
	#
	#
	def reset_model(self, data: DataFrame):
		self.table_model.reset_table_data(data)

		self.setModel(self.table_model)
		self.reset()

		self.resize_columns()

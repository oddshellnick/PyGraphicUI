import typing
import pandas
from copy import deepcopy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyGraphicUI.Objects.AbstractTableModel import PyAbstractTableModel
from PyGraphicUI.Objects.SortFilterProxyModel import PySortFilterProxyModel
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QHeaderView,
	QSizePolicy,
	QTableView,
	QWidget
)


class TableViewOptimize:
	"""
    Configuration settings for optimizing table view performance.

    Attributes:
        optimize_enabled (bool): Whether optimization is enabled. Defaults to False.
        view_length (int): The number of rows to display. Defaults to 100.
    """
	
	def __init__(self, optimize_enabled: bool = False, view_length: int = 100):
		"""Initializes TableViewOptimize with specified settings.

        Args:
            optimize_enabled (bool): Enables/disables optimization.
            view_length (int): Number of rows to display when optimized.
        """
		self.optimize_enabled = optimize_enabled
		self.view_length = view_length


class TableViewInit(WidgetInit):
	"""
    Data class to hold initialization parameters for table views.

    Attributes:
        name (str): The object name of the table view. Defaults to "table_view".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the table view is enabled. Defaults to True.
        visible (bool): Whether the table view is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the table view. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the table view. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the table view. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the table view. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the table view. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the table view. Defaults to None.
        font (QFont): The font for the table view. Defaults to a default PyFont.
        sorting_enabled (bool): Whether sorting is enabled. Defaults to True.
        vertical_optimize (TableViewOptimize): Vertical optimization settings. Defaults to a default TableViewOptimize.
        horizontal_optimize (TableViewOptimize): Horizontal optimization settings. Defaults to a default TableViewOptimize.
    """
	
	def __init__(
			self,
			name: str = "table_view",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			font: QFont = PyFont(),
			sorting_enabled: bool = True,
			vertical_optimize: TableViewOptimize = TableViewOptimize(),
			horizontal_optimize: TableViewOptimize = TableViewOptimize()
	):
		"""
        Initializes a TableViewInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the table view is enabled.
            visible (bool): Whether the table view is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            font (QFont): The font to use.
            sorting_enabled (bool): Whether sorting is enabled.
            vertical_optimize (TableViewOptimize): Vertical optimization settings.
            horizontal_optimize (TableViewOptimize): Horizontal optimization settings.
        """
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
		
		self.font = font
		self.sorting_enabled = sorting_enabled
		self.vertical_optimize = vertical_optimize
		self.horizontal_optimize = horizontal_optimize


class PyTableView(QTableView, PyWidget):
	"""
    A custom table view class with enhanced features.
    """
	
	def __init__(
			self,
			table_view_init: TableViewInit,
			table_model: typing.Union[PySortFilterProxyModel, PyAbstractTableModel]
	):
		"""
        Initializes a PyTableView object.

        Args:
            table_view_init (TableViewInit): Initialization parameters for the table view.
            table_model (typing.Union[PySortFilterProxyModel, PyAbstractTableModel]): The table model to use.
        """
		super().__init__(widget_init=table_view_init)
		
		self.table_model = table_model
		self.vertical_optimize = table_view_init.vertical_optimize
		self.horizontal_optimize = table_view_init.horizontal_optimize
		self.sort_order = Qt.SortOrder.AscendingOrder
		self.last_sorted_column = self.table_model.headerData(0, Qt.Orientation.Horizontal, Qt.ItemDataRole.UserRole)
		self.setModel(self.table_model)
		self.setFont(table_view_init.font)
		self.setSortingEnabled(table_view_init.sorting_enabled)
		self.horizontalHeader().sectionClicked.connect(self.h_header_clicked)
		self.resize_columns()
		
		if self.vertical_optimize.optimize_enabled or self.horizontal_optimize.optimize_enabled:
			if isinstance(table_model, PyAbstractTableModel):
				self.current_data = deepcopy(table_model.table_data)
			else:
				self.current_data = deepcopy(table_model.table_model.table_data)
	
	def sort_table(self, column_index: int):
		"""
        Sorts the table by the specified column.

        Args:
            column_index (int): The index of the column to sort by.
        """
		sorted_column = self.table_model.headerData(column_index, Qt.Orientation.Horizontal, Qt.ItemDataRole.UserRole)
		
		if self.sort_order == Qt.SortOrder.DescendingOrder or self.last_sorted_column != sorted_column:
			self.sort_order = Qt.SortOrder.AscendingOrder
		else:
			self.sort_order = Qt.SortOrder.DescendingOrder
	
	def h_header_clicked(self, column_index: int):
		"""
        Handles clicks on the horizontal header.

        Args:
            column_index (int): The index of the clicked header section.
        """
		self.sort_table(column_index)
	
	def resize_columns(self):
		"""Resizes columns to fit content."""
		for i in range(self.table_model.columnCount()):
			self.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
		
		for i in range(self.table_model.rowCount()):
			self.verticalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
	
	def reset_model(self, data: pandas.DataFrame):
		"""
        Resets the table model with new data.

        Args:
            data (pandas.DataFrame): The new data for the model.
        """
		self.table_model.reset_table_data(data)
		
		self.setModel(self.table_model)
		self.reset()
		
		self.resize_columns()

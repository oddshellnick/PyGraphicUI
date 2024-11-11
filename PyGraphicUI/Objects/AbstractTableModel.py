from typing import Callable
from pandas import DataFrame
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt
#
#
#
#
class AbstractTableModelInit:
	#
	#
	#
	#
	def __init__(
			self,
			data: DataFrame,
			format_data: Callable = None,
			format_data_by_column: dict[int, Callable] = None
	):
		self.data = data
		self.format_data = format_data
		self.format_data_by_column = format_data_by_column
#
#
#
#
class PyAbstractTableModel(QAbstractTableModel):
	#
	#
	#
	#
	def __init__(self, abstract_table_model_init: AbstractTableModelInit):
		super().__init__()
		#
		#
		#
		#
		self.table_data = abstract_table_model_init.data
		self.format_data = abstract_table_model_init.format_data
		self.format_data_by_column = abstract_table_model_init.format_data_by_column
	#
	#
	#
	#
	def rowCount(self, index: QModelIndex = ...):
		return self.table_data.shape[0]
	#
	#
	#
	#
	def reset_table_data(self, data: DataFrame):
		self.beginResetModel()
		self.table_data = data
		self.endResetModel()
	#
	#
	#
	#
	def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
		if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.UserRole:
			if orientation == Qt.Orientation.Horizontal:
				return str(self.table_data.columns[section])
			elif orientation == Qt.Orientation.Vertical:
				return str(self.table_data.index[section] + 1)
	#
	#
	#
	#
	def data(self, index: QModelIndex, role: int = ...):
		if role == Qt.ItemDataRole.DisplayRole:
			if self.format_data_by_column is not None:
				if index.column() in self.format_data_by_column.keys():
					return self.format_data_by_column[index.column()](self.table_data.iloc[index.row(), index.column()])
				elif self.format_data is not None:
					return self.format_data(self.table_data.iloc[index.row(), index.column()])
				else:
					return str(self.table_data.iloc[index.row(), index.column()])
			elif self.format_data is not None:
				return self.format_data(self.table_data.iloc[index.row(), index.column()])
			else:
				return str(self.table_data.iloc[index.row(), index.column()])
	#
	#
	#
	#
	def columnCount(self, index: QModelIndex = ...):
		return self.table_data.shape[1]

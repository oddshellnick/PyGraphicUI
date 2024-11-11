from re import search
from typing import Callable
from pandas import DataFrame
from PyQt6.QtCore import QModelIndex, QSortFilterProxyModel, Qt
from PyGraphicUI.Objects.AbstractTableModel import PyAbstractTableModel
#
#
#
#
class SortFilterProxyModelInit:
	def __init__(
			self,
			table_model: PyAbstractTableModel,
			less_than_key: Callable = None
	):
		self.table_model = table_model
		self.less_than_key = less_than_key
#
#
#
#
class PySortFilterProxyModel(QSortFilterProxyModel):
	def __init__(self, sort_filter_proxy_model_init: SortFilterProxyModelInit):
		super().__init__()
		#
		#
		#
		#
		self.table_model = sort_filter_proxy_model_init.table_model
		self.less_than_key = sort_filter_proxy_model_init.less_than_key
		self.filters = {}
		self.replaces = {}
		#
		#
		#
		#
		self.setSourceModel(self.table_model)
	#
	#
	#
	#
	def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex):
		for key, regex in self.filters.items():
			ix = self.sourceModel().index(
					source_row,
					self.table_model.table_data.columns.get_loc(key),
					source_parent
			)

			if ix.isValid():
				data_string = self.sourceModel().data(ix, Qt.ItemDataRole.DisplayRole)

				for replace in self.replaces[key]:
					data_string = data_string.replace(replace[0], replace[1])

				if search(regex, data_string) is None:
					return False
		return True
	#
	#
	#
	#
	def headerData(
			self,
			section: int,
			orientation: Qt.Orientation,
			role: int = ...
	):
		return self.table_model.headerData(section, orientation, role)
	#
	#
	#
	#
	def lessThan(self, left: QModelIndex, right: QModelIndex):
		left = left.data()
		right = right.data()

		if self.less_than_key is not None:
			left = self.less_than_key(left)
			right = self.less_than_key(right)

		return left > right
	#
	#
	#
	#
	def reset_table_data(self, data: DataFrame):
		self.table_model.reset_table_data(data)
	#
	#
	#
	#
	def setFilterByColumn(
			self,
			regex: str,
			replaces_in_data: list[tuple[str, str]],
			column: str
	):
		self.filters[column] = regex
		self.replaces[column] = replaces_in_data
		self.invalidateFilter()

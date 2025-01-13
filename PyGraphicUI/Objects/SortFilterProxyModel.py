import re
import typing
import pandas
from PyQt6.QtCore import (
	QModelIndex,
	QSortFilterProxyModel,
	Qt
)
from PyGraphicUI.Objects.AbstractTableModel import PyAbstractTableModel


class SortFilterProxyModelInit:
	"""
    Data class to hold initialization parameters for sort filter proxy models.

    Attributes:
        table_model (PyAbstractTableModel): The table model to be filtered and sorted.
        less_than_key (typing.Optional[typing.Callable[[typing.Any], int]]): A callable to apply to data before comparison for sorting. Defaults to None.
    """
	
	def __init__(
			self,
			table_model: PyAbstractTableModel,
			less_than_key: typing.Optional[typing.Callable[[typing.Any], int]] = None
	):
		"""
        Initializes a SortFilterProxyModelInit object.

        Args:
            table_model (PyAbstractTableModel): The table model to use.
            less_than_key (typing.Optional[typing.Callable[[typing.Any], int]]): The key function for sorting.
        """
		self.table_model = table_model
		self.less_than_key = less_than_key


class PySortFilterProxyModel(QSortFilterProxyModel):
	"""
    A custom sort filter proxy model for filtering and sorting table data.

    Attributes:
        table_model (PyAbstractTableModel): The table model to be filtered and sorted.
        less_than_key (typing.Optional[typing.Callable[[typing.Any], int]]): A callable to apply to data before comparison for sorting. Defaults to None.
        filters (dict[str, str]): Filters to apply to data before comparison for sorting.
        replaces (dict[str, list[tuple[str, str]]]): Replaces to apply to data before comparison for sorting.
    """
	
	def __init__(self, sort_filter_proxy_model_init: SortFilterProxyModelInit):
		"""
        Initializes a PySortFilterProxyModel object.

        Args:
            sort_filter_proxy_model_init (SortFilterProxyModelInit): Initialization parameters for the model.
        """
		super().__init__()
		
		self.table_model = sort_filter_proxy_model_init.table_model
		self.less_than_key = sort_filter_proxy_model_init.less_than_key
		self.filters: dict[str, str] = {}
		self.replaces: dict[str, list[tuple[str, str]]] = {}
		self.setSourceModel(self.table_model)
	
	def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
		"""
        Checks if a row should be accepted by the filter.

        Args:
            source_row (int): The row index in the source model.
            source_parent (QModelIndex): The parent index.

        Returns:
            bool: True if the row is accepted, False otherwise.
        """
		for key, regex in self.filters.items():
			ix = self.sourceModel().index(
					source_row,
					self.table_model.table_data.columns.get_loc(key),
					source_parent
			)
		
			if ix.isValid():
				data_string = str(self.sourceModel().data(ix, Qt.ItemDataRole.DisplayRole))
		
				for replace in self.replaces.get(key, []):
					data_string = data_string.replace(replace[0], replace[1])
		
				if re.search(regex, data_string) is None:
					return False
		
		return True
	
	def headerData(
			self,
			section: int,
			orientation: Qt.Orientation,
			role: int = Qt.ItemDataRole.DisplayRole
	) -> typing.Optional[str]:
		"""
        Returns the header data for the given section, orientation, and role.

        Args:
            section (int): The section index.
            orientation (Qt.Orientation): The orientation.
            role (int): The data role. Defaults to Qt.ItemDataRole.DisplayRole

        Returns:
            typing.Optional[str]: The header data.
        """
		return self.table_model.headerData(section, orientation, role)
	
	def lessThan(self, left: QModelIndex, right: QModelIndex) -> bool:
		"""
        Compares two model indices for sorting.

        Args:
            left (QModelIndex): The left index.
            right (QModelIndex): The right index.

        Returns:
            bool: True if left is less than right, False otherwise.
        """
		left_data = left.data()
		right_data = right.data()
		
		if self.less_than_key is not None:
			left_data = self.less_than_key(left_data)
			right_data = self.less_than_key(right_data)
		
		return left_data > right_data
	
	def reset_table_data(self, data: pandas.DataFrame):
		"""
        Resets the table data in the underlying table model.

        Args:
            data (pandas.DataFrame): The new table data.
        """
		self.table_model.reset_table_data(data)
	
	def setFilterByColumn(self, regex: str, replaces_in_data: list[tuple[str, str]], column: str):
		"""
        Sets a filter for a specific column.

        Args:
            regex (str): The regular expression to filter by.
            replaces_in_data (list[tuple[str, str]]): Replacements to perfrom before filtering.
            column (str): The column to filter.
        """
		self.filters[column] = regex
		self.replaces[column] = replaces_in_data
		self.invalidateFilter()

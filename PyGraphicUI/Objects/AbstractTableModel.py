import typing
import pandas
from PyQt6.QtCore import (
	QAbstractTableModel,
	QModelIndex,
	Qt
)


class AbstractTableModelInit:
	"""
    Data class to hold initialization parameters for abstract table models.

    Attributes:
        data (pandas.DataFrame): The pandas.DataFrame to be displayed in the table model.
        format_data (typing.Optional[typing.Union[typing.Callable[[typing.Any], str]]]): A callable to format all data in the table. Defaults to None.
        format_data_by_column (typing.Optional[dict[int, typing.Callable[[typing.Any], str]]]): A dictionary mapping column indices to callables for formatting specific columns. Defaults to None.
    """
	
	def __init__(
			self,
			data: pandas.DataFrame,
			format_data: typing.Optional[typing.Union[typing.Callable[[typing.Any], str]]] = None,
			format_data_by_column: typing.Optional[dict[int, typing.Callable[[typing.Any], str]]] = None
	):
		"""
        Initializes an AbstractTableModelInit object.

        Args:
            data (pandas.DataFrame): The pandas.DataFrame for the model.
            format_data (typing.Optional[typing.Union[typing.Callable[[typing.Any], str]]]): A callable to format all data.
            format_data_by_column (typing.Optional[dict[int, typing.Callable[[typing.Any], str]]]): A dictionary to format data by column.
        """
		self.data = data
		self.format_data = format_data
		self.format_data_by_column = format_data_by_column


class PyAbstractTableModel(QAbstractTableModel):
	"""
    A custom abstract table model based on a pandas pandas.DataFrame.

    Attributes:
        table_data (pandas.DataFrame): The pandas.DataFrame to be displayed in the table model.
        format_data (typing.Optional[typing.Union[typing.Callable[[typing.Any], str]]]): A callable to format all data in the table. Defaults to None.
        format_data_by_column (typing.Optional[dict[int, typing.Callable[[typing.Any], str]]]): A dictionary mapping column indices to callables for formatting specific columns. Defaults to None.
    """
	
	def __init__(self, abstract_table_model_init: AbstractTableModelInit):
		"""
        Initializes a PyAbstractTableModel object.

        Args:
            abstract_table_model_init (AbstractTableModelInit): Initialization parameters for the model.
        """
		super().__init__()
		
		self.table_data = abstract_table_model_init.data
		self.format_data = abstract_table_model_init.format_data
		self.format_data_by_column = abstract_table_model_init.format_data_by_column
	
	def columnCount(self, index: QModelIndex = QModelIndex()) -> int:
		"""
        Returns the number of columns in the model.

        Args:
            index (QModelIndex): The parent index. Defaults to QModelIndex()

        Returns:
            int: The number of columns.
        """
		return self.table_data.shape[1]
	
	def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> typing.Optional[str]:
		"""
        Returns the data for the given index and role.

        Args:
            index (QModelIndex): The index of the data item.
            role (int): The data role. Defaults to Qt.ItemDataRole.DisplayRole.

        Returns:
            typing.Optional[str]: The data.
        """
		if role == Qt.ItemDataRole.DisplayRole:
			if self.format_data_by_column is not None:
				if index.column() in self.format_data_by_column:
					return self.format_data_by_column[index.column()](self.table_data.iloc[index.row(), index.column()])
				elif self.format_data is not None:
					return self.format_data(self.table_data.iloc[index.row(), index.column()])
				else:
					return str(self.table_data.iloc[index.row(), index.column()])
			elif self.format_data is not None:
				return self.format_data(self.table_data.iloc[index.row(), index.column()])
			else:
				return str(self.table_data.iloc[index.row(), index.column()])
		
		return None
	
	def headerData(
			self,
			section: int,
			orientation: Qt.Orientation,
			role: int = Qt.ItemDataRole.DisplayRole
	) -> typing.Optional[str]:
		"""
        Returns the header data for the given section and orientation.

        Args:
            section (int): The section index.
            orientation (Qt.Orientation): The orientation (horizontal or vertical).
            role (int): The data role. Defaults to Qt.ItemDataRole.DisplayRole.

        Returns:
            typing.Optional[str]: The header data.
        """
		if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.UserRole:
			if orientation == Qt.Orientation.Horizontal:
				return str(self.table_data.columns[section])
			elif orientation == Qt.Orientation.Vertical:
				return str(self.table_data.index[section] + 1)
		
		return None
	
	def reset_table_data(self, data: pandas.DataFrame):
		"""
        Resets the table data with a new pandas.DataFrame.

        Args:
            data (pandas.DataFrame): The new pandas.DataFrame to use.
        """
		self.beginResetModel()
		self.table_data = data
		self.endResetModel()
	
	def rowCount(self, index: QModelIndex = QModelIndex()) -> int:
		"""
        Returns the number of rows in the model.

        Args:
            index (QModelIndex): The parent index. Defaults to QModelIndex().

        Returns:
            int: The number of rows.
        """
		return self.table_data.shape[0]

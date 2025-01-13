import typing
from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import (
	GridLayoutItem,
	LinearLayoutItem
)
from PyQt6.QtWidgets import (
	QGridLayout,
	QHBoxLayout,
	QLayout,
	QLayoutItem,
	QVBoxLayout,
	QWidget
)


class PyLayout(QLayout):
	"""
    Base class for custom layouts, providing common functionality.
    """
	
	def get_instance(self, index: int) -> typing.Any:
		"""
        Retrieves the widget or layout at the specified index.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            typing.Any: The widget or layout at the given index.
        """
		return self.itemAt(index).widget()
	
	def remove_instance(self, instance: typing.Union[QWidget, QLayout, int, QLayoutItem]):
		"""
        Removes a widget, layout, or item from the layout.

        Args:
            instance (typing.Union[QWidget, QLayout, int, QLayoutItem]): The instance to remove. Can be a widget, layout, index, or layout item.
        """
		if isinstance(instance, QLayoutItem):
			instance.widget().disconnect()
			self.removeWidget(instance.widget())
		elif isinstance(instance, int):
			item = self.get_instance(instance)
		
			try:
				item.disconnect()
			except TypeError:
				pass
			finally:
				self.removeWidget(item)
		else:
			instance.disconnect()
			self.removeWidget(instance)
	
	def clear_layout(self):
		"""
        Removes all widgets and layouts from the layout.
        """
		for i in reversed(range(self.count())):
			self.remove_instance(i)
	
	def clear_layout_by_type(self, type_to_clear: typing.Union[type, tuple[type, ...]]):
		"""
        Removes all instances of a specific type from the layout.

        Args:
            type_to_clear (typing.Union[type, tuple[type, ...]]): The type of instances to remove.
        """
		for i in reversed(range(self.count())):
			if isinstance(self.get_instance(i), type_to_clear):
				self.remove_instance(i)
	
	def get_all_instances(self) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all widgets and layouts in the layout.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		for i in range(self.count()):
			yield self.get_instance(i)
	
	def get_all_instances_of_type(self, type_to_get: typing.Union[type, tuple[type, ...]]) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all instances of a specific type in the layout.

        Args:
            type_to_get (typing.Union[type, tuple[type, ...]]): The type of instances to retrieve.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		for i in range(self.count()):
			instance = self.get_instance(i)
		
			if isinstance(instance, type_to_get):
				yield instance
	
	def get_number_of_instances(self) -> int:
		"""
        Returns the total number of widgets and layouts in the layout.

        Returns:
            int: The number of instances.
        """
		return self.count()
	
	def get_number_of_instances_of_type(self, type_to_check: typing.Union[type, tuple[type, ...]]) -> int:
		"""
        Returns the number of instances of a specific type in the layout.

        Args:
            type_to_check (typing.Union[type, tuple[type, ...]]): The type of instances to count.

        Returns:
            int: The number of instances of the specified type.
        """
		return sum(
				1
				for i in range(self.count()) if isinstance(self.get_instance(i), type_to_check)
		)


class LayoutInit:
	"""
    Data class to hold initialization parameters for layouts.

    Attributes:
        name (str): The name of the layout. Defaults to "layout".
        parent (typing.Optional[QWidget]): The parent widget of the layout. Defaults to None.
        enabled (bool): Whether the layout is enabled. Defaults to True.
        alignment (typing.Optional[Qt.AlignmentFlag]): The alignment of the layout. Defaults to None.
        contents_margins (typing.Union[tuple[int, int, int, int], None]): The margins of the layout contents. Defaults to None.
        spacing (int): The spacing between items in the layout. Defaults to 0.
    """
	
	def __init__(
			self,
			name: str = "layout",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			alignment: typing.Optional[Qt.AlignmentFlag] = None,
			contents_margins: typing.Union[tuple[int, int, int, int], None] = None,
			spacing: int = 0
	):
		"""
        Initializes a LayoutInit object.

        Args:
            name (str): The name of the layout.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the layout is enabled.
            alignment (typing.Optional[Qt.AlignmentFlag]): The alignment of the layout.
            contents_margins (typing.Union[tuple[int, int, int, int], None]): The margins of the layout contents.
            spacing (int): The spacing between items.
        """
		self.name = name
		self.parent = parent
		self.enabled = enabled
		self.alignment = alignment
		self.contents_margins = contents_margins if contents_margins is not None else (0, 0, 0, 0)
		self.spacing = spacing


class PyVerticalLayout(QVBoxLayout, PyLayout):
	"""
    A custom vertical layout class inheriting from QVBoxLayout and PyLayout.
    """
	
	def __init__(
			self,
			layout_init: LayoutInit = LayoutInit(),
			instances: typing.Optional[typing.Iterable[LinearLayoutItem]] = None
	):
		"""
        Initializes a PyVerticalLayout object.

        Args:
            layout_init (LayoutInit): Initialization parameters for the layout.
            instances (typing.Optional[typing.Iterable[LinearLayoutItem]]): A typing.Iterable of items to add to the layout.
        """
		if isinstance(layout_init.parent, QWidget):
			super().__init__(layout_init.parent)
		else:
			super().__init__()
		
		self.setEnabled(layout_init.enabled)
		self.setObjectName(layout_init.name)
		self.setSpacing(layout_init.spacing)
		
		if isinstance(layout_init.alignment, Qt.AlignmentFlag):
			self.setAlignment(layout_init.alignment)
		
		if isinstance(layout_init.contents_margins, tuple):
			if len(layout_init.contents_margins) == 4:
				self.setContentsMargins(*layout_init.contents_margins)
			else:
				raise ValueError("contents_margins must be of length 4")
		else:
			self.setContentsMargins(0, 0, 0, 0)
		
		if isinstance(instances, typing.Iterable):
			for instance in instances:
				self.add_instance(instance)
	
	def add_instance(self, instance: LinearLayoutItem):
		"""
        Adds a LinearLayoutItem to the layout.

        Args:
            instance (LinearLayoutItem): The item to add.
        """
		parameters = [instance.instance, instance.stretch]
		
		if instance.alignment is not None:
			parameters.append(instance.alignment)
		
		try:
			self.addWidget(*parameters)
		except TypeError:
			self.addLayout(*parameters)
	
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		"""
        Inserts a LinearLayoutItem at a specific index.

        Args:
            index (int): The index to insert at.
            instance (LinearLayoutItem): The item to insert.
        """
		parameters = [instance.instance, instance.stretch]
		
		if instance.alignment is not None:
			parameters.append(instance.alignment)
		
		try:
			self.insertWidget(index, *parameters)
		except TypeError:
			self.insertLayout(index, *parameters)


class PyHorizontalLayout(QHBoxLayout, PyLayout):
	"""
    A custom horizontal layout class inheriting from QHBoxLayout and PyLayout.
    """
	
	def __init__(
			self,
			layout_init: LayoutInit = LayoutInit(),
			instances: typing.Optional[typing.Iterable[LinearLayoutItem]] = None
	):
		"""
        Initializes a PyHorizontalLayout object.

        Args:
            layout_init (LayoutInit): Initialization parameters for the layout.
            instances (typing.Optional[typing.Iterable[LinearLayoutItem]]): A typing.Iterable of items to add to the layout.
        """
		if isinstance(layout_init.parent, QWidget):
			super().__init__(layout_init.parent)
		else:
			super().__init__()
		
		self.setEnabled(layout_init.enabled)
		self.setObjectName(layout_init.name)
		self.setSpacing(layout_init.spacing)
		
		if isinstance(layout_init.alignment, Qt.AlignmentFlag):
			self.setAlignment(layout_init.alignment)
		
		if isinstance(layout_init.contents_margins, tuple):
			if len(layout_init.contents_margins) == 4:
				self.setContentsMargins(*layout_init.contents_margins)
			else:
				raise ValueError("contents_margins must be of length 4")
		else:
			self.setContentsMargins(0, 0, 0, 0)
		
		if isinstance(instances, typing.Iterable):
			for instance in instances:
				self.add_instance(instance)
	
	def add_instance(self, instance: LinearLayoutItem):
		"""
        Adds a LinearLayoutItem to the layout.

        Args:
            instance (LinearLayoutItem): The item to add.
        """
		parameters = [instance.instance, instance.stretch]
		
		if instance.alignment is not None:
			parameters.append(instance.alignment)
		
		try:
			self.addWidget(*parameters)
		except TypeError:
			self.addLayout(*parameters)
	
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		"""
        Inserts a LinearLayoutItem at a specific index.

        Args:
            index (int): The index to insert at.
            instance (LinearLayoutItem): The item to insert.
        """
		parameters = [instance.instance, instance.stretch]
		
		if instance.alignment is not None:
			parameters.append(instance.alignment)
		
		try:
			self.insertWidget(index, *parameters)
		except TypeError:
			self.insertLayout(index, *parameters)


class GridLayout(QGridLayout, PyLayout):
	"""
    A custom grid layout class inheriting from QGridLayout and PyLayout.
    """
	
	def __init__(
			self,
			layout_init: LayoutInit = LayoutInit(),
			instances: typing.Optional[typing.Iterable[GridLayoutItem]] = None
	):
		"""
        Initializes a GridLayout object.

        Args:
            layout_init (LayoutInit): Initialization parameters for the layout.
            instances (typing.Optional[typing.Iterable[GridLayoutItem]]): A typing.Iterable of items to add to the layout.
        """
		if isinstance(layout_init.parent, QWidget):
			super().__init__(layout_init.parent)
		else:
			super().__init__()
		
		self.setEnabled(layout_init.enabled)
		self.setObjectName(layout_init.name)
		self.setSpacing(layout_init.spacing)
		
		if isinstance(layout_init.alignment, Qt.AlignmentFlag):
			self.setAlignment(layout_init.alignment)
		
		if isinstance(layout_init.contents_margins, tuple):
			if len(layout_init.contents_margins) == 4:
				self.setContentsMargins(*layout_init.contents_margins)
			else:
				raise ValueError("contents_margins must be of length 4")
		else:
			self.setContentsMargins(0, 0, 0, 0)
		
		if isinstance(instances, typing.Iterable):
			for instance in instances:
				self.add_instance(instance)
	
	def add_instance(self, instance: GridLayoutItem):
		"""
        Adds a GridLayoutItem to the layout.

        Args:
            instance (GridLayoutItem): The item to add.
        """
		parameters = [
			instance.instance,
			instance.stretch.vertical_position,
			instance.stretch.horizontal_position
		]
		
		if instance.stretch.vertical_stretch is not None:
			parameters.append(instance.stretch.vertical_stretch)
		
		if instance.stretch.horizontal_stretch is not None:
			parameters.append(instance.stretch.horizontal_stretch)
		
		if instance.alignment is not None:
			parameters.append(instance.alignment)
		
		try:
			self.addWidget(*parameters)
		except TypeError:
			self.addLayout(*parameters)

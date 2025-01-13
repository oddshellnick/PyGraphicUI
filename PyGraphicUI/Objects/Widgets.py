import typing
from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import (
	GridLayoutItem,
	LinearLayoutItem,
	ObjectSize
)
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QLayout,
	QLayoutItem,
	QSizePolicy,
	QWidget
)
from PyGraphicUI.Objects.Layouts import (
	GridLayout,
	LayoutInit,
	PyHorizontalLayout,
	PyVerticalLayout
)


class WidgetInit:
	"""
    Data class to hold initialization parameters for widgets.

    Attributes:
        name (str): The object name of the widget. Defaults to "widget".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the widget is enabled. Defaults to True.
        visible (bool): Whether the widget is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the widget. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the widget. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the widget. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the widget. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the widget. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the widget. Defaults to None.
    """
	
	def __init__(
			self,
			name: str = "widget",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None
	):
		"""
        Initializes a WidgetInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the widget is enabled.
            visible (bool): Whether the widget is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
        """
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


class PyWidget(QWidget):
	"""
    A custom widget class with enhanced initialization and utility functions.
    """
	
	def __init__(self, widget_init: WidgetInit = WidgetInit()):
		"""
        Initializes a PyWidget object.

        Args:
            widget_init (WidgetInit): Initialization parameters for the widget.
        """
		if widget_init.parent is None:
			super().__init__()
		else:
			super().__init__(widget_init.parent)
		
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		self.setEnabled(widget_init.enabled)
		self.setGraphicsEffect(widget_init.graphic_effect)
		self.setObjectName(widget_init.name)
		self.setStyleSheet(widget_init.style_sheet)
		self.setVisible(widget_init.visible)
		self.set_fixed_size(widget_init.fixed_size)
		self.set_maximum_size(widget_init.maximum_size)
		self.set_minimum_size(widget_init.minimum_size)
		
		if widget_init.size_policy is not None:
			self.setSizePolicy(widget_init.size_policy)
	
	def set_minimum_size(self, minimum_size: typing.Optional[ObjectSize]):
		"""
        Sets the minimum size of the widget.

        Args:
            minimum_size (typing.Optional[ObjectSize]): The minimum size to set.
        """
		if minimum_size is not None:
			if minimum_size.size is not None:
				self.setMinimumSize(minimum_size.size)
			elif minimum_size.width is not None:
				self.setMinimumWidth(minimum_size.width)
			elif minimum_size.height is not None:
				self.setMinimumHeight(minimum_size.height)
	
	def set_maximum_size(self, maximum_size: typing.Optional[ObjectSize]):
		"""
        Sets the maximum size of the widget.

        Args:
            maximum_size (typing.Optional[ObjectSize]): The maximum size to set.
        """
		if maximum_size is not None:
			if maximum_size.size is not None:
				self.setMaximumSize(maximum_size.size)
			elif maximum_size.width is not None:
				self.setMaximumWidth(maximum_size.width)
			elif maximum_size.height is not None:
				self.setMaximumHeight(maximum_size.height)
	
	def set_fixed_size(self, fixed_size: typing.Optional[ObjectSize]):
		"""
        Sets the fixed size of the widget.

        Args:
            fixed_size (typing.Optional[ObjectSize]): The fixed size to set.
        """
		if fixed_size is not None:
			if fixed_size.size is not None:
				self.setFixedSize(fixed_size.size)
			elif fixed_size.width is not None:
				self.setFixedWidth(fixed_size.width)
			elif fixed_size.height is not None:
				self.setFixedHeight(fixed_size.height)
	
	def disable_and_hide(self):
		"""
        Disables and hides the widget.
        """
		self.setEnabled(False)
		self.setVisible(False)
	
	def enable_and_show(self):
		"""
        Enables and shows the widget.
        """
		self.setEnabled(True)
		self.setVisible(True)


class WidgetWithLayoutInit:
	"""
    Data class to hold initialization parameters for widgets with layouts.

    Attributes:
        widget_init (WidgetInit): Initialization parameters for the widget.
        layout_init (LayoutInit): Initialization parameters for the layout.
    """
	
	def __init__(
			self,
			widget_init: WidgetInit = WidgetInit(),
			layout_init: LayoutInit = LayoutInit()
	):
		"""
        Initializes a WidgetWithLayoutInit object.

        Args:
            widget_init (WidgetInit): Widget initialization parameters.
            layout_init (LayoutInit): Layout initialization parameters.
        """
		self.widget_init = widget_init
		self.layout_init = layout_init


class PyWidgetWithVerticalLayout(PyWidget):
	"""
    A custom widget with a vertical layout.
    """
	
	def __init__(
			self,
			widget_with_layout_init: WidgetWithLayoutInit = WidgetWithLayoutInit(),
			instances: typing.Optional[typing.Iterable[LinearLayoutItem]] = None
	):
		"""
        Initializes a PyWidgetWithVerticalLayout object.

        Args:
            widget_with_layout_init (WidgetWithLayoutInit): Widget and layout initialization parameters.
            instances (typing.Optional[typing.Iterable[LinearLayoutItem]]): a typing.Iterable of LinearLayoutItem objects to be added to the layout.
        """
		super().__init__(widget_init=widget_with_layout_init.widget_init)
		
		widget_with_layout_init.layout_init.parent = self
		
		self.vertical_layout = PyVerticalLayout(layout_init=widget_with_layout_init.layout_init, instances=instances)
		self.setLayout(self.vertical_layout)
	
	def add_instance(self, instance: LinearLayoutItem):
		"""
        Adds a LinearLayoutItem to the layout.

        Args:
            instance (LinearLayoutItem): The item to add.
        """
		self.vertical_layout.add_instance(instance)
	
	def add_stretch(self):
		"""Adds a stretch to the vertical layout."""
		self.vertical_layout.addStretch()
	
	def clear_widget_layout(self):
		"""Clears all items from the layout."""
		self.vertical_layout.clear_layout()
	
	def clear_widget_layout_by_type(self, type_to_clear: typing.Union[type, tuple[type, ...]]):
		"""
        Clears items of a specific type from the layout.

        Args:
            type_to_clear (typing.Union[type, tuple[type, ...]]): The type of items to clear.
        """
		self.vertical_layout.clear_layout_by_type(type_to_clear)
	
	def get_all_instances(self) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all widgets and layouts in the layout.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.vertical_layout.get_all_instances()
	
	def get_all_instances_of_type(self, type_to_get: typing.Union[type, tuple[type, ...]]) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all instances of a specific type in the layout.

        Args:
            type_to_get (typing.Union[type, tuple[type, ...]]): The type of instances to retrieve.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.vertical_layout.get_all_instances_of_type(type_to_get)
	
	def get_instance(self, index: int) -> typing.Any:
		"""
        Returns the instance at a given index.

        Args:
            index (int): Index of the instance.

        Returns:
            typing.Any: The instance at the given index.
        """
		return self.vertical_layout.get_instance(index)
	
	def get_number_of_instances(self) -> int:
		"""
        Returns the number of instances in the layout.

        Returns:
            int: The number of instances.
        """
		return self.vertical_layout.get_number_of_instances()
	
	def get_number_of_instances_of_type(self, type_to_check: typing.Union[type, tuple[type, ...]]) -> int:
		"""
        Returns the number of instances of a specific type.

        Args:
            type_to_check (typing.Union[type, tuple[type, ...]]): The type to check.

        Returns:
            int: The number of instances of the given type.
        """
		return self.vertical_layout.get_number_of_instances_of_type(type_to_check)
	
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		"""
        Inserts an instance at a specific index.

        Args:
            index (int): The index to insert at.
            instance (LinearLayoutItem): The instance to insert.
        """
		self.vertical_layout.insert_instance(index, instance)
	
	def remove_instance(self, instance: typing.Union[QWidget, QLayout, int, QLayoutItem]):
		"""
        Removes an instance from the layout.

        Args:
            instance (typing.Union[QWidget, QLayout, int, QLayoutItem]): The instance to remove.
        """
		self.vertical_layout.remove_instance(instance)


class PyWidgetWithHorizontalLayout(PyWidget):
	"""
    A custom widget with a horizontal layout.
    """
	
	def __init__(
			self,
			widget_with_layout_init: WidgetWithLayoutInit = WidgetWithLayoutInit(),
			instances: typing.Optional[typing.Iterable[LinearLayoutItem]] = None
	):
		"""
        Initializes a PyWidgetWithHorizontalLayout object.

        Args:
            widget_with_layout_init (WidgetWithLayoutInit): Widget and layout initialization parameters.
            instances (typing.Optional[typing.Iterable[LinearLayoutItem]]): A typing.Iterable of LinearLayoutItem objects to be added to the layout.
        """
		super().__init__(widget_init=widget_with_layout_init.widget_init)
		
		widget_with_layout_init.layout_init.parent = self
		
		self.horizontal_layout = PyHorizontalLayout(layout_init=widget_with_layout_init.layout_init, instances=instances)
		self.setLayout(self.horizontal_layout)
	
	def add_instance(self, instance: LinearLayoutItem):
		"""Adds a LinearLayoutItem to the layout.

        Args:
            instance (LinearLayoutItem): The item to add.
        """
		self.horizontal_layout.add_instance(instance)
	
	def add_stretch(self):
		"""Adds a stretch to the horizontal layout."""
		self.horizontal_layout.addStretch()
	
	def clear_widget_layout(self):
		"""Clears all items from the layout."""
		self.horizontal_layout.clear_layout()
	
	def clear_widget_layout_by_type(self, type_to_clear: typing.Union[type, tuple[type, ...]]):
		"""
        Clears items of a specific type from the layout.

        Args:
            type_to_clear (typing.Union[type, tuple[type, ...]]): The type of items to clear.
        """
		self.horizontal_layout.clear_layout_by_type(type_to_clear)
	
	def get_all_instances(self) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all widgets and layouts in the layout.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.horizontal_layout.get_all_instances()
	
	def get_all_instances_of_type(self, type_to_get: typing.Union[type, tuple[type, ...]]) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all instances of a specific type in the layout.

        Args:
            type_to_get (typing.Union[type, tuple[type, ...]]): The type of instances to retrieve.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.horizontal_layout.get_all_instances_of_type(type_to_get)
	
	def get_instance(self, index: int) -> typing.Any:
		"""
        Returns the instance at the specified index.

        Args:
            index (int): The index of the desired instance.

        Returns:
             typing.Any: The instance at the given index.
        """
		return self.horizontal_layout.get_instance(index)
	
	def get_number_of_instances(self) -> int:
		"""
        Returns the total number of instances in the layout.

        Returns:
            int: The total number of instances.

        """
		return self.horizontal_layout.get_number_of_instances()
	
	def get_number_of_instances_of_type(self, type_to_check: typing.Union[type, tuple[type, ...]]) -> int:
		"""
        Returns the number of instances of a specified type.

        Args:
            type_to_check (typing.Union[type, tuple[type, ...]]): The type of instances to count.

        Returns:
            int: The number of instances of the specified type.
        """
		return self.horizontal_layout.get_number_of_instances_of_type(type_to_check)
	
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		"""
        Inserts an instance at the specified index in the layout.

        Args:
            index (int): The index at which to insert the instance.
            instance (LinearLayoutItem): The instance to insert.
        """
		self.horizontal_layout.insert_instance(index, instance)
	
	def remove_instance(self, instance: typing.Union[QWidget, QLayout, int, QLayoutItem]):
		"""
        Removes the specified instance from the layout.

        Args:
            instance (typing.Union[QWidget, QLayout, int, QLayoutItem]): The instance to remove.
        """
		self.horizontal_layout.remove_instance(instance)


class PyWidgetWithGridLayout(PyWidget):
	"""
    A custom widget with a grid layout.
    """
	
	def __init__(
			self,
			widget_with_layout_init: WidgetWithLayoutInit = WidgetWithLayoutInit(),
			instances: typing.Optional[typing.Iterable[GridLayoutItem]] = None,
			# Corrected type hint
	):
		"""
        Initializes a PyWidgetWithGridLayout object.

        Args:
            widget_with_layout_init (WidgetWithLayoutInit): Widget and layout initialization parameters.
            instances (typing.Optional[typing.Iterable[GridLayoutItem]]): A typing.Iterable of GridLayoutItem objects to be added to the layout.
        """
		super().__init__(widget_init=widget_with_layout_init.widget_init)
		
		widget_with_layout_init.layout_init.parent = self
		
		self.grid_layout = GridLayout(layout_init=widget_with_layout_init.layout_init, instances=instances)
		self.setLayout(self.grid_layout)
	
	def add_instance(self, instance: GridLayoutItem):
		"""Adds a GridLayoutItem to the layout.

        Args:
            instance (GridLayoutItem): The item to add.
        """
		self.grid_layout.add_instance(instance)
	
	def clear_widget_layout(self):
		"""Clears all items from the layout."""
		self.grid_layout.clear_layout()
	
	def clear_widget_layout_by_type(self, type_to_clear: typing.Union[type, tuple[type, ...]]):
		"""
        Clears items of a specific type from the layout.

        Args:
            type_to_clear (typing.Union[type, tuple[type, ...]]): The type of items to clear.
        """
		self.grid_layout.clear_layout_by_type(type_to_clear)
	
	def get_all_instances(self) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all widgets and layouts in the layout.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.grid_layout.get_all_instances()
	
	def get_all_instances_of_type(self, type_to_get: typing.Union[type, tuple[type, ...]]) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all instances of a specific type in the layout.

        Args:
            type_to_get (typing.Union[type, tuple[type, ...]]): The type of instances to retrieve.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.grid_layout.get_all_instances_of_type(type_to_get)
	
	def get_instance(self, index: int) -> typing.Any:
		"""
        Returns the instance at a given index.

        Args:
            index (int): Index of the instance.

        Returns:
            typing.Any: The instance at the given index.
        """
		return self.grid_layout.get_instance(index)
	
	def get_number_of_instances(self) -> int:
		"""
        Returns the number of instances in the layout.

        Returns:
            int: The number of instances.
        """
		return self.grid_layout.get_number_of_instances()
	
	def get_number_of_instances_of_type(self, type_to_check: typing.Union[type, tuple[type, ...]]) -> int:
		"""
        Returns the number of instances of a specific type.

        Args:
            type_to_check (typing.Union[type, tuple[type, ...]]): The type to check.

        Returns:
            int: The number of instances of the given type.
        """
		return self.grid_layout.get_number_of_instances_of_type(type_to_check)
	
	def remove_instance(self, instance: typing.Union[QWidget, QLayout, int, QLayoutItem]):
		"""
        Removes an instance from the layout.

        Args:
            instance (typing.Union[QWidget, QLayout, int, QLayoutItem]): The instance to remove.
        """
		self.grid_layout.remove_instance(instance)

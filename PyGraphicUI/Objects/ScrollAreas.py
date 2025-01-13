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
	QScrollArea,
	QSizePolicy,
	QWidget
)
from PyGraphicUI.Objects.Widgets import (
	PyWidget,
	PyWidgetWithGridLayout,
	PyWidgetWithHorizontalLayout,
	PyWidgetWithVerticalLayout,
	WidgetInit,
	WidgetWithLayoutInit
)


class ScrollAreaInit(WidgetInit):
	"""
    Data class to hold initialization parameters for scroll areas.

    Attributes:
        name (str): The object name of the scroll area. Defaults to "scroll_area".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the scroll area is enabled. Defaults to True.
        visible (bool): Whether the scroll area is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the scroll area. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the scroll area. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the scroll area. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the scroll area. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the scroll area. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the scroll area. Defaults to None.
        vertical_scroll_bar_policy (Qt.ScrollBarPolicy): The vertical scroll bar policy. Defaults to Qt.ScrollBarPolicy.ScrollBarAsNeeded.
        horizontal_scroll_bar_policy (Qt.ScrollBarPolicy): The horizontal scroll bar policy. Defaults to Qt.ScrollBarPolicy.ScrollBarAsNeeded.
        central_widget_init (WidgetWithLayoutInit): Initialization parameters for the central widget. Defaults to a default WidgetWithLayoutInit object.
    """
	
	def __init__(
			self,
			name: str = "scroll_area",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			vertical_scroll_bar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAsNeeded,
			horizontal_scroll_bar_policy: Qt.ScrollBarPolicy = Qt.ScrollBarPolicy.ScrollBarAsNeeded,
			central_widget_init: WidgetWithLayoutInit = WidgetWithLayoutInit()
	):
		"""
        Initializes a ScrollAreaInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the scroll area is enabled.
            visible (bool): Whether the scroll area is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            vertical_scroll_bar_policy (Qt.ScrollBarPolicy): The vertical scroll bar policy.
            horizontal_scroll_bar_policy (Qt.ScrollBarPolicy): The horizontal scroll bar policy.
            central_widget_init (WidgetWithLayoutInit): Initialization parameters for the central widget.
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
		
		self.vertical_scroll_bar_policy = vertical_scroll_bar_policy
		self.horizontal_scroll_bar_policy = horizontal_scroll_bar_policy
		self.central_widget_init = central_widget_init


class PyVerticalScrollArea(QScrollArea, PyWidget):
	"""
    A custom vertical scroll area.
    """
	
	def __init__(
			self,
			scroll_area_init: ScrollAreaInit = ScrollAreaInit(),
			instances: typing.Optional[typing.Iterable[LinearLayoutItem]] = None
	):
		"""
        Initializes a PyVerticalScrollArea.

        Args:
            scroll_area_init (ScrollAreaInit): Scroll area initialization parameters.
            instances (typing.Optional[typing.Iterable[LinearLayoutItem]]): A typing.Iterable of items to add to the scroll area content. Defaults to None.
        """
		super().__init__(widget_init=scroll_area_init)
		
		self.horizontal_scroll = PyWidgetWithHorizontalLayout(
				widget_with_layout_init=WidgetWithLayoutInit(widget_init=WidgetInit(parent=self))
		)
		scroll_area_init.central_widget_init.widget_init.parent = self.horizontal_scroll
		
		self.vertical_scroll = PyWidgetWithVerticalLayout(
				widget_with_layout_init=scroll_area_init.central_widget_init,
				instances=instances
		)
		self.horizontal_scroll.add_instance(LinearLayoutItem(self.vertical_scroll))
		self.setHorizontalScrollBarPolicy(scroll_area_init.horizontal_scroll_bar_policy)
		self.setVerticalScrollBarPolicy(scroll_area_init.vertical_scroll_bar_policy)
		self.setWidget(self.horizontal_scroll)
		self.setWidgetResizable(True)
	
	def add_instance(self, instance: LinearLayoutItem):
		"""
        Adds a widget to the scroll area's vertical layout.

        Args:
            instance (LinearLayoutItem): The item to add.
        """
		self.vertical_scroll.add_instance(instance)
	
	def clear_scroll_area(self):
		"""Clears all widgets from the scroll area."""
		self.vertical_scroll.clear_widget_layout()
	
	def clear_scroll_area_by_type(self, type_to_clear: typing.Union[type, tuple[type, ...]]):
		"""
        Clears widgets of the specified type from the scroll area.

        Args:
            type_to_clear (typing.Union[type, tuple[type, ...]]): The type of widgets to clear.
        """
		self.vertical_scroll.clear_widget_layout_by_type(type_to_clear)
	
	def get_all_instances(self) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all widgets and layouts within the scrollable area.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator yielding each widget and layout.
        """
		return self.vertical_scroll.get_all_instances()
	
	def get_instance(self, index: int) -> typing.Any:
		"""
        Returns the widget at the given index in the scrollable area.

        Args:
            index (int): The index of the widget to retrieve.

        Returns:
            typing.Any: The widget at the specified index, or None if the index is out of range.
        """
		return self.vertical_scroll.get_instance(index)
	
	def get_number_of_instances(self) -> int:
		"""
        Returns the number of widgets in the scrollable area.

        Returns:
            int: The total number of widgets currently in the scrollable area.
        """
		return self.vertical_scroll.get_number_of_instances()
	
	def get_number_of_instances_of_type(self, type_to_check: typing.Union[type, tuple[type, ...]]) -> int:
		"""
        Returns the number of instances of a specific type within the vertical scroll area.

        Args:
            type_to_check (typing.Union[type, tuple[type, ...]]): The type of widget or layout to count.

        Returns:
            int: The number of instances of the specified type found within the vertical scroll area.
        """
		return self.vertical_scroll.get_number_of_instances_of_type(type_to_check)

	def get_all_instances_of_type(self, type_to_get: typing.Union[type, tuple[type, ...]]) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all instances of a specific type in the vertical scroll area.

        Args:
            type_to_get (typing.Union[type, tuple[type, ...]]): The type of instances to retrieve.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.vertical_scroll.get_all_instances_of_type(type_to_get)
	
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		"""
        Inserts a widget at a specific index in the scrollable area's vertical layout.

        Args:
            index (int): The index at which to insert the widget.
            instance (LinearLayoutItem): The widget to insert. The widget must not already be in a layout.

        Raises:
            TypeError: If the provided widget is already managed by a layout.
        """
		self.vertical_scroll.insert_instance(index, instance)
	
	def remove_instance(self, instance: typing.Union[QWidget, QLayout, int, QLayoutItem]):
		"""
        Removes a widget or layout item from the scroll area's layout.

        Args:
            instance: The widget, layout item, or index of the item to remove.
        """
		self.vertical_scroll.remove_instance(instance)


class PyHorizontalScrollArea(QScrollArea, PyWidget):
	"""
    A custom horizontal scroll area.
    """
	
	def __init__(
			self,
			scroll_area_init: ScrollAreaInit = ScrollAreaInit(),
			instances: typing.Optional[typing.Iterable[LinearLayoutItem]] = None
	):
		"""
        Initializes a PyHorizontalScrollArea.

        Args:
            scroll_area_init (ScrollAreaInit): Scroll area initialization parameters.
            instances (typing.Optional[typing.Iterable[LinearLayoutItem]]): A typing.Iterable of items to add to the scroll area's content. Defaults to None.
        """
		super().__init__(widget_init=scroll_area_init)
		
		self.vertical_layout = PyWidgetWithVerticalLayout(
				widget_with_layout_init=WidgetWithLayoutInit(widget_init=WidgetInit(parent=self))
		)
		scroll_area_init.central_widget_init.widget_init.parent = self.vertical_layout
		
		self.horizontal_scroll = PyWidgetWithHorizontalLayout(
				widget_with_layout_init=scroll_area_init.central_widget_init,
				instances=instances
		)
		self.vertical_layout.add_instance(LinearLayoutItem(self.horizontal_scroll))
		self.setHorizontalScrollBarPolicy(scroll_area_init.horizontal_scroll_bar_policy)
		self.setVerticalScrollBarPolicy(scroll_area_init.vertical_scroll_bar_policy)
		self.setWidget(self.vertical_layout)
		self.setWidgetResizable(True)
	
	def add_instance(self, instance: LinearLayoutItem):
		"""
        Adds an instance to the horizontal layout within the scroll area.

        Args:
            instance (LinearLayoutItem): The instance to add to the layout.
        """
		self.horizontal_scroll.add_instance(instance)
	
	def clear_scroll_area(self):
		"""Clears all widgets from the horizontal layout within the scroll area."""
		self.horizontal_scroll.clear_widget_layout()
	
	def clear_scroll_area_by_type(self, type_to_clear: typing.Union[type, tuple[type, ...]]):
		"""
        Clears widgets of a specific type from the horizontal layout within the scroll area.

        Args:
            type_to_clear (typing.Union[type, tuple[type, ...]]): The type of widgets to clear.
        """
		self.horizontal_scroll.clear_widget_layout_by_type(type_to_clear)
	
	def get_all_instances(self) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all widgets and layouts in the scroll area.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.horizontal_scroll.get_all_instances()
	
	def get_instance(self, index: int) -> typing.Any:
		"""
        Returns the instance at the specified index.

        Args:
            index (int): The index of the instance to retrieve.

        Returns:
            typing.Any: The instance at the given index, or None if the index is out of range.
        """
		return self.horizontal_scroll.get_instance(index)
	
	def get_number_of_instances(self) -> int:
		"""
        Returns the number of instances in the horizontal layout.

        Returns:
            int: The number of instances in the layout.
        """
		return self.horizontal_scroll.get_number_of_instances()
	
	def get_number_of_instances_of_type(self, type_to_check: typing.Union[type, tuple[type, ...]]) -> int:
		"""
        Returns the number of instances of a specific type in the horizontal scroll area.

        Args:
            type_to_check (typing.Union[type, tuple[type, ...]]): The type of instance to count.

        Returns:
            int: The number of instances of the specified type in the horizontal layout.
        """
		return self.horizontal_scroll.get_number_of_instances_of_type(type_to_check)

	def get_all_instances_of_type(self, type_to_get: typing.Union[type, tuple[type, ...]]) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all instances of a specific type in the horizontal scroll area.

        Args:
            type_to_get (typing.Union[type, tuple[type, ...]]): The type of instances to retrieve.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.horizontal_scroll.get_all_instances_of_type(type_to_get)
	
	def insert_instance(self, index: int, instance: LinearLayoutItem):
		"""
		Inserts an instance at the specified index in the horizontal scroll area.

        Args:
            index (int): The index at which to insert the instance.
            instance (LinearLayoutItem): The instance to be added to the layout.
        """
		self.horizontal_scroll.insert_instance(index, instance)
	
	def remove_instance(self, instance: typing.Union[QWidget, QLayout, int, QLayoutItem]):
		"""
        Removes the specified instance from the horizontal scroll area.

        Args:
            instance (typing.Union[QWidget, QLayout, int, QLayoutItem]): The instance to be removed from the layout.
        """
		self.horizontal_scroll.remove_instance(instance)


class PyGridScrollArea(QScrollArea, PyWidget):
	"""A custom scroll area with a grid layout."""
	
	def __init__(
			self,
			scroll_area_init: ScrollAreaInit = ScrollAreaInit(),
			instances: typing.Optional[typing.Iterable[GridLayoutItem]] = None
	):
		"""
        Initializes a PyGridScrollArea.

        Args:
            scroll_area_init (ScrollAreaInit): Scroll area initialization parameters.
            instances (typing.Optional[typing.Iterable[GridLayoutItem]]): A typing.Iterable of GridLayoutItems to add to the scroll area content. Defaults to None.
        """
		super().__init__(widget_init=scroll_area_init)
		
		vertical_scroll = PyWidgetWithVerticalLayout(
				# Create a separate vertical layout widget widget_with_layout_init=WidgetWithLayoutInit(widget_init=WidgetInit(parent=self))
		)
		scroll_area_init.central_widget_init.widget_init.parent = vertical_scroll
		
		self.grid_scroll = PyWidgetWithGridLayout(
				widget_with_layout_init=scroll_area_init.central_widget_init,
				instances=instances
		)
		vertical_scroll.add_instance(LinearLayoutItem(self.grid_scroll))
		self.setHorizontalScrollBarPolicy(scroll_area_init.horizontal_scroll_bar_policy)
		self.setVerticalScrollBarPolicy(scroll_area_init.vertical_scroll_bar_policy)
		self.setWidget(vertical_scroll)  # Directly use vertical_scroll
		self.setWidgetResizable(True)
	
	def add_instance(self, instance: GridLayoutItem):
		"""
        Adds a GridLayoutItem to the grid layout within the scroll area.

        Args:
            instance (GridLayoutItem): The GridLayoutItem to add.
        """
		self.grid_scroll.add_instance(instance)
	
	def clear_scroll_area(self):
		"""Clears all items from the grid layout within the scroll area."""
		self.grid_scroll.clear_widget_layout()
	
	def clear_scroll_area_by_type(self, type_to_clear: typing.Union[type, tuple[type, ...]]):
		"""
        Clears items of a specific type from the grid layout within the scroll area.

        Args:
            type_to_clear (typing.Union[type, tuple[type, ...]]): The type of items to clear.
        """
		self.grid_scroll.clear_widget_layout_by_type(type_to_clear)
	
	def get_all_instances(self) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator for all instances in the grid layout within the scroll area.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator that yields all widget and layout instances.
        """
		return self.grid_scroll.get_all_instances()
	
	def get_instance(self, index: int) -> typing.Any:
		"""
        Returns the instance at the specified index in the grid scroll area.

        Args:
            index (int): The index of the instance to retrieve.

        Returns:
            typing.Any: The instance at the specified index or None if the index is out of range.
        """
		return self.grid_scroll.get_instance(index)
	
	def get_number_of_instances(self) -> int:
		"""
        Returns the number of instances in the grid layout.

        Returns:
            int: The number of instances.
        """
		return self.grid_scroll.get_number_of_instances()

	def get_all_instances_of_type(self, type_to_get: typing.Union[type, tuple[type, ...]]) -> typing.Generator[typing.Any, typing.Any, None]:
		"""
        Returns a generator of all instances of a specific type in the grid scroll area.

        Args:
            type_to_get (typing.Union[type, tuple[type, ...]]): The type of instances to retrieve.

        Returns:
            typing.Generator[typing.Any, typing.Any, None]: A generator of all widgets and layouts.
        """
		return self.grid_scroll.get_all_instances_of_type(type_to_get)
	
	def get_number_of_instances_of_type(self, type_to_check: typing.Union[type, tuple[type, ...]]) -> int:
		"""
        Returns the number of instances of a specific type in the grid scroll area.

        Args:
            type_to_check (typing.Union[type, tuple[type, ...]]): The type of instance to count.

        Returns:
            int: The number of instances of the given type.
        """
		return self.grid_scroll.get_number_of_instances_of_type(type_to_check)
	
	def remove_instance(self, instance: typing.Union[QWidget, QLayout, int, QLayoutItem]):
		"""
        Removes an instance from the grid layout within the scroll area.

        Args:
            instance (typing.Union[QWidget, QLayout, int, QLayoutItem]): The instance to remove. Can be a widget, layout, index, or layout item.
        """
		self.grid_scroll.remove_instance(instance)

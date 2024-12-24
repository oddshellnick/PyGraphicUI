import typing

from PyQt6.QtWidgets import (
    QDialog,
    QGraphicsEffect,
    QLayout,
    QLayoutItem,
    QSizePolicy,
    QWidget,
)

from PyGraphicUI.Attributes import GridLayoutItem, LinearLayoutItem, ObjectSize
from PyGraphicUI.Objects.Layouts import (
    GridLayout,
    LayoutInit,
    PyHorizontalLayout,
    PyVerticalLayout,
)
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit


class DialogInit(WidgetInit):
    """
    Data class to hold initialization parameters for dialogs.

    Attributes:
        title (str): The title of the dialog. Defaults to "dialog".
        name (str): The object name of the dialog. Defaults to "dialog".
        parent (QWidget | None): The parent widget. Defaults to None.
        enabled (bool): Whether the dialog is enabled. Defaults to True.
        visible (bool): Whether the dialog is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the dialog. Defaults to "".
        minimum_size (ObjectSize | None): The minimum size of the dialog. Defaults to None.
        maximum_size (ObjectSize | None): The maximum size of the dialog. Defaults to None.
        fixed_size (ObjectSize | None): The fixed size of the dialog. Defaults to None.
        size_policy (QSizePolicy | None): The size policy of the dialog. Defaults to None.
        graphic_effect (QGraphicsEffect | None): The graphic effect to apply to the dialog. Defaults to None.
    """

    def __init__(
        self,
        title: str = "dialog",
        name: str = "dialog",
        parent: QWidget | None = None,
        enabled: bool = True,
        visible: bool = True,
        style_sheet: str = "",
        minimum_size: ObjectSize | None = None,
        maximum_size: ObjectSize | None = None,
        fixed_size: ObjectSize | None = None,
        size_policy: QSizePolicy | None = None,
        graphic_effect: QGraphicsEffect | None = None,
    ):
        """Initializes a DialogInit object.

        Args:
            title (str): The title of the dialog.
            name (str): The object name.
            parent (QWidget | None): The parent widget.
            enabled (bool): Whether the dialog is enabled.
            visible (bool): Whether the dialog is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (ObjectSize | None): The minimum size.
            maximum_size (ObjectSize | None): The maximum size.
            fixed_size (ObjectSize | None): The fixed size.
            size_policy (QSizePolicy | None): The size policy.
            graphic_effect (QGraphicsEffect | None): The graphic effect.
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
            graphic_effect,
        )

        self.title = title


class PyDialog(QDialog, PyWidget):
    """
    A custom dialog class inheriting from QDialog and PyWidget.
    """

    def __init__(self, dialog_init: DialogInit = DialogInit()):
        """Initializes a PyDialog object.

        Args:
            dialog_init (DialogInit): Initialization parameters for the dialog.
        """
        super().__init__(widget_init=dialog_init)

        self.setWindowTitle(dialog_init.title)


class DialogWithLayoutInit:
    """
    Data class to hold initialization parameters for dialogs with layouts.


    Attributes:
        dialog_init (DialogInit): Initialization parameters for the dialog.
        layout_init (LayoutInit): Initialization parameters for the layout.
    """

    def __init__(self, dialog_init: DialogInit = DialogInit(), layout_init: LayoutInit = LayoutInit()):
        """
        Initializes a DialogWithLayoutInit object.

        Args:
            dialog_init (DialogInit): Dialog initialization parameters.
            layout_init (LayoutInit): Layout initialization parameters.
        """
        self.dialog_init = dialog_init
        self.layout_init = layout_init


class PyDialogWithVerticalLayout(PyDialog):
    """
    A custom dialog with a vertical layout.
    """

    def __init__(
        self,
        dialog_with_layout_init: DialogWithLayoutInit = DialogWithLayoutInit(),
        instances: list[LinearLayoutItem] | None = None,
    ):
        """Initializes a PyDialogWithVerticalLayout object.


        Args:
            dialog_with_layout_init (DialogWithLayoutInit): Dialog and layout
                initialization parameters.
            instances (list[LinearLayoutItem] | None): A list of LinearLayoutItem
                objects to be added to the layout. Defaults to None.
        """
        super().__init__(dialog_init=dialog_with_layout_init.dialog_init)

        dialog_with_layout_init.layout_init.parent = self

        self.vertical_layout = PyVerticalLayout(layout_init=dialog_with_layout_init.layout_init, instances=instances)
        self.setLayout(self.vertical_layout)

    def add_instance(self, instance: LinearLayoutItem):
        """Adds a LinearLayoutItem to the layout.

        Args:
            instance (LinearLayoutItem): The item to add.
        """
        self.vertical_layout.add_instance(instance)

    def clear_dialog_layout(self):
        """Clears all items from the layout."""
        self.vertical_layout.clear_layout()

    def clear_dialog_layout_by_type(self, type_to_clear: type):
        """Clears items of a specific type from the layout.

        Args:
            type_to_clear (type): The type of items to clear.
        """
        self.vertical_layout.clear_layout_by_type(type_to_clear)

    def get_all_instances(self) -> typing.Generator[QWidget | QLayout, typing.Any, None]:
        """Returns a generator of all widgets and layouts in the layout.


        Returns:
            typing.Generator[QWidget | QLayout, typing.Any, None]: A generator of
                all widgets and layouts.
        """
        return self.vertical_layout.get_all_instances()

    def get_all_instances_of_type(self, type_to_get: type) -> typing.Generator[QWidget | QLayout, typing.Any, None]:
        """Returns a generator of all instances of a specific type in the layout.

        Args:
            type_to_get (type): The type of instances to retrieve.

        Returns:
            typing.Generator[QWidget | QLayout, typing.Any, None]: A generator of all widgets and layouts.
        """
        return self.vertical_layout.get_all_instances_of_type(type_to_get)

    def get_instance(self, index: int) -> QWidget | QLayout:
        """Returns the instance at a given index.

        Args:
            index (int): Index of the instance.

        Returns:
            QWidget | QLayout: The instance at the given index.
        """
        return self.vertical_layout.get_instance(index)

    def get_number_of_instances(self) -> int:
        """Returns the number of instances in the layout.

        Returns:
            int: The number of instances.
        """
        return self.vertical_layout.get_number_of_instances()

    def get_number_of_instances_of_type(self, type_to_check: type) -> int:
        """Returns the number of instances of a specific type.

        Args:
            type_to_check (type): The type to check.

        Returns:
            int: The number of instances of the given type.
        """
        return self.vertical_layout.get_number_of_instances_of_type(type_to_check)

    def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
        """Removes an instance from the layout.

        Args:
            instance (QWidget | QLayout | int | QLayoutItem): The instance to
                remove.
        """
        self.vertical_layout.remove_instance(instance)


class PyDialogWithHorizontalLayout(PyDialog):
    """A custom dialog with a horizontal layout."""

    def __init__(
        self,
        dialog_with_layout_init: DialogWithLayoutInit = DialogWithLayoutInit(),
        instances: list[LinearLayoutItem] | None = None,
    ):
        """Initializes a PyDialogWithHorizontalLayout object.

        Args:
            dialog_with_layout_init (DialogWithLayoutInit): Dialog and layout initialization parameters.
            instances (list[LinearLayoutItem] | None): A list of LinearLayoutItem objects to be added to the layout. Defaults to None.
        """
        super().__init__(dialog_init=dialog_with_layout_init.dialog_init)

        dialog_with_layout_init.layout_init.parent = self

        self.horizontal_layout = PyHorizontalLayout(
            layout_init=dialog_with_layout_init.layout_init, instances=instances
        )
        self.setLayout(self.horizontal_layout)

    def add_instance(self, instance: LinearLayoutItem):
        """Adds a LinearLayoutItem to the layout.

        Args:
            instance (LinearLayoutItem): The item to add.
        """
        self.horizontal_layout.add_instance(instance)

    def clear_dialog_layout(self):
        """Clears all items from the layout."""
        self.horizontal_layout.clear_layout()

    def clear_dialog_layout_by_type(self, type_to_clear: type):
        """Clears items of a specific type from the layout.

        Args:
            type_to_clear (type): The type of items to clear.
        """
        self.horizontal_layout.clear_layout_by_type(type_to_clear)

    def get_all_instances(self) -> typing.Generator[QWidget | QLayout, typing.Any, None]:
        """
        Returns a generator of all widgets and layouts in the layout.

        Returns:
            typing.Generator[QWidget | QLayout, typing.Any, None]: A generator of all widgets and layouts.
        """
        return self.horizontal_layout.get_all_instances()

    def get_all_instances_of_type(self, type_to_get: type) -> typing.Generator[QWidget | QLayout, typing.Any, None]:
        """
        Returns a generator of all instances of a specific type in the layout.

        Args:
            type_to_get (type): The type of instances to retrieve.

        Returns:
            typing.Generator[QWidget | QLayout, typing.Any, None]: A generator of instances of the specified type.
        """
        return self.horizontal_layout.get_all_instances_of_type(type_to_get)

    def get_instance(self, index: int) -> QWidget | QLayout:
        """Returns the instance at a given index.

        Args:
            index (int): Index of the instance.

        Returns:
            QWidget | QLayout: The instance at the given index.
        """
        return self.horizontal_layout.get_instance(index)

    def get_number_of_instances(self) -> int:
        """Returns the number of instances in the layout.

        Returns:
            int: The number of instances.
        """
        return self.horizontal_layout.get_number_of_instances()

    def get_number_of_instances_of_type(self, type_to_check: type) -> int:
        """Returns the number of instances of a specific type.

        Args:
            type_to_check (type): The type to check.

        Returns:
            int: The number of instances of the given type.
        """
        return self.horizontal_layout.get_number_of_instances_of_type(type_to_check)

    def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
        """Removes an instance from the layout.

        Args:
            instance (QWidget | QLayout | int | QLayoutItem): The instance to remove.
        """
        self.horizontal_layout.remove_instance(instance)


class PyDialogWithGridLayout(PyDialog):
    """
    A custom dialog with a grid layout.
    """

    def __init__(
        self,
        dialog_with_layout_init: DialogWithLayoutInit = DialogWithLayoutInit(),
        instances: list[GridLayoutItem] | None = None,  # Corrected type hint
    ):
        """
        Initializes a PyDialogWithGridLayout object.

        Args:
            dialog_with_layout_init (DialogWithLayoutInit): Dialog and layout initialization parameters.
            instances (list[GridLayoutItem] | None): A list of GridLayoutItem objects to be added to the layout. Defaults to None.
        """
        super().__init__(dialog_init=dialog_with_layout_init.dialog_init)

        dialog_with_layout_init.layout_init.parent = self

        self.grid_layout = GridLayout(layout_init=dialog_with_layout_init.layout_init, instances=instances)
        self.setLayout(self.grid_layout)

    def add_instance(self, instance: GridLayoutItem):
        """Adds a GridLayoutItem to the layout.

        Args:
            instance (GridLayoutItem): The item to add.
        """
        self.grid_layout.add_instance(instance)

    def clear_dialog_layout(self):
        """Clears all items from the layout."""
        self.grid_layout.clear_layout()

    def clear_dialog_layout_by_type(self, type_to_clear: type):
        """
        Clears items of a specific type from the layout.

        Args:
            type_to_clear (type): The type of items to clear.
        """
        self.grid_layout.clear_layout_by_type(type_to_clear)

    def get_all_instances(self) -> typing.Generator[QWidget | QLayout, typing.Any, None]:
        """
        Returns a generator of all widgets and layouts in the layout.

        Returns:
            typing.Generator[QWidget | QLayout, typing.Any, None]: A generator of all widgets and layouts.
        """
        return self.grid_layout.get_all_instances()

    def get_all_instances_of_type(self, type_to_get: type) -> typing.Generator[QWidget | QLayout, typing.Any, None]:
        """
        Returns a generator of all instances of a specific type in the layout.

        Args:
            type_to_get (type): The type of instances to retrieve.

        Returns:
            typing.Generator[QWidget | QLayout, typing.Any, None]:  A generator of all instances of a specific type.
        """
        return self.grid_layout.get_all_instances_of_type(type_to_get)

    def get_instance(self, index: int) -> QWidget | QLayout:
        """
        Returns the instance at a given index.

        Args:
            index (int): The index of the desired instance.

        Returns:
            QWidget | QLayout: The instance at the given index.

        """
        return self.grid_layout.get_instance(index)

    def get_number_of_instances(self) -> int:
        """
        Returns the number of instances in the layout.


        Returns:
            int: The number of instances.
        """
        return self.grid_layout.get_number_of_instances()

    def get_number_of_instances_of_type(self, type_to_check: type) -> int:
        """
        Returns the number of instances of a specific type.

        Args:
            type_to_check (type): The type to check for.

        Returns:
            int: The number of instances of the specified type.
        """
        return self.grid_layout.get_number_of_instances_of_type(type_to_check)

    def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
        """
        Removes an instance from the layout.

        Args:
            instance (QWidget | QLayout | int | QLayoutItem): The instance to be removed.
        """
        self.grid_layout.remove_instance(instance)

from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import GridLayoutItem, LinearLayoutItem
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLayout, QLayoutItem, QVBoxLayout, QWidget
#
#
#
#
class PyLayout(QLayout):
    def get_instance(self, index: int):
        return self.itemAt(index).widget()
    #
    #
    #
    #
    def remove_instance(self, instance: QWidget | QLayout | int | QLayoutItem):
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
    #
    #
    #
    #
    def clear_layout(self):
        for i in reversed(range(self.count())):
            self.remove_instance(i)
    #
    #
    #
    #
    def clear_layout_by_type(self, type_to_clear):
        for i in reversed(range(self.count())):
            if isinstance(self.get_instance(i), type_to_clear):
                self.remove_instance(i)
    #
    #
    #
    #
    def get_all_instances(self):
        for i in range(self.count()):
            yield self.get_instance(i)
    #
    #
    #
    #
    def get_all_instances_of_type(self, type_to_get):
        for i in range(self.count()):
            if isinstance(self.get_instance(i), type_to_get):
                yield self.get_instance(i)
    #
    #
    #
    #
    def get_number_of_instances(self):
        return self.count()
    #
    #
    #
    #
    def get_number_of_instances_of_type(self, type_to_check):
        return sum(1 for i in range(self.count()) if isinstance(self.get_instance(i), type_to_check))
#
#
#
#
class LayoutInit:
    def __init__(
            self,
            name: str = "layout",
            parent: QWidget = None,
            enabled: bool = True,
            alignment: Qt.AlignmentFlag = None,
            contents_margins: list[int] = None,
            spacing: int = 0,
    ):
        self.name = name
        self.parent = parent
        self.enabled = enabled
        self.alignment = alignment
        self.contents_margins = contents_margins
        self.spacing = spacing
#
#
#
#
class PyVerticalLayout(QVBoxLayout, PyLayout):
    def __init__(
            self,
            layout_init: LayoutInit = LayoutInit(),
            instances: list[LinearLayoutItem] = None
    ):
        if layout_init.parent is None:
            super().__init__()
        else:
            super().__init__(layout_init.parent)
        #
        #
        #
        #
        self.setEnabled(layout_init.enabled)
        self.setObjectName(layout_init.name)
        self.setSpacing(layout_init.spacing)
        #
        #
        #
        #
        if layout_init.alignment is not None:
            self.setAlignment(layout_init.alignment)
        #
        #
        #
        #
        if layout_init.contents_margins is not None:
            self.setContentsMargins(*layout_init.contents_margins)
        else:
            self.setContentsMargins(0, 0, 0, 0)
        #
        #
        #
        #
        if instances is not None:
            for instance in instances:
                self.add_instance(instance)
    #
    #
    #
    #
    def add_instance(self, instance: LinearLayoutItem):
        parameters = [instance.instance, instance.stretch]

        if instance.alignment is not None:
            parameters.append(instance.alignment)

        try:
            self.addWidget(*parameters)
        except TypeError:
            self.addLayout(*parameters)
    #
    #
    #
    #
    def insert_instance(self, index: int, instance: LinearLayoutItem):
        parameters = [instance.instance, instance.stretch]

        if instance.alignment is not None:
            parameters.append(instance.alignment)

        try:
            self.insertWidget(index, *parameters)
        except TypeError:
            self.insertLayout(index, *parameters)
#
#
#
#
class PyHorizontalLayout(QHBoxLayout, PyLayout):
    def __init__(
            self,
            layout_init: LayoutInit = LayoutInit(),
            instances: list[LinearLayoutItem] = None
    ):
        if layout_init.parent is None:
            super().__init__()
        else:
            super().__init__(layout_init.parent)
        #
        #
        #
        #
        self.setEnabled(layout_init.enabled)
        self.setObjectName(layout_init.name)
        self.setSpacing(layout_init.spacing)
        #
        #
        #
        #
        if layout_init.alignment is not None:
            self.setAlignment(layout_init.alignment)
        #
        #
        #
        #
        if layout_init.contents_margins is not None:
            self.setContentsMargins(*layout_init.contents_margins)
        else:
            self.setContentsMargins(0, 0, 0, 0)
        #
        #
        #
        #
        if instances is not None:
            for instance in instances:
                self.add_instance(instance)
    #
    #
    #
    #
    def add_instance(self, instance: LinearLayoutItem):
        parameters = [instance.instance, instance.stretch]

        if instance.alignment is not None:
            parameters.append(instance.alignment)

        try:
            self.addWidget(*parameters)
        except TypeError:
            self.addLayout(*parameters)
    #
    #
    #
    #
    def insert_instance(self, index: int, instance: LinearLayoutItem):
        parameters = [instance.instance, instance.stretch]

        if instance.alignment is not None:
            parameters.append(instance.alignment)

        try:
            self.insertWidget(index, *parameters)
        except TypeError:
            self.insertLayout(index, *parameters)
#
#
#
#
class GridLayout(QGridLayout, PyLayout):
    def __init__(
            self,
            layout_init: LayoutInit = LayoutInit(),
            instances: list[GridLayoutItem] = None
    ):
        if layout_init.parent is None:
            super().__init__()
        else:
            super().__init__(layout_init.parent)
        #
        #
        #
        #
        self.setEnabled(layout_init.enabled)
        self.setObjectName(layout_init.name)
        self.setSpacing(layout_init.spacing)
        #
        #
        #
        #
        if layout_init.alignment is not None:
            self.setAlignment(layout_init.alignment)
        #
        #
        #
        #
        if layout_init.contents_margins is not None:
            self.setContentsMargins(*layout_init.contents_margins)
        else:
            self.setContentsMargins(0, 0, 0, 0)
        #
        #
        #
        #
        if instances is not None:
            for instance in instances:
                self.add_instance(instance)
    #
    #
    #
    #
    def add_instance(self, instance: GridLayoutItem):
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

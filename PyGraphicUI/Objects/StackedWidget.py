import typing
from PyGraphicUI.Attributes import ObjectSize
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QSizePolicy,
	QStackedWidget,
	QWidget
)


class StackedWidgetInit(WidgetInit):
	"""
    Data class to hold initialization parameters for stacked widgets.

    Attributes:
        name (str): The object name of the stacked widget. Defaults to "stacked_widget".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the stacked widget is enabled. Defaults to True.
        visible (bool): Whether the stacked widget is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the stacked widget. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the stacked widget. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the stacked widget. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the stacked widget. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the stacked widget. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the stacked widget. Defaults to None.
    """
	
	def __init__(
			self,
			name: str = "stacked_widget",
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
        Initializes a StackedWidgetInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the stacked widget is enabled.
            visible (bool): Whether the stacked widget is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
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


class PyStackedWidget(QStackedWidget, PyWidget):
	"""
    A custom stacked widget class.
    """
	
	def __init__(
			self,
			stacked_widget_init: StackedWidgetInit = StackedWidgetInit(),
			stacked_widget_instances: typing.Optional[typing.Iterable[QWidget]] = None
	):
		"""
        Initializes a PyStackedWidget object.

        Args:
            stacked_widget_init (StackedWidgetInit): Initialization parameters.
            stacked_widget_instances (typing.Optional[typing.Iterable[QWidget]]): A typing.Iterable of widgets to add to the stack. Defaults to None.
        """
		super().__init__(widget_init=stacked_widget_init)
		
		if stacked_widget_instances is not None:
			self.add_widgets(stacked_widget_instances)
	
	def add_widgets(self, instances: typing.Union[typing.Iterable[QWidget]]):
		"""
        Adds widgets to the stacked widget.

        Args:
            instances: A single widget or a typing.Iterable of widgets to add.
        """
		if isinstance(instances, typing.Iterable):
			for instance in instances:
				self.addWidget(instance)
		elif isinstance(instances, QWidget):
			self.addWidget(instances)
	
	def clear_stacked_widget(self) -> None:
		"""Removes all widgets from the stacked widget."""
		for _ in range(self.count()):
			self.setCurrentIndex(0)
			self.removeWidget(self.currentWidget())

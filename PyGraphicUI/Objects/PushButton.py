import typing
from PyQt6.QtCore import (
	QTimer,
	Qt,
	pyqtSignal
)
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QPushButton,
	QSizePolicy,
	QWidget
)
from PyGraphicUI.Attributes import (
	IconInstance,
	ObjectSize,
	PyFont,
	TextInstance
)


class PushButtonInit(WidgetInit):
	"""
    Data class to hold initialization parameters for push buttons.

    Attributes:
        name (str): The object name of the push button. Defaults to "button".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the push button is enabled. Defaults to True.
        visible (bool): Whether the push button is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the push button. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the push button. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the push button. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the push button. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the push button. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the push button. Defaults to None.
        cursor (Qt.CursorShape): The cursor shape to use for the push button. Defaults to Qt.CursorShape.PointingHandCursor.
        font (PyFont): The font for the push button. Defaults to a default PyFont object.
    """
	
	def __init__(
			self,
			name: str = "button",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			cursor: Qt.CursorShape = Qt.CursorShape.PointingHandCursor,
			font: PyFont = PyFont()
	):
		"""Initializes a PushButtonInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the push button is enabled.
            visible (bool): Whether the push button is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            cursor (Qt.CursorShape): The cursor shape to use.
            font (PyFont): The font to use.
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
		
		self.cursor = cursor
		self.font = font


class PyPushButton(QPushButton, PyWidget):
	"""
    A custom push button class with enhanced features.
    """
	
	doubleClicked = pyqtSignal()
	clicked = pyqtSignal()
	
	def __init__(
			self,
			button_init: PushButtonInit = PushButtonInit(),
			instance: typing.Optional[typing.Union[str, IconInstance]] = None
	):
		"""
        Initializes a PyPushButton object.

        Args:
            button_init (PushButtonInit): Initialization parameters for the push button.
            instance (typing.Optional[typing.Union[str, IconInstance]]): The initial content of the button. Can be text or an IconInstance. Defaults to None.
        """
		super().__init__(widget_init=button_init)
		
		self.setCursor(button_init.cursor)
		
		self.setFont(button_init.font)
		
		self.button_instance = instance
		self.set_button_instance(self.button_instance)
		
		self.timer = QTimer()
		self.timer.setSingleShot(True)
		self.timer.timeout.connect(self.clicked.emit)
		
		super().clicked.connect(self.check_double_click)
	
	def check_double_click(self):
		"""
        Checks for double clicks and emits the appropriate signal.
        """
		if self.timer.isActive():
			self.doubleClicked.emit()
			self.timer.stop()
		else:
			self.timer.start(250)
	
	def set_button_instance(
			self,
			button_instance: typing.Optional[typing.Union[str, TextInstance, IconInstance]] = None
	):
		"""
        Sets the content of the button.

        Args:
            button_instance (typing.Optional[typing.Union[str, TextInstance, IconInstance]]): The content to set. Can be text or an IconInstance. Defaults to None.
        """
		if isinstance(button_instance, TextInstance):
			self.setText(button_instance.text)
			self.setFont(button_instance.font)
		elif isinstance(button_instance, IconInstance):
			self.setIcon(button_instance.icon)
			self.setIconSize(button_instance.icon_size)
		elif isinstance(button_instance, str):
			self.setText(button_instance)
		elif button_instance is None:
			self.setText("")
	
	def set_default_button_instance(self):
		"""Resets the button's content to its initial instance."""
		self.set_button_instance(self.button_instance)

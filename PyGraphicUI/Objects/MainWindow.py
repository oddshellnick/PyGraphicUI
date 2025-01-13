import typing
from PyQt6.QtCore import Qt
from PyGraphicUI.Attributes import ObjectSize
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QMainWindow,
	QSizePolicy,
	QWidget
)


class MainWindowInit:
	"""
    Data class to hold initialization parameters for main windows.

    Attributes:
        name (str): The object name of the main window. Defaults to "main_window".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the main window is enabled. Defaults to True.
        visible (bool): Whether the main window is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the main window. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the main window. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the main window. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the main window. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the main window. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the main window. Defaults to None.
        window_flag (tuple[Qt.WindowType, bool]): The window flags to set. Defaults to (Qt.WindowType.Window, True).
    """
	
	def __init__(
			self,
			name: str = "main_window",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			window_flag: tuple[Qt.WindowType, bool] = (Qt.WindowType.Window, True),
			window_title: str = "program"
	):
		"""
        Initializes a MainWindowInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the main window is enabled.
            visible (bool): Whether the main window is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            window_flag (tuple[Qt.WindowType, bool]): The window flags.
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
		self.window_flag = window_flag
		self.window_title = window_title


class PyMainWindow(QMainWindow):
	"""
    A custom main window class with enhanced initialization.
    """
	
	def __init__(self, main_window_init: MainWindowInit = MainWindowInit()):
		"""
        Initializes a PyMainWindow object.

        Args:
            main_window_init (MainWindowInit): Initialization parameters for the main window.
        """
		super().__init__()
		
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		self.setEnabled(main_window_init.enabled)
		self.setGraphicsEffect(main_window_init.graphic_effect)
		self.setObjectName(main_window_init.name)
		self.setStyleSheet(main_window_init.style_sheet)
		self.setVisible(main_window_init.visible)
		self.set_fixed_size(main_window_init.fixed_size)
		self.set_maximum_size(main_window_init.maximum_size)
		self.set_minimum_size(main_window_init.minimum_size)
		self.setWindowFlag(*main_window_init.window_flag)
		self.setWindowTitle(main_window_init.window_title)
		
		if main_window_init.size_policy is not None:
			self.setSizePolicy(main_window_init.size_policy)
	
	def set_minimum_size(self, minimum_size: typing.Optional[ObjectSize]):
		"""
        Sets the minimum size of the main window.

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
        Sets the maximum size of the main window.

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
        Sets the fixed size of the main window.

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

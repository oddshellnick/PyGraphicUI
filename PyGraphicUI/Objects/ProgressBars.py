import typing
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyGraphicUI.Attributes import ObjectSize
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QProgressBar,
	QSizePolicy,
	QWidget
)


class ProgressBarInit(WidgetInit):
	"""
    Data class to hold initialization parameters for progress bars.

    Attributes:
        name (str): The object name of the progress bar. Defaults to "progress_bar".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the progress bar is enabled. Defaults to True.
        visible (bool): Whether the progress bar is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the progress bar. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the progress bar. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the progress bar. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the progress bar. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the progress bar. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the progress bar. Defaults to None.
        font (typing.Optional[QFont]): The font to use for the progress bar text. Defaults to None.
        alignment (Qt.AlignmentFlag): The alignment of the progress bar text. Defaults to Qt.AlignmentFlag.AlignCenter.
        minimum_value (int): The minimum value of the progress bar. Defaults to 0.
        maximum_value (int): The maximum value of the progress bar. Defaults to 100.
        format_ (str): The format string for displaying the progress value. Defaults to "%.02f %%".
    """
	
	def __init__(
			self,
			name: str = "progress_bar",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			font: typing.Optional[QFont] = None,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			minimum_value: int = 0,
			maximum_value: int = 100,
			format_: str = "%.02f %%"
	):
		"""
        Initializes a ProgressBarInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the progress bar is enabled.
            visible (bool): Whether the progress bar is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            font (typing.Optional[QFont]): The font for the text.
            alignment (Qt.AlignmentFlag): The text alignment.
            minimum_value (int): The minimum value.
            maximum_value (int): The maximum value.
            format_ (str): The format string.
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
		
		self.font = font
		self.alignment = alignment
		self.minimum_value = minimum_value
		self.maximum_value = maximum_value
		self.format_ = format_


class PyProgressBar(QProgressBar, PyWidget):
	"""
    A custom progress bar widget.
    """
	
	def __init__(self, progress_bar_init: ProgressBarInit = ProgressBarInit()):
		"""
        Initializes a PyProgressBar object.

        Args:
            progress_bar_init: Progress bar initialization parameters.
        """
		super().__init__(widget_init=progress_bar_init)
		
		self.progress_bar_format = progress_bar_init.format_
		self.setAlignment(progress_bar_init.alignment)
		self.setRange(progress_bar_init.minimum_value, progress_bar_init.maximum_value)
		self.setValue(progress_bar_init.minimum_value)
		
		if progress_bar_init.font is not None:
			self.setFont(progress_bar_init.font)
		
		self.valueChanged.connect(self.set_new_value)
		
		self.set_new_value()
	
	def set_new_value(self):
		"""Updates the displayed text of the progress bar according to the format."""
		self.setFormat(
				self.progress_bar_format % (((self.value() / self.maximum()) * 100) if self.maximum() != 0 else 0)
		)
	
	def reset_range(self, minimum_value: int, maximum_value: int) -> None:
		"""
        Resets the progress bar's range and sets the current value to the new minimum.

        Args:
            minimum_value: The new minimum value.
            maximum_value: The new maximum value.
        """
		self.setRange(minimum_value, maximum_value)
		self.setValue(minimum_value)
	
	def update_progress(self) -> None:
		"""Increments the progress bar's current value by 1."""
		self.setValue(self.value() + 1)

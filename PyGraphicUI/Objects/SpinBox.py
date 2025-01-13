import typing
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QAbstractSpinBox,
	QGraphicsEffect,
	QSizePolicy,
	QSpinBox,
	QWidget
)


class SpinBoxInit(WidgetInit):
	"""
    Data class to hold initialization parameters for spin boxes.

    Attributes:
        name (str): The object name of the spin box. Defaults to "spinbox".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the spin box is enabled. Defaults to True.
        visible (bool): Whether the spin box is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the spin box. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the spin box. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the spin box. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the spin box. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the spin box. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the spin box. Defaults to None.
        font (PyFont): The font to use for the spin box text. Defaults to a default QFont object.
        minimum (int): The minimum value of the spin box. Defaults to 0.
        maximum (int): The maximum value of the spin box. Defaults to 99.
        step (int): The step value for the spin box. Defaults to 1.
        step_type (QAbstractSpinBox.StepType): The step type for the spin box. Defaults to QAbstractSpinBox.StepType.DefaultStepType.
        prefix (str): The prefix to display before the spin box value. Defaults to "".
        suffix (str): The suffix to display after the spin box value. Defaults to "".
    """
	
	def __init__(
			self,
			name: str = "spinbox",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			font: PyFont = PyFont(),
			minimum: int = 0,
			maximum: int = 99,
			step: int = 1,
			step_type: QAbstractSpinBox.StepType = QAbstractSpinBox.StepType.DefaultStepType,
			prefix: str = "",
			suffix: str = ""
	):
		"""
        Initializes a SpinBoxInit object.

        Args:
            name (str): The object name.
            parent (typing.Optional[QWidget]): The parent widget.
            enabled (bool): Whether the spin box is enabled.
            visible (bool): Whether the spin box is visible.
            style_sheet (str): The style sheet to apply.
            minimum_size (typing.Optional[ObjectSize]): The minimum size.
            maximum_size (typing.Optional[ObjectSize]): The maximum size.
            fixed_size (typing.Optional[ObjectSize]): The fixed size.
            size_policy (typing.Optional[QSizePolicy]): The size policy.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect.
            font (PyFont): The font for the text.
            minimum (int): The minimum value.
            maximum (int): The maximum value.
            step (int): The step value.
            step_type (QAbstractSpinBox.StepType): The step type.
            prefix (str): The prefix string.
            suffix (str): The suffix string.
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
		self.minimum = minimum
		self.maximum = maximum
		self.step = step
		self.step_type = step_type
		self.prefix = prefix
		self.suffix = suffix


class PySpinBox(QSpinBox, PyWidget):
	"""
    A custom spin box widget.
    """
	
	def __init__(self, spinbox_init: SpinBoxInit = SpinBoxInit()):
		"""
        Initializes a PySpinBox object.

        Args:
            spinbox_init (SpinBoxInit): The initialization parameters.
        """
		super().__init__(widget_init=spinbox_init)
		
		self.setFont(spinbox_init.font)
		self.lineEdit().setFont(spinbox_init.font)
		self.setRange(spinbox_init.minimum, spinbox_init.maximum)
		self.setSingleStep(spinbox_init.step)
		self.setStepType(spinbox_init.step_type)
		self.setPrefix(spinbox_init.prefix)
		self.setSuffix(spinbox_init.suffix)

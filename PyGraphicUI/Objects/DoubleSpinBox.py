import typing
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import (
	QAbstractSpinBox,
	QDoubleSpinBox,
	QGraphicsEffect,
	QSizePolicy,
	QWidget
)


class DoubleSpinBoxInit(WidgetInit):
	"""
    Data class to hold initialization parameters for double spin boxes.

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
        minimum (float): The minimum value of the spin box. Defaults to 0.0.
        maximum (float): The maximum value of the spin box. Defaults to 100.0.
        step (float The step value for the spin box. Defaults to 0.1.
        step_type (QAbstractSpinBox.StepType): The step type for the spin box. Defaults to QAbstractSpinBox.StepType.DefaultStepType.
        prefix (str): The prefix to display before the spin box value. Defaults to "".
        suffix (str): The suffix to display after the spin box value. Defaults to "".
    """
	
	def __init__(
			self,
			name: str = "double_spinbox",
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
			minimum: float = 0.0,
			maximum: float = 100.0,
			step: float = 0.1,
			step_type: QAbstractSpinBox.StepType = QAbstractSpinBox.StepType.DefaultStepType,
			prefix: str = "",
			suffix: str = ""
	):
		"""
        Initializes a DoubleSpinBoxInit object.

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


class PyDoubleSpinBox(QDoubleSpinBox, PyWidget):
	"""
    A custom double spin box widget.
    """
	
	def __init__(self, double_spinbox_init: DoubleSpinBoxInit = DoubleSpinBoxInit()):
		"""
        Initializes a PyDoubleSpinBox object.

        Args:
            double_spinbox_init (DoubleSpinBoxInit): The initialization parameters.
        """
		super().__init__(widget_init=double_spinbox_init)
		
		self.setFont(double_spinbox_init.font)
		self.lineEdit().setFont(double_spinbox_init.font)
		self.setRange(double_spinbox_init.minimum, double_spinbox_init.maximum)
		self.setSingleStep(double_spinbox_init.step)
		self.setStepType(double_spinbox_init.step_type)
		self.setPrefix(double_spinbox_init.prefix)
		self.setSuffix(double_spinbox_init.suffix)

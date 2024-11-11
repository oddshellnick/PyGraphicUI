from PyQt6.QtCore import Qt
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QGraphicsEffect, QLabel, QSizePolicy, QWidget
from PyGraphicUI.Attributes import ObjectSize, PixmapInstance, PyFont, TextInstance
#
#
#
#
class LabelInit(WidgetInit):
	def __init__(
			self,
			name: str = "label",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			scaled_contents: bool = False,
			word_wrap: bool = True,
			indent: int = 0,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
			font: PyFont = PyFont(point_size=10),
			margin: int = 0
	):
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
		#
		#
		#
		#
		self.scaled_contents = scaled_contents
		self.word_wrap = word_wrap
		self.indent = indent
		self.alignment = alignment
		self.interaction_flag = interaction_flag
		self.font = font
		self.margin = margin
#
#
#
#
class PyLabel(QLabel, PyWidget):
	def __init__(
			self,
			label_init: LabelInit = LabelInit(),
			instance: str | PixmapInstance = ""
	):
		super().__init__(widget_init=label_init)
		#
		#
		#
		#
		self.label_instance = instance
		#
		#
		#
		#
		self.setAlignment(label_init.alignment)
		self.setAutoFillBackground(False)
		self.setIndent(label_init.indent)
		self.setScaledContents(label_init.scaled_contents)
		self.setTextInteractionFlags(label_init.interaction_flag)
		self.setWordWrap(label_init.word_wrap)
		self.setFont(label_init.font)
		self.setMargin(label_init.margin)
		self.set_label_instance(instance)
	#
	#
	#
	#
	def set_label_instance(
			self,
			label_instance: str | TextInstance | PixmapInstance = ""
	):
		if type(label_instance) == TextInstance:
			self.setText(label_instance.text)
			self.setFont(label_instance.font)

		elif type(label_instance) == PixmapInstance:
			label_instance = label_instance.pixmap.scaled(label_instance.pixmap_size)

			self.setPixmap(label_instance)
		elif type(label_instance) == str:
			self.setText(label_instance)
	#
	#
	#
	#
	def set_default_label_instance(self):
		self.set_label_instance(self.label_instance)

from PyQt6.QtCore import QRect, QRectF, Qt
from PyQt6.QtGui import QFont, QFontMetrics
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Widgets import PyWidget, WidgetInit
from PyQt6.QtWidgets import QGraphicsEffect, QHeaderView, QSizePolicy, QWidget
#
#
#
#
class HeaderViewInit(WidgetInit):
	#
	#
	#
	#
	def __init__(
			self,
			orientation: Qt.Orientation,
			name: str = "header_view",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			font: QFont = PyFont()
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
		self.orientation = orientation
		self.font = font
#
#
#
#
class PyHeaderView(QHeaderView):
	#
	#
	#
	#
	def __init__(self, header_view_init: HeaderViewInit):
		if header_view_init.parent is None:
			super().__init__(header_view_init.orientation)
		else:
			super().__init__(header_view_init.orientation, header_view_init.parent)
		#
		#
		#
		#
		self.font = header_view_init.font
		#
		#
		#
		#
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		self.setEnabled(header_view_init.enabled)
		self.setGraphicsEffect(header_view_init.graphic_effect)
		self.setObjectName(header_view_init.name)
		self.setStyleSheet(header_view_init.style_sheet)
		self.setVisible(header_view_init.visible)
		self.set_fixed_size(header_view_init.fixed_size)
		self.set_maximum_size(header_view_init.maximum_size)
		self.set_minimum_size(header_view_init.minimum_size)
		self.setFont(header_view_init.font)
		#
		#
		#
		#
		if header_view_init.size_policy is not None:
			self.setSizePolicy(header_view_init.size_policy)
	#
	#
	#
	#
	def set_minimum_size(self, minimum_size: ObjectSize):
		if minimum_size is not None:
			if minimum_size.size is not None:
				self.setMinimumSize(minimum_size.size)
			elif minimum_size.width is not None:
				self.setMinimumWidth(minimum_size.width)
			elif minimum_size.height is not None:
				self.setMinimumHeight(minimum_size.height)
	#
	#
	#
	#
	def set_maximum_size(self, maximum_size: ObjectSize):
		if maximum_size is not None:
			if maximum_size.size is not None:
				self.setMaximumSize(maximum_size.size)
			elif maximum_size.width is not None:
				self.setMaximumWidth(maximum_size.width)
			elif maximum_size.height is not None:
				self.setMaximumHeight(maximum_size.height)
	#
	#
	#
	#
	def set_fixed_size(self, fixed_size: ObjectSize):
		if fixed_size is not None:
			if fixed_size.size is not None:
				self.setFixedSize(fixed_size.size)
			elif fixed_size.width is not None:
				self.setFixedWidth(fixed_size.width)
			elif fixed_size.height is not None:
				self.setFixedHeight(fixed_size.height)
	#
	#
	#
	#
	def sectionSizeFromContents(self, logicalIndex):
		if self.model():
			headerText = self.model().headerData(logicalIndex, self.orientation(), Qt.ItemDataRole.DisplayRole)

			metrics = QFontMetrics(self.font)
			maxWidth = self.sectionSize(logicalIndex)

			rect = metrics.boundingRect(
					QRect(0, 0, maxWidth, 5000),
					self.defaultAlignment() | Qt.TextFlag.TextWordWrap | Qt.TextFlag.TextExpandTabs,
					headerText,
					4
			)
			return rect.size()
		else:
			return QHeaderView.sectionSizeFromContents(self, logicalIndex)

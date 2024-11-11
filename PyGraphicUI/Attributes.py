from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QLayout, QSizePolicy, QWidget
from PyQt6.QtGui import QBrush, QColor, QFont, QIcon, QImage, QPen, QPixmap, QTransform
#
#
#
#
class PyFont(QFont):
	#
	#
	#
	#
	def __init__(
			self,
			capitalization: QFont.Capitalization = QFont.Capitalization.MixedCase,
			font_family: str = "Arial",
			fixed_pitch: bool = True,
			hinting_preference: QFont.HintingPreference = QFont.HintingPreference.PreferFullHinting,
			kerning: bool = False,
			letter_spacing: tuple[QFont.SpacingType, float] = (QFont.SpacingType.PercentageSpacing, 100),
			overline: bool = False,
			stretch: int = 0,
			strike_out: bool = False,
			style: QFont.Style = QFont.Style.StyleNormal,
			style_hint: QFont.StyleHint = QFont.StyleHint.AnyStyle,
			style_strategy: QFont.StyleStrategy = QFont.StyleStrategy.PreferAntialias | QFont.StyleStrategy.PreferQuality,
			underline: bool = False,
			weight: int = 50,
			word_spacing: int = 0,
			pixel_size: int = None,
			point_size: int = None,
			pointf_size: float = None
	):
		super().__init__()
		#
		#
		#
		#
		self.setCapitalization(capitalization)
		self.setFamily(font_family)
		self.setFixedPitch(fixed_pitch)
		self.setHintingPreference(hinting_preference)
		self.setKerning(kerning)
		self.setLetterSpacing(*letter_spacing)
		self.setOverline(overline)
		self.setStretch(stretch)
		self.setStrikeOut(strike_out)
		self.setStyle(style)
		self.setStyleHint(style_hint)
		self.setStyleStrategy(style_strategy)
		self.setUnderline(underline)
		self.setWeight(weight)
		self.setWordSpacing(word_spacing)
		#
		#
		#
		#
		if pixel_size is not None:
			self.setPixelSize(pixel_size)
		elif point_size is not None:
			self.setPointSize(point_size)
		elif pointf_size is not None:
			self.setPointSizeF(pointf_size)
#
#
#
#
class TextInstance:
	#
	#
	#
	#
	def __init__(self, font: QFont = PyFont(point_size=10), text: str = ""):
		self.font, self.text = font, text
#
#
#
#
class PySizePolicy(QSizePolicy):
	#
	#
	#
	#
	def __init__(
			self,
			horizontal_stretch: int = 0,
			vertical_stretch: int = 0,
			horizontal_policy: QSizePolicy.Policy = QSizePolicy.Policy.Preferred,
			vertical_policy: QSizePolicy.Policy = QSizePolicy.Policy.Preferred,
			height_for_width: bool = True,
			width_for_height: bool = True,
			control_type: QSizePolicy.ControlType = QSizePolicy.ControlType.DefaultType
	):
		super().__init__()
		#
		#
		#
		#
		self.setHorizontalStretch(horizontal_stretch)
		self.setVerticalStretch(vertical_stretch)
		self.setHorizontalPolicy(horizontal_policy)
		self.setVerticalPolicy(vertical_policy)
		self.setHeightForWidth(height_for_width)
		self.setWidthForHeight(width_for_height)
		self.setControlType(control_type)
#
#
#
#
class PyRGBFColor(QColor):
	#
	#
	#
	#
	def __init__(
			self,
			red: float = 0.0,
			green: float = 0.0,
			blue: float = 0.0,
			alpha: float = 255.0
	):
		super().__init__()
		#
		#
		#
		#
		self.setRgbF(red, green, blue, alpha)
#
#
#
#
class PyHSVFColor(QColor):
	#
	#
	#
	#
	def __init__(
			self,
			hue: float = 0.0,
			saturation: float = 0.0,
			value: float = 0.0,
			alpha: float = 255.0
	):
		super().__init__()
		#
		#
		#
		#
		self.setHsvF(hue, saturation, value, alpha)
#
#
#
#
class PyHSVColor(QColor):
	#
	#
	#
	#
	def __init__(self, hue: int = 0, saturation: int = 0, value: int = 0, alpha: int = 255):
		super().__init__()
		#
		#
		#
		#
		self.setHsv(hue, saturation, value, alpha)
#
#
#
#
class PyHSLFColor(QColor):
	#
	#
	#
	#
	def __init__(
			self,
			hue: float = 0.0,
			saturation: float = 0.0,
			lightness: float = 0.0,
			alpha: float = 255.0
	):
		super().__init__()
		#
		#
		#
		#
		self.setHslF(hue, saturation, lightness, alpha)
#
#
#
#
class PyHSLColor(QColor):
	#
	#
	#
	#
	def __init__(self, hue: int = 0, saturation: int = 0, lightness: int = 0, alpha: int = 255):
		super().__init__()
		#
		#
		#
		#
		self.setHsl(hue, saturation, lightness, alpha)
#
#
#
#
class PyCMYKFColor(QColor):
	#
	#
	#
	#
	def __init__(
			self,
			cyan: float = 0.0,
			magenta: float = 0.0,
			yellow: float = 0.0,
			black: float = 0.0,
			alpha: float = 255.0
	):
		super().__init__()
		#
		#
		#
		#
		self.setCmykF(cyan, magenta, yellow, black, alpha)
#
#
#
#
class PyCMYKColor(QColor):
	#
	#
	#
	#
	def __init__(
			self,
			cyan: int = 0,
			magenta: int = 0,
			yellow: int = 0,
			black: int = 0,
			alpha: int = 255
	):
		super().__init__()
		#
		#
		#
		#
		self.setCmyk(cyan, magenta, yellow, black, alpha)
#
#
#
#
class PixmapInstance:
	#
	#
	#
	#
	def __init__(self, pixmap: QPixmap, pixmap_size: QSize):
		self.pixmap, self.pixmap_size = pixmap, pixmap_size
#
#
#
#
class ObjectSize:
	#
	#
	#
	#
	def __init__(self, width: int = None, height: int = None):
		self.width, self.height = width, height
		#
		#
		#
		#
		if self.width is not None and self.height is not None:
			self.size = QSize(self.width, self.height)
		else:
			self.size = None
#
#
#
#
class LinearLayoutItem:
	#
	#
	#
	#
	def __init__(
			self,
			instance: QWidget | QLayout,
			stretch: int = 0,
			alignment: Qt.AlignmentFlag = None
	):
		self.instance, self.stretch, self.alignment = instance, stretch, alignment
#
#
#
#
class IconInstance:
	#
	#
	#
	#
	def __init__(self, icon: QIcon, icon_size: QSize):
		self.icon, self.icon_size = icon, icon_size
#
#
#
#
class GridRectangle:
	#
	#
	#
	#
	def __init__(
			self,
			vertical_position: int = 0,
			horizontal_position: int = 0,
			vertical_stretch: int = 0,
			horizontal_stretch: int = 0
	):
		self.vertical_position, self.horizontal_position, self.vertical_stretch, self.horizontal_stretch = vertical_position, horizontal_position, vertical_stretch, horizontal_stretch
#
#
#
#
class GridLayoutItem:
	#
	#
	#
	#
	def __init__(
			self,
			instance: QWidget | QLayout,
			stretch: GridRectangle = None,
			alignment: Qt.AlignmentFlag = None
	):
		self.instance, self.stretch, self.alignment = instance, stretch, alignment
#
#
#
#
class PyRGBColor(QColor):
	#
	#
	#
	#
	def __init__(self, red: int = 0, green: int = 0, blue: int = 0, alpha: int = 255):
		super().__init__()
		#
		#
		#
		#
		self.setRgb(red, green, blue, alpha)
#
#
#
#
class PyPen(QPen):
	#
	#
	#
	#
	def __init__(
			self,
			cap_style: Qt.PenCapStyle = Qt.PenCapStyle.RoundCap,
			color: QColor = PyRGBColor(),
			cosmetic: bool = True,
			dash_offset: float = 0.0,
			dash_patters: list[float] = None,
			join_style: Qt.PenJoinStyle = Qt.PenJoinStyle.RoundJoin,
			miter_limit: float = 0.0,
			style: Qt.PenStyle = Qt.PenStyle.SolidLine,
			width: int = 1
	):
		super().__init__()
		#
		#
		#
		#
		if dash_patters is None:
			dash_patters = [0.0, 0.0]
		#
		#
		#
		#
		self.setCapStyle(cap_style)
		self.setColor(color)
		self.setCosmetic(cosmetic)
		self.setDashOffset(dash_offset)
		self.setDashPattern(dash_patters)
		self.setJoinStyle(join_style)
		self.setMiterLimit(miter_limit)
		self.setStyle(style)
		self.setWidth(width)
#
#
#
#
class PyBrush(QBrush):
	#
	#
	#
	#
	def __init__(
			self,
			style: Qt.BrushStyle = Qt.BrushStyle.SolidPattern,
			color: QColor = None,
			texture: QPixmap = None,
			transform: QTransform = None,
			texture_image: QImage = None
	):
		super().__init__()
		#
		#
		#
		#
		self.setStyle(style)
		#
		#
		#
		#
		if color is not None:
			self.setColor(color)
		#
		#
		#
		#
		if texture is not None:
			self.setTexture(texture)
		#
		#
		#
		#
		if transform is not None:
			self.setTransform(transform)
		#
		#
		#
		#
		if texture_image is not None:
			self.setTextureImage(texture_image)

import typing
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
	QLayout,
	QSizePolicy,
	QWidget
)
from PyQt6.QtGui import (
	QBrush,
	QColor,
	QFont,
	QIcon,
	QImage,
	QPen,
	QPixmap,
	QTransform
)


class PyFont(QFont):
	"""
    A custom QFont class that provides convenience methods for setting common font properties.

    :Usage:
        font = PyFont(font_family="Times New Roman", size=12, size_type="point")
    """
	
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
			size_type: typing.Literal["pixel", "point", "pointf"] = "point",
			size: typing.Union[int, float] = 10
	):
		"""
        Initializes a PyFont object.

        Args:
            capitalization (QFont.Capitalization): The capitalization style for the font.
            font_family (str): The font family name.
            fixed_pitch (bool): Whether the font is fixed-pitch.
            hinting_preference (QFont.HintingPreference): The hinting preference for the font.
            kerning (bool): Whether kerning should be applied.
            letter_spacing (tuple[QFont.SpacingType, float]): A tuple containing the letter spacing type and value.
            overline (bool): Whether the text should be overlined.
            stretch (int): The font stretch factor.
            strike_out (bool): Whether the text should be struck out.
            style (QFont.Style): The font style.
            style_hint (QFont.StyleHint): The style hint for the font.
            style_strategy (QFont.StyleStrategy): The style strategy for the font.
            underline (bool): Whether the text should be underlined.
            weight (int): The font weight.
            word_spacing (int): The word spacing value.
            size_type (str): The type of size unit ("pixel", "point", or "pointf").
            size ( typing.Union[int, float]): The font size.

        Raises:
            ValueError: If an invalid size type or value is provided.

        :Usage:
            font = PyFont(font_family="Times New Roman", size=12, size_type="point")
            font2 = PyFont(size=14, size_type="pixel")

        """
		super().__init__()
		
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
		
		if size_type == "pixel" and isinstance(size, int):
			self.setPixelSize(size)
		elif size_type == "point" and isinstance(size, int):
			self.setPointSize(size)
		elif size_type == "pointf" and isinstance(size, float):
			self.setPointSizeF(size)
		else:
			raise ValueError("Invalid size type or value.")


class TextInstance:
	"""
    A class for storing and representing text information.

    Attributes:
        font (QFont): The font used for the text.
        text (str): The text string.

    :Usage:
        text_instance = TextInstance(font=PyFont(size=14), text="Hello, world!")
    """
	
	def __init__(self, font: QFont = PyFont(), text: str = ""):
		"""
        Initializes a TextInstance object.

        Args:
            font (QFont): The font to use for the text.
            text (str): The text string.


        :Usage:
            default_text = TextInstance()
            custom_text = TextInstance(font=PyFont(size=14, size_type="point"), text="Custom Text")

        """
		self.font, self.text = font, text


class PySizePolicy(QSizePolicy):
	"""
    A custom QSizePolicy class that provides convenience methods for setting common size policy properties.

    :Usage:
        size_policy = PySizePolicy(horizontal_policy=QSizePolicy.Policy.Expanding, vertical_policy=QSizePolicy.Policy.Fixed)

    """
	
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
		"""
        Initializes a PySizePolicy object.

        Args:
            horizontal_stretch (int): The horizontal stretch factor.
            vertical_stretch (int): The vertical stretch factor.
            horizontal_policy (QSizePolicy.Policy): The horizontal size policy.
            vertical_policy (QSizePolicy.Policy): The vertical size policy.
            height_for_width (bool): Whether the height should be calculated based on the width.
            width_for_height (bool): Whether the width should be calculated based on the height.
            control_type (QSizePolicy.ControlType): The type of control for the size policy.

        :Usage:
            default_policy = PySizePolicy()
            expanding_policy = PySizePolicy(horizontal_policy=QSizePolicy.Policy.Expanding, horizontal_stretch=1)

        """
		super().__init__()
		
		self.setHorizontalStretch(horizontal_stretch)
		self.setVerticalStretch(vertical_stretch)
		self.setHorizontalPolicy(horizontal_policy)
		self.setVerticalPolicy(vertical_policy)
		self.setHeightForWidth(height_for_width)
		self.setWidthForHeight(width_for_height)
		self.setControlType(control_type)


class PyRGBFColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using float values.

    :Usage:
        color = PyRGBFColor(red=1.0, green=0.5, blue=0.0)
    """
	
	def __init__(
			self,
			red: float = 0.0,
			green: float = 0.0,
			blue: float = 0.0,
			alpha: float = 255.0
	):
		"""
        Initializes a PyRGBFColor object.

        Args:
            red (float): The red component of the color, between 0.0 and 1.0.
            green (float): The green component of the color, between 0.0 and 1.0.
            blue (float): The blue component of the color, between 0.0 and 1.0.
            alpha (float): The alpha component of the color, between 0.0 and 255.0.

        :Usage:
            opaque_red = PyRGBFColor(red=1.0)
            translucent_green = PyRGBFColor(green=1.0, alpha=128.0)
        """
		super().__init__()
		
		self.setRgbF(red, green, blue, alpha)


class PyRGBColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using RGB values.
    """
	
	def __init__(self, red: int = 0, green: int = 0, blue: int = 0, alpha: int = 255):
		"""
        Initializes a PyRGBColor object.

        Args:
            red (int): The red component of the color, between 0 and 255. Defaults to 0.
            green (int): The green component of the color, between 0 and 255. Defaults to 0.
            blue (int): The blue component of the color, between 0 and 255. Defaults to 0.
            alpha (int): The alpha component of the color, between 0 and 255. Defaults to 255.
        """
		super().__init__()
		
		self.setRgb(red, green, blue, alpha)


class PyPen(QPen):
	"""
    A custom QPen class that provides convenience methods for setting common pen properties.
    """
	
	def __init__(
			self,
			cap_style: Qt.PenCapStyle = Qt.PenCapStyle.RoundCap,
			color: QColor = PyRGBColor(),
			cosmetic: bool = True,
			dash_offset: float = 0.0,
			dash_patters: typing.Optional[typing.Iterable[float]] = None,
			join_style: Qt.PenJoinStyle = Qt.PenJoinStyle.RoundJoin,
			miter_limit: float = 0.0,
			style: Qt.PenStyle = Qt.PenStyle.SolidLine,
			width: int = 1
	):
		"""
        Initializes a PyPen object.

        Args:
            cap_style (Qt.PenCapStyle): The cap style for the pen. Defaults to Qt.PenCapStyle.RoundCap.
            color (QColor): The color of the pen. Defaults to PyRGBColor().
            cosmetic (bool): Whether the pen is cosmetic. Defaults to True.
            dash_offset (float): The dash offset value. Defaults to 0.0.
            dash_patters (typing.Optional[typing.Iterable[float]]): A typing.Iterable of float values representing the dash pattern. Defaults to None.
            join_style (Qt.PenJoinStyle): The join style for the pen. Defaults to Qt.PenJoinStyle.RoundJoin.
            miter_limit (float): The miter limit value. Defaults to 0.0.
            style (Qt.PenStyle): The pen style. Defaults to Qt.PenStyle.SolidLine.
            width (int): The width of the pen. Defaults to 1.
        """
		super().__init__()
		
		if dash_patters is None:
			dash_patters = [0.0, 0.0]
		
		self.setCapStyle(cap_style)
		self.setColor(color)
		self.setCosmetic(cosmetic)
		self.setDashOffset(dash_offset)
		self.setDashPattern(dash_patters)
		self.setJoinStyle(join_style)
		self.setMiterLimit(miter_limit)
		self.setStyle(style)
		self.setWidth(width)


class PyHSVFColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using HSV float values.

    :Usage:
        color = PyHSVFColor(hue=120.0, saturation=1.0, value=0.5)

    """
	
	def __init__(
			self,
			hue: float = 0.0,
			saturation: float = 0.0,
			value: float = 0.0,
			alpha: float = 255.0
	):
		"""
        Initializes a PyHSVFColor object.

        Args:
            hue (float): The hue component of the color, between 0.0 and 360.0.
            saturation (float): The saturation component of the color, between 0.0 and 1.0.
            value (float): The value component of the color, between 0.0 and 1.0.
            alpha (float): The alpha component of the color, between 0.0 and 255.0.

        :Usage:
            vivid_green = PyHSVFColor(hue=120.0, saturation=1.0, value=1.0)
            pastel_blue = PyHSVFColor(hue=240.0, saturation=0.5, value=1.0)


        """
		super().__init__()
		
		self.setHsvF(hue, saturation, value, alpha)


class PyHSVColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using HSV values.

    :Usage:
        color = PyHSVColor(hue=120, saturation=255, value=128)
    """
	
	def __init__(
			self,
			hue: int = 0,
			saturation: int = 0,
			value: int = 0,
			alpha: int = 255
	):
		"""
        Initializes a PyHSVColor object.

        Args:
            hue (int): The hue component of the color, between 0 and 360.
            saturation (int): The saturation component of the color, between 0 and 255.
            value (int): The value component of the color, between 0 and 255.
            alpha (int): The alpha component of the color, between 0 and 255.

        :Usage:
            bright_red = PyHSVColor(hue=0, saturation=255, value=255)
            dark_blue = PyHSVColor(hue=240, saturation=255, value=128)

        """
		super().__init__()
		
		self.setHsv(hue, saturation, value, alpha)


class PyHSLFColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using HSL float values.
    """
	
	def __init__(
			self,
			hue: float = 0.0,
			saturation: float = 0.0,
			lightness: float = 0.0,
			alpha: float = 255.0
	):
		"""
        Initializes a PyHSLFColor object.

        Args:
            hue (float): The hue component of the color, between 0.0 and 360.0. Defaults to 0.0.
            saturation (float): The saturation component of the color, between 0.0 and 1.0. Defaults to 0.0.
            lightness (float): The lightness component of the color, between 0.0 and 1.0. Defaults to 0.0.
            alpha (float): The alpha component of the color, between 0.0 and 255.0. Defaults to 255.0.
        """
		super().__init__()
		
		self.setHslF(hue, saturation, lightness, alpha)


class PyHSLColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using HSL values.
    """
	
	def __init__(
			self,
			hue: int = 0,
			saturation: int = 0,
			lightness: int = 0,
			alpha: int = 255
	):
		"""
        Initializes a PyHSLColor object.

        Args:
            hue (int): The hue component of the color, between 0 and 360. Defaults to 0.
            saturation (int): The saturation component of the color, between 0 and 255. Defaults to 0.
            lightness (int): The lightness component of the color, between 0 and 255. Defaults to 0.
            alpha (int): The alpha component of the color, between 0 and 255. Defaults to 255.
        """
		super().__init__()
		
		self.setHsl(hue, saturation, lightness, alpha)


class PyCMYKFColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using CMYK float values.
    """
	
	def __init__(
			self,
			cyan: float = 0.0,
			magenta: float = 0.0,
			yellow: float = 0.0,
			black: float = 0.0,
			alpha: float = 255.0
	):
		"""
        Initializes a PyCMYKFColor object.

        Args:
            cyan (float): The cyan component of the color, between 0.0 and 1.0. Defaults to 0.0.
            magenta (float): The magenta component of the color, between 0.0 and 1.0. Defaults to 0.0.
            yellow (float): The yellow component of the color, between 0.0 and 1.0. Defaults to 0.0.
            black (float): The black component of the color, between 0.0 and 1.0. Defaults to 0.0.
            alpha (float): The alpha component of the color, between 0.0 and 255.0. Defaults to 255.0.
        """
		super().__init__()
		
		self.setCmykF(cyan, magenta, yellow, black, alpha)


class PyCMYKColor(QColor):
	"""
    A custom QColor class that provides a convenience method for setting the color using CMYK values.
    """
	
	def __init__(
			self,
			cyan: int = 0,
			magenta: int = 0,
			yellow: int = 0,
			black: int = 0,
			alpha: int = 255
	):
		"""
        Initializes a PyCMYKColor object.

        Args:
            cyan (int): The cyan component of the color, between 0 and 255. Defaults to 0.
            magenta (int): The magenta component of the color, between 0 and 255. Defaults to 0.
            yellow (int): The yellow component of the color, between 0 and 255. Defaults to 0.
            black (int): The black component of the color, between 0 and 255. Defaults to 0.
            alpha (int): The alpha component of the color, between 0 and 255. Defaults to 255.
        """
		super().__init__()
		
		self.setCmyk(cyan, magenta, yellow, black, alpha)


class PyBrush(QBrush):
	"""
    A custom QBrush class that provides convenience methods for setting common brush properties.
    """
	
	def __init__(
			self,
			style: Qt.BrushStyle = Qt.BrushStyle.SolidPattern,
			color: typing.Optional[QColor] = None,
			texture: typing.Optional[QPixmap] = None,
			transform: typing.Optional[QTransform] = None,
			texture_image: typing.Optional[QImage] = None
	):
		"""
        Initializes a PyBrush object.

        Args:
            style (Qt.BrushStyle): The brush style. Defaults to Qt.BrushStyle.SolidPattern.
            color (typing.Optional[QColor]): The color of the brush. Defaults to None.
            texture (typing.Optional[QPixmap]): The texture of the brush. Defaults to None.
            transform (typing.Optional[QTransform]): The transformation to be applied to the texture. Defaults to None.
            texture_image (typing.Optional[QImage]): The image to be used as the texture. Defaults to None.
        """
		super().__init__()
		
		self.setStyle(style)
		
		if color is not None:
			self.setColor(color)
		
		if texture is not None:
			self.setTexture(texture)
		
		if transform is not None:
			self.setTransform(transform)
		
		if texture_image is not None:
			self.setTextureImage(texture_image)


class PixmapInstance:
	"""
    A class for storing and representing QPixmap information.

    Attributes:
        pixmap (QPixmap): The QPixmap object.
        pixmap_size (QSize): The size of the pixmap.

    :Usage:
        pixmap = QPixmap("image.png")
        pixmap_instance = PixmapInstance(pixmap, pixmap.size())
    """
	
	def __init__(self, pixmap: QPixmap, pixmap_size: QSize):
		"""
        Initializes a PixmapInstance object.

        Args:
            pixmap (QPixmap): The QPixmap object.
            pixmap_size (QSize): The size of the pixmap.

        :Usage:
            pixmap = QPixmap("image.png")
            pixmap_instance = PixmapInstance(pixmap, pixmap.size())
        """
		self.pixmap, self.pixmap_size = pixmap, pixmap_size


class ObjectSize:
	"""
    A class for representing the size of an object.

    Attributes:
        width (typing.Optional[int]): The width of the object.
        height (typing.Optional[int]): The height of the object.
        size (QSize | None): The size of the object as a QSize object.

    :Usage:
        size = ObjectSize(width=100, height=50)
        size2 = ObjectSize()

    """
	
	def __init__(
			self,
			width: typing.Optional[int] = None,
			height: typing.Optional[int] = None
	):
		"""
        Initializes an ObjectSize object.

        Args:
            width (typing.Optional[int]): The width of the object.
            height (typing.Optional[int]): The height of the object.

        :Usage:
            fixed_size = ObjectSize(width=100, height=50)
            dynamic_size = ObjectSize() # Width and Height can be set later
        """
		self.width, self.height = width, height
		if self.width is not None and self.height is not None:
			self.size = QSize(self.width, self.height)
		else:
			self.size = None


class LinearLayoutItem:
	"""
    A class for representing an item in a linear layout.

    Attributes:
        instance (typing.Union[QWidget, QLayout]): The widget or layout instance.
        stretch (int): The stretch factor.
        alignment (typing.Optional[Qt.AlignmentFlag]): The alignment flag.

    :Usage:
        widget = QWidget()
        layout_item = LinearLayoutItem(widget, stretch=1, alignment=Qt.AlignmentFlag.AlignCenter)
    """
	
	def __init__(
			self,
			instance: typing.Union[QWidget, QLayout],
			stretch: int = 0,
			alignment: typing.Optional[Qt.AlignmentFlag] = None
	):
		"""
        Initializes a LinearLayoutItem object.

        Args:
            instance (typing.Union[QWidget, QLayout]): The widget or layout to be placed in the linear layout.
            stretch (int): The stretch factor for the item.
            alignment (typing.Optional[Qt.AlignmentFlag]): The alignment of the item within its space.

        :Usage:
            label = QLabel("Label")
            item = LinearLayoutItem(label, stretch=1, alignment=Qt.AlignmentFlag.AlignLeft)

        """
		self.instance, self.stretch, self.alignment = instance, stretch, alignment


class IconInstance:
	"""
    A class for storing and representing QIcon information.

    Attributes:
        icon (QIcon): The QIcon object.
        icon_size (QSize): The size of the icon.

    :Usage:
        icon = QIcon("icon.png")
        icon_instance = IconInstance(icon, QSize(32, 32))
    """
	
	def __init__(self, icon: QIcon, icon_size: QSize):
		"""
        Initializes an IconInstance object.

        Args:
            icon (QIcon): The QIcon object.
            icon_size (QSize): The size of the icon.

        :Usage:
            icon = QIcon("icon.png")
            icon_instance = IconInstance(icon, QSize(24,24))

        """
		self.icon, self.icon_size = icon, icon_size


class GridRectangle:
	"""
    A class for representing a rectangular area within a grid layout.

    Attributes:
        vertical_position (int): The vertical position.
        horizontal_position (int): The horizontal position.
        vertical_stretch (int): The vertical stretch factor.
        horizontal_stretch (int): The horizontal stretch factor.


    :Usage:
        rect = GridRectangle(vertical_position=1, horizontal_position=0, vertical_stretch=2, horizontal_stretch=1)

    """
	
	def __init__(
			self,
			vertical_position: int = 0,
			horizontal_position: int = 0,
			vertical_stretch: int = 0,
			horizontal_stretch: int = 0
	):
		"""
        Initializes a GridRectangle object.

        Args:
            vertical_position (int): The vertical position of the rectangle within the grid.
            horizontal_position (int): The horizontal position of the rectangle within the grid.
            vertical_stretch (int): The vertical stretch factor for the rectangle.
            horizontal_stretch (int): The horizontal stretch factor for the rectangle.

        :Usage:
            default_rect = GridRectangle()
            stretched_rect = GridRectangle(vertical_position=1, horizontal_position=2, vertical_stretch=1, horizontal_stretch=2)

        """
		self.vertical_position, self.horizontal_position, self.vertical_stretch, self.horizontal_stretch = (
				vertical_position,
				horizontal_position,
				vertical_stretch,
				horizontal_stretch
		)


class GridLayoutItem:
	"""
    A class for representing an item in a grid layout.

    Attributes:
        instance (typing.Union[QWidget, QLayout]): The widget or layout instance.
        stretch (GridRectangle | None): The stretch rectangle.
        alignment (typing.Optional[Qt.AlignmentFlag]): The alignment flag.

    :Usage:
        widget = QWidget()
        stretch = GridRectangle(vertical_stretch=1)
        layout_item = GridLayoutItem(widget, stretch=stretch, alignment=Qt.AlignmentFlag.AlignTop)

    """
	
	def __init__(
			self,
			instance: typing.Union[QWidget, QLayout],
			stretch: GridRectangle = GridRectangle(),
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter
	):
		"""
        Initializes a GridLayoutItem object.

        Args:
            instance (typing.Union[QWidget, QLayout]): The widget or layout to be placed in the grid layout.
            stretch (GridRectangle): The stretch factors for the item within the grid.
            alignment (Qt.AlignmentFlag): The alignment of the item within its space.

        :Usage:
            button = QPushButton("Button")
            stretch = GridRectangle(horizontal_stretch=1, vertical_stretch=1)
            grid_item = GridLayoutItem(button, stretch=stretch, alignment=Qt.AlignmentFlag.AlignCenter)
        """
		self.instance, self.stretch, self.alignment = instance, stretch, alignment

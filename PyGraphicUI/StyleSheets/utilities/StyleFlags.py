from dataclasses import dataclass


@dataclass(frozen=True)
class StyleFlags:
	"""
    Constants representing various style flags and options used in CSS.
    """
	
	@dataclass(frozen=True)
	class Alignment:
		"""
        Constants for alignment properties.
        """
		
		Top = "top"
		Bottom = "bottom"
		Left = "left"
		Right = "right"
		Center = "center"
		
		TopLeft = "top left"
		TopRight = "top right"
		BottomLeft = "bottom left"
		BottomRight = "bottom right"
		
		TopCenter = "top center"
		BottomCenter = "bottom center"
		LeftCenter = "left center"
		RightCenter = "right center"
	
	@dataclass(frozen=True)
	class Attachment:
		"""
        Constants for background-attachment property.
        """
		
		Scroll = "scroll"
		Fixed = "fixed"
	
	@dataclass(frozen=True)
	class Background:
		"""
        Constants for background property.
        """
		
		None_ = "none"
	
	@dataclass(frozen=True)
	class BorderStyle:
		"""
        Constants for border-style property.
        """
		
		Dashed = "dashed"
		DotDash = "dot-dash"
		DotDotDash = "dot-dot-dash"
		Dotted = "dotted"
		Double = "double"
		Groove = "groove"
		Inset = "inset"
		Outset = "outset"
		Ridge = "ridge"
		Solid = "solid"
		None_ = "none"
	
	@dataclass(frozen=True)
	class ColorName:
		"""
        Constants for color names.
        """
		
		Transparent = "transparent"
	
	@dataclass(frozen=True)
	class FontStyle:
		"""
        Constants for font-style property.
        """
		
		Normal = "normal"
		Italic = "italic"
		Oblique = "oblique"
	
	@dataclass(frozen=True)
	class FontWeight:
		"""
        Constants for font-weight property.
        """
		
		Normal = "normal"
		Bold = "bold"
	
	@dataclass(frozen=True)
	class IconMode:
		"""
        Constants for icon modes.
        """
		
		Disabled = "disabled"
		Active = "active"
		Normal = "normal"
		Selected = "selected"
	
	@dataclass(frozen=True)
	class IconState:
		"""
        Constants for icon states.
        """
		
		On = "on"
		Off = "off"
	
	@dataclass(frozen=True)
	class LineStyle:
		"""
        Constants for border-style property and similar.
        """
		
		Dashed = "dashed"
		DotDash = "dot-dash"
		DotDotDash = "dot-dot-dash"
		Double = "double"
		Groove = "groove"
		Inset = "inset"
		Outset = "outset"
		Ridge = "ridge"
		Solid = "solid"
		none = "none"
	
	@dataclass(frozen=True)
	class Origin:
		"""
        Constants for background-origin property.
        """
		
		Margin = "margin"
		Padding = "padding"
		Content = "content"
		Border = "border"
	
	@dataclass(frozen=True)
	class PaletteRole:
		"""
        Constants for palette roles, used with background color, etc.
        """
		
		AlternateBase = "alternate-base"
		Base = "base"
		BrightText = "bright-text"
		Button = "button"
		ButtonText = "button-text"
		Dark = "dark"
		Highlight = "highlight"
		HighlightedText = "highlighted-text"
		Light = "light"
		Link = "link"
		LinkVisited = "link-visited"
		Mid = "mid"
		Midlight = "midlight"
		Shadow = "shadow"
		Text = "text"
		Window = "window"
		WindowText = "window-text"
	
	@dataclass(frozen=True)
	class Repeat:
		"""
        Constants for background-repeat property.
        """
		
		RepeatX = "repeat-x"
		RepeatY = "repeat-y"
		Repeat = "repeat"
		NoRepeat = "no-repeat"

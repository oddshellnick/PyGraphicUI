from PyGraphicUI.StyleSheets.utilities.Font import Font
from PyGraphicUI.StyleSheets.utilities.Opacity import Opacity
from PyGraphicUI.StyleSheets.utilities.Image import Image, ImagePosition
from PyGraphicUI.StyleSheets.utilities.Text import TextAlign, TextColor, TextDecoration
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import ObjectOfStyle, StyleSheetObject
from PyGraphicUI.StyleSheets.utilities.Selection import SelectionBackgroundColor, SelectionColor
from PyGraphicUI.StyleSheets.utilities.Size import Height, MaxHeight, MaxWidth, MinHeight, MinWidth, Width
from PyGraphicUI.StyleSheets.utilities.Border import Border, BorderBottom, BorderLeft, BorderRight, BorderTop
from PyGraphicUI.StyleSheets.utilities.Margin import Margin, MarginBottom, MarginLeft, MarginRight, MarginTop
from PyGraphicUI.StyleSheets.utilities.Padding import Padding, PaddingBottom, PaddingLeft, PaddingRight, PaddingTop
from PyGraphicUI.StyleSheets.utilities.BorderColor import BorderBottomColor, BorderColor, BorderLeftColor, BorderRightColor, BorderTopColor
from PyGraphicUI.StyleSheets.utilities.BorderWidth import BorderBottomWidth, BorderLeftWidth, BorderRightWidth, BorderTopWidth, BorderWidth
from PyGraphicUI.StyleSheets.utilities.BorderStyle import BorderBottomStyle, BorderLeftStyle, BorderRightStyle, BorderTopStyle, BordersStyle
from PyGraphicUI.StyleSheets.utilities.BorderRadius import BorderBottomLeftRadius, BorderBottomRightRadius, BorderRadius, BorderTopLeftRadius, BorderTopRightRadius
from PyGraphicUI.StyleSheets.utilities.Outline import Outline, OutlineBottomLeftRadius, OutlineBottomRightRadius, OutlineColor, OutlineRadius, OutlineStyle, OutlineTopLeftRadius, OutlineTopRightRadius
from PyGraphicUI.StyleSheets.utilities.Background import AlternateBackgroundColor, Background, BackgroundAttachment, BackgroundClip, BackgroundColor, BackgroundImage, BackgroundOrigin, BackgroundPosition
#
#
#
#
class BaseStyle:
	#
	#
	#
	#
	def __init__(
			self,
			object_of_style: ObjectOfStyle | list[ObjectOfStyle] = None,
			alternate_background_color: AlternateBackgroundColor = None,
			background: Background = None,
			background_attachment: BackgroundAttachment = None,
			background_clip: BackgroundClip = None,
			background_color: BackgroundColor = None,
			background_image: BackgroundImage = None,
			background_origin: BackgroundOrigin = None,
			background_position: BackgroundPosition = None,
			border: Border = None,
			border_bottom: BorderBottom = None,
			border_bottom_color: BorderBottomColor = None,
			border_bottom_left_radius: BorderBottomLeftRadius = None,
			border_bottom_right_radius: BorderBottomRightRadius = None,
			border_bottom_style: BorderBottomStyle = None,
			border_bottom_width: BorderBottomWidth = None,
			border_color: BorderColor = None,
			border_left: BorderLeft = None,
			border_left_color: BorderLeftColor = None,
			border_left_style: BorderLeftStyle = None,
			border_left_width: BorderLeftWidth = None,
			border_radius: BorderRadius = None,
			border_right: BorderRight = None,
			border_right_color: BorderRightColor = None,
			border_right_style: BorderRightStyle = None,
			border_right_width: BorderRightWidth = None,
			border_top: BorderTop = None,
			border_top_color: BorderTopColor = None,
			border_top_left_radius: BorderTopLeftRadius = None,
			border_top_right_radius: BorderTopRightRadius = None,
			border_top_style: BorderTopStyle = None,
			border_top_width: BorderTopWidth = None,
			border_width: BorderWidth = None,
			borders_style: BordersStyle = None,
			font: Font = None,
			height: Height = None,
			image: Image = None,
			image_position: ImagePosition = None,
			margin: Margin = None,
			margin_bottom: MarginBottom = None,
			margin_left: MarginLeft = None,
			margin_right: MarginRight = None,
			margin_top: MarginTop = None,
			max_height: MaxHeight = None,
			max_width: MaxWidth = None,
			min_height: MinHeight = None,
			min_width: MinWidth = None,
			opacity: Opacity = None,
			outline: Outline = None,
			outline_bottom_left_radius: OutlineBottomLeftRadius = None,
			outline_bottom_right_radius: OutlineBottomRightRadius = None,
			outline_color: OutlineColor = None,
			outline_radius: OutlineRadius = None,
			outline_style: OutlineStyle = None,
			outline_top_left_radius: OutlineTopLeftRadius = None,
			outline_top_right_radius: OutlineTopRightRadius = None,
			padding: Padding = None,
			padding_bottom: PaddingBottom = None,
			padding_left: PaddingLeft = None,
			padding_right: PaddingRight = None,
			padding_top: PaddingTop = None,
			selection_background_color: SelectionBackgroundColor = None,
			selection_color: SelectionColor = None,
			text_align: TextAlign = None,
			text_color: TextColor = None,
			text_decoration: TextDecoration = None,
			width: Width = None
	):
		self.style = ""
		self.style_sheet_object = None
		self.instances = {}
		#
		#
		#
		#
		if object_of_style is not None:
			self.set_style_sheet_object(object_of_style)
		#
		#
		#
		#
		if alternate_background_color is not None:
			self.add_alternate_background_color(alternate_background_color)
		#
		#
		#
		#
		if background is not None:
			self.add_background(background)
		#
		#
		#
		#
		if background_attachment is not None:
			self.add_background_attachment(background_attachment)
		#
		#
		#
		#
		if background_clip is not None:
			self.add_background_clip(background_clip)
		#
		#
		#
		#
		if background_color is not None:
			self.add_background_color(background_color)
		#
		#
		#
		#
		if background_image is not None:
			self.add_background_image(background_image)
		#
		#
		#
		#
		if background_origin is not None:
			self.add_background_origin(background_origin)
		#
		#
		#
		#
		if background_position is not None:
			self.add_background_position(background_position)
		#
		#
		#
		#
		if border is not None:
			self.add_border(border)
		#
		#
		#
		#
		if border_bottom is not None:
			self.add_border_bottom(border_bottom)
		#
		#
		#
		#
		if border_bottom_color is not None:
			self.add_border_bottom_color(border_bottom_color)
		#
		#
		#
		#
		if border_bottom_left_radius is not None:
			self.add_border_bottom_left_radius(border_bottom_left_radius)
		#
		#
		#
		#
		if border_bottom_right_radius is not None:
			self.add_border_bottom_right_radius(border_bottom_right_radius)
		#
		#
		#
		#
		if border_bottom_style is not None:
			self.add_border_bottom_style(border_bottom_style)
		#
		#
		#
		#
		if border_bottom_width is not None:
			self.add_border_bottom_width(border_bottom_width)
		#
		#
		#
		#
		if border_color is not None:
			self.add_border_color(border_color)
		#
		#
		#
		#
		if border_left is not None:
			self.add_border_left(border_left)
		#
		#
		#
		#
		if border_left_color is not None:
			self.add_border_left_color(border_left_color)
		#
		#
		#
		#
		if border_left_style is not None:
			self.add_border_left_style(border_left_style)
		#
		#
		#
		#
		if border_left_width is not None:
			self.add_border_left_width(border_left_width)
		#
		#
		#
		#
		if border_radius is not None:
			self.add_border_radius(border_radius)
		#
		#
		#
		#
		if border_right is not None:
			self.add_border_right(border_right)
		#
		#
		#
		#
		if border_right_color is not None:
			self.add_border_right_color(border_right_color)
		#
		#
		#
		#
		if border_right_style is not None:
			self.add_border_right_style(border_right_style)
		#
		#
		#
		#
		if border_right_width is not None:
			self.add_border_right_width(border_right_width)
		#
		#
		#
		#
		if border_top is not None:
			self.add_border_top(border_top)
		#
		#
		#
		#
		if border_top_color is not None:
			self.add_border_top_color(border_top_color)
		#
		#
		#
		#
		if border_top_left_radius is not None:
			self.add_border_top_left_radius(border_top_left_radius)
		#
		#
		#
		#
		if border_top_right_radius is not None:
			self.add_border_top_right_radius(border_top_right_radius)
		#
		#
		#
		#
		if border_top_style is not None:
			self.add_border_top_style(border_top_style)
		#
		#
		#
		#
		if border_top_width is not None:
			self.add_border_top_width(border_top_width)
		#
		#
		#
		#
		if border_width is not None:
			self.add_border_width(border_width)
		#
		#
		#
		#
		if borders_style is not None:
			self.add_border_style(borders_style)
		#
		#
		#
		#
		if font is not None:
			self.add_font(font)
		#
		#
		#
		#
		if height is not None:
			self.add_height(height)
		#
		#
		#
		#
		if image is not None:
			self.add_image(image)
		#
		#
		#
		#
		if image_position is not None:
			self.add_image_position(image_position)
		#
		#
		#
		#
		if margin is not None:
			self.add_margin(margin)
		#
		#
		#
		#
		if margin_bottom is not None:
			self.add_margin_bottom(margin_bottom)
		#
		#
		#
		#
		if margin_left is not None:
			self.add_margin_left(margin_left)
		#
		#
		#
		#
		if margin_right is not None:
			self.add_margin_right(margin_right)
		#
		#
		#
		#
		if margin_top is not None:
			self.add_margin_top(margin_top)
		#
		#
		#
		#
		if max_height is not None:
			self.add_max_height(max_height)
		#
		#
		#
		#
		if max_width is not None:
			self.add_max_width(max_width)
		#
		#
		#
		#
		if min_height is not None:
			self.add_min_height(min_height)
		#
		#
		#
		#
		if min_width is not None:
			self.add_min_width(min_width)
		#
		#
		#
		#
		if opacity is not None:
			self.add_opacity(opacity)
		#
		#
		#
		#
		if outline is not None:
			self.add_outline(outline)
		#
		#
		#
		#
		if outline_bottom_left_radius is not None:
			self.add_outline_bottom_left_radius(outline_bottom_left_radius)
		#
		#
		#
		#
		if outline_bottom_right_radius is not None:
			self.add_outline_bottom_right_radius(outline_bottom_right_radius)
		#
		#
		#
		#
		if outline_color is not None:
			self.add_outline_color(outline_color)
		#
		#
		#
		#
		if outline_radius is not None:
			self.add_outline_radius(outline_radius)
		#
		#
		#
		#
		if outline_style is not None:
			self.add_outline_style(outline_style)
		#
		#
		#
		#
		if outline_top_left_radius is not None:
			self.add_outline_top_left_radius(outline_top_left_radius)
		#
		#
		#
		#
		if outline_top_right_radius is not None:
			self.add_outline_top_right_radius(outline_top_right_radius)
		#
		#
		#
		#
		if padding is not None:
			self.add_padding(padding)
		#
		#
		#
		#
		if padding_bottom is not None:
			self.add_padding_bottom(padding_bottom)
		#
		#
		#
		#
		if padding_left is not None:
			self.add_padding_left(padding_left)
		#
		#
		#
		#
		if padding_right is not None:
			self.add_padding_right(padding_right)
		#
		#
		#
		#
		if padding_top is not None:
			self.add_padding_top(padding_top)
		#
		#
		#
		#
		if selection_background_color is not None:
			self.add_selection_background_color(selection_background_color)
		#
		#
		#
		#
		if selection_color is not None:
			self.add_selection_color(selection_color)
		#
		#
		#
		#
		if text_align is not None:
			self.add_text_align(text_align)
		#
		#
		#
		#
		if text_color is not None:
			self.add_text_color(text_color)
		#
		#
		#
		#
		if text_decoration is not None:
			self.add_text_decoration(text_decoration)
		#
		#
		#
		#
		if width is not None:
			self.add_width(width)
	#
	#
	#
	#
	def update_style(self):
		properties = list(filter(lambda item: item != "", self.instances.values()))

		if len(properties) > 0:
			if self.style_sheet_object is None:
				self.style = "{%s;}" % "; ".join(properties)
			else:
				self.style = "%s {%s;}" % (self.style_sheet_object.style_sheet_object, "; ".join(properties))
		else:
			self.style = "{}"

		return self
	#
	#
	#
	#
	def add_width(self, width: Width):
		self.instances["width"] = width.width
		return self.update_style()
	#
	#
	#
	#
	def add_text_decoration(self, text_decoration: TextDecoration):
		self.instances["text_decoration"] = text_decoration.text_decoration
		return self.update_style()
	#
	#
	#
	#
	def add_text_color(self, text_color: TextColor):
		self.instances["text_color"] = text_color.text_color
		return self.update_style()
	#
	#
	#
	#
	def add_text_align(self, text_align: TextAlign):
		self.instances["text_align"] = text_align.text_align
		return self.update_style()
	#
	#
	#
	#
	def add_selection_color(self, selection_color: SelectionColor):
		self.instances["selection_color"] = selection_color.selection_color
		return self.update_style()
	#
	#
	#
	#
	def add_selection_background_color(self, selection_background_color: SelectionBackgroundColor):
		self.instances["selection_background_color"] = selection_background_color.selection_background_color
		return self.update_style()
	#
	#
	#
	#
	def add_padding_top(self, padding_top: PaddingTop):
		self.instances["padding_top"] = padding_top.padding_top
		return self.update_style()
	#
	#
	#
	#
	def add_padding_right(self, padding_right: PaddingRight):
		self.instances["padding_right"] = padding_right.padding_right
		return self.update_style()
	#
	#
	#
	#
	def add_padding_left(self, padding_left: PaddingLeft):
		self.instances["padding_left"] = padding_left.padding_left
		return self.update_style()
	#
	#
	#
	#
	def add_padding_bottom(self, padding_bottom: PaddingBottom):
		self.instances["padding_bottom"] = padding_bottom.padding_bottom
		return self.update_style()
	#
	#
	#
	#
	def add_padding(self, padding: Padding):
		self.instances["padding"] = padding.padding
		return self.update_style()
	#
	#
	#
	#
	def add_outline_top_right_radius(self, outline_top_right_radius: OutlineTopRightRadius):
		self.instances["outline_top_right_radius"] = outline_top_right_radius.outline_top_right_radius
		return self.update_style()
	#
	#
	#
	#
	def add_outline_top_left_radius(self, outline_top_left_radius: OutlineTopLeftRadius):
		self.instances["outline_top_left_radius"] = outline_top_left_radius.outline_top_left_radius
		return self.update_style()
	#
	#
	#
	#
	def add_outline_style(self, outline_style: OutlineStyle):
		self.instances["outline_style"] = outline_style.outline_style
		return self.update_style()
	#
	#
	#
	#
	def add_outline_radius(self, outline_radius: OutlineRadius):
		self.instances["outline_radius"] = outline_radius.outline_radius
		return self.update_style()
	#
	#
	#
	#
	def add_outline_color(self, outline_color: OutlineColor):
		self.instances["outline_color"] = outline_color.outline_color
		return self.update_style()
	#
	#
	#
	#
	def add_outline_bottom_right_radius(self, outline_bottom_right_radius: OutlineBottomRightRadius):
		self.instances["outline_bottom_right_radius"] = outline_bottom_right_radius.outline_bottom_right_radius
		return self.update_style()
	#
	#
	#
	#
	def add_outline_bottom_left_radius(self, outline_bottom_left_radius: OutlineBottomLeftRadius):
		self.instances["outline_bottom_left_radius"] = outline_bottom_left_radius.outline_bottom_left_radius
		return self.update_style()
	#
	#
	#
	#
	def add_outline(self, outline: Outline):
		self.instances["outline"] = outline.outline
		return self.update_style()
	#
	#
	#
	#
	def add_opacity(self, opacity: Opacity):
		self.instances["opacity"] = opacity.opacity
		return self.update_style()
	#
	#
	#
	#
	def add_min_width(self, min_width: MinWidth):
		self.instances["min_width"] = min_width.min_width
		return self.update_style()
	#
	#
	#
	#
	def add_min_height(self, min_height: MinHeight):
		self.instances["min_height"] = min_height.min_height
		return self.update_style()
	#
	#
	#
	#
	def add_max_width(self, max_width: MaxWidth):
		self.instances["max_width"] = max_width.max_width
		return self.update_style()
	#
	#
	#
	#
	def add_max_height(self, max_height: MaxHeight):
		self.instances["max_height"] = max_height.max_height
		return self.update_style()
	#
	#
	#
	#
	def add_margin_top(self, margin_top: MarginTop):
		self.instances["margin_top"] = margin_top.margin_top
		return self.update_style()
	#
	#
	#
	#
	def add_margin_right(self, margin_right: MarginRight):
		self.instances["margin_right"] = margin_right.margin_right
		return self.update_style()
	#
	#
	#
	#
	def add_margin_left(self, margin_left: MarginLeft):
		self.instances["margin_left"] = margin_left.margin_left
		return self.update_style()
	#
	#
	#
	#
	def add_margin_bottom(self, margin_bottom: MarginBottom):
		self.instances["margin_bottom"] = margin_bottom.margin_bottom
		return self.update_style()
	#
	#
	#
	#
	def add_margin(self, margin: Margin):
		self.instances["margin"] = margin.margin
		return self.update_style()
	#
	#
	#
	#
	def add_image_position(self, image_position: ImagePosition):
		self.instances["image_position"] = image_position.image_position
		return self.update_style()
	#
	#
	#
	#
	def add_image(self, image: Image):
		self.instances["image"] = image.image
		return self.update_style()
	#
	#
	#
	#
	def add_height(self, height: Height):
		self.instances["height"] = height.height
		return self.update_style()
	#
	#
	#
	#
	def add_font(self, font: Font):
		self.instances["font"] = font.font
		return self.update_style()
	#
	#
	#
	#
	def add_border_style(self, borders_style: BordersStyle):
		self.instances["borders_style"] = borders_style.borders_style
		return self.update_style()
	#
	#
	#
	#
	def add_border_width(self, border_width: BorderWidth):
		self.instances["border_width"] = border_width.border_width
		return self.update_style()
	#
	#
	#
	#
	def add_border_top_width(self, border_top_width: BorderTopWidth):
		self.instances["border_top_width"] = border_top_width.border_top_width
		return self.update_style()
	#
	#
	#
	#
	def add_border_top_style(self, borders_top_style: BorderTopStyle):
		self.instances["borders_top_style"] = borders_top_style.borders_top_style
		return self.update_style()
	#
	#
	#
	#
	def add_border_top_right_radius(self, border_top_right_radius: BorderTopRightRadius):
		self.instances["border_top_right_radius"] = border_top_right_radius.border_top_right_radius
		return self.update_style()
	#
	#
	#
	#
	def add_border_top_left_radius(self, border_top_left_radius: BorderTopLeftRadius):
		self.instances["border_top_left_radius"] = border_top_left_radius.border_top_left_radius
		return self.update_style()
	#
	#
	#
	#
	def add_border_top_color(self, border_top_color: BorderTopColor):
		self.instances["border_top_color"] = border_top_color.border_top_color
		return self.update_style()
	#
	#
	#
	#
	def add_border_top(self, border_top: BorderTop):
		self.instances["border_top"] = border_top.border_top
		return self.update_style()
	#
	#
	#
	#
	def add_border_right_width(self, border_right_width: BorderRightWidth):
		self.instances["border_right_width"] = border_right_width.border_right_width
		return self.update_style()
	#
	#
	#
	#
	def add_border_right_style(self, borders_right_style: BorderRightStyle):
		self.instances["borders_right_style"] = borders_right_style.borders_right_style
		return self.update_style()
	#
	#
	#
	#
	def add_border_right_color(self, border_right_color: BorderRightColor):
		self.instances["border_right_color"] = border_right_color.border_right_color
		return self.update_style()
	#
	#
	#
	#
	def add_border_right(self, border_right: BorderRight):
		self.instances["border_right"] = border_right.border_right
		return self.update_style()
	#
	#
	#
	#
	def add_border_radius(self, border_radius: BorderRadius):
		self.instances["border_radius"] = border_radius.border_radius
		return self.update_style()
	#
	#
	#
	#
	def add_border_left_width(self, border_left_width: BorderLeftWidth):
		self.instances["border_left_width"] = border_left_width.border_left_width
		return self.update_style()
	#
	#
	#
	#
	def add_border_left_style(self, borders_left_style: BorderLeftStyle):
		self.instances["borders_left_style"] = borders_left_style.borders_left_style
		return self.update_style()
	#
	#
	#
	#
	def add_border_left_color(self, border_left_color: BorderLeftColor):
		self.instances["border_left_color"] = border_left_color.border_left_color
		return self.update_style()
	#
	#
	#
	#
	def add_border_left(self, border_left: BorderLeft):
		self.instances["border_left"] = border_left.border_left
		return self.update_style()
	#
	#
	#
	#
	def add_border_color(self, border_color: BorderColor):
		self.instances["border_color"] = border_color.border_color
		return self.update_style()
	#
	#
	#
	#
	def add_border_bottom_width(self, border_bottom_width: BorderBottomWidth):
		self.instances["border_bottom_width"] = border_bottom_width.border_bottom_width
		return self.update_style()
	#
	#
	#
	#
	def add_border_bottom_style(self, borders_bottom_style: BorderBottomStyle):
		self.instances["borders_bottom_style"] = borders_bottom_style.borders_bottom_style
		return self.update_style()
	#
	#
	#
	#
	def add_border_bottom_right_radius(self, border_bottom_right_radius: BorderBottomRightRadius):
		self.instances["border_bottom_right_radius"] = border_bottom_right_radius.border_bottom_right_radius
		return self.update_style()
	#
	#
	#
	#
	def add_border_bottom_left_radius(self, border_bottom_left_radius: BorderBottomLeftRadius):
		self.instances["border_bottom_left_radius"] = border_bottom_left_radius.border_bottom_left_radius
		return self.update_style()
	#
	#
	#
	#
	def add_border_bottom_color(self, border_bottom_color: BorderBottomColor):
		self.instances["border_bottom_color"] = border_bottom_color.border_bottom_color
		return self.update_style()
	#
	#
	#
	#
	def add_border_bottom(self, border_bottom: BorderBottom):
		self.instances["border_bottom"] = border_bottom.border_bottom
		return self.update_style()
	#
	#
	#
	#
	def add_border(self, border: Border):
		self.instances["border"] = border.border
		return self.update_style()
	#
	#
	#
	#
	def add_background_position(self, background_position: BackgroundPosition):
		self.instances["background_position"] = background_position.background_position
		return self.update_style()
	#
	#
	#
	#
	def add_background_origin(self, background_origin: BackgroundOrigin):
		self.instances["background_origin"] = background_origin.background_origin
		return self.update_style()
	#
	#
	#
	#
	def add_background_image(self, background_image: BackgroundImage):
		self.instances["background_image"] = background_image.background_image
		return self.update_style()
	#
	#
	#
	#
	def add_background_color(self, background_color: BackgroundColor):
		self.instances["background_color"] = background_color.background_color
		return self.update_style()
	#
	#
	#
	#
	def add_background_clip(self, background_clip: BackgroundClip):
		self.instances["background_clip"] = background_clip.background_clip
		return self.update_style()
	#
	#
	#
	#
	def add_background_attachment(self, background_attachment: BackgroundAttachment):
		self.instances["background_attachment"] = background_attachment.background_attachment
		return self.update_style()
	#
	#
	#
	#
	def add_background(self, background: Background):
		self.instances["background"] = background.background
		return self.update_style()
	#
	#
	#
	#
	def add_alternate_background_color(self, alternate_background_color: AlternateBackgroundColor):
		self.instances["alternate_background_color"] = alternate_background_color.alternate_background_color
		return self.update_style()
	#
	#
	#
	#
	def set_style_sheet_object(self, object_of_style: ObjectOfStyle | list[ObjectOfStyle]):
		self.style_sheet_object = StyleSheetObject(object_of_style)
		return self.update_style()
#
#
#
#
class BaseStyleSheet:
	#
	#
	#
	#
	def __init__(self):
		self.style_sheet = ""
		self.instances = {}
	#
	#
	#
	#
	def update_style_sheet(self):
		self.style_sheet = " ".join(list(filter(lambda item: item != "", self.instances.values())))
		return self
	#
	#
	#
	#
	def add_style(self, style: BaseStyle):
		self.instances[style.style_sheet_object.style_sheet_object] = style.style
		return self.update_style_sheet()

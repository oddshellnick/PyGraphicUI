from PyGraphicUI.StyleSheets.utilities.Background import (
    AlternateBackgroundColor,
    Background,
    BackgroundAttachment,
    BackgroundClip,
    BackgroundColor,
    BackgroundImage,
    BackgroundOrigin,
    BackgroundPosition,
)
from PyGraphicUI.StyleSheets.utilities.Border import (
    Border,
    BorderBottom,
    BorderLeft,
    BorderRight,
    BorderTop,
)
from PyGraphicUI.StyleSheets.utilities.BorderColor import (
    BorderBottomColor,
    BorderColor,
    BorderLeftColor,
    BorderRightColor,
    BorderTopColor,
)
from PyGraphicUI.StyleSheets.utilities.BorderRadius import (
    BorderBottomLeftRadius,
    BorderBottomRightRadius,
    BorderRadius,
    BorderTopLeftRadius,
    BorderTopRightRadius,
)
from PyGraphicUI.StyleSheets.utilities.BorderStyle import (
    BorderBottomStyle,
    BorderLeftStyle,
    BorderRightStyle,
    BordersStyle,
    BorderTopStyle,
)
from PyGraphicUI.StyleSheets.utilities.BorderWidth import (
    BorderBottomWidth,
    BorderLeftWidth,
    BorderRightWidth,
    BorderTopWidth,
    BorderWidth,
)
from PyGraphicUI.StyleSheets.utilities.Font import Font
from PyGraphicUI.StyleSheets.utilities.Image import Image, ImagePosition
from PyGraphicUI.StyleSheets.utilities.Margin import (
    Margin,
    MarginBottom,
    MarginLeft,
    MarginRight,
    MarginTop,
)
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import (
    ObjectOfStyle,
    StyleSheetObject,
)
from PyGraphicUI.StyleSheets.utilities.Opacity import Opacity
from PyGraphicUI.StyleSheets.utilities.Outline import (
    Outline,
    OutlineBottomLeftRadius,
    OutlineBottomRightRadius,
    OutlineColor,
    OutlineRadius,
    OutlineStyle,
    OutlineTopLeftRadius,
    OutlineTopRightRadius,
)
from PyGraphicUI.StyleSheets.utilities.Padding import (
    Padding,
    PaddingBottom,
    PaddingLeft,
    PaddingRight,
    PaddingTop,
)
from PyGraphicUI.StyleSheets.utilities.Selection import (
    SelectionBackgroundColor,
    SelectionColor,
)
from PyGraphicUI.StyleSheets.utilities.Size import (
    Height,
    MaxHeight,
    MaxWidth,
    MinHeight,
    MinWidth,
    Width,
)
from PyGraphicUI.StyleSheets.utilities.Text import TextAlign, TextColor, TextDecoration


class BaseStyle:
    """
    Base class for all style classes.

    Attributes:
        style (str): The CSS style string.
        style_sheet_object (StyleSheetObject | None): The style sheet object that the style is applied to.
        instances (dict): A dictionary of style properties and their values.

    :Usage:
        style = BaseStyle(object_of_style=ObjectOfStyle(css_objects=CssObject(widget="QWidget")))
        style.add_background_color(BackgroundColor(Brush(Color(RGB(100, 100, 100)))))
        print(style.style)
        "QWidget {background-color: rgb(100, 100, 100);}"
    """

    def __init__(
        self,
        object_of_style: ObjectOfStyle | list[ObjectOfStyle] | None = None,
        alternate_background_color: AlternateBackgroundColor | None = None,
        background: Background | None = None,
        background_attachment: BackgroundAttachment | None = None,
        background_clip: BackgroundClip | None = None,
        background_color: BackgroundColor | None = None,
        background_image: BackgroundImage | None = None,
        background_origin: BackgroundOrigin | None = None,
        background_position: BackgroundPosition | None = None,
        border: Border | None = None,
        border_bottom: BorderBottom | None = None,
        border_bottom_color: BorderBottomColor | None = None,
        border_bottom_left_radius: BorderBottomLeftRadius | None = None,
        border_bottom_right_radius: BorderBottomRightRadius | None = None,
        border_bottom_style: BorderBottomStyle | None = None,
        border_bottom_width: BorderBottomWidth | None = None,
        border_color: BorderColor | None = None,
        border_left: BorderLeft | None = None,
        border_left_color: BorderLeftColor | None = None,
        border_left_style: BorderLeftStyle | None = None,
        border_left_width: BorderLeftWidth | None = None,
        border_radius: BorderRadius | None = None,
        border_right: BorderRight | None = None,
        border_right_color: BorderRightColor | None = None,
        border_right_style: BorderRightStyle | None = None,
        border_right_width: BorderRightWidth | None = None,
        border_top: BorderTop | None = None,
        border_top_color: BorderTopColor | None = None,
        border_top_left_radius: BorderTopLeftRadius | None = None,
        border_top_right_radius: BorderTopRightRadius | None = None,
        border_top_style: BorderTopStyle | None = None,
        border_top_width: BorderTopWidth | None = None,
        border_width: BorderWidth | None = None,
        borders_style: BordersStyle | None = None,
        font: Font | None = None,
        height: Height | None = None,
        image: Image | None = None,
        image_position: ImagePosition | None = None,
        margin: Margin | None = None,
        margin_bottom: MarginBottom | None = None,
        margin_left: MarginLeft | None = None,
        margin_right: MarginRight | None = None,
        margin_top: MarginTop | None = None,
        max_height: MaxHeight | None = None,
        max_width: MaxWidth | None = None,
        min_height: MinHeight | None = None,
        min_width: MinWidth | None = None,
        opacity: Opacity | None = None,
        outline: Outline | None = None,
        outline_bottom_left_radius: OutlineBottomLeftRadius | None = None,
        outline_bottom_right_radius: OutlineBottomRightRadius | None = None,
        outline_color: OutlineColor | None = None,
        outline_radius: OutlineRadius | None = None,
        outline_style: OutlineStyle | None = None,
        outline_top_left_radius: OutlineTopLeftRadius | None = None,
        outline_top_right_radius: OutlineTopRightRadius | None = None,
        padding: Padding | None = None,
        padding_bottom: PaddingBottom | None = None,
        padding_left: PaddingLeft | None = None,
        padding_right: PaddingRight | None = None,
        padding_top: PaddingTop | None = None,
        selection_background_color: SelectionBackgroundColor | None = None,
        selection_color: SelectionColor | None = None,
        text_align: TextAlign | None = None,
        text_color: TextColor | None = None,
        text_decoration: TextDecoration | None = None,
        width: Width | None = None,
    ):
        """
        Initializes a BaseStyle object.

        Args:
            object_of_style (ObjectOfStyle | list[ObjectOfStyle] | None): The style sheet object or list of objects that the style is applied to.
            alternate_background_color (AlternateBackgroundColor | None): The alternate background color value.
            background (Background | None): The background value.
            background_attachment (BackgroundAttachment | None): The background attachment value.
            background_clip (BackgroundClip | None): The background clip value.
            background_color (BackgroundColor | None): The background color value.
            background_image (BackgroundImage | None): The background image value.
            background_origin (BackgroundOrigin | None): The background origin value.
            background_position (BackgroundPosition | None): The background position value.
            border (Border | None): The border value.
            border_bottom (BorderBottom | None): The border bottom value.
            border_bottom_color (BorderBottomColor | None): The border bottom color value.
            border_bottom_left_radius (BorderBottomLeftRadius | None): The border bottom left radius value.
            border_bottom_right_radius (BorderBottomRightRadius | None): The border bottom right radius value.
            border_bottom_style (BorderBottomStyle | None): The border bottom style value.
            border_bottom_width (BorderBottomWidth | None): The border bottom width value.
            border_color (BorderColor | None): The border color value.
            border_left (BorderLeft | None): The border left value.
            border_left_color (BorderLeftColor | None): The border left color value.
            border_left_style (BorderLeftStyle | None): The border left style value.
            border_left_width (BorderLeftWidth | None): The border left width value.
            border_radius (BorderRadius | None): The border radius value.
            border_right (BorderRight | None): The border right value.
            border_right_color (BorderRightColor | None): The border right color value.
            border_right_style (BorderRightStyle | None): The border right style value.
            border_right_width (BorderRightWidth | None): The border right width value.
            border_top (BorderTop | None): The border top value.
            border_top_color (BorderTopColor | None): The border top color value.
            border_top_left_radius (BorderTopLeftRadius | None): The border top left radius value.
            border_top_right_radius (BorderTopRightRadius | None): The border top right radius value.
            border_top_style (BorderTopStyle | None): The border top style value.
            border_top_width (BorderTopWidth | None): The border top width value.
            border_width (BorderWidth | None): The border width value.
            borders_style (BordersStyle | None): The border style value.
            font (Font | None): The font value.
            height (Height | None): The height value.
            image (Image | None): The image value.
            image_position (ImagePosition | None): The image position value.
            margin (Margin | None): The margin value.
            margin_bottom (MarginBottom | None): The margin bottom value.
            margin_left (MarginLeft | None): The margin left value.
            margin_right (MarginRight | None): The margin right value.
            margin_top (MarginTop | None): The margin top value.
            max_height (MaxHeight | None): The maximum height value.
            max_width (MaxWidth | None): The maximum width value.
            min_height (MinHeight | None): The minimum height value.
            min_width (MinWidth | None): The minimum width value.
            opacity (Opacity | None): The opacity value.
            outline (Outline | None): The outline value.
            outline_bottom_left_radius (OutlineBottomLeftRadius | None): The outline bottom left radius value.
            outline_bottom_right_radius (OutlineBottomRightRadius | None): The outline bottom right radius value.
            outline_color (OutlineColor | None): The outline color value.
            outline_radius (OutlineRadius | None): The outline radius value.
            outline_style (OutlineStyle | None): The outline style value.
            outline_top_left_radius (OutlineTopLeftRadius | None): The outline top left radius value.
            outline_top_right_radius (OutlineTopRightRadius | None): The outline top right radius value.
            padding (Padding | None): The padding value.
            padding_bottom (PaddingBottom | None): The padding bottom value.
            padding_left (PaddingLeft | None): The padding left value.
            padding_right (PaddingRight | None): The padding right value.
            padding_top (PaddingTop | None): The padding top value.
            selection_background_color (SelectionBackgroundColor | None): The selection background color value.
            selection_color (SelectionColor | None): The selection color value.
            text_align (TextAlign | None): The text alignment value.
            text_color (TextColor | None): The text color value.
            text_decoration (TextDecoration | None): The text decoration value.
            width (Width | None): The width value.
        """
        self.style = ""
        self.style_sheet_object: StyleSheetObject | None = None
        self.instances: dict[str, str] = {}

        if object_of_style is not None:
            self.set_style_sheet_object(object_of_style)

        if alternate_background_color is not None:
            self.add_alternate_background_color(alternate_background_color)

        if background is not None:
            self.add_background(background)

        if background_attachment is not None:
            self.add_background_attachment(background_attachment)

        if background_clip is not None:
            self.add_background_clip(background_clip)

        if background_color is not None:
            self.add_background_color(background_color)

        if background_image is not None:
            self.add_background_image(background_image)

        if background_origin is not None:
            self.add_background_origin(background_origin)

        if background_position is not None:
            self.add_background_position(background_position)

        if border is not None:
            self.add_border(border)

        if border_bottom is not None:
            self.add_border_bottom(border_bottom)

        if border_bottom_color is not None:
            self.add_border_bottom_color(border_bottom_color)

        if border_bottom_left_radius is not None:
            self.add_border_bottom_left_radius(border_bottom_left_radius)

        if border_bottom_right_radius is not None:
            self.add_border_bottom_right_radius(border_bottom_right_radius)

        if border_bottom_style is not None:
            self.add_border_bottom_style(border_bottom_style)

        if border_bottom_width is not None:
            self.add_border_bottom_width(border_bottom_width)

        if border_color is not None:
            self.add_border_color(border_color)

        if border_left is not None:
            self.add_border_left(border_left)

        if border_left_color is not None:
            self.add_border_left_color(border_left_color)

        if border_left_style is not None:
            self.add_border_left_style(border_left_style)

        if border_left_width is not None:
            self.add_border_left_width(border_left_width)

        if border_radius is not None:
            self.add_border_radius(border_radius)

        if border_right is not None:
            self.add_border_right(border_right)

        if border_right_color is not None:
            self.add_border_right_color(border_right_color)

        if border_right_style is not None:
            self.add_border_right_style(border_right_style)

        if border_right_width is not None:
            self.add_border_right_width(border_right_width)

        if border_top is not None:
            self.add_border_top(border_top)

        if border_top_color is not None:
            self.add_border_top_color(border_top_color)

        if border_top_left_radius is not None:
            self.add_border_top_left_radius(border_top_left_radius)

        if border_top_right_radius is not None:
            self.add_border_top_right_radius(border_top_right_radius)

        if border_top_style is not None:
            self.add_border_top_style(border_top_style)

        if border_top_width is not None:
            self.add_border_top_width(border_top_width)

        if border_width is not None:
            self.add_border_width(border_width)

        if borders_style is not None:
            self.add_border_style(borders_style)

        if font is not None:
            self.add_font(font)

        if height is not None:
            self.add_height(height)

        if image is not None:
            self.add_image(image)

        if image_position is not None:
            self.add_image_position(image_position)

        if margin is not None:
            self.add_margin(margin)

        if margin_bottom is not None:
            self.add_margin_bottom(margin_bottom)

        if margin_left is not None:
            self.add_margin_left(margin_left)

        if margin_right is not None:
            self.add_margin_right(margin_right)

        if margin_top is not None:
            self.add_margin_top(margin_top)

        if max_height is not None:
            self.add_max_height(max_height)

        if max_width is not None:
            self.add_max_width(max_width)

        if min_height is not None:
            self.add_min_height(min_height)

        if min_width is not None:
            self.add_min_width(min_width)

        if opacity is not None:
            self.add_opacity(opacity)

        if outline is not None:
            self.add_outline(outline)

        if outline_bottom_left_radius is not None:
            self.add_outline_bottom_left_radius(outline_bottom_left_radius)

        if outline_bottom_right_radius is not None:
            self.add_outline_bottom_right_radius(outline_bottom_right_radius)

        if outline_color is not None:
            self.add_outline_color(outline_color)

        if outline_radius is not None:
            self.add_outline_radius(outline_radius)

        if outline_style is not None:
            self.add_outline_style(outline_style)

        if outline_top_left_radius is not None:
            self.add_outline_top_left_radius(outline_top_left_radius)

        if outline_top_right_radius is not None:
            self.add_outline_top_right_radius(outline_top_right_radius)

        if padding is not None:
            self.add_padding(padding)

        if padding_bottom is not None:
            self.add_padding_bottom(padding_bottom)

        if padding_left is not None:
            self.add_padding_left(padding_left)

        if padding_right is not None:
            self.add_padding_right(padding_right)

        if padding_top is not None:
            self.add_padding_top(padding_top)

        if selection_background_color is not None:
            self.add_selection_background_color(selection_background_color)

        if selection_color is not None:
            self.add_selection_color(selection_color)

        if text_align is not None:
            self.add_text_align(text_align)

        if text_color is not None:
            self.add_text_color(text_color)

        if text_decoration is not None:
            self.add_text_decoration(text_decoration)

        if width is not None:
            self.add_width(width)

    def update_style(self) -> "BaseStyle":
        """
        Updates the CSS style string.

        Returns:
            BaseStyle: The updated style object.
        """
        properties = list(filter(lambda item: item != "", self.instances.values()))

        if len(properties) > 0:
            if self.style_sheet_object is None:
                self.style = "{%s;}" % "; ".join(properties)
            else:
                self.style = "%s {%s;}" % (self.style_sheet_object.style_sheet_object, "; ".join(properties))
        else:
            self.style = "{}"

        return self

    def add_width(self, width: Width) -> "BaseStyle":
        """
        Adds the width style property.

        Args:
            width (Width): The width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["width"] = width.width
        return self.update_style()

    def add_text_decoration(self, text_decoration: TextDecoration) -> "BaseStyle":
        """
        Adds the text decoration style property.

        Args:
            text_decoration (TextDecoration): The text decoration object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["text_decoration"] = text_decoration.text_decoration
        return self.update_style()

    def add_text_color(self, text_color: TextColor) -> "BaseStyle":
        """
        Adds the text color style property.

        Args:
            text_color (TextColor): The text color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["text_color"] = text_color.text_color
        return self.update_style()

    def add_text_align(self, text_align: TextAlign) -> "BaseStyle":
        """
        Adds the text align style property.

        Args:
            text_align (TextAlign): The text align object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["text_align"] = text_align.text_align
        return self.update_style()

    def add_selection_color(self, selection_color: SelectionColor) -> "BaseStyle":
        """
        Adds the selection color style property.

        Args:
            selection_color (SelectionColor): The selection color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["selection_color"] = selection_color.selection_color
        return self.update_style()

    def add_selection_background_color(self, selection_background_color: SelectionBackgroundColor) -> "BaseStyle":
        """
        Adds the selection background color style property.

        Args:
            selection_background_color (SelectionBackgroundColor): The selection background color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["selection_background_color"] = selection_background_color.selection_background_color
        return self.update_style()

    def add_padding_top(self, padding_top: PaddingTop) -> "BaseStyle":
        """
        Adds the padding top style property.

        Args:
            padding_top (PaddingTop): The padding top object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["padding_top"] = padding_top.padding_top
        return self.update_style()

    def add_padding_right(self, padding_right: PaddingRight) -> "BaseStyle":
        """
        Adds the padding right style property.

        Args:
            padding_right (PaddingRight): The padding right object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["padding_right"] = padding_right.padding_right
        return self.update_style()

    def add_padding_left(self, padding_left: PaddingLeft) -> "BaseStyle":
        """
        Adds the padding left style property.

        Args:
            padding_left (PaddingLeft): The padding left object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["padding_left"] = padding_left.padding_left
        return self.update_style()

    def add_padding_bottom(self, padding_bottom: PaddingBottom) -> "BaseStyle":
        """
        Adds the padding bottom style property.

        Args:
            padding_bottom (PaddingBottom): The padding bottom object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["padding_bottom"] = padding_bottom.padding_bottom
        return self.update_style()

    def add_padding(self, padding: Padding) -> "BaseStyle":
        """
        Adds the padding style property.

        Args:
            padding (Padding): The padding object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["padding"] = padding.padding
        return self.update_style()

    def add_outline_top_right_radius(self, outline_top_right_radius: OutlineTopRightRadius) -> "BaseStyle":
        """
        Adds the outline top right radius style property.

        Args:
            outline_top_right_radius (OutlineTopRightRadius): The outline top right radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline_top_right_radius"] = outline_top_right_radius.outline_top_right_radius
        return self.update_style()

    def add_outline_top_left_radius(self, outline_top_left_radius: OutlineTopLeftRadius) -> "BaseStyle":
        """
        Adds the outline top left radius style property.

        Args:
            outline_top_left_radius (OutlineTopLeftRadius): The outline top left radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline_top_left_radius"] = outline_top_left_radius.outline_top_left_radius
        return self.update_style()

    def add_outline_style(self, outline_style: OutlineStyle) -> "BaseStyle":
        """
        Adds the outline style style property.

        Args:
            outline_style (OutlineStyle): The outline style object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline_style"] = outline_style.outline_style
        return self.update_style()

    def add_outline_radius(self, outline_radius: OutlineRadius) -> "BaseStyle":
        """
        Adds the outline radius style property.

        Args:
            outline_radius (OutlineRadius): The outline radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline_radius"] = outline_radius.outline_radius
        return self.update_style()

    def add_outline_color(self, outline_color: OutlineColor) -> "BaseStyle":
        """
        Adds the outline color style property.

        Args:
            outline_color (OutlineColor): The outline color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline_color"] = outline_color.outline_color
        return self.update_style()

    def add_outline_bottom_right_radius(self, outline_bottom_right_radius: OutlineBottomRightRadius) -> "BaseStyle":
        """
        Adds the outline bottom right radius style property.

        Args:
            outline_bottom_right_radius (OutlineBottomRightRadius): The outline bottom right radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline_bottom_right_radius"] = outline_bottom_right_radius.outline_bottom_right_radius
        return self.update_style()

    def add_outline_bottom_left_radius(self, outline_bottom_left_radius: OutlineBottomLeftRadius) -> "BaseStyle":
        """
        Adds the outline bottom left radius style property.

        Args:
            outline_bottom_left_radius (OutlineBottomLeftRadius): The outline bottom left radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline_bottom_left_radius"] = outline_bottom_left_radius.outline_bottom_left_radius
        return self.update_style()

    def add_outline(self, outline: Outline) -> "BaseStyle":
        """
        Adds the outline style property.

        Args:
            outline (Outline): The outline object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["outline"] = outline.outline
        return self.update_style()

    def add_opacity(self, opacity: Opacity) -> "BaseStyle":
        """
        Adds the opacity style property.

        Args:
            opacity (Opacity): The opacity object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["opacity"] = opacity.opacity
        return self.update_style()

    def add_min_width(self, min_width: MinWidth) -> "BaseStyle":
        """
        Adds the min width style property.

        Args:
            min_width (MinWidth): The min width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["min_width"] = min_width.min_width
        return self.update_style()

    def add_min_height(self, min_height: MinHeight) -> "BaseStyle":
        """
        Adds the min height style property.

        Args:
            min_height (MinHeight): The min height object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["min_height"] = min_height.min_height
        return self.update_style()

    def add_max_width(self, max_width: MaxWidth) -> "BaseStyle":
        """
        Adds the max width style property.

        Args:
            max_width (MaxWidth): The max width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["max_width"] = max_width.max_width
        return self.update_style()

    def add_max_height(self, max_height: MaxHeight) -> "BaseStyle":
        """
        Adds the max height style property.

        Args:
            max_height (MaxHeight): The max height object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["max_height"] = max_height.max_height
        return self.update_style()

    def add_margin_top(self, margin_top: MarginTop) -> "BaseStyle":
        """
        Adds the margin top style property.

        Args:
            margin_top (MarginTop): The margin top object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["margin_top"] = margin_top.margin_top
        return self.update_style()

    def add_margin_right(self, margin_right: MarginRight) -> "BaseStyle":
        """
        Adds the margin right style property.

        Args:
            margin_right (MarginRight): The margin right object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["margin_right"] = margin_right.margin_right
        return self.update_style()

    def add_margin_left(self, margin_left: MarginLeft) -> "BaseStyle":
        """
        Adds the margin left style property.

        Args:
            margin_left (MarginLeft): The margin left object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["margin_left"] = margin_left.margin_left
        return self.update_style()

    def add_margin_bottom(self, margin_bottom: MarginBottom) -> "BaseStyle":
        """
        Adds the margin bottom style property.

        Args:
            margin_bottom (MarginBottom): The margin bottom object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["margin_bottom"] = margin_bottom.margin_bottom
        return self.update_style()

    def add_margin(self, margin: Margin) -> "BaseStyle":
        """
        Adds the margin style property.

        Args:
            margin (Margin): The margin object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["margin"] = margin.margin
        return self.update_style()

    def add_image_position(self, image_position: ImagePosition) -> "BaseStyle":
        """
        Adds the image position style property.

        Args:
            image_position (ImagePosition): The image position object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["image_position"] = image_position.image_position
        return self.update_style()

    def add_image(self, image: Image) -> "BaseStyle":
        """
        Adds the image style property.

        Args:
            image (Image): The image object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["image"] = image.image
        return self.update_style()

    def add_height(self, height: Height) -> "BaseStyle":
        """
        Adds the height style property.

        Args:
            height (Height): The height object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["height"] = height.height
        return self.update_style()

    def add_font(self, font: Font) -> "BaseStyle":
        """
        Adds the font style property.

        Args:
            font (Font): The font object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["font"] = font.font
        return self.update_style()

    def add_border_style(self, borders_style: BordersStyle) -> "BaseStyle":
        """
        Adds the border style style property.

        Args:
            borders_style (BordersStyle): The border style object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["borders_style"] = borders_style.borders_style
        return self.update_style()

    def add_border_width(self, border_width: BorderWidth) -> "BaseStyle":
        """
        Adds the border width style property.

        Args:
            border_width (BorderWidth): The border width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_width"] = border_width.border_width
        return self.update_style()

    def add_border_top_width(self, border_top_width: BorderTopWidth) -> "BaseStyle":
        """
        Adds the border top width style property.

        Args:
            border_top_width (BorderTopWidth): The border top width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_top_width"] = border_top_width.border_top_width
        return self.update_style()

    def add_border_top_style(self, borders_top_style: BorderTopStyle) -> "BaseStyle":
        """
        Adds the border top style style property.

        Args:
            borders_top_style (BorderTopStyle): The border top style object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["borders_top_style"] = borders_top_style.borders_top_style
        return self.update_style()

    def add_border_top_right_radius(self, border_top_right_radius: BorderTopRightRadius) -> "BaseStyle":
        """
        Adds the border top right radius style property.

        Args:
            border_top_right_radius (BorderTopRightRadius): The border top right radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_top_right_radius"] = border_top_right_radius.border_top_right_radius
        return self.update_style()

    def add_border_top_left_radius(self, border_top_left_radius: BorderTopLeftRadius) -> "BaseStyle":
        """
        Adds the border top left radius style property.

        Args:
            border_top_left_radius (BorderTopLeftRadius): The border top left radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_top_left_radius"] = border_top_left_radius.border_top_left_radius
        return self.update_style()

    def add_border_top_color(self, border_top_color: BorderTopColor) -> "BaseStyle":
        """
        Adds the border top color style property.

        Args:
            border_top_color (BorderTopColor): The border top color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_top_color"] = border_top_color.border_top_color
        return self.update_style()

    def add_border_top(self, border_top: BorderTop) -> "BaseStyle":
        """
        Adds the border top style property.

        Args:
            border_top (BorderTop): The border top object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_top"] = border_top.border_top
        return self.update_style()

    def add_border_right_width(self, border_right_width: BorderRightWidth) -> "BaseStyle":
        """
        Adds the border right width style property.

        Args:
            border_right_width (BorderRightWidth): The border right width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_right_width"] = border_right_width.border_right_width
        return self.update_style()

    def add_border_right_style(self, borders_right_style: BorderRightStyle) -> "BaseStyle":
        """
        Adds the border right style style property.

        Args:
            borders_right_style (BorderRightStyle): The border right style object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["borders_right_style"] = borders_right_style.borders_right_style
        return self.update_style()

    def add_border_right_color(self, border_right_color: BorderRightColor) -> "BaseStyle":
        """
        Adds the border right color style property.

        Args:
            border_right_color (BorderRightColor): The border right color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_right_color"] = border_right_color.border_right_color
        return self.update_style()

    def add_border_right(self, border_right: BorderRight) -> "BaseStyle":
        """
        Adds the border right style property.

        Args:
            border_right (BorderRight): The border right object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_right"] = border_right.border_right
        return self.update_style()

    def add_border_radius(self, border_radius: BorderRadius) -> "BaseStyle":
        """
        Adds the border radius style property.

        Args:
            border_radius (BorderRadius): The border radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_radius"] = border_radius.border_radius
        return self.update_style()

    def add_border_left_width(self, border_left_width: BorderLeftWidth) -> "BaseStyle":
        """
        Adds the border left width style property.

        Args:
            border_left_width (BorderLeftWidth): The border left width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_left_width"] = border_left_width.border_left_width
        return self.update_style()

    def add_border_left_style(self, borders_left_style: BorderLeftStyle) -> "BaseStyle":
        """
        Adds the border left style style property.

        Args:
            borders_left_style (BorderLeftStyle): The border left style object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["borders_left_style"] = borders_left_style.borders_left_style
        return self.update_style()

    def add_border_left_color(self, border_left_color: BorderLeftColor) -> "BaseStyle":
        """
        Adds the border left color style property.

        Args:
            border_left_color (BorderLeftColor): The border left color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_left_color"] = border_left_color.border_left_color
        return self.update_style()

    def add_border_left(self, border_left: BorderLeft) -> "BaseStyle":
        """
        Adds the border left style property.

        Args:
            border_left (BorderLeft): The border left object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_left"] = border_left.border_left
        return self.update_style()

    def add_border_color(self, border_color: BorderColor) -> "BaseStyle":
        """
        Adds the border color style property.

        Args:
            border_color (BorderColor): The border color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_color"] = border_color.border_color
        return self.update_style()

    def add_border_bottom_width(self, border_bottom_width: BorderBottomWidth) -> "BaseStyle":
        """
        Adds the border bottom width style property.

        Args:
            border_bottom_width (BorderBottomWidth): The border bottom width object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_bottom_width"] = border_bottom_width.border_bottom_width
        return self.update_style()

    def add_border_bottom_style(self, borders_bottom_style: BorderBottomStyle) -> "BaseStyle":
        """
        Adds the border bottom style style property.

        Args:
            borders_bottom_style (BorderBottomStyle): The border bottom style object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["borders_bottom_style"] = borders_bottom_style.borders_bottom_style
        return self.update_style()

    def add_border_bottom_right_radius(self, border_bottom_right_radius: BorderBottomRightRadius) -> "BaseStyle":
        """
        Adds the border bottom right radius style property.

        Args:
            border_bottom_right_radius (BorderBottomRightRadius): The border bottom right radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_bottom_right_radius"] = border_bottom_right_radius.border_bottom_right_radius
        return self.update_style()

    def add_border_bottom_left_radius(self, border_bottom_left_radius: BorderBottomLeftRadius) -> "BaseStyle":
        """
        Adds the border bottom left radius style property.

        Args:
            border_bottom_left_radius (BorderBottomLeftRadius): The border bottom left radius object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_bottom_left_radius"] = border_bottom_left_radius.border_bottom_left_radius
        return self.update_style()

    def add_border_bottom_color(self, border_bottom_color: BorderBottomColor) -> "BaseStyle":
        """
        Adds the border bottom color style property.

        Args:
            border_bottom_color (BorderBottomColor): The border bottom color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_bottom_color"] = border_bottom_color.border_bottom_color
        return self.update_style()

    def add_border_bottom(self, border_bottom: BorderBottom) -> "BaseStyle":
        """
        Adds the border bottom style property.

        Args:
            border_bottom (BorderBottom): The border bottom object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border_bottom"] = border_bottom.border_bottom
        return self.update_style()

    def add_border(self, border: Border) -> "BaseStyle":
        """
        Adds the border style property.

        Args:
            border (Border): The border object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["border"] = border.border
        return self.update_style()

    def add_background_position(self, background_position: BackgroundPosition) -> "BaseStyle":
        """
        Adds the background position style property.

        Args:
            background_position (BackgroundPosition): The background position object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["background_position"] = background_position.background_position
        return self.update_style()

    def add_background_origin(self, background_origin: BackgroundOrigin) -> "BaseStyle":
        """
        Adds the background origin style property.

        Args:
            background_origin (BackgroundOrigin): The background origin object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["background_origin"] = background_origin.background_origin
        return self.update_style()

    def add_background_image(self, background_image: BackgroundImage) -> "BaseStyle":
        """
        Adds the background image style property.

        Args:
            background_image (BackgroundImage): The background image object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["background_image"] = background_image.background_image
        return self.update_style()

    def add_background_color(self, background_color: BackgroundColor) -> "BaseStyle":
        """
        Adds the background color style property.

        Args:
            background_color (BackgroundColor): The background color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["background_color"] = background_color.background_color
        return self.update_style()

    def add_background_clip(self, background_clip: BackgroundClip) -> "BaseStyle":
        """
        Adds the background clip style property.

        Args:
            background_clip (BackgroundClip): The background clip object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["background_clip"] = background_clip.background_clip
        return self.update_style()

    def add_background_attachment(self, background_attachment: BackgroundAttachment) -> "BaseStyle":
        """
        Adds the background attachment style property.

        Args:
            background_attachment (BackgroundAttachment): The background attachment object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["background_attachment"] = background_attachment.background_attachment
        return self.update_style()

    def add_background(self, background: Background) -> "BaseStyle":
        """
        Adds the background style property.

        Args:
            background (Background): The background object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["background"] = background.background
        return self.update_style()

    def add_alternate_background_color(self, alternate_background_color: AlternateBackgroundColor) -> "BaseStyle":
        """
        Adds the alternate background color style property.

        Args:
            alternate_background_color (AlternateBackgroundColor): The alternate background color object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.instances["alternate_background_color"] = alternate_background_color.alternate_background_color
        return self.update_style()

    def set_style_sheet_object(self, object_of_style: ObjectOfStyle | list[ObjectOfStyle]) -> "BaseStyle":
        """
        Sets the style sheet object that the style is applied to.

        Args:
            object_of_style (ObjectOfStyle | list[ObjectOfStyle]): The style sheet object.

        Returns:
            BaseStyle: The updated style object.
        """
        self.style_sheet_object = StyleSheetObject(object_of_style)
        return self.update_style()


class BaseStyleSheet:
    """
    Base class for all style sheet classes.

    Attributes:
        style_sheet (str): The CSS style sheet string.
        instances (dict): A dictionary of style sheet objects and their styles.

    :Usage:
        style = BaseStyle(object_of_style=ObjectOfStyle(css_objects=CssObject(widget="QWidget")))
        style.add_background_color(BackgroundColor(Brush(Color(RGB(100, 100, 100)))))
        style_sheet = BaseStyleSheet()
        style_sheet.add_style(style)
        style_sheet.style_sheet
        "QWidget {background-color: rgb(100, 100, 100);}"
    """

    def __init__(self):
        """
        Initializes a BaseStyleSheet object.
        """
        self.style_sheet = ""
        self.instances = {}

    def update_style_sheet(self) -> "BaseStyleSheet":
        """
        Updates the CSS style sheet string by concatenating all styles in the instances dictionary.

        Returns:
            BaseStyleSheet: The updated style sheet object.
        """
        self.style_sheet = " ".join(list(filter(lambda item: item != "", self.instances.values())))
        return self

    def add_style(self, style: BaseStyle) -> "BaseStyleSheet":
        """
        Adds a style to the style sheet by associating the style sheet object with its corresponding style string.

        Args:
            style (BaseStyle): The style object to add.

        Returns:
            BaseStyleSheet: The updated style sheet object.
        """
        self.instances[style.style_sheet_object.style_sheet_object] = style.style
        return self.update_style_sheet()

class StyleFlags:
    """
    Constants representing various style flags and options used in CSS.
    """

    class Repeat:
        """
        Constants for background-repeat property.
        """

        RepeatX = "repeat-x"
        RepeatY = "repeat-y"
        Repeat = "repeat"
        NoRepeat = "no-repeat"

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

    class Origin:
        """
        Constants for background-origin property.
        """

        Margin = "margin"
        Padding = "padding"
        Content = "content"
        Border = "border"

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

    class IconState:
        """
        Constants for icon states.
        """

        On = "on"
        Off = "off"

    class IconMode:
        """
        Constants for icon modes.
        """

        Disabled = "disabled"
        Active = "active"
        Normal = "normal"
        Selected = "selected"

    class FontWeight:
        """
        Constants for font-weight property.
        """

        Normal = "normal"
        Bold = "bold"

    class FontStyle:
        """
        Constants for font-style property.
        """

        Normal = "normal"
        Italic = "italic"
        Oblique = "oblique"

    class ColorName:
        """
        Constants for color names.
        """

        Transparent = "transparent"

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

    class Background:
        """
        Constants for background property.
        """

        None_ = "none"

    class Attachment:
        """
        Constants for background-attachment property.
        """

        Scroll = "scroll"
        Fixed = "fixed"

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
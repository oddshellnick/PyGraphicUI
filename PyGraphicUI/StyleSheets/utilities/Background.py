from PyGraphicUI.StyleSheets.utilities.Attachment import Attachment
from PyGraphicUI.StyleSheets.utilities.Color import Brush
from PyGraphicUI.StyleSheets.utilities.Origin import Origin
from PyGraphicUI.StyleSheets.utilities.Position import Alignment
from PyGraphicUI.StyleSheets.utilities.Repeat import Repeat
from PyGraphicUI.StyleSheets.utilities.Url import Url


class BackgroundPosition:
    """
    Represents the background-position CSS property.

    Attributes:
        background_position (str): The background position value.

    :Usage:
        position = Alignment(alignment="center")
        background_position = BackgroundPosition(background_position=position)
        background_position.background_position
        "background-position: center"
    """

    def __init__(self, background_position: Alignment):
        """
        Initializes a BackgroundPosition object.

        Args:
            background_position (Alignment): The background position value.
        """
        self.background_position = ""
        self.set_background_position(background_position)

    def set_background_position(self, background_position: Alignment):
        """
        Sets the background position value.

        Args:
            background_position (Alignment): The background position value.

        Returns:
            BackgroundPosition: The updated background position object.
        """
        self.background_position = "background-position: %s" % background_position.alignment
        return self


class BackgroundOrigin:
    """
    Represents the background-origin CSS property.

    Attributes:
        background_origin (str): The background origin value.

    :Usage:
        origin = Origin(origin="border-box")
        background_origin = BackgroundOrigin(background_origin=origin)
        background_origin.background_origin
        "background-origin: border-box"
    """

    def __init__(self, background_origin: Origin):
        """
        Initializes a BackgroundOrigin object.

        Args:
            background_origin (Origin): The background origin value.
        """
        self.background_origin = ""
        self.set_background_origin(background_origin)

    def set_background_origin(self, background_origin: Origin):
        """
        Sets the background origin value.

        Args:
            background_origin (Origin): The background origin value.

        Returns:
            BackgroundOrigin: The updated background origin object.
        """
        self.background_origin = "background-origin: %s" % background_origin.origin
        return self


class BackgroundImage:
    """
    Represents the background-image CSS property.

    Attributes:
        background_image (str): The background image value.

    :Usage:
        image = Url(url="url("image.png")")
        background_image = BackgroundImage(background_image=image)
        background_image.background_image
        "background-image: url("image.png")"
    """

    def __init__(self, background_image: Url):
        """
        Initializes a BackgroundImage object.

        Args:
            background_image (Url): The background image value.
        """
        self.background_image = ""
        self.set_background_image(background_image)

    def set_background_image(self, background_image: Url):
        """
        Sets the background image value.

        Args:
            background_image (Url): The background image value.

        Returns:
            BackgroundImage: The updated background image object.
        """
        self.background_image = "background-image: %s" % background_image.url
        return self


class BackgroundColor:
    """
    Represents the background-color CSS property.

    Attributes:
        background_color (str): The background color value.

    :Usage:
        color = Brush(brush="red")
        background_color = BackgroundColor(background_color=color)
        background_color.background_color
        "background-color: red"
    """

    def __init__(self, background_color: Brush):
        """
        Initializes a BackgroundColor object.

        Args:
            background_color (Brush): The background color value.
        """
        self.background_color = ""
        self.set_background_color(background_color)

    def set_background_color(self, background_color: Brush):
        """
        Sets the background color value.

        Args:
            background_color (Brush): The background color value.

        Returns:
            BackgroundColor: The updated background color object.
        """
        self.background_color = "background-color: %s" % background_color.brush
        return self


class BackgroundClip:
    """
    Represents the background-clip CSS property.

    Attributes:
        background_clip (str): The background clip value.

    :Usage:
        origin = Origin(origin="padding-box")
        background_clip = BackgroundClip(background_clip=origin)
        background_clip.background_clip
        "background-clip: padding-box"
    """

    def __init__(self, background_clip: Origin):
        """
        Initializes a BackgroundClip object.

        Args:
            background_clip (Origin): The background clip value.
        """
        self.background_clip = ""
        self.set_background_clip(background_clip)

    def set_background_clip(self, background_clip: Origin):
        """
        Sets the background clip value.

        Args:
            background_clip (Origin): The background clip value.

        Returns:
            BackgroundClip: The updated background clip object.
        """
        self.background_clip = "background-clip: %s" % background_clip.origin
        return self


class BackgroundAttachment:
    """
    Represents the background-attachment CSS property.

    Attributes:
        background_attachment (str): The background attachment value.

    :Usage:
        attachment = Attachment(attachment="fixed")
        background_attachment = BackgroundAttachment(background_attachment=attachment)
        background_attachment.background_attachment
        "background-attachment: fixed"
    """

    def __init__(self, background_attachment: Attachment):
        """
        Initializes a BackgroundAttachment object.

        Args:
            background_attachment (Attachment): The background attachment value.
        """
        self.background_attachment = ""
        self.set_background_attachment(background_attachment)

    def set_background_attachment(self, background_attachment: Attachment):
        """
        Sets the background attachment value.

        Args:
            background_attachment (Attachment): The background attachment value.

        Returns:
            BackgroundAttachment: The updated background attachment object.
        """
        self.background_attachment = "background-attachment: %s" % background_attachment.attachment
        return self


class Background:
    """
    Represents the background shorthand CSS property.

    Attributes:
        background (str): The background value.

    :Usage:
        background = Background(
        ...     background="red",
        ...     repeat=Repeat(repeat="no-repeat"),
        ...     alignment=Alignment(alignment="center")
        ... )
        background.background
        "background: red no-repeat center"
    """

    def __init__(self, background: Url | Brush | str, repeat: Repeat | None = None, alignment: Alignment | None = None):
        """
        Initializes a Background object.

        Args:
            background (Url | Brush | str): The background value.
            repeat (Repeat | None): The background repeat value, optional.
            alignment (Alignment | None): The background alignment value, optional.
        """
        self.background = ""
        self.set_background(background, repeat, alignment)

    def set_background(
        self, background: Url | Brush | str, repeat: Repeat | None = None, alignment: Alignment | None = None
    ):
        """
        Sets the background value.

        Args:
            background (Url | Brush | str): The background value.
            repeat (Repeat | None): The background repeat value, optional.
            alignment (Alignment | None): The background alignment value, optional.

        Returns:
            Background: The updated background object.
        """
        instances = [
            background
            if isinstance(background, str)
            else background.brush
            if isinstance(background, Brush)
            else background.url
        ]

        if repeat is not None:
            instances.append(repeat.repeat)

        if alignment is not None:
            instances.append(alignment.alignment)

        self.background = "background: %s" % " ".join(instances)
        return self


class AlternateBackgroundColor:
    """
    Represents the alternate-background-color CSS property.

    Attributes:
        alternate_background_color (str): The alternate background color value.

    :Usage:
        color = Brush(brush="blue")
        alternate_background_color = AlternateBackgroundColor(alternate_background_color=color)
        alternate_background_color.alternate_background_color
        "alternate-background-color: blue"
    """

    def __init__(self, alternate_background_color: Brush):
        """
        Initializes an AlternateBackgroundColor object.

        Args:
            alternate_background_color (Brush): The alternate background color value.
        """
        self.alternate_background_color = ""
        self.set_alternate_background_color(alternate_background_color)

    def set_alternate_background_color(self, alternate_background_color: Brush):
        """
        Sets the alternate background color value.

        Args:
            alternate_background_color (Brush): The alternate background color value.

        Returns:
            AlternateBackgroundColor: The updated alternate background color object.
        """
        self.alternate_background_color = "alternate-background-color: %s" % alternate_background_color.brush
        return self

from PyGraphicUI.StyleSheets.utilities.Position import Alignment
from PyGraphicUI.StyleSheets.utilities.Url import Url


class ImagePosition:
    """
    Represents the image-position CSS property.

    Attributes:
        image_position (str): The image position value as a string.

    :Usage:
        image_position = ImagePosition(Alignment("center"))
        image_position.image_position
        "image-position: center"
    """

    def __init__(self, image_position: Alignment):
        """
        Initializes an ImagePosition object.

        Args:
            image_position (Alignment): The image position value.
        """
        self.image_position = ""
        self.set_image_position(image_position)

    def set_image_position(self, image_position: Alignment):
        """
        Sets the image position value.

        Args:
            image_position (Alignment): The image position value to set.

        Returns:
            ImagePosition: The updated ImagePosition object.
        """
        self.image_position = "image-position: %s" % image_position.alignment
        return self


class Image:
    """
    Represents the image CSS property.

    Attributes:
        image (str): The image value as a string.

    :Usage:
        image = Image(Url("https://example.com/image.jpg"))
        image.image
        "image: url(https://example.com/image.jpg)"
    """

    def __init__(self, image: Url):
        """
        Initializes an Image object.

        Args:
            image (Url): The image value.
        """
        self.image = ""
        self.set_image(image)

    def set_image(self, image: Url):
        """
        Sets the image value.

        Args:
            image (Url): The image value to set.

        Returns:
            Image: The updated Image object.
        """
        self.image = "image: %s" % image.url
        return self

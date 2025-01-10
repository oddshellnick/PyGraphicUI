from PyQt6.QtCore import QRect
from PyQt6.QtGui import QFont, QFontMetrics


def get_text_size(text: str, font: QFont) -> QRect:
	"""
    Calculates the bounding rectangle of a given text using the specified font.

    Args:
        text (str): The text string.
        font (QFont): The font to use for the calculation.

    Returns:
        QRect: The bounding rectangle of the text.

    :Usage:
        font = QFont("Arial", 12)
        text = "Hello, world!"
        rect = get_text_size(text, font)
        width = rect.width()
        height = rect.height()
    """
	return QFontMetrics(font).boundingRect(text)

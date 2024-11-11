from PyQt6.QtGui import QFont, QFontMetrics
#
#
#
#
def get_text_size(
		text: str,
		font: QFont
):
	return QFontMetrics(font).boundingRect(text)

from PyGraphicUI.StyleSheets.utilities.Url import Url
from PyGraphicUI.StyleSheets.utilities.Position import Alignment
#
#
#
#
class ImagePosition:
	#
	#
	#
	#
	image_position = ""
	#
	#
	#
	#
	def __init__(self, image_position: Alignment):
		self.set_image_position(image_position)
	#
	#
	#
	#
	def set_image_position(self, image_position: Alignment):
		self.image_position = "image-position: %s" % image_position.alignment
		return self
#
#
#
#
class Image:
	#
	#
	#
	#
	image = ""
	#
	#
	#
	#
	def __init__(self, image: Url):
		self.set_image(image)
	#
	#
	#
	#
	def set_image(self, image: Url):
		self.image = "image: %s" % image.url
		return self

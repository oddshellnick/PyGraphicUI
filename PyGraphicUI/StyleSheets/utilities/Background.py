from PyGraphicUI.StyleSheets.utilities.Url import Url
from PyGraphicUI.StyleSheets.utilities.Color import Brush
from PyGraphicUI.StyleSheets.utilities.Origin import Origin
from PyGraphicUI.StyleSheets.utilities.Repeat import Repeat
from PyGraphicUI.StyleSheets.utilities.Position import Alignment
from PyGraphicUI.StyleSheets.utilities.Attachment import Attachment
#
#
#
#
class BackgroundPosition:
	background_position = ""
	#
	#
	#
	#
	def __init__(self, background_position: Alignment):
		self.set_background_position(background_position)
	#
	#
	#
	#
	def set_background_position(self, background_position: Alignment):
		self.background_position = "background-position: %s" % background_position.alignment
		return self
#
#
#
#
class BackgroundOrigin:
	background_origin = ""
	#
	#
	#
	#
	def __init__(self, background_origin: Origin):
		self.set_background_origin(background_origin)
	#
	#
	#
	#
	def set_background_origin(self, background_origin: Origin):
		self.background_origin = "background-origin: %s" % background_origin.origin
		return self
#
#
#
#
class BackgroundImage:
	background_image = ""
	#
	#
	#
	#
	def __init__(self, background_image: Url):
		self.set_background_image(background_image)
	#
	#
	#
	#
	def set_background_image(self, background_image: Url):
		self.background_image = "background-image: %s" % background_image.url
		return self
#
#
#
#
class BackgroundColor:
	background_color = ""
	#
	#
	#
	#
	def __init__(self, background_color: Brush):
		self.set_background_color(background_color)
	#
	#
	#
	#
	def set_background_color(self, background_color: Brush):
		self.background_color = "background-color: %s" % background_color.brush
		return self
#
#
#
#
class BackgroundClip:
	background_clip = ""
	#
	#
	#
	#
	def __init__(self, background_clip: Origin):
		self.set_background_clip(background_clip)
	#
	#
	#
	#
	def set_background_clip(self, background_clip: Origin):
		self.background_clip = "background-clip: %s" % background_clip.origin
		return self
#
#
#
#
class BackgroundAttachment:
	background_attachment = ""
	#
	#
	#
	#
	def __init__(self, background_attachment: Attachment):
		self.set_background_attachment(background_attachment)
	#
	#
	#
	#
	def set_background_attachment(self, background_attachment: Attachment):
		self.background_attachment = "background-attachment: %s" % background_attachment.attachment
		return self
#
#
#
#
class Background:
	background = ""
	#
	#
	#
	#
	def __init__(
			self,
			background: Url | Brush | str,
			repeat: Repeat = None,
			alignment: Alignment = None
	):
		self.set_background(background, repeat, alignment)
	#
	#
	#
	#
	def set_background(
			self,
			background: Url | Brush | str,
			repeat: Repeat = None,
			alignment: Alignment = None
	):
		instances = [background if type(background) == str else background.brush if type(background) == Brush else background.url]

		if repeat is not None:
			instances.append(repeat.repeat)

		if alignment is not None:
			instances.append(alignment.alignment)

		self.background = "background: %s" % " ".join(instances)
		return self
#
#
#
#
class AlternateBackgroundColor:
	alternate_background_color = ""
	#
	#
	#
	#
	def __init__(self, alternate_background_color: Brush):
		self.set_alternate_background_color(alternate_background_color)
	#
	#
	#
	#
	def set_alternate_background_color(self, alternate_background_color):
		self.alternate_background_color = "alternate-background-color: %s" % alternate_background_color.brush
		return self

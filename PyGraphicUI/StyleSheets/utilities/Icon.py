from PyGraphicUI.StyleSheets.utilities.Url import Url
#
#
#
#
class Icon:
	#
	#
	#
	#
	icon = ""
	#
	#
	#
	#
	def __init__(self, url: Url, mode: str = None, state: str = None):
		self.set_url(url, mode, state)
	#
	#
	#
	#
	def set_url(self, url: Url, mode: str = None, state: str = None):
		instances = [url.url]

		if mode is not None:
			instances.append(mode)

		if state is not None:
			instances.append(state)

		self.icon = " ".join(instances)
		return self
#
#
#
#
class IconProperty:
	#
	#
	#
	#
	icon_property = ""
	#
	#
	#
	#
	def __init__(self, icon: Icon | list[Icon]):
		self.set_url(icon)
	#
	#
	#
	#
	def set_url(self, icon: Icon | list[Icon]):
		if type(icon) != list:
			self.icon_property = "qproperty-icon: %s" % icon.icon
		else:
			self.icon_property = "qproperty-icon: %s" % " ".join([a.icon for a in icon])
		return self

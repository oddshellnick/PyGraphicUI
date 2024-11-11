#
#
#
#
class Url:
	url = ""
	#
	#
	#
	#
	def __init__(self, url: str):
		self.set_url(url)
	#
	#
	#
	#
	def set_url(self, url: str):
		if url != "none":
			self.url = "url(%s)" % url
		else:
			self.url = url

		return self

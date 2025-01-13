class Url:
	"""
    Represents a URL value for a background image.

    Attributes:
        url (str): The URL value as a string.

    :Usage:
        url = Url("https://example.com/image.jpg")
        url.url
        "url(https://example.com/image.jpg)"
    """
	
	def __init__(self, url: str):
		"""
        Initializes a Url object.

        Args:
            url (str): The URL value.
        """
		self.url = ""
		self.set(url)
	
	def set(self, url: str):
		"""
        Sets the URL value.

        Args:
            url (str): The URL value to set.

        Returns:
            Url: The updated Url object.
        """
		if url != "none":
			self.url = "url(%s)" % url
		else:
			self.url = url
		
		return self

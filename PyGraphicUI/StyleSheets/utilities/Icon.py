import typing
from PyGraphicUI.StyleSheets.utilities.Url import Url


class Icon:
	"""
    Represents the icon value for a widget, including optional mode and state.

    Attributes:
        icon (str): The formatted icon value as a string.

    :Usage:
        icon = Icon(Url("https://example.com/icon.png"))
        icon.icon
        "url(https://example.com/icon.png)"

        icon = Icon(Url("https://example.com/icon.png"), mode="normal", state="on")
        icon.icon
        "url(https://example.com/icon.png) normal on"
    """
	
	def __init__(self, url: Url, mode: typing.Optional[str], state: typing.Optional[str]):
		"""
        Initializes an Icon object.

        Args:
            url (Url): The URL of the icon image.
            mode (typing.Optional[str]): Optional mode for the icon. Default is None.
            state (typing.Optional[str]): Optional state for the icon. Default is None.
        """
		self.icon = ""
		self.set(url, mode, state)
	
	def set(self, url: Url, mode: typing.Optional[str], state: typing.Optional[str]):
		"""
        Sets the icon value with optional mode and state.

        Args:
            url (Url): The URL of the icon image.
            mode (typing.Optional[str]): Optional mode for the icon. Default is None.
            state (typing.Optional[str]): Optional state for the icon. Default is None.

        Returns:
            Icon: The updated Icon object.
        """
		instances = [url.url]
		
		if mode is not None:
			instances.append(mode)
		
		if state is not None:
			instances.append(state)
		
		self.icon = " ".join(instances)
		return self


class IconProperty:
	"""
    Represents the qproperty-icon CSS property.

    Attributes:
        icon_property (str): The formatted icon property value as a string.

    :Usage:
        icon = Icon(Url("https://example.com/icon.png"))
        icon_property = IconProperty(icon)
        icon_property.icon_property
        "qproperty-icon: url(https://example.com/icon.png)"

        icon_property = IconProperty([Icon(Url("https://example.com/icon1.png")), Icon(Url("https://example.com/icon2.png"))])
        icon_property.icon_property
        "qproperty-icon: url(https://example.com/icon1.png) url(https://example.com/icon2.png)"
    """
	
	def __init__(self, icon: typing.Union[Icon, typing.Iterable[Icon]]):
		"""
        Initializes an IconProperty object.

        Args:
            icon (typing.Union[Icon, typing.Iterable[Icon]]): The icon value(s).
        """
		self.icon_property = ""
		self.set(icon)
	
	def set(self, icon: typing.Union[Icon, typing.Iterable[Icon]]):
		"""
        Sets the icon property value.

        Args:
            icon (typing.Union[Icon, typing.Iterable[Icon]]): The icon value(s) to set.

        Returns:
            IconProperty: The updated IconProperty object.
        """
		if isinstance(icon, Icon):
			self.icon_property = "qproperty-icon: %s" % icon.icon
		elif isinstance(icon, typing.Iterable) and all(isinstance(a, Icon) for a in icon):
			self.icon_property = "qproperty-icon: %s" % " ".join([a.icon for a in icon])
		else:
			raise TypeError("icon must be an Icon or a typing.Iterable of Icons")
		
		return self

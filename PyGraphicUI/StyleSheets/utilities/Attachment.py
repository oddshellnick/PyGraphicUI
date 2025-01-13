class Attachment:
	"""
    Represents the background-attachment CSS property.

    Attributes:
        attachment (str): The attachment value.

    :Usage:
        attachment = Attachment(attachment="scroll")
        attachment.attachment
        "scroll"

        attachment = Attachment(attachment="fixed")
        attachment.attachment
        "fixed"
    """
	
	def __init__(self, attachment: str):
		"""
        Initializes an Attachment object.

        Args:
            attachment (str): The attachment value, e.g., "scroll" or "fixed".
        """
		self.attachment = ""
		self.set(attachment)
	
	def set(self, attachment: str):
		"""
        Sets the attachment value.

        Args:
            attachment (str): The attachment value, e.g., "scroll" or "fixed".

        Returns:
            Attachment: The updated Attachment object.
        """
		self.attachment = attachment
		return self

#
#
#
#
class Attachment:
	#
	#
	#
	#
	attachment = ""
	#
	#
	#
	#
	def __init__(self, attachment: str):
		self.set_attachment(attachment)
	#
	#
	#
	#
	def set_attachment(self, attachment: str):
		self.attachment = attachment
		return self

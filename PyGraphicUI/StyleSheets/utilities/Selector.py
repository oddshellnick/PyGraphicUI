#
#
#
#
class Selector:
	selector_type = ""
	selector = ""
	#
	#
	#
	#
	def __init__(self, selector_type: str):
		self.set_selector_type(selector_type)
	#
	#
	#
	#
	def set_selector_type(self, selector_type: str):
		self.selector_type = selector_type
		self.selector = {
			"universal": "*",
			"type": "%s",
			"property": "%s[%s]",
			"class": ".%s",
			"id": "%s#%s",
			"descendant": "%s %s",
			"child": "%s > %s"
		}[selector_type]

		return self
#
#
#
#
class WidgetSelector:
	widget_selector = ""
	#
	#
	#
	#
	def __init__(self, selector: Selector, widget_name: str = None, object_name: str = None):
		self.set_widget_selector(selector, widget_name, object_name)
	#
	#
	#
	#
	def set_widget_selector(self, selector: Selector, widget_name: str = None, object_name: str = None):
		if selector.selector_type == "universal":
			self.widget_selector = "*"
		elif selector.selector_type == "type":
			self.widget_selector = widget_name
		elif selector.selector_type == "class":
			self.widget_selector = ".%s" % widget_name
		elif selector.selector_type == "property":
			self.widget_selector = "%s[%s]" % (widget_name, object_name)
		elif selector.selector_type == "id":
			self.widget_selector = "%s#%s" % (widget_name, object_name)
		elif selector.selector_type == "descendant":
			self.widget_selector = "%s %s" % (widget_name, object_name)
		elif selector.selector_type == "child":
			self.widget_selector = "%s > %s" % (widget_name, object_name)
#
#
#
#
class SelectorFlag:
	Universal = "universal"
	Type = "type"
	Property = "property"
	Class = "class"
	ID = "id"
	Descendant = "descendant"
	Child = "child"

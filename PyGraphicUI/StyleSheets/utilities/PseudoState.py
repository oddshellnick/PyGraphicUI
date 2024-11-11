#
#
#
#
class PseudoStateFlags:
	Active = "active"
	AdjoinsItem = "adjoins-item"
	Alternate = "alternate"
	Bottom = "bottom"
	Checked = "checked"
	Closable = "closable"
	Closed = "closed"
	Default = "default"
	Disabled = "disabled"
	Editable = "editable"
	EditFocus = "edit-focus"
	Enabled = "enabled"
	Exclusive = "exclusive"
	First = "first"
	Flat = "flat"
	Floatable = "floatable"
	Focus = "focus"
	HasChildren = "has-children"
	HasSiblings = "has-siblings"
	Horizontal = "horizontal"
	Hover = "hover"
	Indeterminate = "indeterminate"
	Last = "last"
	Left = "left"
	Maximized = "maximized"
	Middle = "middle"
	Minimized = "minimized"
	Movable = "movable"
	NoFrame = "no-frame"
	NonExclusive = "non-exclusive"
	Off = "off"
	On = "on"
	OnlyOne = "only-one"
	Open = "open"
	NextSelected = "next-selected"
	Pressed = "pressed"
	PreviousSelected = "previous-selected"
	ReadOnly = "read-only"
	Right = "right"
	Selected = "selected"
	Top = "top"
	Unchecked = "unchecked"
	Vertical = "vertical"
	Window = "window"
#
#
#
#
class PseudoState:
	pseudo_state = ""
	#
	#
	#
	#
	def __init__(self, pseudo_state: str | list[str]):
		self.set_pseudo_state(pseudo_state)
	#
	#
	#
	#
	def set_pseudo_state(self, pseudo_state: str | list[str]):
		if type(pseudo_state) == str:
			self.pseudo_state = ":%s" % pseudo_state
		else:
			self.pseudo_state = ":%s" % ":".join(pseudo_state)

		return self

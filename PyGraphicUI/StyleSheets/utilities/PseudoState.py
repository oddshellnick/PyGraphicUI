import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class PseudoStateFlags:
	"""
    Constants representing different pseudo-states in Qt.
    """
	
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


class PseudoState:
	"""
    Represents a pseudo-state in a CSS selector.

    Attributes:
        pseudo_state (str): The pseudo-state value as a string.

    :Usage:
        pseudo_state = PseudoState(PseudoStateFlags.Hover)
        pseudo_state.pseudo_state
        ":hover"

        pseudo_state = PseudoState([PseudoStateFlags.Hover, PseudoStateFlags.Focus])
        pseudo_state.pseudo_state
        ":hover:focus"
    """
	
	def __init__(self, pseudo_state: typing.Union[str, typing.Iterable[str]]):
		"""
        Initializes a PseudoState object.

        Args:
            pseudo_state (typing.Union[str, typing.Iterable[str]]): The pseudo-state value(s).
        """
		self.pseudo_state = ""
		self.set(pseudo_state)
	
	def set(self, pseudo_state: typing.Union[str, typing.Iterable[str]]):
		"""
        Sets the pseudo-state value.

        Args:
            pseudo_state (typing.Union[str, typing.Iterable[str]]): The pseudo-state value(s) to set.

        Returns:
            PseudoState: The updated PseudoState object.
        """
		if isinstance(pseudo_state, str):
			self.pseudo_state = ":%s" % pseudo_state
		else:
			self.pseudo_state = ":%s" % ":".join(pseudo_state)
		
		return self

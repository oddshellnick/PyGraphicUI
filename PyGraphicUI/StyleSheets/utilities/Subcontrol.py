from PyGraphicUI.StyleSheets.utilities.Origin import Origin
from PyGraphicUI.StyleSheets.utilities.Position import Alignment
#
#
#
#
class SubcontrolPosition:
	subcontrol_position = ""
	#
	#
	#
	#
	def __init__(self, subcontrol_position: Alignment):
		self.set_subcontrol_position(subcontrol_position)
	#
	#
	#
	#
	def set_subcontrol_position(self, subcontrol_position: Alignment):
		self.subcontrol_position = "subcontrol-position: %s" % subcontrol_position.alignment
		return self
#
#
#
#
class SubcontrolOrigin:
	subcontrol_origin = ""
	#
	#
	#
	#
	def __init__(self, subcontrol_origin: Origin):
		self.set_subcontrol_origin(subcontrol_origin)
	#
	#
	#
	#
	def set_subcontrol_origin(self, subcontrol_origin: Origin):
		self.subcontrol_origin = "subcontrol-origin: %s" % subcontrol_origin.origin
		return self
#
#
#
#
class SubControls:
	#
	#
	#
	#
	class TreeView:
		Branch = "::branch"
	#
	#
	#
	#
	class ToolButton:
		MenuIndicator = "::menu-indicator"
		MenuArrow = "::menu-arrow"
		MenuButton = "::menu-button"
	#
	#
	#
	#
	class TableView:
		Item = "::item"
		Indicator = "::indicator"
	#
	#
	#
	#
	class TableCornerButton:
		Section = "::section"
	#
	#
	#
	#
	class TabWidget:
		LeftCorner = "::left-corner"
		RightCorner = "::right-corner"
		Pane = "::pane"
		TabBar = "::tab-bar"
	#
	#
	#
	#
	class TabBar:
		CloseButton = "::close-button"
		Scroller = "::scroller"
		Tab = "::tab"
		Tear = "::tear"
	#
	#
	#
	#
	class StatusBar:
		Item = "::item"
	#
	#
	#
	#
	class Splitter:
		Handle = "::handle"
	#
	#
	#
	#
	class SpinBox:
		DownArrow = "::down-arrow"
		DownButton = "::down-button"
		UpArrow = "::up-arrow"
		UpButton = "::up-button"
	#
	#
	#
	#
	class Slider:
		Handle = "::handle"
		Groove = "::groove"
	#
	#
	#
	#
	class ScrollBar:
		AddLine = "::add-line"
		AddPage = "::add-page"
		DownArrow = "::down-arrow"
		DownButton = "::down-button"
		Handle = "::handle"
		LeftArrow = "::left-arrow"
		RightArrow = "::right-arrow"
		SubLine = "::sub-line"
		SubPage = "::sub-page"
		UpArrow = "::up-arrow"
		UpButton = "::up-button"
	#
	#
	#
	#
	class ScrollArea:
		Corner = "::corner"
	#
	#
	#
	#
	class RadioButton:
		Indicator = "::indicator"
	#
	#
	#
	#
	class ProgressBar:
		Chunk = "::chunk"
	#
	#
	#
	#
	class MenuBar:
		Item = "::item"
	#
	#
	#
	#
	class Menu:
		Indicator = "::indicator"
		Icon = "::icon"
		Item = "::item"
		RightArrow = "::right-arrow"
		Scroller = "::scroller"
		Separator = "::separator"
		TearOff = "::tearoff"
	#
	#
	#
	#
	class ListView:
		Item = "::item"
	#
	#
	#
	#
	class ItemView:
		Indicator = "::indicator"
		Icon = "::icon"
		Item = "::item"
		Text = "::text"
	#
	#
	#
	#
	class HeaderView:
		DownArrow = "::down-arrow"
		Section = "::section"
		UpArrow = "::up-arrow"
	#
	#
	#
	#
	class GroupBox:
		Indicator = "::indicator"
		Title = "::title"
	#
	#
	#
	#
	class DockWidget:
		FloatingButton = "::float-button"
		CloseButton = "::close-button"
		Title = "::title"
	#
	#
	#
	#
	class ComboBox:
		DownArrow = "::down-arrow"
		DropDown = "::drop-down"
	#
	#
	#
	#
	class CheckBox:
		Indicator = "::indicator"
	#
	#
	#
	#
	class Button:
		MenuIndicator = "::menu-indicator"

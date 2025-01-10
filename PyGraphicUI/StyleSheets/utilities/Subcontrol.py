from dataclasses import dataclass
from PyGraphicUI.StyleSheets.utilities.Origin import Origin
from PyGraphicUI.StyleSheets.utilities.Position import Alignment


class SubcontrolPosition:
	"""
    Represents the subcontrol-position CSS property.

    Attributes:
        subcontrol_position (str): The subcontrol position value as a string.

    :Usage:
        subcontrol_position = SubcontrolPosition(Alignment("left"))
        subcontrol_position.subcontrol_position
        "subcontrol-position: left"
    """
	
	def __init__(self, subcontrol_position: Alignment):
		"""
        Initializes a SubcontrolPosition object.

        Args:
            subcontrol_position (Alignment): The subcontrol position value.
        """
		self.subcontrol_position = ""
		self.set_subcontrol_position(subcontrol_position)
	
	def set_subcontrol_position(self, subcontrol_position: Alignment):
		"""
        Sets the subcontrol position value.

        Args:
            subcontrol_position (Alignment): The subcontrol position value to set.

        Returns:
            SubcontrolPosition: The updated SubcontrolPosition object.
        """
		self.subcontrol_position = "subcontrol-position: %s" % subcontrol_position.alignment
		return self


class SubcontrolOrigin:
	"""
    Represents the subcontrol-origin CSS property.

    Attributes:
        subcontrol_origin (str): The subcontrol origin value as a string.

    :Usage:
        subcontrol_origin = SubcontrolOrigin(Origin("top-left"))
        subcontrol_origin.subcontrol_origin
        "subcontrol-origin: top-left"
    """
	
	def __init__(self, subcontrol_origin: Origin):
		"""
        Initializes a SubcontrolOrigin object.

        Args:
            subcontrol_origin (Origin): The subcontrol origin value.
        """
		self.subcontrol_origin = ""
		self.set_subcontrol_origin(subcontrol_origin)
	
	def set_subcontrol_origin(self, subcontrol_origin: Origin):
		"""
        Sets the subcontrol origin value.

        Args:
            subcontrol_origin (Origin): The subcontrol origin value to set.

        Returns:
            SubcontrolOrigin: The updated SubcontrolOrigin object.
        """
		self.subcontrol_origin = "subcontrol-origin: %s" % subcontrol_origin.origin
		return self


@dataclass
class SubControls:
	"""
    Contains subcontrol names for different Qt widgets.

    :Usage:
        SubControls.TreeView.Branch
        "::branch"
    """
	
	@dataclass
	class Button:
		"""
        Subcontrol names for QPushButton widgets.
        """
		
		MenuIndicator = "::menu-indicator"
	
	@dataclass
	class CheckBox:
		"""
        Subcontrol names for QCheckBox widgets.
        """
		
		Indicator = "::indicator"
	
	@dataclass
	class ComboBox:
		"""
        Subcontrol names for QComboBox widgets.
        """
		
		DownArrow = "::down-arrow"
		DropDown = "::drop-down"
	
	@dataclass
	class DockWidget:
		"""
        Subcontrol names for QDockWidget widgets.
        """
		
		FloatingButton = "::float-button"
		CloseButton = "::close-button"
		Title = "::title"
	
	@dataclass
	class GroupBox:
		"""
        Subcontrol names for QGroupBox widgets.
        """
		
		Indicator = "::indicator"
		Title = "::title"
	
	@dataclass
	class HeaderView:
		"""
        Subcontrol names for QHeaderView widgets.
        """
		
		DownArrow = "::down-arrow"
		Section = "::section"
		UpArrow = "::up-arrow"
	
	@dataclass
	class ItemView:
		"""
        Subcontrol names for QItemView widgets.
        """
		
		Indicator = "::indicator"
		Icon = "::icon"
		Item = "::item"
		Text = "::text"
	
	@dataclass
	class ListView:
		"""
        Subcontrol names for QListView widgets.
        """
		
		Item = "::item"
	
	@dataclass
	class Menu:
		"""
        Subcontrol names for QMenu widgets.
        """
		
		Indicator = "::indicator"
		Icon = "::icon"
		Item = "::item"
		RightArrow = "::right-arrow"
		Scroller = "::scroller"
		Separator = "::separator"
		TearOff = "::tearoff"
	
	@dataclass
	class MenuBar:
		"""
        Subcontrol names for QMenuBar widgets.
        """
		
		Item = "::item"
	
	@dataclass
	class ProgressBar:
		"""
        Subcontrol names for QProgressBar widgets.
        """
		
		Chunk = "::chunk"
	
	@dataclass
	class RadioButton:
		"""
        Subcontrol names for QRadioButton widgets.
        """
		
		Indicator = "::indicator"
	
	@dataclass
	class ScrollArea:
		"""
        Subcontrol names for QScrollArea widgets.
        """
		
		Corner = "::corner"
	
	@dataclass
	class ScrollBar:
		"""
        Subcontrol names for QScrollBar widgets.
        """
		
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
	
	@dataclass
	class Slider:
		"""
        Subcontrol names for QSlider widgets.
        """
		
		Handle = "::handle"
		Groove = "::groove"
	
	@dataclass
	class SpinBox:
		"""
        Subcontrol names for QSpinBox widgets.
        """
		
		DownArrow = "::down-arrow"
		DownButton = "::down-button"
		UpArrow = "::up-arrow"
		UpButton = "::up-button"
	
	@dataclass
	class Splitter:
		"""
        Subcontrol names for QSplitter widgets.
        """
		
		Handle = "::handle"
	
	@dataclass
	class StatusBar:
		"""
        Subcontrol names for QStatusBar widgets.
        """
		
		Item = "::item"
	
	@dataclass
	class TabBar:
		"""
        Subcontrol names for QTabBar widgets.
        """
		
		CloseButton = "::close-button"
		Scroller = "::scroller"
		Tab = "::tab"
		Tear = "::tear"
	
	@dataclass
	class TabWidget:
		"""
        Subcontrol names for QTabWidget widgets.
        """
		
		LeftCorner = "::left-corner"
		RightCorner = "::right-corner"
		Pane = "::pane"
		TabBar = "::tab-bar"
	
	@dataclass
	class TableCornerButton:
		"""
        Subcontrol names for QTableCornerButton widgets.
        """
		
		Section = "::section"
	
	@dataclass
	class TableView:
		"""
        Subcontrol names for QTableView widgets.
        """
		
		Item = "::item"
		Indicator = "::indicator"
	
	@dataclass
	class ToolButton:
		"""
        Subcontrol names for QToolButton widgets.
        """
		
		MenuIndicator = "::menu-indicator"
		MenuArrow = "::menu-arrow"
		MenuButton = "::menu-button"
	
	@dataclass
	class TreeView:
		"""
        Subcontrol names for QTreeView widgets.
        """
		
		Branch = "::branch"

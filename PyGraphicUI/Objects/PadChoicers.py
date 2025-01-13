import typing
from functools import partial
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QPushButton, QWidget
from PyGraphicUI.Objects.Layouts import LayoutInit
from PyGraphicUI.Attributes import LinearLayoutItem
from PyGraphicUI.Objects.StackedWidget import (
	PyStackedWidget,
	StackedWidgetInit
)
from PyGraphicUI.Objects.ScrollAreas import (
	PyHorizontalScrollArea,
	ScrollAreaInit
)
from PyGraphicUI.Objects.Widgets import (
	PyWidgetWithHorizontalLayout,
	PyWidgetWithVerticalLayout,
	WidgetInit,
	WidgetWithLayoutInit
)


class HorizontalPadChoicerInit(WidgetWithLayoutInit):
	"""
    Initialization parameters for a HorizontalPadChoicer.

    Attributes:
        widget_init (WidgetInit): Initialization parameters for the widget.
        layout_init (LayoutInit): Initialization parameters for the layout.
        buttons_area_init (ScrollAreaInit): Initialization parameters for the buttons area.
        pads_area_init (StackedWidgetInit): Initialization parameters for the pads area.
        header_on_top (bool): Whether the header (buttons) should be on top. Defaults to True.
    """
	
	def __init__(
			self,
			main_widget_init: WidgetWithLayoutInit = WidgetWithLayoutInit(),
			buttons_area_init: ScrollAreaInit = ScrollAreaInit(
					central_widget_init=WidgetWithLayoutInit(
							layout_init=LayoutInit(
									alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
									contents_margins=(0, 10, 0, 10),
									spacing=10
							)
					),
					vertical_scroll_bar_policy=Qt.ScrollBarPolicy.ScrollBarAlwaysOff
			),
			pads_area_init: StackedWidgetInit = StackedWidgetInit(),
			header_on_top: bool = True
	):
		"""
        Initializes a HorizontalPadChoicerInit object.

        Args:
            main_widget_init (WidgetWithLayoutInit): Main widget initialization parameters.
            buttons_area_init (ScrollAreaInit): Buttons area initialization parameters.
            pads_area_init (StackedWidgetInit): Pads area initialization parameters.
            header_on_top (bool): Whether the header is on top.
        """
		super().__init__(
				widget_init=main_widget_init.widget_init,
				layout_init=main_widget_init.layout_init
		)
		
		self.buttons_area_init = buttons_area_init
		self.pads_area_init = pads_area_init
		self.header_on_top = header_on_top


class PadChoicerItem:
	"""
    Represents an item in a PadChoicer, consisting of a button and a pad widget.

    Attributes:
        item_name (str): The name of the item.
        button (QPushButton): The button associated with the item.
        pad (QWidget): The pad widget displayed when the button is clicked.
    """
	
	def __init__(self, item_name: str, button: QPushButton, pad: QWidget):
		"""
        Initializes a PadChoicerItem.

        Args:
            item_name (str): The item name.
            button (QPushButton): The associated button.
            pad (QWidget): The associated pad widget.
        """
		self.item_name = item_name
		self.button = button
		self.pad = pad
	
	def get_button_size(self) -> QSize:
		"""
        Returns the size of the button.

        Returns:
            QSize: The size of the button.
        """
		return self.button.size()
	
	def get_pad_size(self) -> QSize:
		"""
        Returns the size of the pad widget.

        Returns:
            QSize: The size of the pad widget.
        """
		return self.pad.size()


class PyHorizontalPadChoicer(PyWidgetWithVerticalLayout):
	"""
    A widget that allows choosing between different "pads" (widgets) using a horizontal button bar.
    """
	
	def __init__(
			self,
			pad_choicer_init: HorizontalPadChoicerInit = HorizontalPadChoicerInit()
	):
		"""
        Initializes a PyHorizontalPadChoicer.

        Args:
            pad_choicer_init (HorizontalPadChoicerInit): Initialization parameters.
        """
		super().__init__(widget_with_layout_init=pad_choicer_init)
		
		self.pad_choicer_items: list[PadChoicerItem] = []
		self.layout_init = pad_choicer_init.buttons_area_init.central_widget_init.layout_init
		pad_choicer_init.pads_area_init.parent = self
		pad_choicer_init.buttons_area_init.parent = self
		self.buttons_widget = PyWidgetWithHorizontalLayout(
				widget_with_layout_init=WidgetWithLayoutInit(
						widget_init=WidgetInit(
								parent=self,
								minimum_size=pad_choicer_init.buttons_area_init.minimum_size,
								maximum_size=pad_choicer_init.buttons_area_init.maximum_size,
								fixed_size=pad_choicer_init.buttons_area_init.fixed_size
						)
				)
		)
		
		self.buttons_to_choice_scroll_area = PyHorizontalScrollArea(scroll_area_init=pad_choicer_init.buttons_area_init)
		self.buttons_widget.add_instance(LinearLayoutItem(self.buttons_to_choice_scroll_area))
		
		if pad_choicer_init.header_on_top:
			self.add_instance(LinearLayoutItem(self.buttons_widget))
			
			
			self.pads_choice_widget = PyStackedWidget(stacked_widget_init=pad_choicer_init.pads_area_init)
			self.add_instance(LinearLayoutItem(self.pads_choice_widget))
		else:
			self.pads_choice_widget = PyStackedWidget(stacked_widget_init=pad_choicer_init.pads_area_init)
			
			
			self.add_instance(LinearLayoutItem(self.pads_choice_widget))
			self.add_instance(LinearLayoutItem(self.buttons_widget))
	
	def choice_pad(self, pad_to_choice: typing.Union[int, str]):
		"""
        Chooses the specified pad.

        Args:
            pad_to_choice (typing.Union[int, str]): The index or name of the pad to choose.
        """
		number_of_pad = (
				pad_to_choice if isinstance(pad_to_choice, int)
				else [
					pad_choicer_item_.item_name
					for pad_choicer_item_ in self.pad_choicer_items
				].index(pad_to_choice)
		)
		
		for i in range(len(self.pad_choicer_items)):
			self.pad_choicer_items[i].button.setEnabled(i != number_of_pad)
		
		self.pads_choice_widget.setCurrentIndex(number_of_pad)
	
	def add_pad(self, pad_choicer_item: PadChoicerItem):
		"""
        Adds a new pad to the choicer.

        Args:
            pad_choicer_item (PadChoicerItem): The pad item to add.
        """
		pad_choicer_item.button.clicked.connect(partial(self.choice_pad, len(self.pad_choicer_items)))
		
		self.buttons_to_choice_scroll_area.add_instance(LinearLayoutItem(pad_choicer_item.button))
		self.pads_choice_widget.addWidget(pad_choicer_item.pad)
		
		self.pad_choicer_items.append(pad_choicer_item)
		
		self.buttons_widget.setFixedHeight(
				int(
						max(
								pad_choicer_item_.button.size().height()
								for pad_choicer_item_ in self.pad_choicer_items
						) +
						self.layout_init.contents_margins[1] +
						self.layout_init.contents_margins[3]
				)
		)
		
		if self.pad_choicer_items[self.pads_choice_widget.currentIndex()].button.isEnabled():
			self.pad_choicer_items[self.pads_choice_widget.currentIndex()].button.setEnabled(False)
	
	def create_pads_choicer(self, pad_choicer_items: list[PadChoicerItem]):
		"""
        Creates the pads choicer with the given items.

        Args:
            pad_choicer_items (list[PadChoicerItem]): The pad choicer items.
        """
		self.buttons_to_choice_scroll_area.clear_scroll_area()
		self.pads_choice_widget.clear_stacked_widget()
		
		self.pad_choicer_items.clear()
		
		for pad_choicer_item in pad_choicer_items:
			self.add_pad(pad_choicer_item)
		
		if len(self.pad_choicer_items) > 0:
			self.pad_choicer_items[0].button.setEnabled(False)
	
	def remove_pad(self, index: int):
		"""
        Removes a pad at the specified index.

        Args:
            index (int): The index of the pad to remove.
        """
		if len(self.pad_choicer_items) > index:
			pad_choicer_item = self.pad_choicer_items.pop(index)
		
			self.pads_choice_widget.removeWidget(pad_choicer_item.pad)
			self.buttons_to_choice_scroll_area.remove_instance(pad_choicer_item.button)
		
			if len(self.pad_choicer_items) > 0:
				self.buttons_widget.setFixedHeight(
						int(
								max(
										pad_choicer_item_.button.size().height()
										for pad_choicer_item_ in self.pad_choicer_items
								) +
								self.layout_init.contents_margins[1] +
								self.layout_init.contents_margins[3]
						)
				)
	
	def to_button_parent(self) -> PyWidgetWithHorizontalLayout:
		"""
        Returns the parent widget of the buttons.

        Returns:
             PyWidgetWithHorizontalLayout: The parent widget for the buttons.
        """
		return self.buttons_to_choice_scroll_area.horizontal_scroll
	
	def to_pad_parent(self) -> PyStackedWidget:
		"""
        Returns the parent widget of the pads.

        Returns:
            PyStackedWidget: The parent widget for the pads.
        """
		return self.pads_choice_widget

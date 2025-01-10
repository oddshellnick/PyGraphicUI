# PyGraphicUI: Enhanced PyQt6 GUI Development

PyGraphicUI is a Python library built on top of PyQt6 that streamlines the creation of graphical user interfaces. It provides a more intuitive and Pythonic approach to designing and managing PyQt6 widgets and layouts, simplifying complex tasks and reducing boilerplate code.

## Key Features:

* **Simplified Widget Initialization:** Create PyQt6 widgets with ease using dedicated initialization classes like `WidgetInit`, `SpinBoxInit`, `LabelInit`, and more.  These classes provide a cleaner way to set widget properties during creation.
* **Enhanced Layout Management:** Easily construct and manage complex layouts with `PyVerticalLayout`, `PyHorizontalLayout`, and `GridLayout`. Add, remove, and access layout items with convenient methods.
* **Dynamic Time-Based Widgets:** Incorporate dynamic time display with `PyTimer` and `PyStopWatch`, offering customizable formatting and update intervals. Also includes a `PyProgressWatcher` for tracking progress with estimated time remaining.
* **Powerful Styling with StyleSheets:** Create and apply custom stylesheets using a structured and object-oriented approach. `BaseStyle`, `BaseStyleSheet`, and specialized style classes for different widgets provide fine-grained control over appearance. Chain styles together for complex selectors.

## Installation:

* **With pip:**
    ```bash
    pip install PyGraphicUI
    ```

* **With git:**
    ```bash
    pip install git+https://github.com/oddshellnick/PyGraphicUI.git
    ```

## Example Usage:

```python
from PyGraphicUI.PyObjects import PyWidgetWithVerticalLayout, WidgetWithLayoutInit, WidgetInit, LayoutInit, PyPushButton, PushButtonInit
from PyGraphicUI.PyStyleSheets import WidgetStyleSheet, WidgetStyle, Background, Brush, Color, RGB, PushButtonStyleSheet, PushButtonStyle, BorderRadius, BoxLengths, Length, PX, TextColor
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyGraphicUI.Attributes import LinearLayoutItem
from PyQt6.QtCore import Qt, QMetaObject
import sys


class MainProjectWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window = PyWidgetWithVerticalLayout(
                widget_with_layout_init=WidgetWithLayoutInit(
                        widget_init=WidgetInit(
                                parent=self,
                                minimum_size=ObjectSize(800, 600),
                                style_sheet=WidgetStyleSheet(
                                        WidgetStyle(
                                                background=Background(Brush(Color(RGB(45, 45, 45))))
                                        )
                                ).style_sheet
                        ),
                        layout_init=LayoutInit(
                                alignment=Qt.AlignmentFlag.AlignCenter,
                                contents_margins=(10, 10, 10, 10),
                                spacing=10
                        )
                )
        )

        self.button = PyPushButton(
                button_init=PushButtonInit(
                        parent=self.main_window,
                        style_sheet=PushButtonStyleSheet(
                                PushButtonStyle(
                                        background=Background(Brush(Color(RGB(90, 90, 90)))),
                                        border_radius=BorderRadius(BoxLengths(Length(PX(10)))),
                                        text_color=TextColor(Brush(Color(RGB(230, 230, 230))))
                                )
                        ).style_sheet,
                        fixed_size=ObjectSize(width=100, height=50),
                        font=PyFont(size=32, size_type="point")
                ),
                instance="Click"
        )
        self.main_window.add_instance(LinearLayoutItem(self.button))

        self.setCentralWidget(self.main_window)
        QMetaObject.connectSlotsByName(self)
        self.show()

        
def run_program():
    app = QApplication(sys.argv)

    main_window = MainProjectWindow()

    sys.exit(app.exec())

run_program()
```

## Future Notes

PyGraphicUI is actively maintained and will continue to be updated with new widgets, styles, and features. We encourage contributions and welcome suggestions for improvements. Don't hesitate to propose new additions or report any issues you encounter.

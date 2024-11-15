from PyGraphicUI.StyleSheets.Objects.AbstractButton import (
    AbstractButtonStyle,
    ChainAbstractButtonStyle,
)
from PyGraphicUI.StyleSheets.Objects.Base import BaseStyleSheet
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.Selector import Selector


class ToolButtonStyle(AbstractButtonStyle):
    """
    A style class used to style QToolButton.

    :Usage:
        ToolButtonStyle(text="Tool Button", icon=IconProperty("path/to/icon.png"))
    """

    def __init__(self, **kwargs):
        """
        Initializes a ToolButtonStyle object.

        Args:
            **kwargs: Additional keyword arguments passed to the AbstractButtonStyle constructor.
        """
        super().__init__(button_type="QToolButton", **kwargs)


class ToolButtonStyleSheet(BaseStyleSheet):
    """
    A style sheet class used to manage styles for multiple QToolButton objects.

    :Usage:
        ToolButtonStyleSheet(button_style=[ToolButtonStyle(text="Tool Button 1"), ToolButtonStyle(text="Tool Button 2")])
    """

    def __init__(self, button_style: ToolButtonStyle | list[ToolButtonStyle] | None = None):
        """
        Initializes a ToolButtonStyleSheet object.

        Args:
            button_style (ToolButtonStyle | list[ToolButtonStyle] | None): A ToolButtonStyle object or list of  ToolButtonStyle objects representing the styles to be applied to the QToolButton objects.
        """
        super().__init__()

        if button_style is not None:
            if isinstance(button_style, ToolButtonStyle):
                self.add_style(button_style)
            else:
                for style in button_style:
                    self.add_style(style)

        self.update_style_sheet()


class ChainToolButtonStyle(ChainAbstractButtonStyle):
    """
    A style class that can be chained to apply styles to any subclass of QToolButton.

    :Usage:
        ChainToolButtonStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """

    def __init__(
        self,
        parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
        widget_selector: tuple[str, Selector] | None = None,
        **kwargs
    ):
        """
        Initializes a ChainToolButtonStyle object.

        Args:
            parent_css_object (ObjectOfStyle | list[ObjectOfStyle]): The style sheet object or list of objects that the style is applied to, from which the QToolButton will inherit styles.
            widget_selector (tuple[str, Selector] | None): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the ChainAbstractButtonStyle constructor.
        """

        super().__init__(
            parent_css_object=parent_css_object, button_type="QToolButton", widget_selector=widget_selector, **kwargs
        )

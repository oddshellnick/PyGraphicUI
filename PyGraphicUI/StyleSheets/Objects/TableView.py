from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.Objects.HeaderView import ChainHeaderViewStyle
from PyGraphicUI.StyleSheets.Objects.ScrollBar import ChainScrollBarStyle
from PyGraphicUI.StyleSheets.Objects.TableCornerButton import (
    ChainTableCornerButtonStyle,
)
from PyGraphicUI.StyleSheets.utilities.Color import GridLineColor
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.Subcontrol import (
    SubcontrolOrigin,
    SubcontrolPosition,
)
from PyGraphicUI.StyleSheets.utilities.utils import (
    get_kwargs_without_arguments,
    get_new_parent_objects,
    get_objects_of_style,
)


class TableViewStyle(BaseStyle):
    """
    A style class used to style QTableView.

    :Usage:
        TableViewStyle(gridline_color=GridLineColor(Color(RGB(100, 100, 100))))
    """

    class ScrollBar(ChainScrollBarStyle):
        """
        A nested class to apply styles specifically to the scroll bar of QTableView.
        """

        def __init__(
            self,
            subcontrol_position: SubcontrolPosition | None = None,
            subcontrol_origin: SubcontrolOrigin | None = None,
            **kwargs
        ):
            """
            Initializes a ScrollBar object.

            Args:
                subcontrol_position (SubcontrolPosition | None): A SubcontrolPosition object representing the position of the subcontrol to style.
                subcontrol_origin (SubcontrolOrigin | None): A SubcontrolOrigin object representing the origin of the subcontrol to style.
                **kwargs: Additional keyword arguments passed to the ChainScrollBarStyle constructor.
            """
            parent_objects, kwargs = get_objects_of_style(("QTableView", Selector(SelectorFlag.Type)), **kwargs)
            super().__init__(
                parent_css_object=parent_objects,
                widget_selector=None,
                subcontrol_position=subcontrol_position,
                subcontrol_origin=subcontrol_origin,
                **kwargs
            )

    class HeaderView(ChainHeaderViewStyle):
        """
        A nested class to apply styles specifically to the header view of QTableView.
        """

        def __init__(
            self,
            subcontrol_position: SubcontrolPosition | None = None,
            subcontrol_origin: SubcontrolOrigin | None = None,
            **kwargs
        ):
            """
            Initializes a HeaderView object.

            Args:
                subcontrol_position (SubcontrolPosition | None): A SubcontrolPosition object representing the position of the subcontrol to style.
                subcontrol_origin (SubcontrolOrigin | None): A SubcontrolOrigin object representing the origin of the subcontrol to style.
                **kwargs: Additional keyword arguments passed to the ChainHeaderViewStyle constructor.
            """
            parent_objects, kwargs = get_objects_of_style(("QTableView", Selector(SelectorFlag.Type)), **kwargs)
            super().__init__(
                parent_css_object=parent_objects,
                widget_selector=None,
                subcontrol_position=subcontrol_position,
                subcontrol_origin=subcontrol_origin,
                **kwargs
            )

    class CornerButton(ChainTableCornerButtonStyle):
        """
        A nested class to apply styles specifically to the corner button of QTableView.
        """

        def __init__(self, **kwargs):
            """
            Initializes a CornerButton object.

            Args:
                **kwargs: Additional keyword arguments passed to the ChainTableCornerButtonStyle constructor.
            """
            parent_objects, kwargs = get_objects_of_style(("QTableView", Selector(SelectorFlag.Type)), **kwargs)
            super().__init__(parent_css_object=parent_objects, widget_selector=None, **kwargs)

    def __init__(self, gridline_color: GridLineColor | None = None, **kwargs):
        """
        Initializes a TableViewStyle object.

        Args:
            gridline_color (GridLineColor | None): A GridLineColor object representing the color to be used for the grid lines.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
        object_of_style, kwargs = get_objects_of_style(("QTableView", Selector(SelectorFlag.Type)), **kwargs)

        super().__init__(object_of_style=object_of_style, **kwargs)

        if gridline_color is not None:
            self.add_gridline_color(gridline_color)

        self.update_style()

    def add_gridline_color(self, gridline_color: GridLineColor):
        """
        Adds a grid line color to the style.

        Args:
            gridline_color (GridLineColor): A GridLineColor object representing the color to be used for the grid lines.

        Returns:
            TableViewStyle: The current TableViewStyle object for method chaining.
        """
        self.instances["gridline_color"] = gridline_color.grid_line_color
        return self.update_style()


class TableViewStyleSheet(BaseStyleSheet):
    """
    A style sheet class used to manage styles for multiple QTableView objects.

    :Usage:
        TableViewStyleSheet(table_view_style=[TableViewStyle(gridline_color=GridLineColor(Color(RGB(100, 100, 100)))), TableViewStyle.ScrollBar(subcontrol_position=SubcontrolPosition.AddLine)])
    """

    def __init__(
        self,
        table_view_style: TableViewStyle
        | TableViewStyle.HeaderView
        | TableViewStyle.ScrollBar
        | TableViewStyle.CornerButton
        | list[TableViewStyle | TableViewStyle.HeaderView | TableViewStyle.ScrollBar | TableViewStyle.CornerButton]
        | None = None,
    ):
        """
        Initializes a TableViewStyleSheet object.

        Args:
            table_view_style (TableViewStyle | TableViewStyle.HeaderView | TableViewStyle.ScrollBar | TableViewStyle.CornerButton | list[TableViewStyle | TableViewStyle.HeaderView | TableViewStyle.ScrollBar | TableViewStyle.CornerButton] | None): A TableViewStyle object, TableViewStyle.HeaderView object, TableViewStyle.ScrollBar object, TableViewStyle.CornerButton object, or list of  TableViewStyle, TableViewStyle.HeaderView, TableViewStyle.ScrollBar, or TableViewStyle.CornerButton objects representing the styles to be applied to the QTableView objects.
        """
        super().__init__()

        if table_view_style is not None:
            if isinstance(
                table_view_style,
                (TableViewStyle, TableViewStyle.HeaderView, TableViewStyle.ScrollBar, TableViewStyle.CornerButton),
            ):
                self.add_style(table_view_style)
            else:
                for style in table_view_style:
                    self.add_style(style)

        self.update_style_sheet()


class ChainTableViewStyles(BaseStyle):
    """
    A style class that can be chained to apply styles to any subclass of QTableView.

    :Usage:
        ChainTableViewStyles(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """

    class ScrollBar(ChainScrollBarStyle):
        """
        A nested class to apply styles specifically to the scroll bar of QTableView.
        """

        def __init__(
            self,
            parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
            widget_selector: tuple[str, Selector] | None = None,
            subcontrol_position: SubcontrolPosition | None = None,
            subcontrol_origin: SubcontrolOrigin | None = None,
            **kwargs
        ):
            """
            Initializes a ScrollBar object.

            Args:
                parent_css_object (ObjectOfStyle | list[ObjectOfStyle]): The parent style sheet object or list of objects.
                widget_selector (tuple[str, Selector] | None): A tuple containing the type of widget and the selector to apply the styles to.
                subcontrol_position (SubcontrolPosition | None): A SubcontrolPosition object representing the position of the subcontrol to style.
                subcontrol_origin (SubcontrolOrigin | None): A SubcontrolOrigin object representing the origin of the subcontrol to style.
                **kwargs: Additional keyword arguments passed to the ChainScrollBarStyle constructor.
            """
            new_parent_objects = get_new_parent_objects(
                parent_css_object, widget_selector, ("QTableView", Selector(SelectorFlag.Descendant))
            )
            parent_objects, kwargs = get_objects_of_style(
                (new_parent_objects.css_object.css_object, Selector(SelectorFlag.Type)), **kwargs
            )
            super().__init__(
                parent_css_object=parent_objects,
                widget_selector=None,
                subcontrol_position=subcontrol_position,
                subcontrol_origin=subcontrol_origin,
                **kwargs
            )

    class HeaderView(ChainHeaderViewStyle):
        """
        A nested class to apply styles specifically to the header view of QTableView.
        """

        def __init__(
            self,
            parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
            widget_selector: tuple[str, Selector] | None = None,
            subcontrol_position: SubcontrolPosition | None = None,
            subcontrol_origin: SubcontrolOrigin | None = None,
            **kwargs
        ):
            """
            Initializes a HeaderView object.

            Args:
                parent_css_object (ObjectOfStyle | list[ObjectOfStyle]): The parent style sheet object or list of objects.
                widget_selector (tuple[str, Selector] | None): A tuple containing the type of widget and the selector to apply the styles to.
                subcontrol_position (SubcontrolPosition | None): A SubcontrolPosition object representing the position of the subcontrol to style.
                subcontrol_origin (SubcontrolOrigin | None): A SubcontrolOrigin object representing the origin of the subcontrol to style.
                **kwargs: Additional keyword arguments passed to the ChainHeaderViewStyle constructor.
            """
            new_parent_objects = get_new_parent_objects(
                parent_css_object, widget_selector, ("QTableView", Selector(SelectorFlag.Descendant))
            )
            parent_objects, kwargs = get_objects_of_style(
                (new_parent_objects.css_object.css_object, Selector(SelectorFlag.Type)), **kwargs
            )
            super().__init__(
                parent_css_object=parent_objects,
                widget_selector=None,
                subcontrol_position=subcontrol_position,
                subcontrol_origin=subcontrol_origin,
                **kwargs
            )

    class CornerButton(ChainTableCornerButtonStyle):
        """
        A nested class to apply styles specifically to the corner button of QTableView.
        """

        def __init__(
            self,
            parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
            widget_selector: tuple[str, Selector] | None = None,
            **kwargs
        ):
            """
            Initializes a CornerButton object.

            Args:
                parent_css_object (ObjectOfStyle | list[ObjectOfStyle]): The parent style sheet object or list of objects.
                widget_selector (tuple[str, Selector] | None): A tuple containing the type of widget and the selector to apply the styles to.
                **kwargs: Additional keyword arguments passed to the ChainTableCornerButtonStyle constructor.
            """
            new_parent_objects = get_new_parent_objects(
                parent_css_object, widget_selector, ("QTableView", Selector(SelectorFlag.Descendant))
            )
            parent_objects, kwargs = get_objects_of_style(
                (new_parent_objects.css_object.css_object, Selector(SelectorFlag.Type)), **kwargs
            )
            super().__init__(parent_css_object=parent_objects, widget_selector=None, **kwargs)

    def __init__(
        self,
        parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
        widget_selector: tuple[str, Selector] | None = None,
        gridline_color: GridLineColor | None = None,
        **kwargs
    ):
        """
        Initializes a ChainTableViewStyles object.

        Args:
            parent_css_object (ObjectOfStyle | list[ObjectOfStyle]): The style sheet object or list of objects that the style is applied to, from which the QTableView will inherit styles.
            widget_selector (tuple[str, Selector] | None): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            gridline_color (GridLineColor | None): A GridLineColor object representing the color to be used for the grid lines.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
        new_parent_objects = get_new_parent_objects(
            parent_css_object, widget_selector, ("QTableView", Selector(SelectorFlag.Descendant))
        )

        kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)

        super().__init__(object_of_style=new_parent_objects, **kwargs)

        if gridline_color is not None:
            self.add_gridline_color(gridline_color)

        self.update_style()

    def add_gridline_color(self, gridline_color: GridLineColor):
        """
        Adds a grid line color to the style.

        Args:
            gridline_color (GridLineColor): A GridLineColor object representing the color to be used for the grid lines.

        Returns:
            ChainTableViewStyles: The current ChainTableViewStyles object for method chaining.
        """
        self.instances["gridline_color"] = gridline_color.grid_line_color
        return self.update_style()

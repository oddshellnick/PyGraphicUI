from PyGraphicUI.StyleSheets.Objects.Base import BaseStyle, BaseStyleSheet
from PyGraphicUI.StyleSheets.Objects.LineEdit import ChainLineEditStyle
from PyGraphicUI.StyleSheets.utilities.LineEdit import (
    LineEditPasswordCharacter,
    LineEditPasswordMaskDelay,
)
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag
from PyGraphicUI.StyleSheets.utilities.Subcontrol import (
    SubcontrolOrigin,
    SubcontrolPosition,
)
from PyGraphicUI.StyleSheets.utilities.Text import PlaceholderTextColor
from PyGraphicUI.StyleSheets.utilities.utils import (
    get_kwargs_without_arguments,
    get_new_parent_objects,
    get_objects_of_style,
)


class DoubleSpinBoxStyle(BaseStyle):
    """
    A style class used to style QDoubleSpinBox.

    :Usage:
        DoubleSpinBoxStyle(subcontrol_position=SubcontrolPosition.DownArrow, subcontrol_origin=SubcontrolOrigin.DownButton)
    """

    class LineEdit(ChainLineEditStyle):
        """
        A nested class to apply styles specifically to the line edit of QSpinBox.
        """

        def __init__(
            self,
            placeholder_text_color: PlaceholderTextColor | None = None,
            line_edit_password_character: LineEditPasswordCharacter | None = None,
            line_edit_password_mask_delay: LineEditPasswordMaskDelay | None = None,
            **kwargs
        ):
            """
            Initializes a LineEdit object.

            Args:
                placeholder_text_color (PlaceholderTextColor | None): A PlaceholderTextColor object representing the color to be used for the placeholder text.
                line_edit_password_character (LineEditPasswordCharacter | None): A LineEditPasswordCharacter object representing the character to be used to mask the text in a password line edit.
                line_edit_password_mask_delay (LineEditPasswordMaskDelay | None): A LineEditPasswordMaskDelay object representing the delay (in milliseconds) before the password mask is applied.
                **kwargs: Additional keyword arguments passed to the ChainLineEditStyle constructor.
            """
            parent_objects, kwargs = get_objects_of_style(("QDoubleSpinBox", Selector(SelectorFlag.Descendant)), **kwargs)
            super().__init__(
                parent_css_object=parent_objects,
                widget_selector=("qt_spinbox_lineedit", Selector(SelectorFlag.ID)),
                placeholder_text_color=placeholder_text_color,
                line_edit_password_character=line_edit_password_character,
                line_edit_password_mask_delay=line_edit_password_mask_delay,
                **kwargs
            )

    def __init__(
        self,
        subcontrol_position: SubcontrolPosition | None = None,
        subcontrol_origin: SubcontrolOrigin | None = None,
        **kwargs
    ):
        """
        Initializes a DoubleSpinBoxStyle object.

        Args:
            subcontrol_position (SubcontrolPosition | None): A SubcontrolPosition object representing the position of the subcontrol to style.
            subcontrol_origin (SubcontrolOrigin | None): A SubcontrolOrigin object representing the origin of the subcontrol to style.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
        super().__init__(**kwargs)

        if self.style_sheet_object is None:
            self.set_style_sheet_object(ObjectOfStyle(CssObject("QDoubleSpinBox")))
        else:
            self.style_sheet_object.add_css_object_to_style_sheet("QDoubleSpinBox")

        if subcontrol_position is not None:
            self.add_subcontrol_position(subcontrol_position)

        if subcontrol_origin is not None:
            self.add_subcontrol_origin(subcontrol_origin)

        self.update_style()

    def add_subcontrol_origin(self, subcontrol_origin: SubcontrolOrigin):
        """
        Adds a subcontrol origin to the style.

        Args:
            subcontrol_origin (SubcontrolOrigin): A SubcontrolOrigin object representing the origin of the subcontrol to style.

        Returns:
            DoubleSpinBoxStyle: The current SpinBoxStyle object for method chaining.
        """
        self.instances["subcontrol_origin"] = subcontrol_origin.subcontrol_origin
        return self.update_style()

    def add_subcontrol_position(self, subcontrol_position: SubcontrolPosition):
        """
        Adds a subcontrol position to the style.

        Args:
            subcontrol_position (SubcontrolPosition): A SubcontrolPosition object representing the position of the subcontrol to style.

        Returns:
            DoubleSpinBoxStyle: The current SpinBoxStyle object for method chaining.
        """
        self.instances["subcontrol_position"] = subcontrol_position.subcontrol_position
        return self.update_style()


class DoubleSpinBoxStyleSheet(BaseStyleSheet):
    """
    A style sheet class used to manage styles for multiple QDoubleSpinBox objects.

    :Usage:
        SpinBoxStyleSheet(widget_style=[SpinBoxStyle(subcontrol_position=SubcontrolPosition.DownArrow), SpinBoxStyle(subcontrol_position=SubcontrolPosition.UpArrow)])
    """

    def __init__(self, widget_style: DoubleSpinBoxStyle | list[DoubleSpinBoxStyle] | None = None):
        """
        Initializes a DoubleSpinBoxStyleSheet object.

        Args:
            widget_style (DoubleSpinBoxStyle | list[DoubleSpinBoxStyle] | None): A SpinBoxStyle object or list of SpinBoxStyle objects representing the styles to be applied to the QSpinBox objects.
        """
        super().__init__()

        if widget_style is not None:
            if isinstance(widget_style, DoubleSpinBoxStyle):
                self.add_style(widget_style)
            else:
                for style in widget_style:
                    self.add_style(style)

        self.update_style_sheet()


class ChainDoubleSpinBoxStyle(BaseStyle):
    """
    A style class that can be chained to apply styles to any subclass of QSpinBox.

    :Usage:
        ChainDoubleSpinBoxStyle(parent_css_object=ObjectOfStyle(CssObject("QWidget")))
    """

    class LineEdit(ChainLineEditStyle):
        """
        A nested class to apply styles specifically to the line edit of QDoubleSpinBox.
        """

        def __init__(
            self,
            parent_css_object: ObjectOfStyle,
            widget_selector: tuple[str, Selector] | None = None,
            placeholder_text_color: PlaceholderTextColor | None = None,
            line_edit_password_character: LineEditPasswordCharacter | None = None,
            line_edit_password_mask_delay: LineEditPasswordMaskDelay | None = None,
            **kwargs
        ):
            """
            Initializes a LineEdit object.

            Args:
                parent_css_object (ObjectOfStyle): The parent style sheet object.
                widget_selector (tuple[str, Selector] | None): A tuple containing the type of widget and the selector to apply the styles to.
                placeholder_text_color (PlaceholderTextColor | None): A PlaceholderTextColor object representing the color to be used for the placeholder text.
                line_edit_password_character (LineEditPasswordCharacter | None): A LineEditPasswordCharacter object representing the character to be used to mask the text in a password line edit.
                line_edit_password_mask_delay (LineEditPasswordMaskDelay | None): A LineEditPasswordMaskDelay object representing the delay (in milliseconds) before the password mask is applied.
                **kwargs: Additional keyword arguments passed to the ChainLineEditStyle constructor.
            """
            new_parent_objects = get_new_parent_objects(
                parent_css_object, widget_selector, ("QDoubleSpinBox", Selector(SelectorFlag.Descendant))
            )
            parent_objects, kwargs = get_objects_of_style(
                (new_parent_objects.css_object.css_object, Selector(SelectorFlag.Type)), **kwargs
            )
            super().__init__(
                parent_css_object=parent_objects,
                widget_selector=("qt_spinbox_lineedit", Selector(SelectorFlag.ID)),
                placeholder_text_color=placeholder_text_color,
                line_edit_password_character=line_edit_password_character,
                line_edit_password_mask_delay=line_edit_password_mask_delay,
                **kwargs
            )

    def __init__(
        self,
        parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
        widget_selector: tuple[str, Selector] | None = None,
        **kwargs
    ):
        """
        Initializes a ChainDoubleSpinBoxStyle object.

        Args:
            parent_css_object (ObjectOfStyle | list[ObjectOfStyle]): The style sheet object or list of objects that the style is applied to, from which the QSpinBox will inherit styles.
            widget_selector (tuple[str, Selector] | None): A tuple containing the type of widget and the selector to apply the styles to, in case the widget is not a direct descendant of the parent_css_object.
            **kwargs: Additional keyword arguments passed to the BaseStyle constructor.
        """
        new_parent_objects = get_new_parent_objects(
            parent_css_object, widget_selector, ("QDoubleSpinBox", Selector(SelectorFlag.Descendant))
        )

        kwargs = get_kwargs_without_arguments("object_of_style", **kwargs)

        super().__init__(object_of_style=new_parent_objects, **kwargs)

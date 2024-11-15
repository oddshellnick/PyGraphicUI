import typing

from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
from PyGraphicUI.StyleSheets.utilities.Selector import Selector, SelectorFlag


def get_new_parent_objects(
    parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
    widget_selector: tuple[str, Selector] | None,
    next_widget_selector: tuple[str, Selector],
) -> ObjectOfStyle | list[ObjectOfStyle]:
    """
    Updates parent CSS objects by adding a new child widget selector.

    Args:
        parent_css_object (ObjectOfStyle | list[ObjectOfStyle]): The parent CSS object(s) to update.
        widget_selector (tuple[str, Selector]  | None): An optional widget selector to also add to the parent.
        next_widget_selector (tuple[str, Selector]): The widget selector to add as a child of the parent.

    Returns:
        ObjectOfStyle | list[ObjectOfStyle]: The updated parent CSS object(s).
    """
    if isinstance(parent_css_object, list):
        for i in range(len(parent_css_object)):
            parent_css_object[i].add_css_object_to_object(next_widget_selector[0], next_widget_selector[1])

            if widget_selector is not None:
                parent_css_object[i].add_css_object_to_object(widget_selector[0], widget_selector[1])
    else:
        parent_css_object.add_css_object_to_object(next_widget_selector[0], next_widget_selector[1])

        if widget_selector is not None:
            parent_css_object.add_css_object_to_object(widget_selector[0], widget_selector[1])

    return parent_css_object


def get_object_of_style_arg(**kwargs) -> tuple[ObjectOfStyle | list[ObjectOfStyle] | None, dict[str, typing.Any]]:
    """
    Extracts the "object_of_style" argument from function arguments.

    Args:
        **kwargs: Keyword arguments.

    Returns:
        tuple[ObjectOfStyle | list[ObjectOfStyle] | None, typing.Any]: A tuple containing the "object_of_style" argument and remaining keyword arguments.
    """
    if "object_of_style" in kwargs:
        object_of_style_arg = kwargs.pop("object_of_style")
        return object_of_style_arg, kwargs

    return None, kwargs


def get_objects_of_style(
    parent_objects: tuple[str, Selector], **kwargs
) -> tuple[ObjectOfStyle | list[ObjectOfStyle] | None, dict[str, typing.Any]]:
    """
    Creates or updates an ObjectOfStyle based on parent objects and arguments.

    Args:
        parent_objects (tuple[str, Selector]): The parent CSS object represented by a widget name and selector.
        **kwargs: Keyword arguments.

    Returns:
        tuple[ObjectOfStyle | list[ObjectOfStyle] | None, typing.Any]: A tuple containing the updated ObjectOfStyle and keyword arguments.
    """
    object_of_style, kwargs = get_object_of_style_arg(**kwargs)

    if isinstance(object_of_style, list):
        for i in range(len(object_of_style)):
            object_of_style[i].add_css_object_to_object(parent_objects[0], parent_objects[1])
    elif isinstance(object_of_style, ObjectOfStyle):
        object_of_style.add_css_object_to_object(parent_objects[0], parent_objects[1])
    else:
        object_of_style = ObjectOfStyle(CssObject(parent_objects[0], Selector(SelectorFlag.Type)))

    return object_of_style, kwargs


def get_kwargs_without_arguments(arguments: str | list[str], **kwargs) -> dict[str, typing.Any]:
    """
    Removes the arguments from function arguments.

    Args:
        arguments (str | list[str]): The arguments to remove.
        **kwargs: Keyword arguments.

    Returns:
        dict[str, typing.Any]: A dict containing the remaining keyword arguments.
    """
    if isinstance(arguments, str):
        if arguments in kwargs:
            kwargs.pop(arguments)
    elif isinstance(arguments, list) and all(isinstance(arg, str) for arg in arguments):
        for arg in arguments:
            if arg in kwargs:
                kwargs.pop(arg)

    return kwargs

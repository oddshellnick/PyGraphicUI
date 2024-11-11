from PyGraphicUI.StyleSheets.utilities.Selector import Selector
from PyGraphicUI.StyleSheets.utilities.ObjectOfStyle import CssObject, ObjectOfStyle
#
#
#
#
def get_new_parent_objects(
		parent_css_object: ObjectOfStyle | list[ObjectOfStyle],
		widget_selector: tuple[str, Selector] | None,
		next_widget_selector: tuple[str, Selector]
):
	if type(parent_css_object) == list:
		for i in range(len(parent_css_object)):
			parent_css_object[i].add_css_object_to_object(next_widget_selector[0], next_widget_selector[1])

			if widget_selector is not None:
				parent_css_object[i].add_css_object_to_object(widget_selector[0], widget_selector[1])
	else:
		parent_css_object.add_css_object_to_object(next_widget_selector[0], next_widget_selector[1])

		if widget_selector is not None:
			parent_css_object.add_css_object_to_object(widget_selector[0], widget_selector[1])

	return parent_css_object
#
#
#
#
def get_object_of_style_arg(*args, **kwargs):
	if "object_of_style" in list(kwargs.keys()):
		object_of_style_arg = kwargs.pop("object_of_style")
		return object_of_style_arg, args, kwargs
	else:
		args = list(args)

		for i in range(len(args)):
			if type(args[i]) == ObjectOfStyle:
				object_of_style_arg = args.pop(i)
				return object_of_style_arg, args, kwargs
			elif type(args[i]) == list:
				if len(args[i]) > 0:
					if type(args[i][0]) == ObjectOfStyle:
						object_of_style_arg = args.pop(i)
						return object_of_style_arg, args, kwargs

		return None, args, kwargs
#
#
#
#
def get_objects_of_style(parent_objects: tuple[str, Selector], *args, **kwargs):
	object_of_style, args, kwargs = get_object_of_style_arg(*args, **kwargs)

	if type(object_of_style) == list:
		for i in range(len(object_of_style)):
			object_of_style[i].add_css_object_to_object(parent_objects[0], parent_objects[1])
	elif type(object_of_style) == ObjectOfStyle:
		object_of_style.add_css_object_to_object(parent_objects[0], parent_objects[1])
	else:
		object_of_style = ObjectOfStyle(
				CssObject(
						parent_objects[0],
						parent_objects[1]
				)
		)

	return object_of_style, args, kwargs
#
#
#
#
def get_args_without_object_of_style(*args, **kwargs):
	if "object_of_style" in list(kwargs.keys()):
		kwargs.pop("object_of_style")
		return args, kwargs
	else:
		args = list(args)

		for i in range(len(args)):
			if type(args[i]) == ObjectOfStyle:
				args.pop(i)
				return args, kwargs
			elif type(args[i]) == list:
				if len(args[i]) > 0:
					if type(args[i][0]) == ObjectOfStyle:
						args.pop(i)
						return args, kwargs

		return args, kwargs

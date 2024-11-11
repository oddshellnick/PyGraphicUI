import mplfinance
from pandas import DataFrame
from matplotlib.axes import Axes
from PyGraphicUI.Objects.Layouts import LayoutInit
from PyGraphicUI.Attributes import LinearLayoutItem
from PyGraphicUI.Charts.Canvas import PyFigureCanvas
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from PyGraphicUI.Objects.Widgets import PyWidgetWithVerticalLayout, WidgetInit, WidgetWithLayoutInit
#
#
#
#
class FinancialFigureInit:
	#
	#
	#
	#
	def __init__(
			self,
			data: DataFrame,
			chart_type: str,
			add_plot: dict | list[dict] = None,
			axes: Axes = None,
			axes_off: bool = None,
			axes_title: str | dict = None,
			block_until_figure_close: bool = None,
			close_figure: bool = None,
			columns: tuple[str, str, str, str, str] = None,
			datetime_format: str = None,
			draw_volume_panel: bool = None,
			figure_size: tuple[int, int] = None,
			font_scale: float | int = None,
			line_color: str = None,
			panel_ratios: list[int | float] = None,
			pnf_params: dict = None,
			renko_params: dict = None,
			scale_padding: float = 1.0,
			show_non_trading: bool = False,
			style: str | dict = None,
			tight_layout: bool = None,
			title: str = None,
			tz_localize: bool = None,
			volume_alpha: int | float = None,
			volume_exponent: int | str = None,
			volume_y_axis_label: str = None,
			volume_y_axis_scale: str = None,
			warn_too_much_data: int = None,
			x_axis_label: str = None,
			x_axis_rotation: int | float = None,
			y_axis_label: str = None,
			y_axis_scale: str = None
	):
		self.data = data
		#
		#
		#
		#
		self.kwargs = {"type": chart_type, "returnfig": True}
		#
		#
		#
		#
		if add_plot is not None:
			self.kwargs["addplot"] = add_plot
		#
		#
		#
		#
		if axes is not None:
			self.kwargs["ax"] = axes
		#
		#
		#
		#
		if axes_off is not None:
			self.kwargs["axisoff"] = axes_off
		#
		#
		#
		#
		if axes_title is not None:
			self.kwargs["axtitle"] = axes_title
		#
		#
		#
		#
		if block_until_figure_close is not None:
			self.kwargs["block"] = block_until_figure_close
		#
		#
		#
		#
		if close_figure is not None:
			self.kwargs["closefig"] = close_figure
		#
		#
		#
		#
		if columns is not None:
			self.kwargs["columns"] = columns
		#
		#
		#
		#
		if datetime_format is not None:
			self.kwargs["datetime_format"] = datetime_format
		#
		#
		#
		#
		if draw_volume_panel is not None:
			self.kwargs["volume"] = draw_volume_panel
		#
		#
		#
		#
		if figure_size is not None:
			self.kwargs["figsize"] = figure_size
		#
		#
		#
		#
		if font_scale is not None:
			self.kwargs["fontscale"] = font_scale
		#
		#
		#
		#
		if line_color is not None:
			self.kwargs["linecolor"] = line_color
		#
		#
		#
		#
		if panel_ratios is not None:
			self.kwargs["panel_ratios"] = panel_ratios
		#
		#
		#
		#
		if pnf_params is not None:
			self.kwargs["pnf_params"] = pnf_params
		#
		#
		#
		#
		if renko_params is not None:
			self.kwargs["renko_params"] = renko_params
		#
		#
		#
		#
		if scale_padding is not None:
			self.kwargs["scale_padding"] = scale_padding
		#
		#
		#
		#
		if show_non_trading is not None:
			self.kwargs["show_nontrading"] = show_non_trading
		#
		#
		#
		#
		if style is not None:
			self.kwargs["style"] = style
		#
		#
		#
		#
		if tight_layout is not None:
			self.kwargs["tight_layout"] = tight_layout
		#
		#
		#
		#
		if title is not None:
			self.kwargs["title"] = title
		#
		#
		#
		#
		if tz_localize is not None:
			self.kwargs["tz_localize"] = tz_localize
		#
		#
		#
		#
		if volume_alpha is not None:
			self.kwargs["volume_alpha"] = volume_alpha
		#
		#
		#
		#
		if volume_exponent is not None:
			self.kwargs["volume_exponent"] = volume_exponent
		#
		#
		#
		#
		if volume_y_axis_label is not None:
			self.kwargs["ylabel_lower"] = volume_y_axis_label
		#
		#
		#
		#
		if volume_y_axis_scale is not None:
			self.kwargs["volume_yscale"] = volume_y_axis_scale
		#
		#
		#
		#
		if warn_too_much_data is not None:
			self.kwargs["warn_too_much_data"] = warn_too_much_data
		#
		#
		#
		#
		if x_axis_label is not None:
			self.kwargs["xlabel"] = x_axis_label
		#
		#
		#
		#
		if x_axis_rotation is not None:
			self.kwargs["xrotation"] = x_axis_rotation
		#
		#
		#
		#
		if y_axis_label is not None:
			self.kwargs["ylabel"] = y_axis_label
		#
		#
		#
		#
		if y_axis_scale is not None:
			self.kwargs["yscale"] = y_axis_scale
#
#
#
#
class FinancialChartInit(WidgetWithLayoutInit):
	#
	#
	#
	#
	def __init__(
			self,
			draw_navigation_bar: bool = True,
			navigation_bar_on_top: bool = True,
			widget_init: WidgetInit = WidgetInit(),
			layout_init: LayoutInit = LayoutInit()
	):
		super().__init__(widget_init=widget_init, layout_init=layout_init)
		#
		#
		#
		#
		self.draw_navigation_bar = draw_navigation_bar
		self.navigation_bar_on_top = navigation_bar_on_top
#
#
#
#
class PyFinancialChart(PyWidgetWithVerticalLayout):
	#
	#
	#
	#
	def __init__(
			self,
			financial_chart_init: FinancialChartInit,
			financial_figure_init: FinancialFigureInit
	):
		super().__init__(widget_with_layout_init=financial_chart_init)
		#
		#
		#
		#
		self.draw_navigation_bar = financial_chart_init.draw_navigation_bar
		self.navigation_bar_on_top = financial_chart_init.navigation_bar_on_top
		#
		#
		#
		#
		self.redraw_chart(financial_figure_init)
	#
	#
	#
	#
	def redraw_chart(self, financial_figure_init: FinancialFigureInit):
		self.clear_widget_layout()

		figure, axes = mplfinance.plot(data=financial_figure_init.data, **financial_figure_init.kwargs)

		figure_canvas = PyFigureCanvas(figure, axes)

		if self.draw_navigation_bar:
			navigation_bar = NavigationToolbar2QT(figure_canvas, self)

			if self.navigation_bar_on_top:
				self.add_instance(LinearLayoutItem(navigation_bar))
				self.add_instance(LinearLayoutItem(figure_canvas))
			else:
				self.add_instance(LinearLayoutItem(figure_canvas))
				self.add_instance(LinearLayoutItem(navigation_bar))
		else:
			self.add_instance(LinearLayoutItem(figure_canvas))

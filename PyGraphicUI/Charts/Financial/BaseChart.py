import typing
import mplfinance
from pandas import DataFrame
from matplotlib.axes import Axes
from PyGraphicUI.Objects.Layouts import LayoutInit
from PyGraphicUI.Attributes import LinearLayoutItem
from PyGraphicUI.Charts.Canvas import PyFigureCanvas
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from PyGraphicUI.Objects.Widgets import (
	PyWidgetWithVerticalLayout,
	WidgetInit,
	WidgetWithLayoutInit
)


class FinancialChartInit(WidgetWithLayoutInit):
	"""
    Class responsible for initializing the parameters of the financial chart widget.

    Attributes:
        draw_navigation_bar (bool): Whether to draw the navigation bar.
        navigation_bar_on_top (bool): Whether to place the navigation bar on top of the chart.
        widget_init (WidgetInit): Initialization parameters for the widget.
        layout_init (LayoutInit): Initialization parameters for the layout.

    :Usage:
        financial_chart_init = FinancialChartInit(
            draw_navigation_bar=True,
            navigation_bar_on_top=True,
        )
        financial_chart = PyFinancialChart(financial_chart_init=financial_chart_init, financial_figure_init=financial_figure_init)
    """
	
	def __init__(
			self,
			draw_navigation_bar: bool = True,
			navigation_bar_on_top: bool = True,
			widget_init: WidgetInit = WidgetInit(),
			layout_init: LayoutInit = LayoutInit()
	):
		"""
        Initializes a FinancialChartInit object.

        Args:
            draw_navigation_bar (bool): Whether to draw the navigation bar. Defaults to True.
            navigation_bar_on_top (bool): Whether to place the navigation bar on top of the chart. Defaults to True.
            widget_init (WidgetInit): The widget initialization parameters. Defaults to WidgetInit().
            layout_init (LayoutInit): The layout initialization parameters. Defaults to LayoutInit().
        """
		super().__init__(widget_init=widget_init, layout_init=layout_init)
		
		self.draw_navigation_bar = draw_navigation_bar
		self.navigation_bar_on_top = navigation_bar_on_top


class FinancialFigureInit:
	"""
    Class responsible for initializing the parameters of the financial figure.

    Attributes:
        data (DataFrame): DataFrame containing the financial data.
        kwargs (dict): Dictionary containing keyword arguments for the `mplfinance.plot` function.

    :Usage:
        financial_figure_init = FinancialFigureInit(
            data=data,
            chart_type="candle",
            title="Financial Chart",
        )
        figure, axes = mplfinance.plot(data=financial_figure_init.data, **financial_figure_init.kwargs)
    """
	
	def __init__(
			self,
			data: DataFrame,
			chart_type: typing.Literal["candle", "ohlc", "line", "renko", "pnf", "hollow_and_filled"] = "candle",
			add_plot: typing.Optional[typing.Union[dict, list[dict]]] = None,
			axes: typing.Optional[Axes] = None,
			axes_off: typing.Optional[bool] = None,
			axes_title: typing.Optional[typing.Union[str, dict]] = None,
			block_until_figure_close: typing.Optional[bool] = None,
			close_figure: typing.Optional[bool] = None,
			columns: typing.Optional[tuple[str, str, str, str, str]] = None,
			datetime_format: typing.Optional[str] = None,
			draw_volume_panel: typing.Optional[bool] = None,
			figure_size: typing.Optional[tuple[int, int]] = None,
			font_scale: typing.Optional[typing.Union[float, int]] = None,
			line_color: typing.Optional[str] = None,
			panel_ratios: typing.Optional[typing.Union[list[typing.Union[int, float]]]] = None,
			pnf_params: typing.Optional[dict] = None,
			renko_params: typing.Optional[dict] = None,
			scale_padding: float = 1.0,
			show_non_trading: bool = False,
			style: typing.Optional[typing.Union[str, dict]] = None,
			tight_layout: typing.Optional[bool] = None,
			title: typing.Optional[str] = None,
			tz_localize: typing.Optional[bool] = None,
			volume_alpha: typing.Optional[typing.Union[float, int]] = None,
			volume_exponent: typing.Optional[typing.Union[str, int]] = None,
			volume_y_axis_label: typing.Optional[str] = None,
			volume_y_axis_scale: typing.Optional[str] = None,
			warn_too_much_data: typing.Optional[int] = None,
			x_axis_label: typing.Optional[str] = None,
			x_axis_rotation: typing.Optional[typing.Union[float, int]] = None,
			y_axis_label: typing.Optional[str] = None,
			y_axis_scale: typing.Optional[str] = None
	):
		"""
        Initializes a FinancialFigureInit object.

        Args:
            data (DataFrame): The DataFrame containing the financial data.
            chart_type (typing.Optional[str]): The type of chart to be plotted. Defaults to "candle".
            add_plot (typing.Optional[typing.Union[dict, list[dict]]]): A dictionary or typing.Iterable of dictionaries containing the parameters for additional plots. Defaults to None.
            axes (typing.Optional[Axes]): The matplotlib Axes object to plot on. Defaults to None.
            axes_off (typing.Optional[bool]): Whether to turn off the axes. Defaults to None.
            axes_title (typing.Optional[typing.Union[str, dict]]): The title of the axes. Defaults to None.
            block_until_figure_close (typing.Optional[bool]): Whether to block the program until the figure is closed. Defaults to None.
            close_figure (typing.Optional[bool]): Whether to close the figure after plotting. Defaults to None.
            columns (typing.Optional[tuple[str, str, str, str, str]]): The names of the columns in the DataFrame. Defaults to None.
            datetime_format (typing.Optional[str]): The format of the datetime column. Defaults to None.
            draw_volume_panel (typing.Optional[bool]): Whether to draw a volume panel. Defaults to None.
            figure_size (typing.Optional[tuple[int, int]]): The size of the figure. Defaults to None.
            font_scale (float |  typing.Optional[int]): The font scale for the figure. Defaults to None.
            line_color (typing.Optional[str]): The color of the line for line charts. Defaults to None.
            panel_ratios (list[ typing.Union[int, float]] | None): The ratios of the panels in the figure. Defaults to None.
            pnf_params (typing.Optional[dict]): The parameters for the Point and Figure chart. Defaults to None.
            renko_params (typing.Optional[dict]): The parameters for the Renko chart. Defaults to None.
            scale_padding (float | None): The padding for the scale. Defaults to 1.0.
            show_non_trading (typing.Optional[bool]): Whether to show non-trading days. Defaults to False.
            style (typing.Optional[typing.Union[str, dict]]): The style of the figure. Defaults to None.
            tight_layout (typing.Optional[bool]): Whether to use tight layout. Defaults to None.
            title (typing.Optional[str]): The title of the figure. Defaults to None.
            tz_localize (typing.Optional[bool]): Whether to localize the datetime column. Defaults to None.
            volume_alpha ( typing.Optional[typing.Union[float, int]]): The alpha value for the volume panel. Defaults to None.
            volume_exponent (typing.Optional[typing.Union[str, int]]): The exponent for the volume panel. Defaults to None.
            volume_y_axis_label (typing.Optional[str]): The label for the volume y-axis. Defaults to None.
            volume_y_axis_scale (typing.Optional[str]): The scale for the volume y-axis. Defaults to None.
            warn_too_much_data (typing.Optional[int]): The maximum number of data points allowed before a warning is issued. Defaults to None.
            x_axis_label (typing.Optional[str]): The label for the x-axis. Defaults to None.
            x_axis_rotation ( typing.Optional[typing.Union[float, int]]): The rotation of the x-axis labels. Defaults to None.
            y_axis_label (typing.Optional[str]): The label for the y-axis. Defaults to None.
            y_axis_scale (typing.Optional[str]): The scale for the y-axis. Defaults to None.
        """
		self.data = data
		self.kwargs: dict[str, typing.Any] = {"type": chart_type, "returnfig": True}
		
		if add_plot is not None:
			self.kwargs["addplot"] = add_plot
		
		if axes is not None:
			self.kwargs["ax"] = axes
		
		if axes_off is not None:
			self.kwargs["axisoff"] = axes_off
		
		if axes_title is not None:
			self.kwargs["axtitle"] = axes_title
		
		if block_until_figure_close is not None:
			self.kwargs["block"] = block_until_figure_close
		
		if close_figure is not None:
			self.kwargs["closefig"] = close_figure
		
		if columns is not None:
			self.kwargs["columns"] = columns
		
		if datetime_format is not None:
			self.kwargs["datetime_format"] = datetime_format
		
		if draw_volume_panel is not None:
			self.kwargs["volume"] = draw_volume_panel
		
		if figure_size is not None:
			self.kwargs["figsize"] = figure_size
		
		if font_scale is not None:
			self.kwargs["fontscale"] = font_scale
		
		if line_color is not None:
			self.kwargs["linecolor"] = line_color
		
		if panel_ratios is not None:
			self.kwargs["panel_ratios"] = panel_ratios
		
		if pnf_params is not None:
			self.kwargs["pnf_params"] = pnf_params
		
		if renko_params is not None:
			self.kwargs["renko_params"] = renko_params
		
		if scale_padding is not None:
			self.kwargs["scale_padding"] = scale_padding
		
		if show_non_trading is not None:
			self.kwargs["show_nontrading"] = show_non_trading
		
		if style is not None:
			self.kwargs["style"] = style
		
		if tight_layout is not None:
			self.kwargs["tight_layout"] = tight_layout
		
		if title is not None:
			self.kwargs["title"] = title
		
		if tz_localize is not None:
			self.kwargs["tz_localize"] = tz_localize
		
		if volume_alpha is not None:
			self.kwargs["volume_alpha"] = volume_alpha
		
		if volume_exponent is not None:
			self.kwargs["volume_exponent"] = volume_exponent
		
		if volume_y_axis_label is not None:
			self.kwargs["ylabel_lower"] = volume_y_axis_label
		
		if volume_y_axis_scale is not None:
			self.kwargs["volume_yscale"] = volume_y_axis_scale
		
		if warn_too_much_data is not None:
			self.kwargs["warn_too_much_data"] = warn_too_much_data
		
		if x_axis_label is not None:
			self.kwargs["xlabel"] = x_axis_label
		
		if x_axis_rotation is not None:
			self.kwargs["xrotation"] = x_axis_rotation
		
		if y_axis_label is not None:
			self.kwargs["ylabel"] = y_axis_label
		
		if y_axis_scale is not None:
			self.kwargs["yscale"] = y_axis_scale


class PyFinancialChart(PyWidgetWithVerticalLayout):
	"""
    Class representing a financial chart widget.

    Attributes:
        draw_navigation_bar (bool): Whether to draw the navigation bar.
        navigation_bar_on_top (bool): Whether to place the navigation bar on top of the chart.

    :Usage:
        financial_chart = PyFinancialChart(financial_chart_init=financial_chart_init, financial_figure_init=financial_figure_init)
    """
	
	def __init__(
			self,
			financial_chart_init: FinancialChartInit,
			financial_figure_init: FinancialFigureInit
	):
		"""
        Initializes a PyFinancialChart object.

        Args:
            financial_chart_init (FinancialChartInit): The initialization parameters for the financial chart.
            financial_figure_init (FinancialFigureInit): The initialization parameters for the financial figure.
        """
		super().__init__(widget_with_layout_init=financial_chart_init)
		
		self.draw_navigation_bar = financial_chart_init.draw_navigation_bar
		self.navigation_bar_on_top = financial_chart_init.navigation_bar_on_top
		self.redraw_chart(financial_figure_init)
	
	def redraw_chart(self, financial_figure_init: FinancialFigureInit):
		"""
        Redraws the financial chart with the specified initialization parameters.

        Args:
            financial_figure_init (FinancialFigureInit): Initialization parameters for the financial figure.

        :Usage:
            financial_chart.redraw_chart(financial_figure_init)
        """
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

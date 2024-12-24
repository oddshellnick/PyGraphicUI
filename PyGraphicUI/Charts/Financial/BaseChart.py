import typing

import mplfinance
from matplotlib.axes import Axes
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from pandas import DataFrame

from PyGraphicUI.Attributes import LinearLayoutItem
from PyGraphicUI.Charts.Canvas import PyFigureCanvas
from PyGraphicUI.Objects.Layouts import LayoutInit
from PyGraphicUI.Objects.Widgets import (
    PyWidgetWithVerticalLayout,
    WidgetInit,
    WidgetWithLayoutInit,
)


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
        add_plot: dict | list[dict] | None = None,
        axes: Axes | None = None,
        axes_off: bool | None = None,
        axes_title: str | dict | None = None,
        block_until_figure_close: bool | None = None,
        close_figure: bool | None = None,
        columns: tuple[str, str, str, str, str] | None = None,
        datetime_format: str | None = None,
        draw_volume_panel: bool | None = None,
        figure_size: tuple[int, int] | None = None,
        font_scale: float | int | None = None,
        line_color: str | None = None,
        panel_ratios: list[int | float] | None = None,
        pnf_params: dict | None = None,
        renko_params: dict | None = None,
        scale_padding: float = 1.0,
        show_non_trading: bool = False,
        style: str | dict | None = None,
        tight_layout: bool | None = None,
        title: str | None = None,
        tz_localize: bool | None = None,
        volume_alpha: int | float | None = None,
        volume_exponent: int | str | None = None,
        volume_y_axis_label: str | None = None,
        volume_y_axis_scale: str | None = None,
        warn_too_much_data: int | None = None,
        x_axis_label: str | None = None,
        x_axis_rotation: int | float | None = None,
        y_axis_label: str | None = None,
        y_axis_scale: str | None = None,
    ):
        """
        Initializes a FinancialFigureInit object.

        Args:
            data (DataFrame): The DataFrame containing the financial data.
            chart_type (str | None): The type of chart to be plotted. Defaults to "candle".
            add_plot (dict | list[dict] | None): A dictionary or list of dictionaries containing the parameters for additional plots. Defaults to None.
            axes (Axes | None): The matplotlib Axes object to plot on. Defaults to None.
            axes_off (bool | None): Whether to turn off the axes. Defaults to None.
            axes_title (str | dict | None): The title of the axes. Defaults to None.
            block_until_figure_close (bool | None): Whether to block the program until the figure is closed. Defaults to None.
            close_figure (bool | None): Whether to close the figure after plotting. Defaults to None.
            columns (tuple[str, str, str, str, str] | None): The names of the columns in the DataFrame. Defaults to None.
            datetime_format (str | None): The format of the datetime column. Defaults to None.
            draw_volume_panel (bool | None): Whether to draw a volume panel. Defaults to None.
            figure_size (tuple[int, int] | None): The size of the figure. Defaults to None.
            font_scale (float | int | None): The font scale for the figure. Defaults to None.
            line_color (str | None): The color of the line for line charts. Defaults to None.
            panel_ratios (list[int | float] | None): The ratios of the panels in the figure. Defaults to None.
            pnf_params (dict | None): The parameters for the Point and Figure chart. Defaults to None.
            renko_params (dict | None): The parameters for the Renko chart. Defaults to None.
            scale_padding (float | None): The padding for the scale. Defaults to 1.0.
            show_non_trading (bool | None): Whether to show non-trading days. Defaults to False.
            style (str | dict | None): The style of the figure. Defaults to None.
            tight_layout (bool | None): Whether to use tight layout. Defaults to None.
            title (str | None): The title of the figure. Defaults to None.
            tz_localize (bool | None): Whether to localize the datetime column. Defaults to None.
            volume_alpha (int | float | None): The alpha value for the volume panel. Defaults to None.
            volume_exponent (int | str | None): The exponent for the volume panel. Defaults to None.
            volume_y_axis_label (str | None): The label for the volume y-axis. Defaults to None.
            volume_y_axis_scale (str | None): The scale for the volume y-axis. Defaults to None.
            warn_too_much_data (int | None): The maximum number of data points allowed before a warning is issued. Defaults to None.
            x_axis_label (str | None): The label for the x-axis. Defaults to None.
            x_axis_rotation (int | float | None): The rotation of the x-axis labels. Defaults to None.
            y_axis_label (str | None): The label for the y-axis. Defaults to None.
            y_axis_scale (str | None): The scale for the y-axis. Defaults to None.
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
        layout_init: LayoutInit = LayoutInit(),
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


class PyFinancialChart(PyWidgetWithVerticalLayout):
    """
    Class representing a financial chart widget.

    Attributes:
        draw_navigation_bar (bool): Whether to draw the navigation bar.
        navigation_bar_on_top (bool): Whether to place the navigation bar on top of the chart.

    :Usage:
        financial_chart = PyFinancialChart(financial_chart_init=financial_chart_init, financial_figure_init=financial_figure_init)
    """

    def __init__(self, financial_chart_init: FinancialChartInit, financial_figure_init: FinancialFigureInit):
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

from matplotlib.axes import Axes
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class PyFigureCanvas(FigureCanvasQTAgg):
    """
    A class representing a PyFigureCanvas widget.

    Attributes:
        figure (Figure): The matplotlib Figure object.
        axes (list[Axes]): A list of matplotlib Axes objects.

    :Usage:
        figure, axes = mplfinance.plot(data=data, **kwargs)
        figure_canvas = PyFigureCanvas(figure=figure, axes=axes)
    """

    def __init__(self, figure: Figure, axes: list[Axes]):
        """
        Initializes a PyFigureCanvas object.

        Args:
            figure (Figure): The matplotlib Figure object.
            axes (list[Axes]): A list of matplotlib Axes objects.
        """
        self.axes = axes
        super().__init__(figure)

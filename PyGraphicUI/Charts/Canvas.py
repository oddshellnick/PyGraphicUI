from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
#
#
#
#
class PyFigureCanvas(FigureCanvasQTAgg):
    #
    #
    #
    #
    def __init__(self, figure: Figure, axes: list[Axes]):
        self.axes = axes
        super().__init__(figure)

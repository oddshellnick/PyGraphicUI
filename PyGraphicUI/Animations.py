from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QColor, QIcon, QPainter, QPixmap, QTransform
from PyQt6.QtCore import QAbstractAnimation, QByteArray, QPropertyAnimation, QSize, QVariantAnimation, Qt
from PyGraphicUI.Objects.Label import PyLabel
from PyGraphicUI.Objects.PushButton import PyPushButton
#
#
#
#
class AbstractAnimation(QAbstractAnimation):
    animated_widget = None
    #
    #
    #
    #
    def __init__(self):
        #
        #
        #
        #
        super().__init__()
    #
    #
    #
    #
    def start_animation(self):
        pass
    #
    #
    #
    #
    def end_animation(self):
        pass
#
#
#
#
class FadeOutAnimation(QPropertyAnimation, AbstractAnimation):
    #
    #
    #
    #
    def __init__(
            self,
            pixmap: QPixmap,
            pixmap_size: QSize,
            duration: int = 2500,
            loop_count: int = -1,
            parent: QLabel | QPushButton = None,
            start_color: QColor = QColor(0, 0, 0),
            end_color: QColor = QColor(255, 255, 255)
    ):
        #
        #
        #
        #
        super().__init__()
        #
        #
        #
        #
        self.animated_widget, self.pixmap_to_animate, self.pixmap_size, self.start_color, self.end_color = parent, pixmap, pixmap_size, start_color, end_color
        #
        #
        #
        #
        self.pixmap_to_animate = self.pixmap_to_animate.scaled(self.pixmap_size, transformMode=Qt.TransformationMode.SmoothTransformation)
        #
        #
        #
        #
        self.previous_color = self.start_color
        #
        #
        #
        #
        self.setStartValue(self.start_color)
        self.setDuration(duration)
        self.setEndValue(self.end_color)
        self.setLoopCount(loop_count)
        self.setParent(self.animated_widget)
        self.setPropertyName(QByteArray(b"color"))
        self.valueChanged.connect(self.fade_out)
    #
    #
    #
    #
    def change_pixmap_color(self, pixmap: QPixmap, new_color: QColor):
        new_pixmap = pixmap
        new_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(new_pixmap)
        painter.setCompositionMode(painter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(new_pixmap.rect(), new_color)
        painter.end()

        return new_pixmap
    #
    #
    #
    #
    def fade_out(self, value):
        if type(self.animated_widget) == QLabel or type(self.animated_widget) == FadeOutAnimatedLabel:
            self.animated_widget.setPixmap(self.change_pixmap_color(self.pixmap_to_animate, value))
        elif type(self.animated_widget) == QPushButton or type(self.animated_widget) == FadeOutAnimatedPushButton:
            self.animated_widget.setIcon(QIcon(self.change_pixmap_color(self.pixmap_to_animate, value)))

        if value == self.startValue():
            self.setDirection(QPropertyAnimation.Direction.Forward)
        elif value == self.endValue():
            self.setDirection(QPropertyAnimation.Direction.Backward)
    #
    #
    #
    #
    def start_animation(self):
        self.start()
    #
    #
    #
    #
    def end_animation(self):
        self.stop()
#
#
#
#
class FadeOutAnimatedPushButton(PyPushButton):
    #
    #
    #
    #
    def __init__(
            self,
            pixmap_to_animate: QPixmap,
            pixmap_to_animate_size: QSize,
            duration: int = 2500,
            loop_count: int = -1,
            start_color: QColor = QColor(0, 0, 0),
            end_color: QColor = QColor(255, 255, 255),
            **kwargs
    ):
        #
        #
        #
        #
        super().__init__(**kwargs)
        #
        #
        #
        #
        self.button_animation = FadeOutAnimation(
                pixmap_to_animate,
                pixmap_to_animate_size,
                duration,
                loop_count,
                self,
                start_color,
                end_color
        )
        self.button_animation.finished.connect(self.set_default_button_instance)
#
#
#
#
class FadeOutAnimatedLabel(PyLabel):
    #
    #
    #
    #
    def __init__(
            self,
            pixmap_to_animate: QPixmap,
            pixmap_to_animate_size: QSize,
            duration: int = 2500,
            loop_count: int = -1,
            start_color: QColor = QColor(0, 0, 0),
            end_color: QColor = QColor(255, 255, 255),
            **kwargs
    ):
        #
        #
        #
        #
        super().__init__(**kwargs)
        #
        #
        #
        #
        self.label_animation = FadeOutAnimation(
                pixmap_to_animate,
                pixmap_to_animate_size,
                duration,
                loop_count,
                self,
                start_color,
                end_color
        )
        self.label_animation.finished.connect(self.set_default_label_instance)
#
#
#
#
class SpinAnimation(QVariantAnimation, AbstractAnimation):
    #
    #
    #
    #
    def __init__(
            self,
            pixmap: QPixmap,
            pixmap_size: QSize,
            duration: int = 1000,
            loop_count: int = -1,
            parent: QLabel | QPushButton = None
    ):
        #
        #
        #
        #
        super().__init__()
        #
        #
        #
        #
        self.animated_widget, self.pixmap_to_animate, self.pixmap_size = parent, pixmap, pixmap_size
        #
        #
        #
        #
        self.pixmap_to_animate = self.pixmap_to_animate.scaled(self.pixmap_size, transformMode=Qt.TransformationMode.SmoothTransformation)
        #
        #
        #
        #
        self.setStartValue(0.0)
        self.setDuration(duration)
        self.setEndValue(360.0)
        self.setLoopCount(loop_count)
        self.valueChanged.connect(self.rotate)
    #
    #
    #
    #
    def rotate(self, value):
        if type(self.animated_widget) == QLabel or type(self.animated_widget) == SpinAnimatedLabel:
            self.animated_widget.setPixmap(self.pixmap_to_animate.transformed(QTransform().rotate(value)))
        elif type(self.animated_widget) == QPushButton or type(self.animated_widget) == SpinAnimatedPushButton:
            self.animated_widget.setIcon(QIcon(self.pixmap_to_animate.transformed(QTransform().rotate(value))))
    #
    #
    #
    #
    def start_animation(self):
        self.start()
    #
    #
    #
    #
    def end_animation(self):
        self.stop()
#
#
#
#
class SpinAnimatedPushButton(PyPushButton):
    #
    #
    #
    #
    def __init__(
            self,
            pixmap_to_animate: QPixmap,
            pixmap_to_animate_size: QSize,
            duration: int = 1000,
            loop_count: int = -1,
            **kwargs
    ):
        #
        #
        #
        #
        super().__init__(**kwargs)
        #
        #
        #
        #
        self.button_animation = SpinAnimation(pixmap_to_animate, pixmap_to_animate_size, duration, loop_count, self)
        self.button_animation.animated_widget = self
        self.button_animation.finished.connect(self.set_default_button_instance)
#
#
#
#
class SpinAnimatedLabel(PyLabel):
    #
    #
    #
    #
    def __init__(
            self,
            pixmap_to_animate: QPixmap,
            pixmap_to_animate_size: QSize,
            duration: int = 1000,
            loop_count: int = -1,
            **kwargs
    ):
        #
        #
        #
        #
        super().__init__(**kwargs)
        #
        #
        #
        #
        self.label_animation = SpinAnimation(pixmap_to_animate, pixmap_to_animate_size, duration, loop_count, self)
        self.label_animation.animated_widget = self
        self.label_animation.finished.connect(self.set_default_label_instance)

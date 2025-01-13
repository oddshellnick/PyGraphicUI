import typing
from time import time
from datetime import datetime
from PyQt6.QtCore import QTimer, Qt
from dateutil.relativedelta import relativedelta
from PyGraphicUI.Attributes import ObjectSize, PyFont
from PyGraphicUI.Objects.Label import LabelInit, PyLabel
from PyQt6.QtWidgets import (
	QGraphicsEffect,
	QSizePolicy,
	QWidget
)


class TimerInit(LabelInit):
	"""
    Data class for initializing timer widgets. Inherits from LabelInit.

    Attributes:
        name (str): The object name of the timer. Defaults to "timer".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the timer is enabled. Defaults to True.
        visible (bool): Whether the timer is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the timer. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the timer. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the timer. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the timer. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the timer. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the timer. Defaults to None.
        scaled_contents (bool): Whether the contents should be scaled. Defaults to False.
        word_wrap (bool): Whether word wrap is enabled. Defaults to True.
        indent (int): The indentation. Defaults to 10.
        alignment (Qt.AlignmentFlag): The alignment flag. Defaults to Qt.AlignmentFlag.AlignCenter.
        interaction_flag (Qt.TextInteractionFlag): The text interaction flag. Defaults to Qt.TextInteractionFlag.NoTextInteraction.
        font (PyFont): The font for the text.
        update_interval (int): The update interval in milliseconds. Defaults to 100.
        always_print_years (bool): Whether to always print years, even if zero. Defaults to False.
        always_print_months (bool): Whether to always print months, even if zero. Defaults to False.
        always_print_weeks (bool): Whether to always print weeks, even if zero. Defaults to False.
        always_print_days (bool): Whether to always print days, even if zero. Defaults to False.
        always_print_hours (bool): Whether to always print hours, even if zero. Defaults to True.
        always_print_minutes (bool): Whether to always print minutes, even if zero. Defaults to True.
        always_print_seconds (bool): Whether to always print seconds, even if zero. Defaults to True.
        years_format (str): Format string for years. Defaults to "{value}y".
        months_format (str): Format string for months. Defaults to "{value}mon".
        weeks_format (str): Format string for weeks. Defaults to "{value}w".
        days_format (str): Format string for days. Defaults to "{value}d".
        hours_format (str): Format string for hours. Defaults to "{value:02d}".
        minutes_format (str): Format string for minutes. Defaults to "{value:02d}".
        seconds_format (str): Format string for seconds. Defaults to "{value:02d}".
        disable_negative_time (bool): Whether to disable displaying negative time. Defaults to True.
        prefix (str): Prefix string for the displayed time. Defaults to "".
        postfix (str): Postfix string for the displayed time. Defaults to "".

    :Usage:
        timer_init = TimerInit(update_interval=500, always_print_minutes=False, prefix="Time remaining: ")
        timer = PyTimer(timer_init)
        end_time = datetime.now() + timedelta(minutes=5)
        timer.start_timer(end_time)

    """
	
	def __init__(
			self,
			name: str = "timer",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			scaled_contents: bool = False,
			word_wrap: bool = True,
			indent: int = 10,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
			font: PyFont = PyFont(),
			update_interval: int = 100,
			always_print_years: bool = False,
			always_print_months: bool = False,
			always_print_weeks: bool = False,
			always_print_days: bool = False,
			always_print_hours: bool = True,
			always_print_minutes: bool = True,
			always_print_seconds: bool = True,
			years_format: str = "{value}y",
			months_format: str = "{value}mon",
			weeks_format: str = "{value}w",
			days_format: str = "{value}d",
			hours_format: str = "{value:02d}",
			minutes_format: str = "{value:02d}",
			seconds_format: str = "{value:02d}",
			disable_negative_time: bool = True,
			prefix: str = "",
			postfix: str = ""
	):
		"""
        Initializes a TimerInit object.

        Args:
            name (str): The object name of the timer. Defaults to "timer".
            parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
            enabled (bool): Whether the timer is enabled. Defaults to True.
            visible (bool): Whether the timer is visible. Defaults to True.
            style_sheet (str): The style sheet to apply to the timer. Defaults to "".
            minimum_size (typing.Optional[ObjectSize]): The minimum size of the timer. Defaults to None.
            maximum_size (typing.Optional[ObjectSize]): The maximum size of the timer. Defaults to None.
            fixed_size (typing.Optional[ObjectSize]): The fixed size of the timer. Defaults to None.
            size_policy (typing.Optional[QSizePolicy]): The size policy of the timer. Defaults to None.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the timer. Defaults to None.
            scaled_contents (bool): Whether the contents should be scaled. Defaults to False.
            word_wrap (bool): Whether word wrap is enabled. Defaults to True.
            indent (int): The indentation. Defaults to 10.
            alignment (Qt.AlignmentFlag): The alignment flag. Defaults to Qt.AlignmentFlag.AlignCenter.
            interaction_flag (Qt.TextInteractionFlag): The text interaction flag. Defaults to Qt.TextInteractionFlag.NoTextInteraction.
            font (PyFont): The font for the text.
            update_interval (int): The update interval in milliseconds. Defaults to 100.
            always_print_years (bool): Whether to always print years, even if zero. Defaults to False.
            always_print_months (bool): Whether to always print months, even if zero. Defaults to False.
            always_print_weeks (bool): Whether to always print weeks, even if zero. Defaults to False.
            always_print_days (bool): Whether to always print days, even if zero. Defaults to False.
            always_print_hours (bool): Whether to always print hours, even if zero. Defaults to True.
            always_print_minutes (bool): Whether to always print minutes, even if zero. Defaults to True.
            always_print_seconds (bool): Whether to always print seconds, even if zero. Defaults to True.
            years_format (str): Format string for years. Defaults to "{value}y".
            months_format (str): Format string for months. Defaults to "{value}mon".
            weeks_format (str): Format string for weeks. Defaults to "{value}w".
            days_format (str): Format string for days. Defaults to "{value}d".
            hours_format (str): Format string for hours. Defaults to "{value:02d}".
            minutes_format (str): Format string for minutes. Defaults to "{value:02d}".
            seconds_format (str): Format string for seconds. Defaults to "{value:02d}".
            disable_negative_time (bool): Whether to disable displaying negative time. Defaults to True.
            prefix (str): Prefix string for the displayed time. Defaults to "".
            postfix (str): Postfix string for the displayed time. Defaults to "".
        """
		super().__init__(
				name,
				parent,
				enabled,
				visible,
				style_sheet,
				minimum_size,
				maximum_size,
				fixed_size,
				size_policy,
				graphic_effect,
				scaled_contents,
				word_wrap,
				indent,
				alignment,
				interaction_flag,
				font
		)
		
		self.update_interval = update_interval
		self.always_print_years = always_print_years
		self.always_print_months = always_print_months
		self.always_print_weeks = always_print_weeks
		self.always_print_days = always_print_days
		self.always_print_hours = always_print_hours
		self.always_print_minutes = always_print_minutes
		self.always_print_seconds = always_print_seconds
		self.years_format = years_format
		self.months_format = months_format
		self.weeks_format = weeks_format
		self.days_format = days_format
		self.hours_format = hours_format
		self.minutes_format = minutes_format
		self.seconds_format = seconds_format
		self.disable_negative_time = disable_negative_time
		self.prefix = prefix
		self.postfix = postfix


class PyTimer(PyLabel):
	"""
    A custom timer widget based on PyLabel.
    """
	
	def __init__(self, timer_init: TimerInit = TimerInit()):
		"""
        Initializes the PyTimer widget.

        Args:
            timer_init (TimerInit): The initialization parameters for the timer.
        """
		super().__init__(label_init=timer_init)
		
		self.update_interval = timer_init.update_interval
		self.always_print_years = timer_init.always_print_years
		self.always_print_months = timer_init.always_print_months
		self.always_print_weeks = timer_init.always_print_weeks
		self.always_print_days = timer_init.always_print_days
		self.always_print_hours = timer_init.always_print_hours
		self.always_print_minutes = timer_init.always_print_minutes
		self.always_print_seconds = timer_init.always_print_seconds
		self.years_format = timer_init.years_format
		self.months_format = timer_init.months_format
		self.weeks_format = timer_init.weeks_format
		self.days_format = timer_init.days_format
		self.hours_format = timer_init.hours_format
		self.minutes_format = timer_init.minutes_format
		self.seconds_format = timer_init.seconds_format
		self.end_time: typing.Optional[datetime] = None
		self.disable_negative_time = timer_init.disable_negative_time
		self.prefix = timer_init.prefix
		self.postfix = timer_init.postfix
		
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.print_time)
		
		self.setText("%s%s%s" % (self.prefix, self.get_time_string(), self.postfix))
	
	def get_time_string(self, time_: typing.Optional[relativedelta] = None) -> str:
		"""
        Formats the time difference into a string.

        Args:
            time_ (typing.Optional[relativedelta]): The time difference to format.

        Returns:
            str: The formatted time string.
        """
		if time_ is None:
			time_ = relativedelta(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0)
		
		years_s = self.years_format.format(value=time_.years) if time_.years or self.always_print_years else ""
		months_s = self.months_format.format(value=time_.months) if time_.months or self.always_print_months else ""
		weeks_s = self.weeks_format.format(value=time_.weeks) if time_.weeks or self.always_print_weeks else ""
		days_s = self.days_format.format(value=time_.days) if time_.days or self.always_print_days else ""
		hours_s = self.hours_format.format(value=time_.hours) if time_.hours or self.always_print_hours else ""
		minutes_s = (
				self.minutes_format.format(value=time_.minutes)
				if time_.minutes
				or self.always_print_minutes
				else ""
		)
		seconds_s = (
				self.seconds_format.format(value=time_.seconds)
				if time_.seconds
				or self.always_print_seconds
				else ""
		)
		
		time_out_of_day = " ".join(list(filter(None, [years_s, months_s, weeks_s, days_s])))
		time_in_day_string = ":".join(list(filter(None, [hours_s, minutes_s, seconds_s])))
		
		return " ".join(list(filter(None, [time_out_of_day, time_in_day_string])))
	
	def get_estimated_time_string(self) -> str:
		"""
        Calculates and formats the estimated time string.

        Returns:
            str: The estimated time string.
        """
		if self.end_time is not None:
			time_diff = self.end_time.timestamp() - datetime.now().timestamp()
			if time_diff >= 0:
				return self.get_time_string(relativedelta(self.end_time, datetime.now()))
			else:
				if self.disable_negative_time:
					return self.get_time_string()
				else:
					return "-" + self.get_time_string(relativedelta(datetime.now(), self.end_time))
		else:
			return self.get_time_string()
	
	def print_time(self):
		"""Updates the timer display with the current time."""
		self.setText("%s%s%s" % (self.prefix, self.get_estimated_time_string(), self.postfix))
	
	def set_end_time(self, end_time: datetime):
		"""
        Sets the target end time for the timer.

        Args:
            end_time (datetime): The datetime object representing the end time.
        """
		self.end_time = end_time
	
	def start_timer(self, end_time: datetime):
		"""
        Starts the timer with the specified end time.

        Args:
            end_time (datetime): The end time for the timer.
        """
		self.set_end_time(end_time)
		self.timer.start(self.update_interval)
	
	def stop_timer(self):
		"""Stops the timer and resets the end time."""
		self.timer.stop()
		self.end_time = None
	
	def restart_watch(self, end_time: datetime):
		"""
        Restarts the timer with a new end time.

        Args:
            end_time (datetime): The new end time for the timer.
        """
		self.stop_timer()
		self.start_timer(end_time)


class StopWatchInit(LabelInit):
	"""
    Data class for initializing stopwatch widgets.

    Attributes:
        name (str): The object name of the stopwatch. Defaults to "stop_watch".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the stopwatch is enabled. Defaults to True.
        visible (bool): Whether the stopwatch is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the stopwatch. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the stopwatch. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the stopwatch. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the stopwatch. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the stopwatch. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the stopwatch. Defaults to None.
        scaled_contents (bool): Whether to scale contents. Defaults to False.
        word_wrap (bool): Whether to wrap words. Defaults to True.
        indent (int): Indentation value. Defaults to 10.
        alignment (Qt.AlignmentFlag): Alignment flag. Defaults to Qt.AlignmentFlag.AlignCenter.
        interaction_flag (Qt.TextInteractionFlag): Interaction flag. Defaults to Qt.TextInteractionFlag.NoTextInteraction.
        font (PyFont): The font to use.
        update_interval (int): Update interval in milliseconds. Defaults to 100.
        always_print_years (bool): Whether to always print years. Defaults to False.
        always_print_months (bool): Whether to always print months. Defaults to False.
        always_print_weeks (bool): Whether to always print weeks. Defaults to False.
        always_print_days (bool): Whether to always print days. Defaults to False.
        always_print_hours (bool): Whether to always print hours. Defaults to True.
        always_print_minutes (bool): Whether to always print minutes. Defaults to True.
        always_print_seconds (bool): Whether to always print seconds. Defaults to True.
        years_format (str): Format string for years. Defaults to "{value}y".
        months_format (str): Format string for months. Defaults to "{value}mon".
        weeks_format (str): Format string for weeks. Defaults to "{value}w".
        days_format (str): Format string for days. Defaults to "{value}d".
        hours_format (str): Format string for hours. Defaults to "{value:02d}".
        minutes_format (str): Format string for minutes. Defaults to "{value:02d}".
        seconds_format (str): Format string for seconds. Defaults to "{value:02d}".
        prefix (str): The prefix string. Defaults to "".
        postfix (str): The postfix string. Defaults to "".
    """
	
	def __init__(
			self,
			name: str = "stop_watch",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			scaled_contents: bool = False,
			word_wrap: bool = True,
			indent: int = 10,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
			font: PyFont = PyFont(),
			update_interval: int = 100,
			always_print_years: bool = False,
			always_print_months: bool = False,
			always_print_weeks: bool = False,
			always_print_days: bool = False,
			always_print_hours: bool = True,
			always_print_minutes: bool = True,
			always_print_seconds: bool = True,
			years_format: str = "{value}y",
			months_format: str = "{value}mon",
			weeks_format: str = "{value}w",
			days_format: str = "{value}d",
			hours_format: str = "{value:02d}",
			minutes_format: str = "{value:02d}",
			seconds_format: str = "{value:02d}",
			prefix: str = "",
			postfix: str = ""
	):
		"""
        Initializes a StopWatchInit object.

        Args:
            name (str): The object name of the stopwatch. Defaults to "stop_watch".
            parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
            enabled (bool): Whether the stopwatch is enabled. Defaults to True.
            visible (bool): Whether the stopwatch is visible. Defaults to True.
            style_sheet (str): The style sheet to apply to the stopwatch. Defaults to "".
            minimum_size (typing.Optional[ObjectSize]): The minimum size of the stopwatch. Defaults to None.
            maximum_size (typing.Optional[ObjectSize]): The maximum size of the stopwatch. Defaults to None.
            fixed_size (typing.Optional[ObjectSize]): The fixed size of the stopwatch. Defaults to None.
            size_policy (typing.Optional[QSizePolicy]): The size policy of the stopwatch. Defaults to None.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the stopwatch. Defaults to None.
            scaled_contents (bool): Whether to scale contents. Defaults to False.
            word_wrap (bool): Whether to wrap words. Defaults to True.
            indent (int): Indentation value. Defaults to 10.
            alignment (Qt.AlignmentFlag): Alignment flag. Defaults to Qt.AlignmentFlag.AlignCenter.
            interaction_flag (Qt.TextInteractionFlag): Interaction flag. Defaults to Qt.TextInteractionFlag.NoTextInteraction.
            font (PyFont): The font to use.
            update_interval (int): Update interval in milliseconds. Defaults to 100.
            always_print_years (bool): Whether to always print years. Defaults to False.
            always_print_months (bool): Whether to always print months. Defaults to False.
            always_print_weeks (bool): Whether to always print weeks. Defaults to False.
            always_print_days (bool): Whether to always print days. Defaults to False.
            always_print_hours (bool): Whether to always print hours. Defaults to True.
            always_print_minutes (bool): Whether to always print minutes. Defaults to True.
            always_print_seconds (bool): Whether to always print seconds. Defaults to True.
            years_format (str): Format string for years. Defaults to "{value}y".
            months_format (str): Format string for months. Defaults to "{value}mon".
            weeks_format (str): Format string for weeks. Defaults to "{value}w".
            days_format (str): Format string for days. Defaults to "{value}d".
            hours_format (str): Format string for hours. Defaults to "{value:02d}".
            minutes_format (str): Format string for minutes. Defaults to "{value:02d}".
            seconds_format (str): Format string for seconds. Defaults to "{value:02d}".
            prefix (str): The prefix string. Defaults to "".
            postfix (str): The postfix string. Defaults to "".
        """
		super().__init__(
				name,
				parent,
				enabled,
				visible,
				style_sheet,
				minimum_size,
				maximum_size,
				fixed_size,
				size_policy,
				graphic_effect,
				scaled_contents,
				word_wrap,
				indent,
				alignment,
				interaction_flag,
				font
		)
		
		self.update_interval = update_interval
		self.always_print_years = always_print_years
		self.always_print_months = always_print_months
		self.always_print_weeks = always_print_weeks
		self.always_print_days = always_print_days
		self.always_print_hours = always_print_hours
		self.always_print_minutes = always_print_minutes
		self.always_print_seconds = always_print_seconds
		self.years_format = years_format
		self.months_format = months_format
		self.weeks_format = weeks_format
		self.days_format = days_format
		self.hours_format = hours_format
		self.minutes_format = minutes_format
		self.seconds_format = seconds_format
		self.prefix = prefix
		self.postfix = postfix


class PyStopWatch(PyLabel):
	"""
    A custom stopwatch widget that inherits from PyLabel.
    """
	
	def __init__(self, stop_watch_init: StopWatchInit = StopWatchInit()):
		"""
        Initializes a PyStopWatch object.

        Args:
            stop_watch_init (StopWatchInit): Initialization data for the stopwatch.
        """
		super().__init__(label_init=stop_watch_init)
		
		self.stop_watch_font = stop_watch_init.font
		self.update_interval = stop_watch_init.update_interval
		self.always_print_years = stop_watch_init.always_print_years
		self.always_print_months = stop_watch_init.always_print_months
		self.always_print_weeks = stop_watch_init.always_print_weeks
		self.always_print_days = stop_watch_init.always_print_days
		self.always_print_hours = stop_watch_init.always_print_hours
		self.always_print_minutes = stop_watch_init.always_print_minutes
		self.always_print_seconds = stop_watch_init.always_print_seconds
		self.years_format = stop_watch_init.years_format
		self.months_format = stop_watch_init.months_format
		self.weeks_format = stop_watch_init.weeks_format
		self.days_format = stop_watch_init.days_format
		self.hours_format = stop_watch_init.hours_format
		self.minutes_format = stop_watch_init.minutes_format
		self.seconds_format = stop_watch_init.seconds_format
		self.start_time: typing.Optional[datetime] = None
		self.prefix = stop_watch_init.prefix
		self.postfix = stop_watch_init.postfix
		
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.print_time)
		
		self.setText("%s%s%s" % (self.prefix, self.get_time_string(), self.postfix))
	
	def get_time_string(self, time_: typing.Optional[relativedelta] = None) -> str:
		"""
        Formats a time delta into a string.

        Args:
            time_ (typing.Optional[relativedelta]): A relativedelta object representing the time difference. If None, defaults to zero time.

        Returns:
            str: A formatted time string.
        """
		if time_ is None:
			time_ = relativedelta(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0)
		
		years_s = self.years_format.format(value=time_.years) if time_.years or self.always_print_years else ""
		months_s = self.months_format.format(value=time_.months) if time_.months or self.always_print_months else ""
		weeks_s = self.weeks_format.format(value=time_.weeks) if time_.weeks or self.always_print_weeks else ""
		days_s = self.days_format.format(value=time_.days) if time_.days or self.always_print_days else ""
		hours_s = self.hours_format.format(value=time_.hours) if time_.hours or self.always_print_hours else ""
		minutes_s = (
				self.minutes_format.format(value=time_.minutes)
				if time_.minutes
				or self.always_print_minutes
				else ""
		)
		seconds_s = (
				self.seconds_format.format(value=time_.seconds)
				if time_.seconds
				or self.always_print_seconds
				else ""
		)
		
		time_out_of_day = " ".join(list(filter(None, [years_s, months_s, weeks_s, days_s])))
		time_in_day_string = ":".join(list(filter(None, [hours_s, minutes_s, seconds_s])))
		
		return " ".join(list(filter(None, [time_out_of_day, time_in_day_string])))
	
	def get_time_gone_string(self) -> str:
		"""
        Gets the elapsed time as a formatted string.

        Returns:
            str: The elapsed time string.
        """
		if self.start_time is not None:
			return self.get_time_string(relativedelta(datetime.now(), self.start_time))
		else:
			return self.get_time_string()
	
	def print_time(self):
		"""Updates the stopwatch display with the current elapsed time."""
		self.setText("%s%s%s" % (self.prefix, self.get_time_gone_string(), self.postfix))
	
	def start_watch(self):
		"""Starts the stopwatch."""
		self.start_time = datetime.now()
		self.timer.start(self.update_interval)
	
	def stop_watch(self):
		"""Stops the stopwatch."""
		self.timer.stop()
		self.start_time = None
	
	def restart_watch(self):
		"""Restarts the stopwatch."""
		self.stop_watch()
		self.start_watch()


class ProgressWatcherInit(LabelInit):
	"""
    Data class for initializing progress watcher widgets.

    Attributes:
        name (str): The object name of the progress watcher. Defaults to "progress_watcher".
        parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
        enabled (bool): Whether the progress watcher is enabled. Defaults to True.
        visible (bool): Whether the progress watcher is visible. Defaults to True.
        style_sheet (str): The style sheet to apply to the progress watcher. Defaults to "".
        minimum_size (typing.Optional[ObjectSize]): The minimum size of the progress watcher. Defaults to None.
        maximum_size (typing.Optional[ObjectSize]): The maximum size of the progress watcher. Defaults to None.
        fixed_size (typing.Optional[ObjectSize]): The fixed size of the progress watcher. Defaults to None.
        size_policy (typing.Optional[QSizePolicy]): The size policy of the progress watcher. Defaults to None.
        graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the progress watcher. Defaults to None.
        scaled_contents (bool): Whether to scale the contents. Defaults to False.
        word_wrap (bool): Whether word wrap is enabled. Defaults to True.
        indent (int): The indentation. Defaults to 10.
        alignment (Qt.AlignmentFlag): The alignment of the text. Defaults to Qt.AlignmentFlag.AlignCenter.
        interaction_flag (Qt.TextInteractionFlag): The text interaction flag. Defaults to Qt.TextInteractionFlag.NoTextInteraction.
        font (PyFont): The font for the text.
        update_interval (int): The update interval in milliseconds. Defaults to 100.
        current_point (int): The initial current progress point. Defaults to 0.
        start_point (int): The initial starting progress point. Defaults to 0.
        end_point (int): The initial ending progress point. Defaults to 0.
        always_print_years (bool): Whether to always include years in the time display, even if zero. Defaults to False.
        always_print_months (bool): Whether to always include months in the time display, even if zero. Defaults to False.
        always_print_weeks (bool): Whether to always include weeks in the time display, even if zero. Defaults to False.
        always_print_days (bool): Whether to always include days in the time display, even if zero. Defaults to False.
        always_print_hours (bool): Whether to always include hours in the time display, even if zero. Defaults to True.
        always_print_minutes (bool): Whether to always include minutes in the time display, even if zero. Defaults to True.
        always_print_seconds (bool): Whether to always include seconds in the time display, even if zero. Defaults to True.
        disable_negative_time (bool): Whether to prevent displaying negative time. Defaults to True.
        points_per_year_format (str): Format string for points per year. Defaults to "{points:.2f}/y".
        points_per_month_format (str): Format string for points per month. Defaults to "{points:.2f}/mon".
        points_per_week_format (str): Format string for points per week. Defaults to "{points:.2f}/w".
        points_per_day_format (str): Format string for points per day. Defaults to "{points:.2f}/d".
        points_per_hour_format (str): Format string for points per hour. Defaults to "{points:.2f}/h".
        points_per_minute_format (str): Format string for points per minute. Defaults to "{points:.2f}/m".
        points_per_second_format (str): Format string for points per second. Defaults to "{points:.2f}/s".
        points_per_millisecond_format (str): Format string for points per millisecond. Defaults to "{points:.2f}/ms".
        points_per_microsecond_format (str): Format string for points per microsecond. Defaults to "{points:.2f}/mcs".
        points_per_nanosecond_format (str): Format string for points per nanosecond. Defaults to "{points:.2f}/ns".
        years_format (str): Format string for years. Defaults to "{value}y".
        months_format (str): Format string for months. Defaults to "{value}mon".
        weeks_format (str): Format string for weeks. Defaults to "{value}w".
        days_format (str): Format string for days. Defaults to "{value}d".
        hours_format (str): Format string for hours. Defaults to "{value:02d}".
        minutes_format (str): Format string for minutes. Defaults to "{value:02d}".
        seconds_format (str): Format string for seconds. Defaults to "{value:02d}".
        output_format (str): The output format string. Defaults to "{current_point}/{end_point} ({points_per_time}), {time_gone} / {est_time}".
    """
	
	def __init__(
			self,
			name: str = "progress_watcher",
			parent: typing.Optional[QWidget] = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: typing.Optional[ObjectSize] = None,
			maximum_size: typing.Optional[ObjectSize] = None,
			fixed_size: typing.Optional[ObjectSize] = None,
			size_policy: typing.Optional[QSizePolicy] = None,
			graphic_effect: typing.Optional[QGraphicsEffect] = None,
			scaled_contents: bool = False,
			word_wrap: bool = True,
			indent: int = 10,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
			font: PyFont = PyFont(),
			update_interval: int = 100,
			current_point: int = 0,
			start_point: int = 0,
			end_point: int = 0,
			always_print_years: bool = False,
			always_print_months: bool = False,
			always_print_weeks: bool = False,
			always_print_days: bool = False,
			always_print_hours: bool = True,
			always_print_minutes: bool = True,
			always_print_seconds: bool = True,
			disable_negative_time: bool = True,
			points_per_year_format: str = "{points:.2f}/y",
			points_per_month_format: str = "{points:.2f}/mon",
			points_per_week_format: str = "{points:.2f}/w",
			points_per_day_format: str = "{points:.2f}/d",
			points_per_hour_format: str = "{points:.2f}/h",
			points_per_minute_format: str = "{points:.2f}/m",
			points_per_second_format: str = "{points:.2f}/s",
			points_per_millisecond_format: str = "{points:.2f}/ms",
			points_per_microsecond_format: str = "{points:.2f}/mcs",
			points_per_nanosecond_format: str = "{points:.2f}/ns",
			years_format: str = "{value}y",
			months_format: str = "{value}mon",
			weeks_format: str = "{value}w",
			days_format: str = "{value}d",
			hours_format: str = "{value:02d}",
			minutes_format: str = "{value:02d}",
			seconds_format: str = "{value:02d}",
			output_format: str = "{current_point}/{end_point} ({progress_percent:.2f}%, {points_per_time}), {time_gone} / {est_time}"
	):
		"""
        Initializes a ProgressWatcherInit object.

        Args:
            name (str): The object name of the progress watcher. Defaults to "progress_watcher".
            parent (typing.Optional[QWidget]): The parent widget. Defaults to None.
            enabled (bool): Whether the progress watcher is enabled. Defaults to True.
            visible (bool): Whether the progress watcher is visible. Defaults to True.
            style_sheet (str): The style sheet to apply to the progress watcher. Defaults to "".
            minimum_size (typing.Optional[ObjectSize]): The minimum size of the progress watcher. Defaults to None.
            maximum_size (typing.Optional[ObjectSize]): The maximum size of the progress watcher. Defaults to None.
            fixed_size (typing.Optional[ObjectSize]): The fixed size of the progress watcher. Defaults to None.
            size_policy (typing.Optional[QSizePolicy]): The size policy of the progress watcher. Defaults to None.
            graphic_effect (typing.Optional[QGraphicsEffect]): The graphic effect to apply to the progress watcher. Defaults to None.
            scaled_contents (bool): Whether to scale the contents. Defaults to False.
            word_wrap (bool): Whether word wrap is enabled. Defaults to True.
            indent (int): The indentation. Defaults to 10.
            alignment (Qt.AlignmentFlag): The alignment of the text. Defaults to Qt.AlignmentFlag.AlignCenter.
            interaction_flag (Qt.TextInteractionFlag): The text interaction flag. Defaults to Qt.TextInteractionFlag.NoTextInteraction.
            font (PyFont): The font for the text.
            update_interval (int): The update interval in milliseconds. Defaults to 100.
            current_point (int): The current progress point. Defaults to 0.
            start_point (int): The starting progress point. Defaults to 0.
            end_point (int): The ending progress point. Defaults to 0.
            always_print_years (bool): Whether to always print years, even if zero. Defaults to False.
            always_print_months (bool): Whether to always print months, even if zero. Defaults to False.
            always_print_weeks (bool): Whether to always print weeks, even if zero. Defaults to False.
            always_print_days (bool): Whether to always print days, even if zero. Defaults to False.
            always_print_hours (bool): Whether to always print hours, even if zero. Defaults to True.
            always_print_minutes (bool): Whether to always print minutes, even if zero. Defaults to True.
            always_print_seconds (bool): Whether to always print seconds, even if zero. Defaults to True.
            disable_negative_time (bool): Whether to disable displaying negative time. Defaults to True.
            points_per_year_format (str): Format string for points per year. Defaults to "{points:.2f}/y".
            points_per_month_format (str): Format string for points per month. Defaults to "{points:.2f}/mon".
            points_per_week_format (str): Format string for points per week. Defaults to "{points:.2f}/w".
            points_per_day_format (str): Format string for points per day. Defaults to "{points:.2f}/d".
            points_per_hour_format (str): Format string for points per hour. Defaults to "{points:.2f}/h".
            points_per_minute_format (str): Format string for points per minute. Defaults to "{points:.2f}/m".
            points_per_second_format (str): Format string for points per second. Defaults to "{points:.2f}/s".
            points_per_millisecond_format (str): Format string for points per millisecond. Defaults to "{points:.2f}/ms".
            points_per_microsecond_format (str): Format string for points per microsecond. Defaults to "{points:.2f}/mcs".
            points_per_nanosecond_format (str): Format string for points per nanosecond. Defaults to "{points:.2f}/ns".
            years_format (str): Format string for years. Defaults to "{value}y".
            months_format (str): Format string for months. Defaults to "{value}mon".
            weeks_format (str): Format string for weeks. Defaults to "{value}w".
            days_format (str): Format string for days. Defaults to "{value}d".
            hours_format (str): Format string for hours. Defaults to "{value:02d}".
            minutes_format (str): Format string for minutes. Defaults to "{value:02d}".
            seconds_format (str): Format string for seconds. Defaults to "{value:02d}".
            output_format (str): The output format string. Defaults to "{current_point}/{end_point} ({progress_percent:.2f}%, {points_per_time}), {time_gone} / {est_time}".
        """
		super().__init__(
				name,
				parent,
				enabled,
				visible,
				style_sheet,
				minimum_size,
				maximum_size,
				fixed_size,
				size_policy,
				graphic_effect,
				scaled_contents,
				word_wrap,
				indent,
				alignment,
				interaction_flag
		)
		
		self.font = font
		self.update_interval = update_interval
		self.current_point = current_point
		self.start_point = start_point
		self.end_point = end_point
		self.always_print_years = always_print_years
		self.always_print_months = always_print_months
		self.always_print_weeks = always_print_weeks
		self.always_print_days = always_print_days
		self.always_print_hours = always_print_hours
		self.always_print_minutes = always_print_minutes
		self.always_print_seconds = always_print_seconds
		self.disable_negative_time = disable_negative_time
		self.points_per_year_format = points_per_year_format
		self.points_per_month_format = points_per_month_format
		self.points_per_week_format = points_per_week_format
		self.points_per_day_format = points_per_day_format
		self.points_per_hour_format = points_per_hour_format
		self.points_per_minute_format = points_per_minute_format
		self.points_per_second_format = points_per_second_format
		self.points_per_millisecond_format = points_per_millisecond_format
		self.points_per_microsecond_format = points_per_microsecond_format
		self.points_per_nanosecond_format = points_per_nanosecond_format
		self.years_format = years_format
		self.months_format = months_format
		self.weeks_format = weeks_format
		self.days_format = days_format
		self.hours_format = hours_format
		self.minutes_format = minutes_format
		self.seconds_format = seconds_format
		self.output_format = output_format


class PyProgressWatcher(PyLabel):
	"""A custom widget to display progress with time estimations."""
	
	def __init__(self, progress_watcher_init: ProgressWatcherInit = ProgressWatcherInit()):
		"""
        Initializes a PyProgressWatcher object.

        Args:
            progress_watcher_init: Initialization settings for the progress watcher.
        """
		super().__init__(label_init=progress_watcher_init)
		
		self.stop_watch_font = progress_watcher_init.font
		self.update_interval = progress_watcher_init.update_interval
		self.current_point = progress_watcher_init.current_point
		self.start_point = progress_watcher_init.start_point
		self.end_point = progress_watcher_init.end_point
		self.always_print_years = progress_watcher_init.always_print_years
		self.always_print_months = progress_watcher_init.always_print_months
		self.always_print_weeks = progress_watcher_init.always_print_weeks
		self.always_print_days = progress_watcher_init.always_print_days
		self.always_print_hours = progress_watcher_init.always_print_hours
		self.always_print_minutes = progress_watcher_init.always_print_minutes
		self.always_print_seconds = progress_watcher_init.always_print_seconds
		self.points_per_year_format = progress_watcher_init.points_per_year_format
		self.points_per_month_format = progress_watcher_init.points_per_month_format
		self.points_per_week_format = progress_watcher_init.points_per_week_format
		self.points_per_day_format = progress_watcher_init.points_per_day_format
		self.points_per_hour_format = progress_watcher_init.points_per_hour_format
		self.points_per_minute_format = progress_watcher_init.points_per_minute_format
		self.points_per_second_format = progress_watcher_init.points_per_second_format
		self.points_per_millisecond_format = progress_watcher_init.points_per_millisecond_format
		self.points_per_microsecond_format = progress_watcher_init.points_per_microsecond_format
		self.points_per_nanosecond_format = progress_watcher_init.points_per_nanosecond_format
		self.years_format = progress_watcher_init.years_format
		self.months_format = progress_watcher_init.months_format
		self.weeks_format = progress_watcher_init.weeks_format
		self.days_format = progress_watcher_init.days_format
		self.hours_format = progress_watcher_init.hours_format
		self.minutes_format = progress_watcher_init.minutes_format
		self.seconds_format = progress_watcher_init.seconds_format
		self.disable_negative_time = progress_watcher_init.disable_negative_time
		self.output_format = progress_watcher_init.output_format
		self.start_time: typing.Optional[datetime] = None
		self.end_time: typing.Optional[datetime] = None
		self.block_print = False
		self.seconds_for_point = 0.0
		
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.print_progress)
		
		self.reset_output(self.current_point, self.end_point)
	
	def get_points_per_time_sting(self) -> str:
		"""Returns a formatted string representing the points processed per unit of time."""
		if self.seconds_for_point > 2592000:
			return self.points_per_year_format.format(points=31536000 / self.seconds_for_point)
		elif self.seconds_for_point > 604800:
			return self.points_per_month_format.format(points=2592000 / self.seconds_for_point)
		elif self.seconds_for_point > 84400:
			return self.points_per_week_format.format(points=604800 / self.seconds_for_point)
		elif self.seconds_for_point > 3600:
			return self.points_per_day_format.format(points=84400 / self.seconds_for_point)
		elif self.seconds_for_point > 60:
			return self.points_per_hour_format.format(points=3600 / self.seconds_for_point)
		elif self.seconds_for_point > 1:
			return self.points_per_minute_format.format(points=60 / self.seconds_for_point)
		elif self.seconds_for_point > 1e-3:
			return self.points_per_second_format.format(points=1 / self.seconds_for_point)
		elif self.seconds_for_point > 1e-6:
			return self.points_per_millisecond_format.format(points=1e-3 / self.seconds_for_point)
		elif self.seconds_for_point > 1e-9:
			return self.points_per_microsecond_format.format(points=1e-6 / self.seconds_for_point)
		elif self.seconds_for_point == 0.0:
			return self.points_per_second_format.format(points=0.0)
		else:
			return self.points_per_nanosecond_format.format(points=1e-9 / self.seconds_for_point)
	
	def print_progress(self):
		"""Updates the displayed progress information."""
		if not self.block_print:
			try:
				progress_percent = (self.current_point / self.end_point) * 100
			except ZeroDivisionError:
				progress_percent = 0.0
		
			self.setText(
					self.output_format.format(
							current_point=self.current_point,
							end_point=self.end_point,
							progress_percent=progress_percent,
							points_per_time=self.get_points_per_time_sting(),
							time_gone=self.get_elapsed_time_string(),
							est_time=self.get_estimated_time_string()
					)
			)
	
	def start_progress_watcher(self, start_point: int, end_point: int, current_point: int):
		"""
        Starts the progress watcher.

        Args:
            start_point (int): The starting point of the progress.
            end_point (int): The ending point of the progress.
            current_point (int): The initial current point. Defaults to 0.
        """
		self.start_point = start_point
		self.end_point = end_point
		self.current_point = current_point
		
		self.seconds_for_point = 0.0
		self.block_print = False
		
		self.start_time = datetime.now()
		self.end_time = datetime.now()
		
		self.timer.start(self.update_interval)
	
	def get_time_string(self, time_: typing.Optional[relativedelta] = None) -> str:
		"""
        Formats a relativedelta object or zero time into a string.

        Args:
            time_ (typing.Optional[relativedelta]): The time to format. Defaults to None.

        Returns:
            str: The formatted time string.
        """
		if time_ is None:
			time_ = relativedelta(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0)
		
		years_s = self.years_format.format(value=time_.years) if time_.years or self.always_print_years else ""
		months_s = self.months_format.format(value=time_.months) if time_.months or self.always_print_months else ""
		weeks_s = self.weeks_format.format(value=time_.weeks) if time_.weeks or self.always_print_weeks else ""
		days_s = self.days_format.format(value=time_.days) if time_.days or self.always_print_days else ""
		hours_s = self.hours_format.format(value=time_.hours) if time_.hours or self.always_print_hours else ""
		minutes_s = (
				self.minutes_format.format(value=time_.minutes)
				if time_.minutes
				or self.always_print_minutes
				else ""
		)
		seconds_s = (
				self.seconds_format.format(value=time_.seconds)
				if time_.seconds
				or self.always_print_seconds
				else ""
		)
		
		time_out_of_day = " ".join(list(filter(None, [years_s, months_s, weeks_s, days_s])))
		time_in_day_string = ":".join(list(filter(None, [hours_s, minutes_s, seconds_s])))
		
		return " ".join(list(filter(None, [time_out_of_day, time_in_day_string])))
	
	def get_estimated_time_string(self) -> str:
		"""
        Calculates and returns the estimated remaining time as a string.

        Returns:
            str: The estimated remaining time as a string.
        """
		if self.end_time is not None:
			if self.end_time.timestamp() - datetime.now().timestamp() >= 0:
				return self.get_time_string(relativedelta(self.end_time, datetime.now()))
			else:
				if self.disable_negative_time:
					return self.get_time_string()
				else:
					return "-" + self.get_time_string(relativedelta(datetime.now(), self.end_time))
		else:
			return self.get_time_string()
	
	def get_elapsed_time_string(self) -> str:
		"""
        Returns the elapsed time as a formatted string.

        Returns:
            str: The elapsed time as a formatted string.
        """
		if self.start_time is not None:
			return self.get_time_string(relativedelta(datetime.now(), self.start_time))
		else:
			return self.get_time_string()
	
	def reset_output(self, current_point: int, end_point: int):
		"""
        Resets the output display to initial values.

        Args:
            current_point (int): The current point.
            end_point (int): The end point.
        """
		try:
			progress_percent = (current_point / end_point) * 100
		except ZeroDivisionError:
			progress_percent = 0.0
		
		self.setText(
				self.output_format.format(
						current_point=current_point,
						end_point=end_point,
						progress_percent=progress_percent,
						points_per_time=self.points_per_second_format.format(points=0.0),
						time_gone=self.get_elapsed_time_string(),
						est_time=self.get_estimated_time_string()
				)
		)
	
	def stop_progress_watcher(self, save_output: bool = False):
		"""
        Stops the progress watcher.

        Args:
            save_output (bool): If True, preserves the current output; otherwise, resets it.
        """
		self.timer.stop()
		self.seconds_for_point = 0.0
		self.block_print = False
		
		self.start_time = None
		self.end_time = None
		
		if not save_output:
			self.reset_output(0, 0)
	
	def restart_progress_watcher(self, start_point: int, end_point: int, current_point: int):
		"""
        Restarts the progress watcher with new values.

        Args:
            start_point (int): The starting point of the progress.
            end_point (int): The ending point of the progress.
            current_point (int): The current point.
        """
		self.start_point = start_point
		self.end_point = end_point
		self.current_point = current_point
		self.seconds_for_point = 0.0
		
		self.stop_progress_watcher()
		self.start_progress_watcher(self.start_point, self.end_point, self.current_point)
	
	def update_progress(self):
		"""Updates the current progress and recalculates estimations."""
		self.block_print = True
		
		self.current_point += 1
		try:
			self.seconds_for_point = (time() - self.start_time.timestamp()) / (self.current_point - self.start_point)
			self.end_time = datetime.now() + relativedelta(
					seconds=+int((self.end_point - self.current_point) * self.seconds_for_point)
			)
		except ZeroDivisionError:
			self.seconds_for_point = 0.0
			self.end_time = datetime.now()
		
		self.block_print = False

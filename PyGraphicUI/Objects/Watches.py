from time import time
from datetime import datetime
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer, Qt
from PyGraphicUI.Attributes import ObjectSize
from dateutil.relativedelta import relativedelta
from PyGraphicUI.Objects.Label import LabelInit, PyLabel
from PyQt6.QtWidgets import QGraphicsEffect, QSizePolicy, QWidget
#
#
#
#
class TimerInit(LabelInit):
	def __init__(
			self,
			name: str = "timer",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			scaled_contents: bool = False,
			word_wrap: bool = True,
			indent: int = 10,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
			font: QFont = None,
			update_interval: int = 100,
			print_weeks: bool = True,
			print_days: bool = True,
			print_hours: bool = True,
			print_minutes: bool = True,
			always_print_years: bool = False,
			always_print_months: bool = False,
			always_print_weeks: bool = False,
			always_print_days: bool = False,
			always_print_hours: bool = True,
			always_print_minutes: bool = True,
			always_print_seconds: bool = True,
			disable_negative_time: bool = True,
			prefix: str = "",
			postfix: str = ""
	):
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
		#
		#
		#
		#
		self.font = font
		self.update_interval = update_interval
		self.print_weeks = print_weeks
		self.print_days = print_days
		self.print_hours = print_hours
		self.print_minutes = print_minutes
		self.always_print_years = always_print_years
		self.always_print_months = always_print_months
		self.always_print_weeks = always_print_weeks
		self.always_print_days = always_print_days
		self.always_print_hours = always_print_hours
		self.always_print_minutes = always_print_minutes
		self.always_print_seconds = always_print_seconds
		self.disable_negative_time = disable_negative_time
		self.prefix = prefix
		self.postfix = postfix
#
#
#
#
class PyTimer(PyLabel):
	def __init__(self, timer_init: TimerInit = TimerInit()):
		super().__init__(label_init=timer_init)
		#
		#
		#
		#
		self.timer_font, self.update_interval = timer_init.font, timer_init.update_interval
		self.print_weeks, self.print_days, self.print_hours, self.print_minutes = timer_init.print_weeks, timer_init.print_days, timer_init.print_hours, timer_init.print_minutes
		self.always_print_years, self.always_print_months, self.always_print_weeks, self.always_print_days, self.always_print_hours, self.always_print_minutes, self.always_print_seconds = timer_init.always_print_years, timer_init.always_print_months, timer_init.always_print_weeks, timer_init.always_print_days, timer_init.always_print_hours, timer_init.always_print_minutes, timer_init.always_print_seconds
		self.end_time = None
		self.disable_negative_time = timer_init.disable_negative_time
		self.prefix, self.postfix = timer_init.prefix, timer_init.postfix
		#
		#
		#
		#
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.print_time)
		#
		#
		#
		#
		self.setText("%s%s%s" % (self.prefix, self.get_time_string(), self.postfix))
		#
		#
		#
		#
		if self.timer_font is not None:
			self.setFont(self.timer_font)
	#
	#
	#
	#
	def get_time_string(self, time_: relativedelta = None):
		if time_ is None:
			time_ = relativedelta(
					years=0,
					months=0,
					weeks=0,
					days=0,
					hours=0,
					minutes=0,
					seconds=0
			)

		years_s = "%dг" % time_.years if time_.years or self.always_print_years else ""
		months_s = "%dмес." % time_.months if time_.months or self.always_print_months else ""
		weeks_s = "%dнед." % time_.weeks if time_.weeks or self.always_print_weeks else ""
		days_s = "%dдн." % time_.days if time_.days or self.always_print_days else ""
		hours_s = "%02d" % time_.hours if time_.hours or self.always_print_hours else ""
		minutes_s = "%02d" % time_.minutes if time_.minutes or self.always_print_minutes else ""
		seconds_s = "%02d" % time_.seconds if time_.seconds or self.always_print_seconds else ""

		time_out_of_day = " ".join(list(filter(None, [years_s, months_s, weeks_s, days_s])))
		time_in_day_string = ":".join(list(filter(None, [hours_s, minutes_s, seconds_s])))

		return " ".join(list(filter(None, [time_out_of_day, time_in_day_string])))
	#
	#
	#
	#
	def get_estimated_time_string(self):
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
	#
	#
	#
	#
	def print_time(self):
		self.setText(
				"%s%s%s" % (self.prefix, self.get_estimated_time_string(), self.postfix)
		)
	#
	#
	#
	#
	def set_end_time(self, end_time: datetime):
		self.end_time = end_time
	#
	#
	#
	#
	def start_timer(self, end_time: datetime):
		self.set_end_time(end_time)
		self.timer.start(self.update_interval)
	#
	#
	#
	#
	def stop_timer(self):
		self.timer.stop()
		self.end_time = None
	#
	#
	#
	#
	def restart_watch(self, end_time: datetime):
		self.stop_timer()
		self.start_timer(end_time)
#
#
#
#
class StopWatchInit(LabelInit):
	def __init__(
			self,
			name: str = "stop_watch",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			scaled_contents: bool = False,
			word_wrap: bool = True,
			indent: int = 10,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
			font: QFont = None,
			update_interval: int = 100,
			print_weeks: bool = True,
			print_days: bool = True,
			print_hours: bool = True,
			print_minutes: bool = True,
			always_print_years: bool = False,
			always_print_months: bool = False,
			always_print_weeks: bool = False,
			always_print_days: bool = False,
			always_print_hours: bool = True,
			always_print_minutes: bool = True,
			always_print_seconds: bool = True,
			prefix: str = "",
			postfix: str = ""
	):
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
		#
		#
		#
		#
		self.font = font
		self.update_interval = update_interval
		self.print_weeks = print_weeks
		self.print_days = print_days
		self.print_hours = print_hours
		self.print_minutes = print_minutes
		self.always_print_years = always_print_years
		self.always_print_months = always_print_months
		self.always_print_weeks = always_print_weeks
		self.always_print_days = always_print_days
		self.always_print_hours = always_print_hours
		self.always_print_minutes = always_print_minutes
		self.always_print_seconds = always_print_seconds
		self.prefix = prefix
		self.postfix = postfix
#
#
#
#
class PyStopWatch(PyLabel):
	def __init__(self, stop_watch_init: StopWatchInit = StopWatchInit()):
		super().__init__(label_init=stop_watch_init)
		#
		#
		#
		#
		self.stop_watch_font, self.update_interval = stop_watch_init.font, stop_watch_init.update_interval
		self.print_weeks, self.print_days, self.print_hours, self.print_minutes = stop_watch_init.print_weeks, stop_watch_init.print_days, stop_watch_init.print_hours, stop_watch_init.print_minutes
		self.always_print_years, self.always_print_months, self.always_print_weeks, self.always_print_days, self.always_print_hours, self.always_print_minutes, self.always_print_seconds = stop_watch_init.always_print_years, stop_watch_init.always_print_months, stop_watch_init.always_print_weeks, stop_watch_init.always_print_days, stop_watch_init.always_print_hours, stop_watch_init.always_print_minutes, stop_watch_init.always_print_seconds
		self.start_time = None
		self.prefix, self.postfix = stop_watch_init.prefix, stop_watch_init.postfix
		#
		#
		#
		#
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.print_time)
		#
		#
		#
		#
		self.setText("%s%s%s" % (self.prefix, self.get_time_string(), self.postfix))
		#
		#
		#
		#
		if self.stop_watch_font is not None:
			self.setFont(self.stop_watch_font)
	#
	#
	#
	#
	def get_time_string(self, time_: relativedelta = None):
		if time_ is None:
			time_ = relativedelta(
					years=0,
					months=0,
					weeks=0,
					days=0,
					hours=0,
					minutes=0,
					seconds=0
			)

		years_s = "%dг" % time_.years if time_.years or self.always_print_years else ""
		months_s = "%dмес." % time_.months if time_.months or self.always_print_months else ""
		weeks_s = "%dнед." % time_.weeks if time_.weeks or self.always_print_weeks else ""
		days_s = "%dдн." % time_.days if time_.days or self.always_print_days else ""
		hours_s = "%02d" % time_.hours if time_.hours or self.always_print_hours else ""
		minutes_s = "%02d" % time_.minutes if time_.minutes or self.always_print_minutes else ""
		seconds_s = "%02d" % time_.seconds if time_.seconds or self.always_print_seconds else ""

		time_out_of_day = " ".join(list(filter(None, [years_s, months_s, weeks_s, days_s])))
		time_in_day_string = ":".join(list(filter(None, [hours_s, minutes_s, seconds_s])))

		return " ".join(list(filter(None, [time_out_of_day, time_in_day_string])))
	#
	#
	#
	#
	def get_time_gone_string(self):
		if self.start_time is not None:
			return self.get_time_string(relativedelta(datetime.now(), self.start_time))
		else:
			return self.get_time_string()
	#
	#
	#
	#
	def print_time(self):
		self.setText(
				"%s%s%s" % (self.prefix, self.get_time_gone_string(), self.postfix)
		)
	#
	#
	#
	#
	def start_watch(self):
		self.start_time = datetime.now()
		self.timer.start(self.update_interval)
	#
	#
	#
	#
	def stop_watch(self):
		self.timer.stop()
		self.start_time = None
	#
	#
	#
	#
	def restart_watch(self):
		self.stop_watch()
		self.start_watch()
#
#
#
#
class ProgressWatcherInit(LabelInit):
	def __init__(
			self,
			name: str = "progress_watcher",
			parent: QWidget = None,
			enabled: bool = True,
			visible: bool = True,
			style_sheet: str = "",
			minimum_size: ObjectSize = None,
			maximum_size: ObjectSize = None,
			fixed_size: ObjectSize = None,
			size_policy: QSizePolicy = None,
			graphic_effect: QGraphicsEffect = None,
			scaled_contents: bool = False,
			word_wrap: bool = True,
			indent: int = 10,
			alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
			interaction_flag: Qt.TextInteractionFlag = Qt.TextInteractionFlag.NoTextInteraction,
			font: QFont = None,
			update_interval: int = 100,
			current_point: int = 0,
			start_point: int = 0,
			end_point: int = 0,
			print_weeks: bool = True,
			print_days: bool = True,
			print_hours: bool = True,
			print_minutes: bool = True,
			always_print_years: bool = False,
			always_print_months: bool = False,
			always_print_weeks: bool = False,
			always_print_days: bool = False,
			always_print_hours: bool = True,
			always_print_minutes: bool = True,
			always_print_seconds: bool = True,
			disable_negative_time: bool = True,
			output_format: str = "{current_point}/{end_point} ({point_per_time}), {time_gone} / {est_time}"
	):
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
		#
		#
		#
		#
		self.font = font
		self.update_interval = update_interval
		self.current_point = current_point
		self.start_point = start_point
		self.end_point = end_point
		self.print_weeks = print_weeks
		self.print_days = print_days
		self.print_hours = print_hours
		self.print_minutes = print_minutes
		self.always_print_years = always_print_years
		self.always_print_months = always_print_months
		self.always_print_weeks = always_print_weeks
		self.always_print_days = always_print_days
		self.always_print_hours = always_print_hours
		self.always_print_minutes = always_print_minutes
		self.always_print_seconds = always_print_seconds
		self.disable_negative_time = disable_negative_time
		self.output_format = output_format
#
#
#
#
class PyProgressWatcher(PyLabel):
	def __init__(
			self,
			progress_watcher_init: ProgressWatcherInit = ProgressWatcherInit()
	):
		super().__init__(label_init=progress_watcher_init)
		#
		#
		#
		#
		self.stop_watch_font, self.update_interval = progress_watcher_init.font, progress_watcher_init.update_interval
		self.current_point, self.start_point, self.end_point = progress_watcher_init.current_point, progress_watcher_init.start_point, progress_watcher_init.end_point
		self.print_weeks, self.print_days, self.print_hours, self.print_minutes = progress_watcher_init.print_weeks, progress_watcher_init.print_days, progress_watcher_init.print_hours, progress_watcher_init.print_minutes
		self.always_print_years, self.always_print_months, self.always_print_weeks, self.always_print_days, self.always_print_hours, self.always_print_minutes, self.always_print_seconds = progress_watcher_init.always_print_years, progress_watcher_init.always_print_months, progress_watcher_init.always_print_weeks, progress_watcher_init.always_print_days, progress_watcher_init.always_print_hours, progress_watcher_init.always_print_minutes, progress_watcher_init.always_print_seconds
		self.disable_negative_time = progress_watcher_init.disable_negative_time
		self.output_format = progress_watcher_init.output_format
		self.start_time, self.end_time = None, None
		self.block_print = False
		self.seconds_for_point = 0.0
		#
		#
		#
		#
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.print_progress)
		#
		#
		#
		#
		if self.stop_watch_font is not None:
			self.setFont(self.stop_watch_font)
		#
		#
		#
		#
		self.reset_output(self.current_point, self.end_point)
	#
	#
	#
	#
	def get_point_per_time_sting(self):
		if self.seconds_for_point > 2592000:
			return "%.2f/год" % (31536000 / self.seconds_for_point)
		elif self.seconds_for_point > 604800:
			return "%.2f/мес." % (2592000 / self.seconds_for_point)
		elif self.seconds_for_point > 84400:
			return "%.2f/нед." % (604800 / self.seconds_for_point)
		elif self.seconds_for_point > 3600:
			return "%.2f/день" % (84400 / self.seconds_for_point)
		elif self.seconds_for_point > 60:
			return "%.2f/час" % (3600 / self.seconds_for_point)
		elif self.seconds_for_point > 1:
			return "%.2f/мин." % (60 / self.seconds_for_point)
		elif self.seconds_for_point > 0.001:
			return "%.2f/сек." % (1 / self.seconds_for_point)
		elif self.seconds_for_point > 0.000001:
			return "%.2f/мс." % (self.seconds_for_point / 0.001)
		elif self.seconds_for_point > 0.000000001:
			return "%.2f/мкс." % (self.seconds_for_point / 0.000001)
		elif self.seconds_for_point == 0.0:
			return "0.0/сек."
		else:
			return "%.2f/нс." % (self.seconds_for_point / 0.000000001)
	#
	#
	#
	#
	def print_progress(self):
		if not self.block_print:
			self.setText(
					self.output_format.format(
							current_point=self.current_point,
							end_point=self.end_point,
							point_per_time=self.get_point_per_time_sting(),
							time_gone=self.get_time_gone_string(),
							est_time=self.get_estimated_time_string()
					)
			)
	#
	#
	#
	#
	def start_progress_watcher(self, start_point: int, end_point: int, current_point: int):
		self.start_point = start_point
		self.end_point = end_point
		self.current_point = current_point

		self.seconds_for_point = 0.0
		self.block_print = False

		self.start_time = datetime.now()
		self.end_time = datetime.now()

		self.timer.start(self.update_interval)
	#
	#
	#
	#
	def get_time_string(self, time_: relativedelta = None):
		if time_ is None:
			time_ = relativedelta(
					years=0,
					months=0,
					weeks=0,
					days=0,
					hours=0,
					minutes=0,
					seconds=0
			)

		years_s = "%dг" % time_.years if time_.years or self.always_print_years else ""
		months_s = "%dмес." % time_.months if time_.months or self.always_print_months else ""
		weeks_s = "%dнед." % time_.weeks if time_.weeks or self.always_print_weeks else ""
		days_s = "%dдн." % time_.days if time_.days or self.always_print_days else ""
		hours_s = "%02d" % time_.hours if time_.hours or self.always_print_hours else ""
		minutes_s = "%02d" % time_.minutes if time_.minutes or self.always_print_minutes else ""
		seconds_s = "%02d" % time_.seconds if time_.seconds or self.always_print_seconds else ""

		time_out_of_day = " ".join(list(filter(None, [years_s, months_s, weeks_s, days_s])))
		time_in_day_string = ":".join(list(filter(None, [hours_s, minutes_s, seconds_s])))

		return " ".join(list(filter(None, [time_out_of_day, time_in_day_string])))
	#
	#
	#
	#
	def get_estimated_time_string(self):
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
	#
	#
	#
	#
	def get_time_gone_string(self):
		if self.start_time is not None:
			return self.get_time_string(relativedelta(datetime.now(), self.start_time))
		else:
			return self.get_time_string()
	#
	#
	#
	#
	def reset_output(self, current_point: int, end_point: int):
		self.setText(
				self.output_format.format(
						current_point=current_point,
						end_point=end_point,
						point_per_time="0.0/сек.",
						time_gone=self.get_time_gone_string(),
						est_time=self.get_estimated_time_string()
				)
		)
	#
	#
	#
	#
	def stop_progress_watcher(self, save_output: bool = False):
		self.timer.stop()
		self.seconds_for_point = 0.0
		self.block_print = False

		self.start_time = None
		self.end_time = None

		if not save_output:
			self.reset_output(0, 0)
	#
	#
	#
	#
	def restart_progress_watcher(self, start_point: int, end_point: int, current_point: int):
		self.start_point = start_point
		self.end_point = end_point
		self.current_point = current_point
		self.seconds_for_point = 0.0

		self.stop_progress_watcher()
		self.start_progress_watcher(self.start_point, self.end_point, self.current_point)
	#
	#
	#
	#
	def update_progress(self):
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

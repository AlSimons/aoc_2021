"""
Copied from: https://realpython.com/python-timer/ with very slight mods.
"""
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:

    def __init__(self):
        self._start_time = None
        self.elapsed_time = 0

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        self.elapsed_time += time.perf_counter() - self._start_time
        self._start_time = None

    def reset(self):
        self.__init__()

    def __str__(self):
        seconds = self.elapsed_time
        hours = 0
        minutes = 0
        if seconds >= 3600:
            hours = int(seconds / 3600)
            seconds = seconds - (hours * 3600)
        if seconds >= 60:
            minutes = int(seconds / 60)
            seconds = seconds - (minutes * 60)
        if hours == 1:
            hours_label = "hour"
        else:
            hours_label = "hours"
        if minutes == 1:
            minutes_label = "minute"
        else:
            minutes_label = "minutes"
        if hours:
            ret = "{} {}, {} {}, {:0.0f} seconds".format(
                hours, hours_label, minutes, minutes_label, seconds
            )
        elif minutes:
            ret = "{} {}, {:0.0f} seconds".format(minutes, minutes_label, seconds)
        else:
            if seconds < 10:
                ret = "{:0.4f} seconds".format(seconds)
            else:
                ret = "{:0.2f} seconds".format(seconds)
        return ret
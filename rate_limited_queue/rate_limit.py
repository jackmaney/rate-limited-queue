"""
This class represents a rate limit. It has three main components:

* The duration (in seconds).
* The maximum number of items that can be processed in this duration.
* A ``stopwatch`` object.
* The ``is_exceeded`` method, which checks to see if the limit has been exceeded.
"""

from stopwatch import StopWatch


class RateLimit(object):

    def __init__(self, duration=1, max_per_interval=5):
        """
        The only arguments provided are the duration and the
        max number of items to process per interval.

        :param duration: The duration (in seconds) for this interval
        :type duration: positive integer or float
        :param max_per_interval: The maximum number of items to be processed per interval.
        :type max_per_interval: positive integer
        """

        self.duration = duration
        self.max_per_interval = max_per_interval

        self.stopwatch = StopWatch()
        self.num_processed_this_interval = 0

    def is_exceeded(self):
        """
        Returns whether or not the rate limit has been exceeded for this interval.
        """

        if self.stopwatch.check_time() > self.duration:
            self.stopwatch.start()
            self.num_processed_this_interval = 0
            return False

        return self.num_processed_this_interval >= self.max_per_interval

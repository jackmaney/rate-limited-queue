from time import time


class StopWatch(object):
    """
    A simple timekeeping class.
    Slightly more convenient than keeping track of two time variables.
    """

    def __init__(self):

        self.start_time = None
        self.end_time = None
        self.start()

    def start(self):
        """
        Starts (or restarts) the stopwatch
        """

        now = time()
        self.start_time = now
        self.end_time = now

    def update(self):
        """
        Updates the stopwatch.
        Used by the `check_time` method to report accurate time intervals
        """

        self.end_time = time()

    def check_time(self):
        """
        Returns the number of seconds (as a float) since the last start.
        """

        self.update()
        return self.end_time - self.start_time

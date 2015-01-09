import traceback
from collections import Iterable
from warnings import warn

from rate_limit import RateLimit


class RateLimitedQueue(object):

    def __init__(self, items, processing_function, rate_limits):
        """
        Takes a list of items to be processed, along with a function
        with which to process them, and a list of ``RateLimit`` objects.

        :param items: Items to be processed.
        :type items: list or other iterable
        :param processing_function: The function to call when processing an item.
        :type processing_function: function
        :param rate_limits: One or more ``RateLimit`` objects.
        :type rate_limits: list or other iterable
        """

        self.items = [x for x in items]
        self.processing_function = processing_function
        self.rate_limits = rate_limits

        self._validate_params()

    def _validate_params(self):

        if not isinstance(self.rate_limits, Iterable):
            raise ValueError("The 'rate_limits' parameter must be a list!")

        if not all([isinstance(x, RateLimit) for x in self.rate_limits]):
            raise ValueError("The 'rate_limits' parameter must be a list of RateLimits!")

        if not hasattr(self.processing_function, '__call__'):
            raise ValueError("The 'processing_function' parameter must be a function!")

    def can_process(self):

        return all([not r.is_exceeded() for r in self.rate_limits])

    def process(self):
        """
        Processes the list of ``items`` via application of
        ``processing_function``, but without violating any of the
        ``rate_limits``.

        :rtype: list of processed items
        """

        result = []

        while self.items:

            if self.can_process():
                item = self.items.pop(0)

                processed_item = None

                try:

                    processed_item = self.processing_function(item)

                except:
                    traceback.print_exc()
                    warn("Could not process this item: '%s'" % item)

                result.append(processed_item)

                for rl in self.rate_limits:
                    rl.num_processed_this_interval += 1

        return result

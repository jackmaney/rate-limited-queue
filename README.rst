Rate Limited Queue
==================

.. image:: https://readthedocs.org/projects/rate-limited-queue/badge/?version=latest
    :target: https://readthedocs.org/projects/rate-limited-queue/?badge=latest
    :alt: Documentation Status

A Queue That Respects Rate Limits.

The original prototype for this code was written to rate-limit calls to a
geocoding api via `geopy <https://github.com/geopy/geopy>`_.

.. code-block:: python

    import geopy

    from rate_limited_queue import RateLimitedQueue, RateLimit

    addresses = open("some_file_of_addresses.txt").read().splitlines()

    # No more than ten addresses geocoded per second
    rate_limit = RateLimit(duration=1, max_per_interval=10)

    geocoder = geopy.geocoder.OpenMapQuest()

    q = RateLimitedQueue(
                        addresses,
                        processing_function = geocoder.geocode,
                        rate_limits = [rate_limit])

    # Grabs the geocoded locations, but doesn't process
    # more than ten per second
    geocoded_locations = q.process()

Installation
------------

It's up `on PyPI <https://pypi.python.org/pypi/rate_limited_queue>`_, so just do a::

    pip install rate_limited_queue

or::

    sudo pip install rate_limited_queue

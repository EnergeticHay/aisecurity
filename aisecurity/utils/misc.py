"""

"aisecurity.utils.misc"

Miscellaneous tools.

"""

import asyncio
from contextlib import contextmanager
import functools
import os
import sys
import time
import signal


# TIME LIMIT
# ... why do we need this?
class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)

    try:
        yield
    finally:
        signal.alarm(0)



# PRINT HANDLING
class HidePrints:

    def __enter__(self):
        self.to_show = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self.to_show


# TIMER
def timer(message="Time elapsed"):
    def _timer(func):
        @functools.wraps(func)
        def _func(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print("{}: {}s".format(message, round(time.time() - start, 3)))
            return result

        return _func

    return _timer


# ASYNC
def run_async_method(func, *args, **kwargs):
    async def async_helper(func, *args, **kwargs):
        await func(*args, **kwargs)

    loop = asyncio.new_event_loop()
    task = loop.create_task(async_helper(func, *args, **kwargs))
    loop.run_until_complete(task)

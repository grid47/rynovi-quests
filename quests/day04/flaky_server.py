"""Day 4 · The flaky server

call_with_retry(fn) calls fn() and, when it fails for a reason that might go away, tries again
after waiting a little longer each time.

Two kinds of errors (already defined for you):
  TransientError  - a timeout or a 503. Worth retrying.
  PermanentError  - a 400 or a 404. Retrying won't fix it, so fail at once.

Run `python quest.py 4` after each TODO.
"""
import logging
import time
from typing import Callable, TypeVar
# from tenacity import retry, stop_after_attempt, wait_exponential

T = TypeVar("T")
log = logging.getLogger("rynovi.retry")


class TransientError(Exception):
    pass


class PermanentError(Exception):
    pass


def call_with_retry(fn: Callable[[], T], attempts: int = 4, base_delay: float = 0.5, sleep: Callable[[float], None] = time.sleep) -> T:
    """Call fn() up to `attempts` times.

    TODO 4.1 · Retry with exponential backoff: wait base_delay, then 2x, then 4x... between tries,
              using sleep(seconds) (not time.sleep directly, so the tests run instantly).
              If every attempt fails, raise the last error.
    TODO 4.2 · Only retry TransientError. Any other error is raised immediately, with no waiting.
    TODO 4.3 · Before each wait, log a warning exactly like:
              log.warning("attempt %d failed: %s; retrying in %.1fs", attempt_number, error, delay)
    """

    for attempt in range(1, attempts + 1):
        try:
            return fn()

        except TransientError as error:
            if attempt == attempts:
                raise

            delay = base_delay * (2 ** (attempt - 1))

            log.warning("attempt %d failed: %s; retrying in %.1fs", attempt, error, delay)

            sleep(delay)

        except Exception:
            raise
    # raise NotImplementedError

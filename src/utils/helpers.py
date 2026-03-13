# src/repochat/utils/helpers.py

import time
from functools import wraps
from repochat.utils.logger import logger

def measure_time(func):
    """
    Decorator to measure execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"[bold green]Function {func.__name__} took {elapsed:.2f}s[/bold green]")
        return result
    return wrapper

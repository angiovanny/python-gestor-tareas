#!/usr/bin/env python3
"""
Docstring for gestor.decorators
"""
import time
from functools import wraps

def _now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def log_execution(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[{func.__name__}] Start: {_now()}")
              
        result = func(*args, **kwargs)

        duration = time.time() - start_time
        print(f"[{func.__name__}] End: {_now()}, Duration: {duration:.2f}s")
        return result

    return wrapper
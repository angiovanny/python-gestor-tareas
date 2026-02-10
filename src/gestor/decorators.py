#!/usr/bin/env python3
"""
Docstring for gestor.decorators
"""
import time
from functools import wraps
from context import managed_file
import os

def _now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def log_execution(func):
    from tareas import BASE_DIR
    LOGFILE = os.path.join(BASE_DIR, "tareas.log")
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        with managed_file(LOGFILE, "a") as f:
            f.write(f"[{func.__name__}] Start: {_now()}\n")
        #print(f"[{func.__name__}] Start: {_now()}")
              
            result = func(*args, **kwargs)

            duration = time.time() - start_time
            f.write(f"[{func.__name__}] End: {_now()}, Duration: {duration:.2f}s\n") 
            #print(f"[{func.__name__}] End: {_now()}, Duration: {duration:.2f}s")
        return result

    return wrapper
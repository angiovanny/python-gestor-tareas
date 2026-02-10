#!/usr/bin/env python3

from contextlib import contextmanager

@contextmanager
def managed_file(path: str, mode: str):
    """
    Context manager for safe file handling.
    Ensures file is always closed.
    """
    file = None

    try:
        file = open(path, mode)
        yield file
    
    except Exception as e:
        print(f"Error opening file [{path}]: {e}")
        raise

    finally:
        if file:
            file.close()
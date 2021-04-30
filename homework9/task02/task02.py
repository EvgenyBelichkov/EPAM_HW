"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, name_exception):
        self.name_exception = name_exception
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.name_exception:
            return True


@contextmanager
def suppressor(name_exception):
    try:
        yield
    except name_exception:
        pass

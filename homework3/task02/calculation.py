"""
Here's a not very efficient calculation function that calculates something important:

import time
import struct
import random
import hashlib

def slow_calculate(value):
    "Some weird voodoo magic calculations"
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""

import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    "Some weird voodoo magic calculations"
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def updated_slow_calculate(fun, lst):
    with Pool(500) as calk:
        result = sum(calk.map(fun, lst))
    return result


if __name__ == "__main__":
    lst = [i for i in range(501)]
    print(updated_slow_calculate(slow_calculate, lst))

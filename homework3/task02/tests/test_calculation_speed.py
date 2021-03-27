import time

import pytest

from homework3.task02 import calculation


@pytest.mark.parametrize(
    "lst", [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [0, 0, 0, 0, 0, 0, 0]]
)
def test_speed_of_calculation(lst):
    start = time.time()
    result_slow_calculate = 0
    for i in lst:
        result_slow_calculate += calculation.slow_calculate(i)
    finish = time.time()
    time_slow_calculate = finish - start
    start_fast_calculate = time.time()
    calculation.updated_slow_calculate(calculation.slow_calculate, lst)
    finish_fast_calculate = time.time()
    time_fast_calculate = finish_fast_calculate - start_fast_calculate
    assert time_fast_calculate < time_slow_calculate

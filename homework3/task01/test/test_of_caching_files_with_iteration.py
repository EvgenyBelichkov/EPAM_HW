from unittest.mock import Mock

import pytest

from homework3.task01.cache_continue import cache_func


@pytest.mark.parametrize("times,expected_result", [(3, 2), (0, 6), (1, 3), (100, 1)])
def test_caching_function(times, expected_result):
    m = Mock()
    thing = cache_func(times)(m)
    thing()
    thing()
    thing()
    thing()
    thing()
    thing()
    assert m.call_count == expected_result

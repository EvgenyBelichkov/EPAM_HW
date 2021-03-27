from collections import namedtuple

import pytest

from homework2.task04 import cache_function

Testset = namedtuple("Testset", ["function", "arguments"])

test_examples = [
    Testset(function=lambda a, b: (a ** b) ** 2, arguments=(2, 2)),
    Testset(function=lambda a, b, c, d: a + b + c + d, arguments=(2, 2, 2, 2)),
    Testset(function=lambda a, b: a + b, arguments=("emap", "training")),
]


@pytest.mark.parametrize("testset", test_examples)
def test_cache_function(testset):
    call_number = 0

    def function_with_call_count(*args, **kwargs):
        nonlocal call_number
        call_number += 1
        return testset.function(*args, **kwargs)

    decorated_function = cache_function.cache(function_with_call_count)
    previous_result = decorated_function(*testset.arguments)
    for i in range(10):
        assert decorated_function(*testset.arguments) == previous_result
        assert call_number == 1

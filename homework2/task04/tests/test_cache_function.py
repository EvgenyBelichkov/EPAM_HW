import pytest

from homework2.task04 import cache_function


@pytest.fixture
def fixture():
    def fun1(a, b):
        return (a ** b) ** 2

    cache_funk = cache_function.cache(fun1)
    some = 2, 2
    val_1 = cache_funk(*some)
    val_2 = cache_funk(*some)
    yield val_1, val_2


def test_cache_function_example1(fixture):
    val_1, val_2 = fixture
    assert val_1 == val_2


@pytest.fixture
def fixture():
    def fun2(a, b, c, d):
        return a + b + c + d

    cache_funk = cache_function.cache(fun2)
    some = 2, 2, 2, 2
    val_1 = cache_funk(*some)
    val_2 = cache_funk(*some)
    yield val_1, val_2


def test_cache_function_example2(fixture):
    val_1, val_2 = fixture
    assert val_1 == val_2


@pytest.fixture
def fixture():
    def fun3(a, b):
        return a + b

    cache_funk = cache_function.cache(fun3)
    some = "EPAM", "training"
    val_1 = cache_funk(*some)
    val_2 = cache_funk(*some)
    yield val_1, val_2


def test_cache_function_example3(fixture):
    val_1, val_2 = fixture
    assert val_1 == val_2

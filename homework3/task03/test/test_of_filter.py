import pytest

from homework3.task03 import changing_filter


@pytest.mark.parametrize(
    "function, data, expected_result",
    [[[lambda a: a % 2 == 0], range(10), [0, 2, 4, 6, 8]]],
)
def test_of_checking_filter(data, expected_result, function):
    assert changing_filter.Filter(function).apply(data) == expected_result


@pytest.fixture
def fixture():
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    yield data


def test_of_checking_filter1(fixture):
    data = fixture
    assert changing_filter.make_filter(name="Bill").apply(data) == [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        }
    ]


def test_of_checking_filter2(fixture):
    data = fixture
    assert changing_filter.make_filter().apply(data) == []


def test_of_checking_filter3(fixture):
    data = fixture
    assert changing_filter.make_filter(name="polly", type="bird").apply(data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]

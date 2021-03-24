import pytest

from homework3.task03 import changing_filter


def test_of_checking_class_how_it_count_custom_function():
    assert changing_filter.Filter(
        [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)]
    ).apply(range(10)) == [2, 4, 6, 8]


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
    assert changing_filter.make_filter(name="Bill").apply(data) == [data[0]]


def test_of_checking_filter2(fixture):
    data = fixture
    assert (
        changing_filter.make_filter(name="polly", last_name="Gilbert").apply(data) == []
    )


def test_of_checking_filter3(fixture):
    data = fixture
    assert changing_filter.make_filter(name="polly", type="bird").apply(data) == [
        data[1]
    ]


def test_of_checking_filter4(fixture):
    data = fixture
    assert (
        changing_filter.make_filter(name="polly", last_name="Gilbert").apply(data) == []
    )


def test_of_checking_filter5(fixture):
    data = fixture
    assert changing_filter.make_filter(not_exist_param="polly").apply(data) == []

import pytest

from homework7.task02.comparing_words import backspace_compare


@pytest.mark.parametrize(
    "first_word, second_word, expected_result",
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("", "#", True),
        ("###a", "a", True),
        ("abc###", "", True),
    ],
)
def test_backspace_compare_function(first_word, second_word, expected_result):
    assert backspace_compare(first_word, second_word) == expected_result

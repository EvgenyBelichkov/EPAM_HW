import os

import pytest

from homework4.task01.checking_numbers import checking_function


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ([45, 24, 37], False),
        (["-5", 0, 3], False),
        ([0, "Hello"], False),
    ],
)
def test_of_reading_first_line(number, expected_result):
    file = open("text.txt", "w")
    for i in number:
        file.write(str(i))
        file.write("\n")
    file.close()
    assert checking_function("text.txt") == expected_result
    os.remove("text.txt")


@pytest.mark.parametrize(
    "string", [(["one", "two", "three"]), (["word", "2", "3"]), (["", "2", "3"])]
)
def test_if_words_in_text(string):
    file = open("text.txt", "w")
    for i in string:
        file.write(str(i))
        file.write("\n")
    file.close()
    with pytest.raises(ValueError):
        checking_function("text.txt")
    os.remove("text.txt")

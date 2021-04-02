import os

import pytest

from homework4.task01.checking_numbers import checking_function


def create_test_file(text):
    file = open("text.txt", "w")
    for i in text:
        file.write(str(i))
        file.write("\n")
    file.close()


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ([45, 24, 37], False),
        (["-5", 0, 3], False),
        ([0, "Hello"], False),
        ([2, 24, 37], True),
        ([3, 4, "ok"], False),  # added check boundary values
        ([0, 2], False),  # added check boundary values
    ],
)
def test_of_reading_first_line(number, expected_result):
    create_test_file(number)
    assert checking_function("text.txt") == expected_result
    # os.remove("text.txt")


@pytest.mark.parametrize(
    "string", [(["one", "two", "three"]), (["word", "2", "3"]), (["", "2", "3"])]
)
def test_if_words_in_text(string):
    create_test_file(string)
    with pytest.raises(ValueError):
        checking_function("text.txt")
    os.remove("text.txt")


def test_file_not_exist():  # added check if file not exist
    with pytest.raises(ValueError):
        checking_function("path")


def test_file_with_first_line_is_sentence():  # added check when first line can be sentence with numbers
    with pytest.raises(ValueError):
        checking_function("1 word")

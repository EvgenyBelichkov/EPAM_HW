import os

import pytest

from homework8.task01.task1 import KeyValueStorage


def test_class_where_the_attribute_value_is_undefined():
    example1 = KeyValueStorage(os.path.join(os.path.dirname(__file__), "text1.txt"))
    assert example1.name == "kek"
    assert example1.song_name == "shadilay"
    assert example1["last_name"] == "top"


def test_class_raises_value_error_because_text_file_contains_keyword():
    with pytest.raises(ValueError):
        KeyValueStorage(os.path.join(os.path.dirname(__file__), "text2.txt"))


def test_class_where_attribute_can_not_be_identifier():
    with pytest.raises(ValueError):
        KeyValueStorage(os.path.join(os.path.dirname(__file__), "text3.txt"))

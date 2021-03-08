import os

import pytest

from homework2.task01 import text_counter


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [
            os.path.join(os.path.dirname(__file__), "text1.txt"),
            [
                "asdfghjklzxcv/nmbv",
                "Qwertyuiop",
                "zxcv",
                "vbnm",
                "ееппааамм",
                "gtyu",
                "asd",
                "ghoooo",
                "ghj",
                "ujt",
            ],
        ],
        [
            os.path.join(os.path.dirname(__file__), "data.txt"),
            [
                "Bev\\u00f6lkerungsabschub,",
                "unmi\\u00dfverst\\u00e4ndliche",
                "Werkst\\u00e4ttenlandschaft",
                "Machtbewu\\u00dftsein,",
                "Selbstverst\\u00e4ndlich",
                "Entz\\u00fcndbarkeit.",
                "Werkst\\u00e4ttenlandschaft",
                "r\\u00e9sistance-Bewegungen,",
                "Zahlenverh\\u00e4ltnis-",
                "\\u00fcberw\\u00e4ltigend",
            ],
        ],
    ],
)
def test_longest_diverse_words(file_name, expected_result):
    assert text_counter.get_longest_diverse_words(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "text1.txt"), "w, e, r, i, /"],
        [os.path.join(os.path.dirname(__file__), "data.txt"), "(, )"],
    ],
)
def test_rarest_char(file_name, expected_result):
    assert text_counter.get_rarest_char(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "text1.txt"), 10],
        [os.path.join(os.path.dirname(__file__), "data.txt"), 8277],
    ],
)
def test_count_punctuation_chars(file_name, expected_result):
    assert text_counter.count_punctuation_chars(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "text1.txt"), 9],
        [os.path.join(os.path.dirname(__file__), "data.txt"), 0],
    ],
)
def test_non_ascii_chars(file_name, expected_result):
    assert text_counter.count_non_ascii_chars(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "text1.txt"), "е, п, м"],
        [os.path.join(os.path.dirname(__file__), "data.txt"), "None"],
    ],
)
def test_most_common_non_ascii_chars(file_name, expected_result):
    assert text_counter.get_most_common_non_ascii_char(file_name) == expected_result

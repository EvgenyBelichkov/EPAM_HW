import os

import pytest

from homework2.task01 import text_counter


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [
            os.path.join(os.path.dirname(__file__), "text1.txt"),
            [
                "asdfghjklzxcv",
                "Qwertyuiop",
                "zxcv",
                "vbnm",
                "ееппааамм",
                "nmbv",
                "gtyu",
                "asd",
                "ghoooo",
                "holo",
            ],
        ],
        [
            os.path.join(os.path.dirname(__file__), "text2.txt"),
            [
                "RRЕееПпппАаааМмммRRR",
                "as",
                "ad",
                "af",
                "ag",
                "ah",
                "aj",
                "ak",
                "al",
                "az",
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
        [
            os.path.join(os.path.dirname(__file__), "text2.txt"),
            "s, d, f, g, h, j, k, l, z, x",
        ],
    ],
)
def test_rarest_char(file_name, expected_result):
    assert text_counter.get_rarest_char(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "text1.txt"), 10],
        [os.path.join(os.path.dirname(__file__), "text2.txt"), 22],
    ],
)
def test_count_punctuation_chars(file_name, expected_result):
    assert text_counter.count_punctuation_chars(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "text1.txt"), 9],
        [os.path.join(os.path.dirname(__file__), "text2.txt"), 15],
    ],
)
def test_non_ascii_chars(file_name, expected_result):
    assert text_counter.count_non_ascii_chars(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "text1.txt"), "а"],
        [os.path.join(os.path.dirname(__file__), "text2.txt"), "п, а, м"],
    ],
)
def test_most_common_non_ascii_chars(file_name, expected_result):
    assert text_counter.get_most_common_non_ascii_char(file_name) == expected_result

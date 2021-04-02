from unittest import mock
from unittest.mock import Mock

import pytest

from homework4.task02 import count_i_function
from homework4.task02.count_i_function import getting_html_text


@pytest.mark.parametrize("url", ["https/example.nice-example.com/", "word"])
def test_function_that_counting_i_with_error(url):
    with pytest.raises(ValueError):
        count_i_function.count_dots_on_i(url)


@mock.patch(
    "homework4.task02.count_i_function.getting_html_text",
    mock.MagicMock(return_value="privet"),
)
def test_function_that_counting_i_with_mock_patch():
    assert count_i_function.count_dots_on_i("https://google.com/") == 1


def test_function_that_counting_i_with_monkeypatch(monkeypatch):
    monkeypatch.setattr(
        count_i_function, "getting_html_text", Mock(return_value="iiiiooo")
    )
    assert count_i_function.count_dots_on_i("https://google.com/") == 4

import os
import sys

import pytest

from homework4.task03.stdout_stderr import my_precious_logger


@pytest.mark.parametrize(
    "word, expected_result",
    [("error: file not found", False), ("Ok", True), ("", True), ("1234567", True)],
)
def test_stdout_stderr_function(word, expected_result):
    sys.stdout = open("stdout", "w")
    sys.stderr = open("stderr", "w")
    my_precious_logger(word)
    sys.stdout.close()
    sys.stderr.close()
    size_stdout = os.path.getsize("stdout")
    size_stderr = os.path.getsize("stderr")
    a = size_stdout >= size_stderr
    assert a == expected_result

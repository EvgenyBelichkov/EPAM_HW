import pytest

from homework1.task03.find_maximum_and_minimum import scan



@pytest.mark.parametrize("file_name, expected_result", [('task03/test1.txt', (-5000, 12000)),
                                                        ('task03/test2.txt', (1, 10)),
                                                        ('task03/test3.txt', (-10000, 20000)),
                                                        ('task03/test4.txt', (1, 15))])
def test_maximum_and_minimum(file_name, expected_result):
    assert scan(file_name) == expected_result

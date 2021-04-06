import os

import pytest

from homework8.task02.task2 import TableData


@pytest.fixture()
def creating_instance_class():
    return TableData(
        os.path.join(os.path.dirname(__file__), "example.sqlite"), "presidents"
    )


def test_get_information_about_trump_from_database(creating_instance_class):
    assert creating_instance_class["Trump"] == ("Trump", 1337, "US")


def test_president_in_presidents_table(creating_instance_class):
    assert ("Trump" in creating_instance_class) == True
    assert ("Big Man Tyrone" in creating_instance_class) == True
    assert ("Clinton" in creating_instance_class) == False


def test_len_table(creating_instance_class):
    assert len(creating_instance_class) == 3


def test_iteration_protocol_for_class(creating_instance_class):
    list_of_presidents = []
    for data in creating_instance_class:
        list_of_presidents.append(data[0])
    assert list_of_presidents == ["Yeltsin", "Trump", "Big Man Tyrone"]

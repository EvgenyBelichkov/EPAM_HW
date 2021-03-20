import datetime
from collections import namedtuple

import pytest

from homework5.task01.oop_1 import Homework, Student, Teacher

params = namedtuple(
    "params",
    [
        "first_name_teacher",
        "second_name_teacher",
        "first_name_student",
        "second_name_student",
        "theme",
        "dl",
        "expected_result",
    ],
)

test_examples = [
    params(
        first_name_teacher="Alex",
        second_name_teacher="Lukin",
        first_name_student="Evgeny",
        second_name_student="Belichkov",
        theme="OOP_1",
        dl=0,
        expected_result=True,
    ),
    params(
        first_name_teacher="Roman",
        second_name_teacher="Malginov",
        first_name_student="Alfia",
        second_name_student="Abdulmanova",
        theme="OOP_2",
        dl=5,
        expected_result=False,
    ),
]


@pytest.mark.parametrize("data", test_examples)
def test_do_homework_method_in_student(data):
    task = Teacher(data[0], data[1]).create_homework(data[4], data[5])
    student = Student(data[2], data[3])
    task_completed1 = student.do_homework(task)
    result = task_completed1 is None
    assert result == data[6]


def test_returns_in_create_homework_method_exemplar_of_class_homework():
    task1 = Teacher("Nikol", "Smith").create_homework("regular expressions", 2)
    assert task1.text == "regular expressions"
    assert task1.deadline.days == 2


def test_is_active_method_in_homework_class_in_time():
    task = Homework("functions", 5)
    assert task.is_active()


def test_is_active_method_in_homework_class_expired():
    task = Homework("functions", 0)
    assert task.is_active() == False

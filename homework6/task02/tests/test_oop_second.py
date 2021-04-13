from collections import namedtuple

import pytest

from homework6.task02.oop_second_task import *

params = namedtuple(
    "params",
    [
        "first_name_teacher",
        "second_name_teacher",
        "first_name_student",
        "second_name_student",
        "theme",
        "dl",
        "solution",
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
        solution="solution_1",
    ),
    params(
        first_name_teacher="Roman",
        second_name_teacher="Malginov",
        first_name_student="Alfia",
        second_name_student="Abdulmanova",
        theme="OOP_2",
        dl=5,
        solution="solution_2",
    ),
]


@pytest.mark.parametrize("data", test_examples)
def test_creating_first_name_and_last_name_of_teacher(data):
    oop_teacher = Teacher(data[0], data[1])
    assert oop_teacher.first_name == data[0]
    assert oop_teacher.last_name == data[1]


@pytest.mark.parametrize("data", test_examples)
def test_do_homework_from_student_class(data):
    student = Student(data[0], data[1])
    homework = Teacher(data[0], data[1]).create_homework(data[4], data[5])
    if data[5] == 0:
        with pytest.raises(DeadlineError):
            student.do_homework(homework, data[6])
    else:
        assert (
            isinstance(student.do_homework(homework, data[6]), HomeworkResult) == True
        )


@pytest.mark.parametrize("data", test_examples)
def test_type_error_from_homework_result(data):
    with pytest.raises(TypeError):
        HomeworkResult(data[4], data[6])


def test_dictionary_from_teacher_class():
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    first_student = Student("Lev", "Sokolov")
    second_student = Student("Alex", "Lukin")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    result_1 = first_student.do_homework(oop_hw, "123456")
    result_2 = second_student.do_homework(oop_hw, "123456")

    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_2)
    temp_2 = advanced_python_teacher.homework_done

    temp_3 = Teacher.homework_done

    assert temp_1 == temp_2 == temp_3

    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0

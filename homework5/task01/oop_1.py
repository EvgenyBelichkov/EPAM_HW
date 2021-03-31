"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    """This is a class that takes information about homework from Teacher
    class (text, deadline) and keep it in attributes (text, dl, created)
    :param text: text of homework
    :param dl: quantity days to complete homework
    """

    def __init__(self, text, dl):
        """Constructor method"""
        self.text = text
        self.deadline = datetime.timedelta(days=dl)
        self.created = datetime.datetime.now()

    def is_active(self):
        """Methods checks if the task execution time has expired
        :return: `True` if deadline has not come, `False` otherwise
        :rtype: bool
        """
        return self.created + self.deadline > datetime.datetime.now()


class Student:
    """This is a class that takes and keep first name and last name of student.
    Thanks to method 'do_homework' you can check status of homework.
    class (text, deadline) and keep it in attributes (text, dl, created)
    :param first_name: first name of student
    :param last_name: last name of student"""

    def __init__(self, first_name, last_name):
        """Constructor method"""
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        """Method takes a Homework object and returns it. If the homework is already overdue
        method prints 'You are late' and returns None
        :param homework: takes :class:`Homework` object
        :return: return :class:`Homework` object if deadline has not come, :class:`NoneType` otherwise
        :rtype: :class:`Homework` object or :class:`NoneType` object.
        """
        if homework.is_active() is False:
            print("You are late")
            return
        else:
            return homework


class Teacher:
    """This is a class that takes and keep first name and last name of teacher.
    Thanks to static method 'create_homework' you can return class Homework object.
    :param first_name: first name of teacher
    :param last_name: last name of teacher"""

    def __init__(self, first_name, last_name):
        """Constructor method"""
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, dl):
        """Method takes the text of the task and the number of days for this task, returns an instance of Homework
        :param text: text of the task
        :param dl: quantity days to complete homework
        :return: return :class:`Homework` object
        :rtype: :class:`Homework` object
        """
        return Homework(text, dl)

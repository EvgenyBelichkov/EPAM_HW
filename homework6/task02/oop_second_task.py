"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

import datetime
from collections import defaultdict


class Homework:
    """This is a class that takes information about homework from :class:'Teacher'
    (text, deadline) and keep it in attributes (text, dl, created)
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


class HomeworkResult:
    """This is a class that can take :class:`Homework' object, :class:`Student' object
    and solution in string representation and keep information in attributes (solution,
    author, created).
    :param homework: for :class:`Homework' object. If object isn't correct - raising
    error with message 'You gave a not Homework object'.
    :param solution: stores solution as a string.
    :param student: stores the :class:`Student' object.
    :raises [TypeError]: [raising error with message
    'You gave a not Homework object']
    """

    def __init__(self, homework=None, solution=None, student=None):
        """Constructor method"""
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.author = student
        self.created = datetime.datetime.now()


class Person:
    """This is the class, that realise construction methods
    for :class:'Student' and :class:'Teacher'"""

    def __init__(self, first_name, last_name):
        """Constructor method"""
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """Class inherited from class :class:`Person'.
    This is a class that takes and keep first name and last name of student.
    Thanks to method 'do_homework' you can check status of homework.
    :param first_name: first name of student
    :param last_name: last name of student"""

    def __init__(self, first_name, last_name):
        """Constructor method"""
        super().__init__(first_name, last_name)

    def do_homework(self, homework=None, solution=None, student=None):
        """Method take :class:`Homework' object, :class:`Student' object, solution
        and if homework is active return :class:'HomeworkResult'. Otherwise rise error.
        :param homework: for :class:`Homework' object.
        :param solution: stores solution as a string.
        :param student: stores the :class:`Student' object.
        :raises [DeadlineError]: [if homework out of deadline]
        :return: return :class:'HomeworkResult'
        :rtype: :class:'HomeworkResult'
        """
        if homework.is_active():
            return HomeworkResult(homework, solution, student)
        else:
            raise DeadlineError("You are late")


class Teacher(Person):
    """Class inherited from class :class:`Person'.This is a class that take
    and keep first name and last name of teacher. Class can pass information
    to :class:'Homework' to create homework object, collect solutions and
    reset results from dictionary.
    :param first_name: first name of teacher
    :param last_name: last name of teacher"""

    homework_done = defaultdict(set)

    def __init__(self, first_name, last_name):
        """Constructor method"""
        super().__init__(first_name, last_name)

    @staticmethod
    def create_homework(text, dl):
        """Method takes the text of the task and the number of days for this task,
        returns :class:'Homework' object.
        :param text: text of the task
        :param dl: quantity days to complete homework
        :return: return :class:`Homework` object
        :rtype: :class:`Homework` object
        """
        return Homework(text, dl)

    def check_homework(self, homeworkresult):
        """Method takes  :class:'HomeworkResult' object and checking solution. If solution
        is correct - it will be added to dictionary 'homework_done' and return True
        (guaranteed absence of duplicate results for each task). Otherwise will
        return False.
        :param homeworkresult: :class:'HomeworkResult' object.
        :return: `True` if solution is right, `False` otherwise
        :rtype: bool
        """
        homework = homeworkresult.homework
        if len(homeworkresult.solution) > 5:
            self.homework_done[homework].add(homeworkresult.solution)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        """If method would takes :class:'Homework' object as argument, it
        will remove only the results of this task from homework_done,
        if method would take :class:`NoneType` object, it will completely
        reset homework_done.
        :param homework: :class:'HomeworkResult' object."""
        if homework is None:
            cls.homework_done = defaultdict(list)
        else:
            cls.homework_done[homework] = []


class DeadlineError(Exception):
    """Additional Error class """

    pass

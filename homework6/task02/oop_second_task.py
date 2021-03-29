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
    def __init__(self, text, dl):
        self.text = text
        self.deadline = datetime.timedelta(days=dl)
        self.created = datetime.datetime.now()

    def is_active(self):
        return self.created + self.deadline > datetime.datetime.now()


class HomeworkResult:
    def __init__(self, homework=None, solution=None, student=None):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.author = student
        self.created = datetime.datetime.now()


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework=None, solution=None, student=None):
        if homework.is_active():
            return HomeworkResult(homework, solution, student)
        else:
            raise DeadlineError("You are late")


class Teacher(Student):
    homework_done = defaultdict(list)

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    @staticmethod
    def create_homework(text, dl):
        return Homework(text, dl)

    def check_homework(self, homeworkresult):
        homework = homeworkresult.homework
        if (
            len(homeworkresult.solution) > 5
            and homeworkresult not in self.homework_done[homework]
        ):
            self.homework_done[homework].append(homeworkresult)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework is None:
            cls.homework_done = defaultdict(list)
        else:
            cls.homework_done[homework] = []


class DeadlineError(Exception):
    pass

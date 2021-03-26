"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    class ModifiedUser(cls):
        cls.instance = 0

        def __init__(self, *args, **kwargs):
            cls.instance += 1

        @staticmethod
        def get_created_instances():
            return cls.instance

        @staticmethod
        def reset_instances_counter():
            current_value = cls.instance
            cls.instance = 0
            return current_value

    return ModifiedUser


@instances_counter
class User:
    pass

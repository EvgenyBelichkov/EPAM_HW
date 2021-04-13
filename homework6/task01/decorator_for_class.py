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
        @classmethod
        def creating_counter(cls):
            if not "instance" in cls.__dict__:
                cls.instance = 0

        def __init__(self, *args, **kwargs):
            self.creating_counter()
            super().__init__(*args, **kwargs)
            self.__class__.instance += 1

        @classmethod
        def get_created_instances(cls):
            if not "instance" in cls.__dict__:
                return 0
            return cls.instance

        @classmethod
        def reset_instances_counter(cls):
            current_value = cls.instance
            cls.instance = 0
            return current_value

    return ModifiedUser

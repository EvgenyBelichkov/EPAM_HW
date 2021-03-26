from homework6.task01.decorator_for_class import instances_counter


@instances_counter
class Example:
    instance = 25

    def __init__(self, arg):
        self.instance = arg


def test_Example_without_creating_instance_object():
    assert Example.get_created_instances() == 0


def test_method_get_created_instances_for_Example_with_creating_instance_object():
    first = Example(10)
    second = Example(15)
    assert first.get_created_instances() == 2
    assert second.get_created_instances() == 2


def test_method_reset_instances_counter_for_Example1():
    first = Example(20)
    second = Example(30)
    first.reset_instances_counter()
    assert first.get_created_instances() == 0
    assert second.get_created_instances() == 0

from homework5.task02 import oop2

# checking printing result, __doc__ and __name__  information


@oop2.print_result
def example_1(a, b):
    """This function multiplies 'a' and 'b'"""
    return a * b


def test_printing_result_of_example_1():
    assert example_1(2, 2) == 4


def test_return_doc_and_name_information_of_example1():
    assert example_1.__doc__ == "This function multiplies 'a' and 'b'"
    assert example_1.__name__ == "example_1"


# checking function without printing result

without_print = example_1.__original_func
print(type(without_print(1, 2)))


def test_example1_without_printing():
    assert type(without_print) == type(example_1)

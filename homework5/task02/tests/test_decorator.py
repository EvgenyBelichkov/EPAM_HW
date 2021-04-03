from homework5.task02 import oop2

# checking printing result, __doc__ and __name__  information


def test__return_doc_and_name_information_of_decorated_function():
    @oop2.print_result
    def example_1(a, b):
        """This function multiplies 'a' and 'b'"""
        return a * b

    assert example_1(2, 2) == 4
    assert example_1.__doc__ == "This function multiplies 'a' and 'b'"
    assert example_1.__name__ == "example_1"


# checking function without printing result


def test_example1_without_printing():
    @oop2.print_result
    def printing_important_information():
        print("EPAM is the best training ever")

    without_print = printing_important_information.__original_func
    assert type(without_print) == type(printing_important_information)

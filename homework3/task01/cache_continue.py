"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>> f()
? 1
'1'
>> f()     # will remember previous value
'1'
>> f()     # but use it up to two times only
'1'
>> f()
? 2
'2'
"""


def cache(times: int):
    elements = {}

    def wrap(func):
        def timer(*args):
            if args not in elements:
                value = func(*args)
                elements[args] = [value, 0]
                return elements[args][0]
            elif elements[args][1] < times:
                elements[args][1] += 1
                return elements[args][0]
            else:
                value = func(*args)
                elements[args] = [value, 0]
                return value

        return timer

    return wrap


@cache(times=2)
def cache(fun):
    cache_dict = dict()

    def memory(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = fun(*args)
        cache_dict[args] = result
        return result

    return memory


# def fun1(a):
#     return a ** 2
#
#
# some = [2]
# print(cache(fun1)(*some))
# print(cache(fun1)(*some))
# print(cache(fun1)(*some))
# print(cache(fun1)(*some))

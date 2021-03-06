"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum
# class ColorsEnum(Enum):
#     RED = "RED"
#     BLUE = "BLUE"
#     ORANGE = "ORANGE"
#     BLACK = "BLACK"
# class SizesEnum(Enum):
#     XL = "XL"
#     L = "L"
#     M = "M"
#     S = "S"
#     XS = "XS"



class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")

assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(mcs, name, bases, attrs):
        for method in attrs["_{}__keys".format(name)]:
            attrs[method] = method
        return super().__new__(mcs, name, bases, attrs)

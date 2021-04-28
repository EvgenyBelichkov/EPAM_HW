import pytest

from homework11.task01.task01 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS", "BLACK")


def test_correct_work_of_metaclass():
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
    assert ColorsEnum.BLACK == SizesEnum.BLACK


def test_error_attribute():
    with pytest.raises(AttributeError):
        ColorsEnum.WHITE

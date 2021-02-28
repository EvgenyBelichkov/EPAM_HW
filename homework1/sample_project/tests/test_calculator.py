import pytest

from EPAM_HW.homework1.sample_project.calculator import calc


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(65536, True), (12, False), (34, False)],  # added one more test to check function
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = calc.check_power_of_2(value)

    assert actual_result == expected_result

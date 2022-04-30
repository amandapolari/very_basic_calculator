import pytest
from very_basic_calculator import power


@pytest.mark.parametrize("x, y", [(1, 1), (4, 1), (2, 9), (4, 2), (9, 0)])
def test_power(x, y):
    assert power(x, y) == x**y

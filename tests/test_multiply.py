import pytest
from very_basic_calculator import multiply


@pytest.mark.parametrize("x, y", [(1, 1), (4, 1), (2, 9), (4, 2), (9, 0)])
def test_multiply(x, y):
    assert multiply(x, y) == x * y

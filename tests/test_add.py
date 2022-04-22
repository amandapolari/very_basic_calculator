import pytest
from very_basic_calculator import add


@pytest.mark.parametrize("x, y", [(1, 1), (4, 1), (2, 9), (4, 2), (9, 0)])
def test_add(x, y):
    assert add(x, y) == x + y

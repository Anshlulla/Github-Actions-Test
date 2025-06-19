from src.math_operations import add, subtract

def test_add():
    assert add(2, 4) == 6
    assert add(-1, 8) == 7
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(2, 4) == -2
    assert subtract(-1, 8) == -9
    assert subtract(-1, 1) == -2
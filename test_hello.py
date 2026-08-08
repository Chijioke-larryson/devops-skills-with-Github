# import the hello into here

from hello import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


# test for subtract


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0


# test for multiply


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0


# test for divide


def test_divide():
    assert divide(6, 2) == 3
    assert divide(0, 1) == 0
    assert divide(-1, 1) == -1

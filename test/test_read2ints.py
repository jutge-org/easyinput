import io
import jutge


def check(data, a, b):
    stream = io.StringIO(data)
    x, y = jutge.read(float, float, file=stream)
    assert x == a
    assert y == b


def test_1():
    check("3.0 4.0", 3.0, 4.0)


def test_2():
    check("15.5 12.345", 15.5, 12.345)


def test_3():
    check("15.5 -12.345", 15.5, -12.345)


def test_4():
    check("15.5    -12.345", 15.5, -12.345)


def test_5():
    check("0 0.0", 0, 0)


def test_6():
    check("-0 -0.0", 0, 0)


def test_7():
    check("-0. 0.", 0, 0)


def test_8():
    check("-.123 .124", -0.123, 0.124)

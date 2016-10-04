import io
import jutge


def check(data, a, b):
    stream = io.StringIO(data)
    x, y = jutge.read(int, int, file=stream)
    assert x == a
    assert y == b


def test_1():
    check("3 4", 3, 4)


def test_2():
    check("155 12345", 155, 12345)


def test_3():
    check("155 -12345", 155, -12345)


def test_4():
    check("155    -12345", 155, -12345)


def test_5():
    check("   \n\n      155  \n \n \t  -12345   \t \n ", 155, -12345)


def test_6():
    check("   \n\n      155  \n \n \t  -12345   \t \n", 155, -12345)


def test_7():
    check("   \n   \n      -0  \n \n \t  000   \t \n", 0, 0)


def test_8():
    check("   \n   \n      -00000  \n \n \t  070   \t \n", 0, 70)

import io
import jutge


def count_As(data):
    stream = io.StringIO(data)
    c = 0
    x = jutge.read(chr, file=stream)
    while x is not None:
        if x is 'a':
            c += 1
        x = jutge.read(chr, file=stream)
    return c


def test_1():
    assert count_As("i am a strong boy") == 2


def test_2():
    assert count_As("a") == 1


def test_3():
    assert count_As("") == 0


def test_4():
    assert count_As("a a") == 2


def test_5():
    assert count_As("aa") == 2

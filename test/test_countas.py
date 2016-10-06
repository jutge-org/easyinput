import io
import jutge


def countas(data):
    stream = io.StringIO(data)
    c = 0
    x = jutge.read(chr, file=stream)
    while x is not None:
        if x is 'a':
            c += 1
        x = jutge.read(chr, file=stream)
    return c


def test_1():
    assert countas("i am a strong boy") == 2


def test_2():
    assert countas("a") == 1


def test_3():
    assert countas("") == 0


def test_4():
    assert countas("a a") == 2


def test_5():
    assert countas("aa") == 2

import io
import jutge


def upper_jutge(data):
    stream = io.StringIO(data)
    r = ""
    x = jutge.read(file=stream)
    while x is not None:
        r += x.upper()
        x = jutge.read(file=stream)
    return r


def upper_python(data):
    return "".join(map(str.upper, data.split()))


def check(data):
    assert upper_jutge(data) == upper_python(data)


def test_1():
    check("jordi")


def test_2():
    check("jordi mireia")


def test_3():
    check("jordi mireia arnau")


def test_4():
    check("jordi mireia arnau marta")

import io
import jutge


def sum_jutge(data):
    stream = io.StringIO(data)
    s = 0
    x = jutge.read(int, file=stream)
    while x is not None:
        s += x
        x = jutge.read(int, file=stream)
    return s


def sum_python(data):
    return sum(map(int, data.split()))


def check(data):
    assert sum_jutge(data) == sum_python(data)


def test_1():
    check("")


def test_2():
    check("1")


def test_3():
    check("1 2")


def test_4():
    check("1 2 3")


def test_5():
    check("1 2 3 4")


def test_6():
    check("111 222 333 444")


def test_7():
    check("   111    222     333    444")


def test_8():
    check("   \n  \n\n\n  111 \n   222  \n\n\n   333 \n\n\n444\n\n\n\n")


def test_9():
    data = "1 " * 1000000
    check(data)

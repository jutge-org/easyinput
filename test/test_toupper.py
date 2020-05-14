from __future__ import unicode_literals
import io
import easyinput


def upper_easyinput(data):
    stream = io.StringIO(data)
    return "".join(x.upper() for x in easyinput.read_many(file=stream))


def upper_python(data):
    return "".join(word.upper() for word in data.split())


def check(data):
    assert upper_easyinput(data) == upper_python(data)


def test_1():
    check("jordi")


def test_2():
    check("jordi mireia")


def test_3():
    check("jordi mireia arna")


def test_4():
    check("jordi mireia arnau marta")

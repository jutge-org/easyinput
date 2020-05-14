from __future__ import unicode_literals
import io
import easyinput


def count_As(data):
    stream = io.StringIO(data)
    return sum(x == 'a' for x in (easyinput.read_many(chr, file=stream)))


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

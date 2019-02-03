from __future__ import unicode_literals
import jutge
import io


def test_1():
    source = open('test/text/source3.txt')
    expected = range(1, 13)
    input_gen = jutge.read(int, file=source, amount=12)
    assert all(next(input_gen) == val for val in expected)


def test_2():
    raised = False
    try:
        jutge.read(amount='spam')
    except TypeError:
        raised = True
    assert raised


def test_3():
    raised = False
    try:
        jutge.read(amount=-1)
    except ValueError:
        raised = True
    assert raised


def test_4():
    source = io.StringIO("a2 c3")
    expected = ('a', 2, 'c', 3)
    input_gen = jutge.read(chr, int, amount=2, file=source)
    assert all(next(input_gen) == val for val in expected)

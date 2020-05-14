from __future__ import unicode_literals
import easyinput
import io


def test_1():
    source = open('test/text/source3.txt')
    expected = range(1, 13)
    nums = easyinput.read(int, file=source, amount=12)
    assert all(inp == val for inp, val in zip(nums, expected))


def test_2():
    raised = False
    try:
        easyinput.read(amount='spam')
    except TypeError:
        raised = True
    assert raised


def test_3():
    raised = False
    try:
        easyinput.read(amount=-1)
    except ValueError:
        raised = True
    assert raised


def test_4():
    source = io.StringIO("a2 c3")
    expected = ('a', 2, 'c', 3)
    tokens = easyinput.read(chr, int, amount=2, file=source)
    assert all(inp == val for inp, val in zip(tokens, expected))

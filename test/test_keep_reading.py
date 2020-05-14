from __future__ import unicode_literals
import easyinput


def test_1():
    source = open('./test/text/source1.txt', 'r')
    expected = (
        'hello', 'world', 'Python', 'rocks!', '32.14', r'\n', r'^D'
    )
    input_gen = easyinput.read_many(file=source)
    assert all(next(input_gen) == val for val in expected)


def test_2():
    source = open('./test/text/source1.txt', 'r')
    assert not tuple(easyinput.read_many(int, file=source))


def test_3():
    source = open('./test/text/source2.txt', 'r')
    expected = (
        2, -3, 8
    )
    input_gen = easyinput.read_many(int, file=source)
    assert all(next(input_gen) == val for val in expected)


def test_4():
    source = open('./test/text/source2.txt', 'r')
    expected = (
        2, -3, 8, 3.14, 12
    )
    input_gen = easyinput.read_many(float, file=source)
    assert all(next(input_gen) == val for val in expected)


def test_5():
    source = open('./test/text/source4.txt', 'r')
    expected = (
        ("Avatar", 2008),
        ("Thor", 2010),
        ("The_Great_Gatsby", 1956),
        ("GATTACA", 1999),
        ("Blade_Runner", 1981),
        ("Cars", 2005),
        ("A_Really_Long_Title", 2050),
        ("Monty_Python", 1010)
    )
    input_gen = easyinput.read_many(str, int, file=source)
    assert all(tuple(next(input_gen)) == val for val in expected)


def test_6():
    source = open('./test/text/source3.txt', 'r')
    expected = (tuple(range(1 + 3 * d, 4 + 3 * d)) for d in range(4))
    input_gen = easyinput.read_many(int, file=source, amount=3)
    assert all(tuple(next(input_gen)) == tuple(val) for val in expected)


def test_7():
    source = open('./test/text/source3.txt', 'r')
    expected = (tuple(range(1 + 5 * d, 6 + 5 * d)) for d in range(2))
    input_gen = easyinput.read_many(int, file=source, amount=5)
    assert all(tuple(next(input_gen)) == tuple(val) for val in expected)

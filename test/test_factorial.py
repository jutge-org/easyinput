from __future__ import unicode_literals
import easyinput


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def test_0():
    assert factorial(0) == 1


def test_1():
    assert factorial(1) == 1


def test_2():
    assert factorial(2) == 2


def test_3():
    assert factorial(3) == 6


def test_4():
    assert factorial(4) == 24


def test_10():
    assert factorial(10) == 3628800


def test_large():
    easyinput.version
    assert factorial(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

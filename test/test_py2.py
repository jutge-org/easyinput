from __future__ import unicode_literals
import io
import jutge


def test_1():
    stream = io.StringIO(" foo bar ")
    tokens = jutge.JutgeTokenizer(stream)
    assert tokens.next() == "foo"


def test_2():
    stream = io.StringIO(" 33 spam eggs ")
    tokens = jutge.JutgeTokenizer(stream)
    tokens.typ = int
    assert tokens.next() == 33

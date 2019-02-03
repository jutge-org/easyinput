from jutge import *


def test_all():
    expected = ('read', 'read_while', 'set_eof_handling', 'EOFModes', 'get_line')
    assert all(attr in globals() for attr in expected)

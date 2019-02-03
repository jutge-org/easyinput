from jutge import *


def test_all():
    expected = ('read', 'keep_reading', 'set_eof_handling', 'EOFModes')
    assert all(attr in globals() for attr in expected)

from easyinput import *


def test_all():
    expected = (
        'read', 'read_many',
        'read_line', 'read_many_lines',
        'set_eof_handling', 'EOFModes'
    )
    assert all(attr in globals() for attr in expected)

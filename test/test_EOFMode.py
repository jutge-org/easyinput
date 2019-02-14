from __future__ import unicode_literals
import jutge
import io


def test_1():
    source = io.StringIO('')
    jutge.read(file=source)
    assert jutge.read(file=source) is None


def test_2():
    jutge.set_eof_handling(jutge.EOFModes.RaiseException)
    source = io.StringIO('')

    raised = False
    try:
        jutge.read(file=source)
    except EOFError:
        raised = True
    finally:
        jutge.set_eof_handling(jutge.EOFModes.ReturnNone)

    assert raised

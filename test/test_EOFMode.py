from __future__ import unicode_literals
import easyinput
import io


def test_1():
    source = io.StringIO('')
    easyinput.read(file=source)
    assert easyinput.read(file=source) is None


def test_2():
    easyinput.set_eof_handling(easyinput.EOFModes.RaiseException)
    source = io.StringIO('')

    raised = False
    try:
        easyinput.read(file=source)
    except EOFError:
        raised = True
    finally:
        easyinput.set_eof_handling(easyinput.EOFModes.ReturnNone)

    assert raised

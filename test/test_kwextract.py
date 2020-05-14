from easyinput import read


def test_bad_kwarg():
    raised = False
    try:
        read(nonexistant_kwarg=42)
    except NameError:
        raised = True

    assert raised

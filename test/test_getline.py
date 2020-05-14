import easyinput


def test_read_line():
    with open('test/text/source2.txt') as source:
        easyinput.read_line(file=source)
        easyinput.read(file=source)
        line = easyinput.read_line(file=source, skip_empty=False)
    assert line == '    '


def test_read_line_read():
    with open('test/text/source2.txt') as source:
        easyinput.read_line(file=source)
        result1 = easyinput.read(int, file=source)
        easyinput.read_line(file=source)
        result2 = easyinput.read(float, file=source)
    assert result1 == -3 and result2 == 3.14


def test_read_many_lines():
    with open('test/text/source2.txt') as source:
        for _ in easyinput.read_many_lines(file=source): pass
        assert easyinput.read_line(file=source) is None


def test_skip_empty():
    with open('test/text/source2.txt') as source:
        flag = False
        for line in easyinput.read_many_lines(file=source, skip_empty=True):
            if line == '    ': flag = True
    assert not flag


def test_rstrip():
    with open('test/text/source2.txt') as source:
        easyinput.read_line(file=source)
        easyinput.read(file=source)
        line = easyinput.read_line(file=source, skip_empty=False, rstrip=False)
    assert line == '    \n'

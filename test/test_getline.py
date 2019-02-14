import jutge


def test_read_line():
    with open('test/text/source2.txt') as source:
        jutge.read_line(file=source)
        jutge.read(file=source)
        line = jutge.read_line(file=source, skip_empty=False)
    assert line == '    '


def test_read_line_read():
    with open('test/text/source2.txt') as source:
        jutge.read_line(file=source)
        result1 = jutge.read(int, file=source)
        jutge.read_line(file=source)
        result2 = jutge.read(float, file=source)
    assert result1 == -3 and result2 == 3.14


def test_read_many_lines():
    with open('test/text/source2.txt') as source:
        for _ in jutge.read_many_lines(file=source): pass
        assert jutge.read_line(file=source) is None


def test_skip_empty():
    with open('test/text/source2.txt') as source:
        flag = False
        for line in jutge.read_many_lines(file=source, skip_empty=True):
            if line == '    ': flag = True
    assert not flag


def test_rstrip():
    with open('test/text/source2.txt') as source:
        jutge.read_line(file=source)
        jutge.read(file=source)
        line = jutge.read_line(file=source, skip_empty=False, rstrip=False)
    assert line == '    \n'

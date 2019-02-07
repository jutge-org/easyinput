import jutge


def test_read_line():
    with open('test/text/source2.txt') as source:
        jutge.read_line(file=source)
        jutge.read(file=source)
        line = jutge.read_line(file=source, skip_empty=False)
    assert line == '    \n'


def test_read_many_lines():
    with open('test/text/source2.txt') as source:
        for _ in jutge.read_many_lines(file=source): pass
        assert jutge.read_line(file=source) is None


def test_skip_empty():
    with open('test/text/source2.txt') as source:
        for line in jutge.read_many_lines(file=source, skip_empty=False):
            if line == '    \n': break
        assert jutge.read_line(file=source) == '3.14 12\n'

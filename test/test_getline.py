import jutge


def test_get_line():
    with open('test/text/source4.txt') as source:
        jutge.read(file=source)
        line = jutge.get_line(file=source)
    assert line == 'Thor 2010'

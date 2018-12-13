import jutge


def test1():
    source = open('./test/text/test1.txt', 'r')
    expected = (
        'hello', 'world', 'Python', 'rocks!', '32.14', r'\n', r'^D'
    )
    input_gen = jutge.keep_reading(file=source)
    assert all(next(input_gen) == val for val in expected)


def test2():
    source = open('./test/text/test1.txt', 'r')
    assert not tuple(jutge.keep_reading(int, file=source))


def test3():
    source = open('./test/text/test2.txt', 'r')
    expected = (
        2, -3, 8
    )
    input_gen = jutge.keep_reading(int, file=source)
    assert all(next(input_gen) == val for val in expected)


def test4():
    source = open('./test/text/test2.txt', 'r')
    expected = (
        2, -3, 8, 3.14, 12
    )
    input_gen = jutge.keep_reading(float, file=source)
    assert all(next(input_gen) == val for val in expected)

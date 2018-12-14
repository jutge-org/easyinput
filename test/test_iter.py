from __future__ import unicode_literals
import jutge
import io


class TestJutgeTokenizer():
    def test___iter__(self):
        stream = io.StringIO("foo")  # To allow except-free init
        it = jutge.JutgeTokenizer(stream).__iter__()
        assert hasattr(it, '__iter__')

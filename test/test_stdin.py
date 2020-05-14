from __future__ import unicode_literals
import sys
import io
import easyinput


class Test:
    def test_function(self):
        sys.stdin = io.StringIO("10 20 30")
        [x, y, z] = easyinput.read(int, int, int, file=sys.stdin)
        assert [x, y, z] == [10, 20, 30]

    def test_2(self):
        sys.stdin = io.StringIO("a line\n next line")
        gen = easyinput.StdIn()
        assert next(gen) == "a line"

    def setup_method(self, method):
        self.orig_stdin = sys.stdin

    def teardown_method(self, method):
        sys.stdin = self.orig_stdin

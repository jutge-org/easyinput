from __future__ import unicode_literals
import sys
import io

from jutge import read


class Test:

    def test_function(self):
        sys.stdin = io.StringIO("10 20 30")
        [x, y, z] = read(int, int, int)
        assert [x, y, z] == [10, 20, 30]

    def setup_method(self, method):
        self.orig_stdin = sys.stdin

    def teardown_method(self, method):
        sys.stdin = self.orig_stdin

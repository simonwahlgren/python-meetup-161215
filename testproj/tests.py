import unittest

from foo import foobar


class TestFoo(unittest.TestCase):

    def test_foobar(self):
        assert foobar() == "foobar"

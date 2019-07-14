#!/usr/bin/env python3

# Builtins
import unittest
import pycodestyle
from os import listdir
from os.path import isfile, join, abspath


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide()

        path = abspath(__file__ + "/../../")
        files = [f for f in listdir(path) if isfile(join(path, f))
                 and path.endswith('.py')]

        # for root, dirs, files in os.walk("."):
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()

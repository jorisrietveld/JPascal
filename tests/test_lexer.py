# Author: Joris Rietveld <jorisrietveld@gmail.com>
# Created: 20-08-2017 13:52
# Licence: GPLv3 - General Public Licence version 3
from .context import jpascal

import unittest

class LexerTestSuite(unittest.TestCase):
    """The test suite for the JPascal lexer.

    """

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()

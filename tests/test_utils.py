# -*- coding: utf-8 -*-

"""Test the utilities."""

import pathlib
import unittest

from taxo_info_fetcher.utils import iter_together

HERE = pathlib.Path(__file__).parent


class TestUtils(unittest.TestCase):
    """Test the utilities."""

    def test_my_function(self):
        """Test the utilities."""

        path_1 = HERE.joinpath("test_1.txt")
        path_2 = HERE.joinpath("test_2.txt")
        results = iter_together(path_1, path_2)
        expected = [
            ("hello", "goodbye"),
            ("hi", "aurevoir"),
            ("ciao", "tschuss"),
        ]
        self.assertEqual(expected, results)

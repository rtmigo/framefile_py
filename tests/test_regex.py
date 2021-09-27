# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import re
import unittest

from framefile import hash_pattern_to_regex, pct_pattern_to_regex


class TestHashPatternToRegex(unittest.TestCase):
    def test(self):
        rx = hash_pattern_to_regex('file-####.png')
        with self.subTest("Does not match any string"):
            self.assertIsNone(re.match(rx, "any.png"))
        with self.subTest("Matches exactly four digits:"):
            self.assertIsNone(re.match(rx, "file-543.png"))
        with self.subTest("Dot must be dot:"):
            self.assertIsNone(re.match(rx, "file-5432:png"))
        with self.subTest("The first group is the number sequence:"):
            self.assertEqual(re.match(rx, "file-5432.png").group(1), '5432')


class TestPctPatternToRegex(unittest.TestCase):
    def test(self):
        rx = pct_pattern_to_regex('file-%04d.png')
        with self.subTest("Does not match any string"):
            self.assertIsNone(re.match(rx, "any.png"))
        with self.subTest("Matches exactly four digits:"):
            self.assertIsNone(re.match(rx, "file-543.png"))
        with self.subTest("Dot must be dot:"):
            self.assertIsNone(re.match(rx, "file-5432:png"))
        with self.subTest("The first group is the number sequence:"):
            self.assertEqual(re.match(rx, "file-5432.png").group(1), '5432')

# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest

from framefile import hash_extract_number, pct_extract_number, PatternMismatchError


class TestHashExtractNumber(unittest.TestCase):
    def test_match(self):
        self.assertEqual(hash_extract_number('file_####.jpg', 'file_1234.jpg'),
                         1234)
        self.assertEqual(hash_extract_number('file_####.jpg', 'file_0000.jpg'),
                         0)

    def test_mismatch(self):
        with self.assertRaises(PatternMismatchError):
            hash_extract_number('file_####.jpg', 'file_123.jpg')

class TestPctExtractNumber(unittest.TestCase):
    def test_match(self):
        self.assertEqual(pct_extract_number('file_%04d.jpg', 'file_1234.jpg'),
                         1234)
        self.assertEqual(pct_extract_number('file_%04d.jpg', 'file_0000.jpg'),
                         0)

    def test_mismatch(self):
        with self.assertRaises(PatternMismatchError):
            pct_extract_number('file_%04d.jpg', 'file_123.jpg')


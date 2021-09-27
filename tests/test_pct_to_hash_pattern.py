# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import unittest

from framefile import pct_to_hash_pattern


class TestPctToHashPattern(unittest.TestCase):
    def test(self):
        self.assertEqual(
            pct_to_hash_pattern("/path/to/IMG_%04d.CR2"),
            '/path/to/IMG_####.CR2')

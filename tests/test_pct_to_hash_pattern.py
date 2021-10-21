# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import unittest

from framefile import pct_to_hash_pattern
from tests.common import unislash


class TestPctToHashPattern(unittest.TestCase):
    def test(self):
        self.assertEqual(
            unislash(pct_to_hash_pattern("/path/to/IMG_%04d.CR2")),
            '/path/to/IMG_####.CR2')

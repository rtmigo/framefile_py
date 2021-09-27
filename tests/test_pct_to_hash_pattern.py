import unittest

from framefile._base import pct_to_hash_pattern


class TestPctToHashPattern(unittest.TestCase):
    def test(self):
        self.assertEqual(
            pct_to_hash_pattern("/path/to/IMG_%04d.CR2"),
            '/path/to/IMG_####.CR2')
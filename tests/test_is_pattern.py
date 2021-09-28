import unittest

from framefile import is_pattern, Format


class TestIsPattern(unittest.TestCase):
    def test_pct(self):
        self.assertTrue(is_pattern("/path/to/%05d.png", fmt=Format.percent))
        self.assertFalse(is_pattern("/path/to/#####.png", fmt=Format.percent))
        self.assertFalse(is_pattern("/path/to/image.png", fmt=Format.percent))

    def test_hash(self):
        self.assertTrue(is_pattern("/path/to/#####.png", fmt=Format.hash))
        self.assertFalse(is_pattern("/path/to/%05d.png", fmt=Format.hash))
        self.assertFalse(is_pattern("/path/to/image.png", fmt=Format.hash))
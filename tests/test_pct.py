import unittest

from framefile._base import filename_to_pct_pattern, filename_to_hash_pattern


class TestPct(unittest.TestCase):
    def test(self):
        self.assertEqual(
            filename_to_pct_pattern("/path/to/My-File-8192_00000.exr"),
            "/path/to/My-File-8192_%05d.exr")

        self.assertEqual(
            filename_to_pct_pattern("/path/to/My-File-8192_00000.exr"),
            "/path/to/My-File-8192_%05d.exr")

    def test_canon_pct(self):
        self.assertEqual(
            filename_to_pct_pattern("/path/to/IMG_4567.CR2"),
            "/path/to/IMG_%04d.CR2")
        # without the default min_length=2 it did not work
        self.assertEqual(
            filename_to_pct_pattern("/path/to/IMG_4567.CR2", min_length=1),
            "/path/to/IMG_4567.CR%01d")


class TestHash(unittest.TestCase):

    def test_canon_hash(self):
        self.assertEqual(
            filename_to_hash_pattern("/path/to/IMG_4567.CR2"),
            "/path/to/IMG_####.CR2")
        # without the default min_length=2 it did not work
        self.assertEqual(
            filename_to_hash_pattern("/path/to/IMG_4567.CR2", min_length=1),
            "/path/to/IMG_4567.CR#")

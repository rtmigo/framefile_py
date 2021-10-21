import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from framefile import directory_to_pattern, Format, PatternNotFoundError
from tests.test_pct import unislash


class TestDirToPattern(unittest.TestCase):
    def test(self):
        with TemporaryDirectory() as tds:
            td = Path(tds)
            (td / "frame001.png").touch()
            (td / "frame002.png").touch()
            (td / "frame003.png").touch()
            (td / "img01.png").touch()
            (td / "img02.png").touch()
            (td / ".DS_Store").touch()
            (td / "thumbs.db").touch()

            p = unislash(directory_to_pattern(Format.hash, td))
            self.assertTrue(p.endswith('/frame###.png'), p)

            p = unislash(directory_to_pattern(Format.percent, td))
            self.assertTrue(p.endswith('/frame%03d.png'), p)

    def test_not_found(self):
        with TemporaryDirectory() as tds:
            td = Path(tds)
            (td / ".DS_Store").touch()
            (td / "thumbs.db").touch()
            with self.assertRaises(PatternNotFoundError):
                directory_to_pattern(Format.hash, td)

    def test_empty_dir(self):
        with TemporaryDirectory() as tds:
            td = Path(tds)
            with self.assertRaises(PatternNotFoundError):
                directory_to_pattern(Format.hash, td)

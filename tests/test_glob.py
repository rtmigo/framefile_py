# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import fnmatch
import unittest

from framefile import hash_pattern_to_glob
from framefile._base import pct_pattern_to_glob

_files = ["anything.png",
          "img0001.png",
          "imgABCD.png",
          "img0002:png",
          "img0003.png",
          "something.jpg"]


class TestHashPatternToGlob(unittest.TestCase):
    def test(self):
        self.assertEqual(fnmatch.filter(_files,
                                        hash_pattern_to_glob("img####.png")),
                         ['img0001.png', 'img0003.png'])

    def test_posix_slashes(self):
        self.assertEqual(
            fnmatch.filter(
                ['/path/to/' + fn for fn in _files],
                hash_pattern_to_glob("/path/to/img####.png")),
            ['/path/to/img0001.png', '/path/to/img0003.png'])

    def test_windows_backslashes(self):
        self.assertEqual(
            fnmatch.filter(
                ["W:\\path\\to\\" + fn for fn in _files],
                hash_pattern_to_glob("W:\\path\\to\\img####.png")),
            ['W:\\path\\to\\img0001.png', 'W:\\path\\to\\img0003.png'])

    def test_fn_match_does_not_recognize_hashes(self):
        self.assertEqual(
            fnmatch.filter(_files, "img####.png"),
            [])


class TestPctPatternToGlob(unittest.TestCase):
    def test(self):
        self.assertEqual(fnmatch.filter(_files,
                                        pct_pattern_to_glob("img%04d.png")),
                         ['img0001.png', 'img0003.png'])

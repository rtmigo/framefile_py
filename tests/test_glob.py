# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import fnmatch
import unittest

from framefile import hash_pattern_to_glob, pct_pattern_to_glob

_files_imgXXXX = ["anything.png",
                  "img0001.png",
                  "imgABCD.png",
                  "img0002:png",
                  "img0003.png",
                  "something.jpg"]

_files_XXXX = ["anything.png",
               "0001.png",
               "ABCD.png",
               "0002:png",
               "0003.png",
               "something.jpg"]


class TestHashPatternToGlob(unittest.TestCase):
    def test(self):
        self.assertEqual(fnmatch.filter(_files_imgXXXX,
                                        hash_pattern_to_glob("img####.png")),
                         ['img0001.png', 'img0003.png'])

    def test_posix_slashes(self):
        self.assertEqual(
            fnmatch.filter(
                ['/path/to/' + fn for fn in _files_imgXXXX],
                hash_pattern_to_glob("/path/to/img####.png")),
            ['/path/to/img0001.png', '/path/to/img0003.png'])

    def test_windows_backslashes(self):
        self.assertEqual(
            fnmatch.filter(
                ["W:\\path\\to\\" + fn for fn in _files_imgXXXX],
                hash_pattern_to_glob("W:\\path\\to\\img####.png")),
            ['W:\\path\\to\\img0001.png', 'W:\\path\\to\\img0003.png'])

    def test_hash_after_backslash_fnmatch(self):
        # this test shows that we do not confuse windows directory separator
        # "\" with escaped hash "\#"

        self.assertEqual(
            fnmatch.filter(
                ["W:\\path\\to\\" + fn for fn in _files_XXXX],
                hash_pattern_to_glob("W:\\path\\to\\####.png")),
            ['W:\\path\\to\\0001.png', 'W:\\path\\to\\0003.png'])

    def test_hash_after_backslash_pattern(self):
        self.assertEqual(
            hash_pattern_to_glob(r"D:\Video\renders\earth\######.png"),
            r'D:\Video\renders\earth\[0-9][0-9][0-9][0-9][0-9][0-9].png')

    def test_fn_match_does_not_recognize_hashes(self):
        self.assertEqual(
            fnmatch.filter(_files_imgXXXX, "img####.png"),
            [])


class TestPctPatternToGlob(unittest.TestCase):
    def test(self):
        self.assertEqual(fnmatch.filter(_files_imgXXXX,
                                        pct_pattern_to_glob("img%04d.png")),
                         ['img0001.png', 'img0003.png'])

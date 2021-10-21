# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT
import os
import unittest

from framefile import filename_to_pct_pattern, filename_to_hash_pattern
from framefile._base import PatternNotFoundError

# todo rewrite with newer functions

def unislash(s):
    if os.name == "nt":
        return s.replace("\\", "/")
    else:
        return s


class TestFilenameToPct(unittest.TestCase):
    def test(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                unislash(filename_to_pct_pattern("/path/to/My-File-8192_00000.exr")),
                "/path/to/My-File-8192_%05d.exr")

            self.assertEqual(
                unislash(filename_to_pct_pattern("/path/to/My-File-8192_00000.exr")),
                "/path/to/My-File-8192_%05d.exr")

    def test_canon_pct(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                unislash(filename_to_pct_pattern("/path/to/IMG_4567.CR2")),
                "/path/to/IMG_%04d.CR2")
            # without the default min_length=2 it did not work
            self.assertEqual(
                unislash(filename_to_pct_pattern("/path/to/IMG_4567.CR2", min_length=1)),
                "/path/to/IMG_4567.CR%01d")

    def test_no_pattern(self):
        with self.assertWarns(DeprecationWarning):
            with self.assertRaises(PatternNotFoundError):
                filename_to_pct_pattern('/path/to/virusX/.DS_Store')

            self.assertEqual(unislash(filename_to_pct_pattern('/path/to/virusX/.DS_Store', min_length=0)),'/path/to/virusX/.DS_Store')


        # self.assertEqual(
        #     ,
        #     '')



class TestHash(unittest.TestCase):

    def test_canon_hash(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                unislash(filename_to_hash_pattern("/path/to/IMG_4567.CR2")),
                "/path/to/IMG_####.CR2")
            # without the default min_length=2 it did not work
            self.assertEqual(
                unislash(filename_to_hash_pattern("/path/to/IMG_4567.CR2", min_length=1)),
                "/path/to/IMG_4567.CR#")

    def test_dirname_ignored(self):
        with self.assertWarns(DeprecationWarning):
            with self.assertRaises(PatternNotFoundError):
                unislash(filename_to_hash_pattern("/path/folder0123/IMG_45.CR2",
                                         min_length=4))
            self.assertEqual(
                unislash(filename_to_hash_pattern("/path/folder0123/IMG_45.CR2",
                                         min_length=2)),
                "/path/folder0123/IMG_##.CR2")

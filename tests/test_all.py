# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import fnmatch
import re
import unittest

from hashdigits import extract_number, PatternMismatchError, pattern_to_glob, \
    NumbersCountError, pattern_to_regex





class TestExtractNumber(unittest.TestCase):
    def test_match(self):
        self.assertEqual(extract_number('file_####.jpg', 'file_1234.jpg'), 1234)
        self.assertEqual(extract_number('file_####.jpg', 'file_0000.jpg'), 0)

    def test_mismatch(self):
        with self.assertRaises(PatternMismatchError):
            extract_number('file_####.jpg', 'file_123.jpg')


class TestHashPatternToGlob(unittest.TestCase):
    def test(self):
        self.assertEqual(fnmatch.filter([
            "anything.png",
            "img0001.png",
            "imgABCD.png",
            "img0002:png",
            "img0003.png",
            "something.jpg"],
            pattern_to_glob("img####.png")
        ),
            ['img0001.png', 'img0003.png'])

    def test_posix_slashes(self):
        self.assertEqual(
            fnmatch.filter([
                "/path/to/anything.png",
                "/path/to/img0001.png",
                "/path/to/imgABCD.png",
                "/path/to/img0002:png",
                "/path/to/img0003.png",
                "/path/to/something.jpg"],
                pattern_to_glob("/path/to/img####.png")
            ),
            ['/path/to/img0001.png', '/path/to/img0003.png'])

    def test_windows_backslashes(self):
        files = [
            "W:\\path\\to\\anything.png",
            "W:\\path\\to\\img0001.png",
            "W:\\path\\to\\imgABCD.png",
            "W:\\path\\to\\img0002:png",
            "W:\\path\\to\\img0003.png",
            "W:\\path\\to\\something.jpg"]
        self.assertEqual(
            fnmatch.filter(
                files,
                pattern_to_glob("W:\\path\\to\\img####.png")),
            ['W:\\path\\to\\img0001.png', 'W:\\path\\to\\img0003.png'])

    def test_fn_match_does_not_recognize_hashes(self):
        self.assertEqual(fnmatch.filter([
            "anything.png",
            "img0001.png",
            "imgABCD.png",
            "img0002:png",
            "img0003.png",
            "something.jpg"],
            "img####.png"
        ),
            [])


class TestHashPatternToRegex(unittest.TestCase):
    def test(self):
        rx = pattern_to_regex('file-####.png')
        with self.subTest("Does not match any string"):
            self.assertIsNone(re.match(rx, "any.png"))
        with self.subTest("Matches exactly four digits:"):
            self.assertIsNone(re.match(rx, "file-543.png"))
        with self.subTest("Dot must be dot:"):
            self.assertIsNone(re.match(rx, "file-5432:png"))

        with self.subTest("The first group is the number sequence:"):
            self.assertEqual(re.match(rx, "file-5432.png").group(1), '5432')

    def test_numbers_count_error_default(self):
        with self.assertRaises(NumbersCountError):
            pattern_to_regex("one####_###.jpg")

    def test_numbers_count_error_need_2_to_3(self):
        with self.assertRaises(NumbersCountError):
            pattern_to_regex("##", min_numbers=2, max_numbers=3)
        with self.assertRaises(NumbersCountError):
            pattern_to_regex("##-##-##-##", min_numbers=2, max_numbers=3)

        pattern_to_regex("##-##", min_numbers=2, max_numbers=3)
        pattern_to_regex("##-##-##", min_numbers=2, max_numbers=3)

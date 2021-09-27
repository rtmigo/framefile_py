# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import fnmatch
import re
import unittest

from hashdigits import DuplicateNumberError, count_matches_from_interval, \
    extract_number, PatternMismatchError, pattern_to_glob, \
    NumbersCountError, pattern_to_regex


class TestCountMatches(unittest.TestCase):
    def test(self):
        pattern = "file-####.png"
        files = [
            "labuda.db",
            "file-0001.png",
            "file-0003.png",
            "file-0004.png",
            "file-0005.png",
            "file-0006.png",
            "anything.jpg",
            "file-0007.png",
            "file-0008.png",
            "file-0009.png",
        ]

        with self.subTest("6,7,8,9 of 6..15"):
            self.assertEqual(
                count_matches_from_interval(pattern, 6, 15, files),
                4)

        with self.subTest("1,3,4 of 1,2,3,4"):
            self.assertEqual(
                count_matches_from_interval(pattern, 1, 4, files),
                3)

        with self.subTest("Modified pattern matches nothing"):
            self.assertEqual(
                count_matches_from_interval(pattern + "z", 6, 15, files),
                0)

    def test_duplicate_number(self):
        with self.assertRaises(DuplicateNumberError):
            count_matches_from_interval("img####.jpg", 6, 15,
                                        ["img0001.jpg",
                                         "img0002.jpg",
                                         "img0002.jpg",
                                         "img0003.jpg"])


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

# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT

from typing import Iterable

from hashdigits import extract_number, PatternMismatchError


class DuplicateNumberError(ValueError):
    pass


def _iter_matches_check_unique(pattern: str,
                               strings: Iterable[str]) -> Iterable[int]:
    found_numbers = set()
    for string in strings:
        try:
            num = extract_number(pattern, string)
            if num in found_numbers:
                raise DuplicateNumberError(f"Number {num} found twice.")
            found_numbers.add(num)
            yield num
        except PatternMismatchError:
            pass


def count_matches_from_interval(
        pattern: str,
        start: int,
        end: int,
        strings: Iterable[str]) -> int:
    return sum(1 for num in _iter_matches_check_unique(pattern, strings)
               if start <= num <= end)
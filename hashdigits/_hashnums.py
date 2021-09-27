import glob
import re
from functools import cache
from typing import Iterable


class NumbersCountError(ValueError):
    pass


class PatternMismatchError(ValueError):
    pass


@cache
def hash_pattern_to_regex(pattern: str,
                          min_numbers: int = 1,
                          max_numbers: int = 1) -> str:
    result = re.escape(pattern)

    result = result.replace(r'\#', '#')

    replacements = 0

    def gen_replacement(match: re.Match) -> str:
        nonlocal replacements
        replacements += 1
        return "(\\d{" + str(match.end() - match.start()) + "})"

    result = re.sub(r'#+', gen_replacement, result, flags=re.MULTILINE)

    if not min_numbers <= replacements <= max_numbers:
        raise NumbersCountError(
            f"Pattern '{pattern}' contains {replacements} numbers.")

    return result


@cache
def hash_pattern_to_glob(pattern: str) -> str:
    result = glob.escape(pattern)
    result = result.replace(r'\#', '#')
    result = result.replace(r'#', '[0-9]')
    return result


def extract_number(pattern: str, text: str) -> int:
    rx = hash_pattern_to_regex(pattern)
    m = re.match(rx, text, flags=re.MULTILINE)
    if m is None:
        raise PatternMismatchError
    return int(m.group(1))


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


def num_matches_from_interval(
        pattern: str,
        start: int,
        end: int,
        strings: Iterable[str]) -> int:
    return sum(1 for num in _iter_matches_check_unique(pattern, strings)
               if start <= num <= end)

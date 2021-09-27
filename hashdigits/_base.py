# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import glob
import re
from functools import lru_cache


class NumbersCountError(ValueError):
    pass


class PatternMismatchError(ValueError):
    pass


@lru_cache()
def pattern_to_regex(pattern: str,
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


@lru_cache()
def pattern_to_glob(pattern: str) -> str:
    result = glob.escape(pattern)
    result = result.replace(r'\#', '#')
    result = result.replace(r'#', '[0-9]')
    return result


def extract_number(pattern: str, text: str) -> int:
    rx = pattern_to_regex(pattern)
    m = re.match(rx, text, flags=re.MULTILINE)
    if m is None:
        raise PatternMismatchError
    return int(m.group(1))



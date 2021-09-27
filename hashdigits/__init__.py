# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT

from ._base import extract_number, PatternMismatchError, pattern_to_glob, \
    pattern_to_regex, NumbersCountError
from ._interval import DuplicateNumberError, num_matches_from_interval

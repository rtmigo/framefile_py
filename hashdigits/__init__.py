# SPDX-FileCopyrightText: (c) 2021 Artyom Galkin <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import warnings

from ._base import extract_number, PatternMismatchError, pattern_to_glob, \
    pattern_to_regex, NumbersCountError
from ._interval import DuplicateNumberError, count_matches_from_interval


def num_matches_from_interval(*args, **kwargs):
    # 2021-09
    warnings.warn("Use count_matches_from_interval", DeprecationWarning)
    return count_matches_from_interval(*args, **kwargs)

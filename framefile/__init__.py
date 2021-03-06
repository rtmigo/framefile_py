# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


from ._base import hash_extract_number, pct_extract_number, \
    PatternMismatchError, PatternNotFoundError, hash_pattern_to_glob, pct_pattern_to_glob, \
    hash_pattern_to_regex, NumbersCountError, pct_to_hash_pattern, pct_pattern_to_regex, \
    is_pattern, Format, directory_to_pattern, filename_to_pattern
from ._deprecated import filename_to_pct_pattern, filename_to_hash_pattern

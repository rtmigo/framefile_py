[![PyPI version shields.io](https://img.shields.io/pypi/v/hashdigits.svg)](https://pypi.python.org/pypi/hashdigits/)
[![Generic badge](https://img.shields.io/badge/Python-3.7+-blue.svg)](#)
[![Generic badge](https://img.shields.io/badge/Tested_on-Windows%20|%20Linux-blue.svg)](#)
[![Downloads](https://pepy.tech/badge/hashdigits/month)](https://pepy.tech/project/hashdigits)

# [hashdigits](https://github.com/rtmigo/hashdigits_py#readme)

Python library for matching file or string patterns like `img-####.jpg`,
where `#` denotes a single digit.

Such patterns are used, for example, for the file names of individual video
frames in  [ffmpeg](https://www.ffmpeg.org/)
and [Blender](https://www.blender.org/).

# Install

```
pip3 install hashdigits
```

<details>
<summary>other options</summary>

#### Install pre-release from GitHub:
```
pip3 install git+https://github.com/rtmigo/hashdigits_py@staging#egg=hashdigits
```

</details>

# Use

## Matching with glob

```python
import glob
import hashdigits

file_mask = hashdigits.pattern_to_glob('/path/to/img####.jpg')

print(glob.glob(file_mask))

# prints all files matching /path/to/img####.jpg
```

## Matching with regular expressions

```python
import re
import hashdigits

regex = hashdigits.pattern_to_regex('img####.jpg')

a = re.match(regex, 'img0023.jpg')
print(a.group(0))  # img0023.jpg
print(a.group(1))  # 0023

b = re.match(regex, 'anything.txt')
print(b)  # None
```

## Extracting integers

```python
import hashdigits

x: int = hashdigits.extract_number("img####.jpg", "img0023.jpg")

print(x)  # 23

try:
    y = hashdigits.extract_number("img####.jpg", "thumbs.db")
except hashdigits.PatternMismatchError:
    print("Oops!")
```



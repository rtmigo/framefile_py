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

# Use

## Matching with glob

```python
import glob
import hashdigits

glob_pattern = hashdigits.hash_pattern_to_glob('img####.jpg')

print(glob.glob('/path/to/' + glob_pattern))

# prints all files matching /path/to/img####.jpg
```

## Matching with regular expressions

```python
import re
import hashdigits

regex_pattern = hashdigits.hash_pattern_to_regex('img####.jpg')

m = re.match(regex_pattern, 'img1234.jpg')

print(m.group(0))  # img1234.jpg
print(m.group(1))  # 1234

```

## Extracting integers

```python
import hashdigits

x: int = hashdigits.extract_number("img####.jpg", "img1234.jpg")

print(x)  # 1234

try:
    y = hashdigits.extract_number("img####.jpg", "thumbs.db")
except hashdigits.PatternMismatchError:
    print("Oops!")
```



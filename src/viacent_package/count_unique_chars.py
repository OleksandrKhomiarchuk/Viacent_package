from collections import Counter
from functools import lru_cache

@lru_cache(maxsize = None)
def counter_unique_chars(input_string: str) -> int:
    if not isinstance(input_string, str):
        raise TypeError("Input must be a str")
    char_count = Counter(input_string)
    return sum(map(lambda x: x == 1, char_count.values()))

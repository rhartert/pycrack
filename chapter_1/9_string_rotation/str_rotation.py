# Answers to question 1.9 "String Rotation".
from dataclasses import dataclass


# Time complexity: O(|s1|).
def str_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s3 = s1+s1
    return s2 in s3


# UNIT TESTS
# ----------

@dataclass
class TCase():
    s1: str
    s2: str
    want: bool


# Each test case is tested symmetrically.
TEST_CASES = [
    TCase("a", "a", True),
    TCase("ab", "ab", True),
    TCase("ab", "ba", True),
    TCase("abc", "bca", True),
    TCase("aabbccdd", "aabbccdd", True),
    TCase("aabbccdd", "bccddaab", True),
]


def test():
    for tc in TEST_CASES:
        assert str_rotation(tc.s1, tc.s2) == tc.want
        assert str_rotation(tc.s2, tc.s1) == tc.want

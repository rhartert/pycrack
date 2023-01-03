# Answers to question 1.5 "One Away".
from dataclasses import dataclass


# Time complexity: O(min(|s1|, |s2|)).
def one_away(s1: str, s2: str):
    if len(s1) == len(s2):
        return one_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_insert(s1, s2)
    if len(s1) == len(s2) + 1:
        return one_insert(s2, s1)

    return False


# This function returns True if the s2 is equal to s1 with a single character
# insert. It assumes that s1 has exactly one character less than s2.
def one_insert(s1, s2) -> bool:
    i2 = 0
    i1 = 0
    while i1 < len(s1):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        elif i2 == i1:
            i2 += 1
        else:
            return False

    return True


# This function returns True if the two string differ by at most one character.
# It assumes that s1 and s2 have the same length.
def one_replace(s1: str, s2: str) -> bool:
    one_diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if one_diff:
                return False
            one_diff = True
    return True


# UNIT TESTS
# ----------

@dataclass
class TCase():
    s1: str
    s2: str
    want: bool


# Each test case is tested symmetrically.
TEST_CASES = [
    TCase("", "", True),
    TCase("", "a", True),
    TCase("a", "a", True),
    TCase("a", "b", True),
    TCase("aa", "aa", True),
    TCase("aa", "ab", True),
    TCase("aa", "baa", True),
    TCase("aa", "aba", True),
    TCase("aa", "aab", True),
    TCase("", "aa", False),
    TCase("a", "aba", False),
    TCase("aa", "bb", False),
    TCase("aaa", "bab", False),
]


def test():
    for tc in TEST_CASES:
        assert one_away(tc.s1, tc.s2) == tc.want
        assert one_away(tc.s2, tc.s1) == tc.want

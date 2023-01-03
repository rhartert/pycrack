# Answers to question 1.2 "Check Permutation".
from collections import Counter
from dataclasses import dataclass


# Time complexity: O(|s1| + |s2|).
def check_perm(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    count = Counter(s1)
    for c in s2:
        if count[c] == 0:
            return False
        count[c] -= 1

    return True


# UNIT TESTS
# ----------

@dataclass
class TCase():
    s1: str
    s2: str
    want: bool


TEST_CASES = [
    TCase("", "", True),
    TCase("a", "a", True),
    TCase("ab", "ab", True),
    TCase("abbcccdddd", "abcdbcdcdd", True),
    TCase("", "a", False),
    TCase("a", "b", False),
    TCase("aa", "ba", False),
    TCase("Ab", "ab", False),
    TCase("abbccc", "abcbcb", False),
]


def test_check_perm():
    for tc in TEST_CASES:
        assert check_perm(tc.s1, tc.s2) == tc.want

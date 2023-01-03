# Answers to question 1.4 "Palindrome Permutation".
from collections import Counter
from dataclasses import dataclass


# Time complexity: O(|s|).
def palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True

    counter = Counter(s)

    found_odd = False
    for c in counter:
        n = counter[c]
        if n & 1 == 1:  # odd
            if found_odd:
                return False
            found_odd = True

    return True


# This function assumes that the string only contains letters from a to z. It 
# doesn't improve the time complexity but might be faster than the above 
# implementation in practice.
#
# Time complexity: O(|s|).
def palindrome_bit(s: str) -> bool:
    if len(s) <= 1:
        return True

    # bit vector representing whether char i is odd (1) or not (0). 
    is_odd = 0

    for c in s:
        # Flip the bit corresponding to char c.
        is_odd = is_odd ^ (1 << to_int(c))

    # Check that there is at most one bit set to 1.
    if is_odd & (is_odd - 1) == 0:
        return True

    return False


# Map char to an int so that 'a' is mapped to 0, 'b' to 1, and so on.
def to_int(char: str) -> int:
    return ord(char) - ord("a")


# UNIT TESTS
# ----------

@dataclass
class TCase():
    string: str
    want: bool


TEST_CASES = [
    TCase("", True),
    TCase("a", True),
    TCase("aa", True),
    TCase("bba", True),
    TCase("aabb", True),
    TCase("abbac", True),
    TCase("ab", False),
    TCase("abc", False),
    TCase("abbb", False),
    TCase("abcb", False),
]


def test_check_perm():
    for tc in TEST_CASES:
        assert palindrome(tc.string) == tc.want
        assert palindrome_bit(tc.string) == tc.want

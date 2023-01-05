# Answers to question 1.4 "Palindrome Permutation".
from collections import Counter
import unittest


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


class Test(unittest.TestCase):
    test_cases = [
        ("", True),
        ("a", True),
        ("aa", True),
        ("bba", True),
        ("aabb", True),
        ("abbac", True),
        ("ab", False),
        ("abc", False),
        ("abbb", False),
        ("abcb", False),
    ]

    def test(self):
        for s, want in self.test_cases:
            assert palindrome(s) == want
            assert palindrome_bit(s) == want


if __name__ == "__main__":
    unittest.main()

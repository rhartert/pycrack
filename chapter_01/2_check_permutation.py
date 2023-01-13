# Answers to question 1.2 "Check Permutation".
import unittest
from collections import Counter


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


class Test(unittest.TestCase):
    test_cases = [
        ("", "", True),
        ("a", "a", True),
        ("ab", "ab", True),
        ("abbcccdddd", "abcdbcdcdd", True),
        ("", "a", False),
        ("a", "b", False),
        ("aa", "ba", False),
        ("Ab", "ab", False),
        ("abbccc", "abcbcb", False),
    ]

    def test(self):
        for s1, s2, want in self.test_cases:
            assert check_perm(s1, s2) == want


if __name__ == "__main__":
    unittest.main()

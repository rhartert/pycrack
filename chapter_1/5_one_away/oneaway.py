# Answers to question 1.5 "One Away".
import unittest


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


class Test(unittest.TestCase):
    test_cases = [
        ("", "", True),
        ("", "a", True),
        ("a", "a", True),
        ("a", "b", True),
        ("aa", "aa", True),
        ("aa", "ab", True),
        ("aa", "baa", True),
        ("aa", "aba", True),
        ("aa", "aab", True),
        ("", "aa", False),
        ("a", "aba", False),
        ("aa", "bb", False),
        ("aaa", "bab", False),
    ]

    def test(self):
        for s1, s2, want in self.test_cases:
            assert one_away(s1, s2) == want
            assert one_away(s2, s1) == want


if __name__ == "__main__":
    unittest.main()

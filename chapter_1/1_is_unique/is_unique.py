# Answers to question 1.1 "Is Unique".
import unittest

# This function assumes a finite alphabet of 128 characters.
#
# Time complexity: O(min(|s|, |alphabet|)).
def is_unique_ascii(s: str) -> bool:
    if len(s) > 128:
        return False

    seen = [False for _ in range(128)]
    for c in s:
        if seen[ord(c)]:
            return False
        seen[ord(c)] = True

    return True


# This function assumes that the alphabet in which the string is being
# written is potentially infinite.
#
# Time complexity: O(|s|)
def is_unique(s: str) -> bool:
    seen = {}
    for c in s:
        if c in seen:
            return False
        seen[c] = True

    return True


# This function assumes that no additional structure can be used.
#
# Time complexity: O(|s|^2)
def is_unique_no_struct(s: str) -> bool:
    # Strings are immutable in Python so sorting the string and checking
    # for adjacent equivalent characters is not an option.
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("", True),
        ("a", True),
        ("abc", True),
        ("aa", False),
        ("abcde123a", False),
        ("123abcd3", False),
        ("a b c", False),
        ("a\tb\tc", False),
    ]

    def test(self):
        for s, want in self.test_cases:
            assert is_unique(s) == want
            assert is_unique_ascii(s) == want
            assert is_unique_no_struct(s) == want


if __name__ == "__main__":
    unittest.main()

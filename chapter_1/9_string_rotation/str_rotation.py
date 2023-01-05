# Answers to question 1.9 "String Rotation".
import unittest


# Time complexity: O(|s1|).
def str_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s3 = s1 + s1
    return s2 in s3


class Test(unittest.TestCase):
    test_cases = [
        ("a", "a", True),
        ("ab", "ab", True),
        ("ab", "ba", True),
        ("abc", "bca", True),
        ("aabbccdd", "aabbccdd", True),
        ("aabbccdd", "bccddaab", True),
    ]

    def test(self):
        for s1, s2, want in self.test_cases:
            assert str_rotation(s1, s2) == want
            assert str_rotation(s2, s1) == want


if __name__ == "__main__":
    unittest.main()

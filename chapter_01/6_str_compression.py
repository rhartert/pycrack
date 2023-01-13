# Answers to question 1.6 "String Compression".
import unittest


# Simple implementation of a "Java-like" StringBuffer.
class StringBuffer:
    def __init__(self):
        self._buffer = []
        self._size = 0

    def append(self, s: str):
        self._buffer.append(s)
        self._size += len(s)

    def string(self) -> str:
        return "".join(self._buffer)

    def __len__(self):
        return self._size

    def __str__(self):
        return self.string()


# Time complexity: O(|s|).
def compress(s: str) -> str:
    if len(s) <= 2:
        return s

    # Buffer to contain the compressed string.
    sb = StringBuffer()

    count = 0
    for i in range(len(s)):
        count += 1
        if i + 1 == len(s) or s[i] != s[i + 1]:
            sb.append(s[i])
            sb.append(str(count))
            count = 0  # reset the counter

    if len(sb) >= len(s):
        return s

    return sb.string()


class Test(unittest.TestCase):
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("aa", "aa"),
        ("ab", "ab"),
        ("aaa", "a3"),
        ("abcd", "abcd"),
        ("aabbccdd", "aabbccdd"),
        ("aaabbcccd", "a3b2c3d1"),
        ("aabccccaaa", "a2b1c4a3"),
    ]

    def test(self):
        for s, want in self.test_cases:
            assert compress(s) == want


if __name__ == "__main__":
    unittest.main()

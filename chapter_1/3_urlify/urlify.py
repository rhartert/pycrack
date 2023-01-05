# Answers to question 1.3 "URLify".
import unittest


# The function accepts a list of characters so that the operation can be
# performed inplace.
#
# Time complexity: O(|s|).
def urlify(s: list[str], length: int):
    if length <= 1:
        return

    n_spaces = 0
    for i in range(length):
        if s[i] == " ":
            n_spaces += 1

    if n_spaces == 0:
        return

    j = length + 2 * n_spaces - 1
    for i in range(length - 1, -1, -1):
        if s[i] != " ":
            s[j] = s[i]
            j -= 1
        else:
            s[j] = "0"
            s[j - 1] = "2"
            s[j - 2] = "%"
            j -= 3


class Test(unittest.TestCase):
    test_cases = [
        (list("   "), 0, list("   ")),
        (list("a   "), 1, list("a   ")),
        (list("a b  "), 3, list("a%20b")),
        (list(" ab  "), 3, list("%20ab")),
        (list(" a b    "), 4, list("%20a%20b")),
        (list(" a b      "), 4, list("%20a%20b  ")),
    ]

    def test(self):
        for string, length, want in self.test_cases:
            urlify(string, length)  # inplace
            assert "".join(string) == "".join(want)


if __name__ == "__main__":
    unittest.main()

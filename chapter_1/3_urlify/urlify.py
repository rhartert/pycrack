# Answers to question 1.3 "URLify".
from dataclasses import dataclass


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

    j = length + 2*n_spaces - 1
    for i in range(length - 1, -1, -1):
        if s[i] != " ":
            s[j] = s[i]
            j -= 1
        else:
            s[j] = "0"
            s[j-1] = "2"
            s[j-2] = "%"
            j -= 3


# UNIT TESTS
# ----------

@dataclass
class TCase():
    string: list[str]
    length: int
    want: list[str]


TEST_CASES = [
    TCase(list("   "), 0, list("   ")),
    TCase(list("a   "), 1, list("a   ")),
    TCase(list("a b  "), 3, list("a%20b")),
    TCase(list(" ab  "), 3, list("%20ab")),
    TCase(list(" a b    "), 4, list("%20a%20b")),
    TCase(list(" a b      "), 4, list("%20a%20b  ")),
]


def test():
    for tc in TEST_CASES:
        urlify(tc.string, tc.length)  # inplace
        assert ''.join(tc.string) == ''.join(tc.want)

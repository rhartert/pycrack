# Answers to question 17.1 "Addition without Plus".
import unittest


def add(a: int, b: int) -> int:
    sum = a
    rest = b

    while rest != 0:
        tmp = sum ^ rest
        rest = (sum & rest) << 1
        sum = tmp

    return sum


def add_recursive(a: int, b: int) -> int:
    if b == 0:
        return a
    sum = a ^ b
    rest = (a & b) << 1
    return add_recursive(sum, rest)


class Test(unittest.TestCase):
    def test(self):
        for a in range(101):
            for b in range(101):
                want = a + b
                assert add(a, b) == want
                assert add_recursive(a, b) == want


if __name__ == "__main__":
    unittest.main()

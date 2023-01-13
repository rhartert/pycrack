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


class Test(unittest.TestCase):
    def test(self):
        for a in range(101):
            for b in range(101):
                want = a + b
                assert add(a, b) == want


if __name__ == "__main__":
    unittest.main()

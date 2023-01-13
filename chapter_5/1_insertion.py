# Answers to question 5.1 "Insertion".
import unittest


def insert(a: int, b: int, i: int, j: int) -> int:
    b_length = j - i + 1
    b_mask = (1 << b_length) - 1
    join = a & ~(b_mask << i)
    join = join | (b << i)
    return join


class Test(unittest.TestCase):
    test_cases = [
        (0b10000000000, 0, 5, 5, 0b10000000000),
        (0b10000000000, 1, 5, 5, 0b10000100000),
        (0b10000000000, 0, 1, 10, 0),
        (0b10000000000, 0b10011, 0, 4, 0b10000010011),
        (0b10000000000, 0b10011, 1, 5, 0b10000100110),
        (0b10000000000, 0b10011, 2, 6, 0b10001001100),
        (0b10000000000, 0b10011, 3, 7, 0b10010011000),
        (0b10000000000, 0b10011, 4, 8, 0b10100110000),
        (0b10000000000, 0b10011, 5, 9, 0b11001100000),
        (0b10000000000, 0b10011, 6, 10, 0b10011000000),
    ]

    def test(self):
        for a, b, i, j, want in self.test_cases:
            assert insert(a, b, i, j) == want


if __name__ == "__main__":
    unittest.main()

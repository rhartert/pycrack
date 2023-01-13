# Answers to question 1.8 "Zero Matrix".
import unittest


# This function assumes that the given matrix is NxM.
#
# Time complexity: O(N*M).
def zero(matrix: list[list[int]]):
    n_rows = len(matrix)
    n_columns = len(matrix[0])

    zero_rows = [False for _ in range(n_rows)]
    zero_columns = [False for _ in range(n_columns)]

    for r in range(n_rows):
        for c in range(n_columns):
            if matrix[r][c] == 0:
                zero_rows[r] = True
                zero_columns[c] = True

    for r in range(n_rows):
        if zero_rows[r]:
            for c in range(n_columns):
                matrix[r][c] = 0

    for c in range(n_columns):
        if zero_columns[c]:
            for r in range(n_rows):
                matrix[r][c] = 0


class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1],
            ],
            [
                [1],
            ],
        ),
        (
            [
                [0],
            ],
            [
                [0],
            ],
        ),
        (
            [
                [1, 2],
                [2, 3],
            ],
            [
                [1, 2],
                [2, 3],
            ],
        ),
        (
            [
                [1, 2],
                [2, 0],
            ],
            [
                [1, 0],
                [0, 0],
            ],
        ),
        (
            [
                [0, 2],
                [2, 0],
            ],
            [
                [0, 0],
                [0, 0],
            ],
        ),
        (
            [
                [0, 2, 0],
                [2, 1, 2],
            ],
            [
                [0, 0, 0],
                [0, 1, 0],
            ],
        ),
        (
            [
                [0, 2, 0],
                [2, 1, 2],
                [3, 3, 3],
            ],
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 3, 0],
            ],
        ),
        (
            [
                [0, 2, 3],
                [2, 1, 2],
                [3, 3, 0],
            ],
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
            ],
        ),
        (
            [
                [1, 2, 3],
                [2, 0, 2],
                [3, 3, 3],
            ],
            [
                [1, 0, 3],
                [0, 0, 0],
                [3, 0, 3],
            ],
        ),
    ]

    def test(self):
        for matrix, want in self.test_cases:
            zero(matrix)  # inplace
            assert matrix == want


if __name__ == "__main__":
    unittest.main()

# Answers to question 1.7 "Rotate Matrix".
import unittest


# This function assumes that the given matrix is NxN.
#
# Time complexity: O(N^2).
def rotate(matrix: list[list[int]]):
    n = len(matrix)
    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer
        for i in range(last - first):
            top = matrix[first][last - i]
            # Top <- Left
            matrix[first][last - i] = matrix[first + i][first]
            # Left <- Bottom
            matrix[first + i][first] = matrix[last][first + i]
            # Bottom <- Right
            matrix[last][first + i] = matrix[last - i][last]
            # Right <- Top
            matrix[last - i][last] = top


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
                [1, 2],
                [4, 3],
            ],
            [
                [4, 1],
                [3, 2],
            ],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
            ],
        ),
        (
            [
                [1, 2, 2, 2],
                [1, 5, 6, 3],
                [1, 8, 7, 3],
                [4, 4, 4, 3],
            ],
            [
                [4, 1, 1, 1],
                [4, 8, 5, 2],
                [4, 7, 6, 2],
                [3, 3, 3, 2],
            ],
        ),
        (
            [
                [1, 2, 2, 2, 2],
                [1, 5, 5, 6, 3],
                [1, 8, 9, 6, 3],
                [1, 8, 7, 7, 3],
                [4, 4, 4, 4, 3],
            ],
            [
                [4, 1, 1, 1, 1],
                [4, 8, 8, 5, 2],
                [4, 7, 9, 5, 2],
                [4, 7, 6, 6, 2],
                [3, 3, 3, 3, 2],
            ],
        ),
    ]

    def test(self):
        for matrix, want in self.test_cases:
            rotate(matrix)  # inplace
            assert matrix == want


if __name__ == "__main__":
    unittest.main()

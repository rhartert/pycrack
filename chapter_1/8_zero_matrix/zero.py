# Answers to question 1.8 "Zero Matrix".
from dataclasses import dataclass


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


# UNIT TESTS
# ----------

@dataclass
class TCase():
    matrix: list[list[int]]
    want: list[list[int]]


TEST_CASES = [
    TCase(
        matrix=[
            [1],
        ],
        want=[
            [1],
        ]
    ),
    TCase(
        matrix=[
            [0],
        ],
        want=[
            [0],
        ]
    ),
    TCase(
        matrix=[
            [1, 2],
            [2, 3],
        ],
        want=[
            [1, 2],
            [2, 3],
        ],
    ),
    TCase(
        matrix=[
            [1, 2],
            [2, 0],
        ],
        want=[
            [1, 0],
            [0, 0],
        ],
    ),
    TCase(
        matrix=[
            [0, 2],
            [2, 0],
        ],
        want=[
            [0, 0],
            [0, 0],
        ],
    ),
    TCase(
        matrix=[
            [0, 2, 0],
            [2, 1, 2],
        ],
        want=[
            [0, 0, 0],
            [0, 1, 0],
        ],
    ),
    TCase(
        matrix=[
            [0, 2, 0],
            [2, 1, 2],
            [3, 3, 3]
        ],
        want=[
            [0, 0, 0],
            [0, 1, 0],
            [0, 3, 0]
        ],
    ),
    TCase(
        matrix=[
            [0, 2, 3],
            [2, 1, 2],
            [3, 3, 0]
        ],
        want=[
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
    ),
    TCase(
        matrix=[
            [1, 2, 3],
            [2, 0, 2],
            [3, 3, 3]
        ],
        want=[
            [1, 0, 3],
            [0, 0, 0],
            [3, 0, 3]
        ],
    ),
]


def test():
    for tc in TEST_CASES:
        zero(tc.matrix)  # inplace
        assert tc.matrix == tc.want

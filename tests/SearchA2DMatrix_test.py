import pytest
from prac.SearchA2DMatrix import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "matrix,target,expected",
    [
        # leetcode-style example (rows sorted, first of row > last of prev)
        (
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            3,
            True,
        ),
        (
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            13,
            False,
        ),
        # first and last elements
        ([[1, 2, 3, 4]], 1, True),
        ([[1, 2, 3, 4]], 4, True),
        ([[1, 2, 3, 4]], 5, False),
        # single column
        ([[2], [5], [9], [12]], 9, True),
        ([[2], [5], [9], [12]], 7, False),
        # negatives + non-decreasing rows
        ([[-10, -4, -1], [0, 2, 2], [3, 9, 15]], -4, True),
        ([[-10, -4, -1], [0, 2, 2], [3, 9, 15]], 8, False),
        # one row, one col
        ([[42]], 42, True),
        ([[42]], 41, False),
    ],
)
def test_search_matrix(sol, matrix, target, expected):
    assert sol.searchMatrix(matrix, target) is expected


def test_get_linear_index(sol):
    """
    sanity-check the linear indexer against a 2x4 grid:
    0 1 2 3
    4 5 6 7
    """
    m = [[0, 1, 2, 3], [4, 5, 6, 7]]
    assert sol.get(m, 0) == 0
    assert sol.get(m, 3) == 3
    assert sol.get(m, 4) == 4
    assert sol.get(m, 7) == 7


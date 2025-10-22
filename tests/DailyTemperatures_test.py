# tests/DailyTemperatures_test.py
import pytest
from prac.DailyTemperatures import Solution

@pytest.fixture
def S():
    return Solution()

@pytest.mark.parametrize(
    "temps,expected,case_id",
    [
        ([30, 38, 30, 36, 35, 40, 28], [1, 4, 1, 2, 1, 0, 0], "example_mixed"),
        ([22, 21, 20], [0, 0, 0], "example_descending"),
        ([30], [0], "single_day"),
        ([30, 31], [1, 0], "simple_increase"),
        ([31, 30], [0, 0], "simple_decrease"),
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0], "classic_leetcode"),
        ([40, 40, 40], [0, 0, 0], "no_warmer_duplicates"),
    ],
    ids=lambda param: param[-1],
)
def test_daily_temperatures(S, temps, expected, case_id):
    assert S.dailyTemperatures(temps) == expected

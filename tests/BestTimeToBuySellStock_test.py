import pytest
from typing import List
from prac.BestTimeToBuySellStock import Solution

solution = Solution()

def test_example_1():
    prices = [7,1,5,3,6,4]
    assert solution.maxProfit(prices) == 5

def test_no_profit():
    prices = [7,6,4,3,1]
    assert solution.maxProfit(prices) == 0

def test_empty_list():
    prices = []
    assert solution.maxProfit(prices) == 0

def test_single_day():
    prices = [5]
    assert solution.maxProfit(prices) == 0

def test_increasing_prices():
    prices = [1,2,3,4,5]
    assert solution.maxProfit(prices) == 4

def test_decreasing_then_increasing():
    prices = [3,2,6,5,0,3]
    assert solution.maxProfit(prices) == 4 # Buy at 2, sell at 6

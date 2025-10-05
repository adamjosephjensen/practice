# tests/GenerateParentheses_test.py
# You are given an integer n. Return all well-formed parentheses strings
# that you can generate with n pairs of parentheses.
# You may return the answer in any order.
# Constraints: 1 <= n <= 7

from typing import List
import pytest

from prac.GenerateParentheses import Solution

@pytest.fixture
def S():
    return Solution()

def test_n_1(S):
    assert sorted(S.generateParentheses(1)) == sorted(["()"])

def test_n_2(S):
    actual = S.generateParentheses(2)
    expected = ["()()","(())"]
    assert sorted(actual) == sorted(expected)

def test_n_3(S):
    actual = S.generateParentheses(3)
    expected = ["((()))","(()())","(())()","()(())","()()()"] 
    assert sorted(actual) == sorted(expected)

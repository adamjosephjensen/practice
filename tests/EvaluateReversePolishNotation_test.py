# tests/EvaluateReversePolishNotation_test.py
import pytest

from prac.EvaluateReversePolishNotation import Solution

@pytest.fixture
def S():
    """
    You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

    Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.
    """
    return Solution()

def test_nop(S):
    tokens = ["42"]
    output = S.evalRPN(tokens)
    assert output == 42

def test_addition(S):
    tokens = ["2", "3", "+"]
    output = S.evalRPN(tokens)
    assert output == 5

def test_subtraction(S):
    tokens = ["5", "1", "-"]
    output = S.evalRPN(tokens)
    assert output == 4

def test_multiplication(S):
    tokens = ["21", "2", "*"]
    output = S.evalRPN(tokens)
    assert output == 42

def test_division(S):
    """
    make sure division truncates towards zero
    """
    tokens = ["7", "-2", "/"]
    output = S.evalRPN(tokens)
    assert output == -3

def test_two_steps(S):
    """
    (1 + 2) + 1 = 4
    """
    tokens = ["1","2","+","1","+"]


def test_longer_strings(S):
    """
    Explanation: ((1 + 2) * 3) - 4 = 5
    """
    tokens = ["1","2","+","3","*","4","-"]
    output = S.evalRPN(tokens)
    assert output == 5

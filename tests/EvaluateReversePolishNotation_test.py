# tests/EvaluateReversePolishNotation_test.py
import pytest

from prac.EvaluateReversePolishNotation import Solution

@pytest.fixture
def S():
    return Solution()

# ---- no ops ----------------------------------------------------
def test_empty(S):
    assert S.evalRPN([]) == None

def test_nop(S):
    assert S.evalRPN(["42"]) == 42

# ---- individual ops ----------------------------------------------------

_add_cases = [
    (["2", "3", "+"], 5, "add_pos"),
    (["-2", "-3", "+"], -5, "add_neg"),
    (["-2", "3", "+"], 1, "add_mixed"),
]

@pytest.mark.parametrize("case", _add_cases, ids=lambda c: c[-1])
def test_addition(S, case):
    tokens, expected, _ = case
    assert S.evalRPN(tokens) == expected


_sub_cases = [
    (["5", "1", "-"], 4, "sub_pos_gt"),
    (["1", "5", "-"], -4, "sub_pos_lt"),
    (["-5", "-1", "-"], -4, "sub_neg_minus_neg"),
    (["-5", "1", "-"], -6, "sub_neg_minus_pos"),
]

@pytest.mark.parametrize("case", _sub_cases, ids=lambda c: c[-1])
def test_subtraction(S, case):
    tokens, expected, _ = case
    assert S.evalRPN(tokens) == expected


_mul_cases = [
    (["4", "3", "*"], 12, "mul_pos"),
    (["-4", "3", "*"], -12, "mul_neg_pos"),
    (["-4", "-3", "*"], 12, "mul_neg_neg"),
    (["0", "999", "*"], 0, "mul_zero"),
]

@pytest.mark.parametrize("case", _mul_cases, ids=lambda c: c[-1])
def test_multiplication(S, case):
    tokens, expected, _ = case
    assert S.evalRPN(tokens) == expected


_div_cases = [
    (["7", "3", "/"], 2, "div_pos"),
    (["-7", "3", "/"], -2, "div_neg_pos_trunc_toward_zero"),
    (["7", "-3", "/"], -2, "div_pos_neg_trunc_toward_zero"),
    (["-7", "-3", "/"], 2, "div_neg_neg"),
    (["1", "2", "/"], 0, "div_small_to_zero"),
]

@pytest.mark.parametrize("case", _div_cases, ids=lambda c: c[-1])
def test_division_trunc_toward_zero(S, case):
    tokens, expected, _ = case
    assert S.evalRPN(tokens) == expected


# ---- mixed / integration cases ----------------------------------------------

_mixed_cases = [
    (["2", "1", "+", "3", "*"], 9, "mix_add_then_mul"),
    (["4", "13", "5", "/", "+"], 6, "mix_div_then_add"),
    (
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
        22,
        "mix_big_leetcode"
    ),
]

@pytest.mark.parametrize("case", _mixed_cases, ids=lambda c: c[-1])
def test_mixed_expressions(S, case):
    tokens, expected, _ = case
    assert S.evalRPN(tokens) == expected

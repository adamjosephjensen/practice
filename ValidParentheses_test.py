import pytest
from ValidParentheses import Solution

solution = Solution()

def test_empty_string():
    assert solution.isValid("") == True

def test_simple_valid():
    assert solution.isValid("()") == True
    assert solution.isValid("[]") == True
    assert solution.isValid("{}") == True

def test_nested_valid():
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("{[]}") == True
    assert solution.isValid("([{}])") == True

def test_simple_invalid_mismatch():
    assert solution.isValid("(]") == False
    assert solution.isValid("{)") == False

def test_simple_invalid_unclosed():
    assert solution.isValid("(") == False
    assert solution.isValid("[") == False
    assert solution.isValid("{") == False

def test_simple_invalid_unopened():
    assert solution.isValid(")") == False
    assert solution.isValid("]") == False
    assert solution.isValid("}") == False

def test_complex_invalid():
    assert solution.isValid("([)]") == False
    assert solution.isValid("(((((((((()") == False
    assert solution.isValid("())({}}{()][][") == False

def test_valid_longer():
    assert solution.isValid("((()))") == True
    assert solution.isValid("[[([])]]") == True

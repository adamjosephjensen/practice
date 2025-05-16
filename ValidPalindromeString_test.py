import pytest
from ValidPalindromeString import Solution

solution = Solution()

def test_example_1():
    s = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s) == True

def test_example_2():
    s = "race a car"
    assert solution.isPalindrome(s) == False

def test_empty_string():
    s = ""
    assert solution.isPalindrome(s) == True # Considered a valid palindrome

def test_single_char_string():
    s = "a"
    assert solution.isPalindrome(s) == True

def test_non_alphanumeric():
    s = ",."
    assert solution.isPalindrome(s) == True

def test_simple_palindrome():
    s = "madam"
    assert solution.isPalindrome(s) == True

def test_simple_non_palindrome():
    s = "hello"
    assert solution.isPalindrome(s) == False

def test_mixed_case():
    s = "RaceCar"
    assert solution.isPalindrome(s) == True

import pytest
from ValidAnagram import Solution

solution = Solution()

def test_example_1():
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t) == True

def test_example_2():
    s = "rat"
    t = "car"
    assert solution.isAnagram(s, t) == False

def test_different_lengths():
    s = "a"
    t = "ab"
    assert solution.isAnagram(s, t) == False

def test_empty_strings():
    s = ""
    t = ""
    assert solution.isAnagram(s, t) == True

def test_one_empty_one_not():
    s = "a"
    t = ""
    assert solution.isAnagram(s, t) == False

def test_same_chars_different_counts():
    s = "aab"
    t = "abb"
    assert solution.isAnagram(s, t) == False

def test_unicode_chars(): # Assuming ASCII, but good to consider
    s = "你好"
    t = "好你"
    assert solution.isAnagram(s, t) == True

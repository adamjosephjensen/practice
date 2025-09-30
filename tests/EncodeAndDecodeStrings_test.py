import pytest
from typing import List # Ensure List is imported if needed by tests
from prac.EncodeAndDecodeStrings import Solution

# Test none, one, many, delim
def test_encoding_none():
    solution = Solution()
    s = ""
    r = solution.encode([s])
    assert r == "0||"

def test_encoding_one():
    solution = Solution()
    s = "hello"
    r = solution.encode([s])
    assert r == "5||hello"

def test_encoding_many():
    solution = Solution()
    s = ["hello", "world"]
    r = solution.encode(s)
    assert r == "5||hello5||world" 

def test_decoding_none():
    solution = Solution()
    encoded_s = "0||"
    expected_s_list = [""]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_decoding_one():
    solution = Solution()
    encoded_s = "5||hello"
    expected_s_list = ["hello"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_decoding_many():
    solution = Solution()
    encoded_s = "5||hello5||world"
    expected_s_list = ["hello", "world"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_encoding_special_chars_single_string():
    solution = Solution()
    s = ["!@#$%^&*()"]
    r = solution.encode(s)
    assert r == "10||!@#$%^&*()"

def test_decoding_special_chars_single_string():
    solution = Solution()
    encoded_s = "10||!@#$%^&*()"
    expected_s_list = ["!@#$%^&*()"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_encoding_special_chars_multiple_strings():
    solution = Solution()
    s = ["we","say",":","yes","!@#$%^&*()"]
    r = solution.encode(s)
    assert r == "2||we3||say1||:3||yes10||!@#$%^&*()"

def test_decoding_special_chars_multiple_strings():
    solution = Solution()
    encoded_s = "2||we3||say1||:3||yes10||!@#$%^&*()"
    expected_s_list = ["we","say",":","yes","!@#$%^&*()"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

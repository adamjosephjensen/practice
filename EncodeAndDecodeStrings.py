from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings into a single string with length||string format."""
        return ''.join(f'{len(s)}||{s}' for s in strs)

    def decode(self, encoded: str) -> List[str]:
        """Decodes a string in length||string format into a list of strings."""
        result = []
        i = 0
        while i < len(encoded):
            j = encoded.find('||', i)
            if j == -1:
                raise ValueError("Invalid encoded string")
            length = int(encoded[i:j])
            result.append(encoded[j+2:j+2+length])
            i = j + 2 + length
        return result


import pytest

# Test none, one, many, delim
def test_encoding_none():
    solution = Solution()
    s = ""
    r = solution.encode([s])
    assert r == "0||" # Corrected typo: was `assert r = "|0"`

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

def test_decoding_one(): # Corrected function name
    solution = Solution()
    encoded_s = "5||hello"
    expected_s_list = ["hello"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_decoding_many(): # Corrected function name
    solution = Solution()
    encoded_s = "5||hello5||world"
    expected_s_list = ["hello", "world"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_encoding_special_chars_single_string():
    solution = Solution()
    s = ["!@#$%^&*()"]
    r = solution.encode(s)
    # Length of "!@#$%^&*()" is 10
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
    # Lengths: "we" (2), "say" (3), ":" (1), "yes" (3), "!@#$%^&*()" (10)
    assert r == "2||we3||say1||:3||yes10||!@#$%^&*()"

def test_decoding_special_chars_multiple_strings():
    solution = Solution()
    encoded_s = "2||we3||say1||:3||yes10||!@#$%^&*()"
    expected_s_list = ["we","say",":","yes","!@#$%^&*()"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings into a single string.
        Each string is preceded by its length and a '||' delimiter.
        Format: length1||STRING1length2||STRING2...
        """
        encoding = ""
        for s_item in strs:
            encoding += str(len(s_item)) + "||"
            encoding += s_item
        return encoding

    def decode(self, s: str) -> List[str]:
        """Decodes a single string into a list of strings.
        The input string is expected to be in the format: length1||STRING1length2||STRING2...
        where 'lengthX' is the numerical length of 'STRINGX'.
        Example: "5||hello10||helloworld" decodes to ["hello", "helloworld"]
        "0||" decodes to [""] (representing an empty string in the list if encoded as 0||)
        """
        decoding = []
        p = 0  # Pointer to the start of the current length segment
        while p < len(s):
            delimiter_pos = s.find("||", p)
            if delimiter_pos == -1:
                # This case should ideally not happen if the input string is always valid
                # and was produced by the corresponding encode method.
                # If it can happen, error handling or specific behavior might be needed.
                break 
            
            length_str = s[p:delimiter_pos]
            length = int(length_str)
            
            string_start_idx = delimiter_pos + 2  # Move past "||"
            
            word = s[string_start_idx : string_start_idx + length]
            decoding.append(word)
            
            p = string_start_idx + length # Move to the start of the next length segment
            
        return decoding


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

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """ prepend |n before each string where n is the length
        of the string
        """
        encoding = ""
        for s in strs:
            encoding += "|" + str(len(s))
            encoding += s

        return encoding

    def decode(self, s: str) -> List[str]:
        """Decodes a single string into a list of strings.
        The input string is expected to be in the format: |length1STRING1|length2STRING2...
        where 'lengthX' is the numerical length of 'STRINGX'.
        Example: "|5hello|10helloworld" decodes to ["hello", "helloworld"]
        "|0" decodes to [""] (representing an empty string in the list if encoded as |0)
        """
        p = 0 # current position, should be at a '|'
        decoding = []
        while p < len(s):
            # p is at the '|'
            idx_after_pipe = p + 1
            
            # Find where the digits for the length end.
            # The actual string starts immediately after these digits.
            start_of_string_idx = idx_after_pipe 
            while start_of_string_idx < len(s) and s[start_of_string_idx].isdigit():
                start_of_string_idx += 1
            
            length_str = s[idx_after_pipe : start_of_string_idx]
            length = int(length_str)
            
            # The actual string is s[start_of_string_idx : start_of_string_idx + length]
            word = s[start_of_string_idx : start_of_string_idx + length]
            decoding.append(word)
            
            # Move p to the beginning of the next segment (i.e., the next '|')
            p = start_of_string_idx + length
            
        return decoding


import pytest

# Test none, one, many, delim
def test_encoding_none():
    solution = Solution()
    s = ""
    r = solution.encode([s])
    assert r == "|0" # Corrected typo: was `assert r = "|0"`

def test_encoding_one():
    solution = Solution()
    s = "hello"
    r = solution.encode([s])
    assert r == "|5hello"

def test_encoding_many():
    solution = Solution()
    s = ["hello", "world"]
    r = solution.encode(s)
    assert r == "|5hello|5world" 

def test_decoding_none():
    solution = Solution()
    encoded_s = "|0"
    expected_s_list = [""]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_decoding_one(): # Corrected function name
    solution = Solution()
    encoded_s = "|5hello"
    expected_s_list = ["hello"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_decoding_many(): # Corrected function name
    solution = Solution()
    encoded_s = "|5hello|5world"
    expected_s_list = ["hello", "world"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_encoding_special_chars_single_string():
    solution = Solution()
    s = ["!@#$%^&*()"]
    r = solution.encode(s)
    # Length of "!@#$%^&*()" is 10
    assert r == "|10!@#$%^&*()"

def test_decoding_special_chars_single_string():
    solution = Solution()
    encoded_s = "|10!@#$%^&*()"
    expected_s_list = ["!@#$%^&*()"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

def test_encoding_special_chars_multiple_strings():
    solution = Solution()
    s = ["we","say",":","yes","!@#$%^&*()"]
    r = solution.encode(s)
    # Lengths: "we" (2), "say" (3), ":" (1), "yes" (3), "!@#$%^&*()" (10)
    assert r == "|2we|3say|1:|3yes|10!@#$%^&*()"

def test_decoding_special_chars_multiple_strings():
    solution = Solution()
    encoded_s = "|2we|3say|1:|3yes|10!@#$%^&*()"
    expected_s_list = ["we","say",":","yes","!@#$%^&*()"]
    r = solution.decode(encoded_s)
    assert r == expected_s_list

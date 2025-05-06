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
        """ expect one string with |n before each sub where n is the length
        of the substring
        return a list of strings.
        "|5hello|5world" returns ["hello", "world"]
        "|0" returns [""]
        """
        pass

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

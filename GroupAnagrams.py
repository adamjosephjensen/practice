#Group Anagrams
#Solved 
#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
from typing import List
import pytest
from collections import defaultdict

#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    @staticmethod
    def char_freq(s: str) -> tuple[int, ...]:
        counts = [0] * 26
        for char in s:
            # Ensure only lowercase alphabetic characters are counted
            if 'a' <= char <= 'z':
                counts[ord(char) - ord('a')] += 1
        return tuple(counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a list of strings.
        """
        freq_to_lists = dict()
        for s in strs:
            key = Solution.char_freq(s)
            freq_to_lists[key] = freq_to_lists.get(key, []) + [s]

        return list(freq_to_lists.values())

# Helper function to compare lists of lists ignoring order of sublists and order within sublists
def sort_result(result: List[List[str]]) -> List[List[str]]:
    # Sort strings within each group
    sorted_groups = [sorted(group) for group in result]
    # Sort the groups based on their first element to have a consistent order for comparison
    # Handle empty groups if necessary, though unlikely for this problem
    sorted_groups.sort(key=lambda x: x[0] if x else "")
    return sorted_groups

# --- Test Cases ---

def test_example_case():
    """Tests the example provided in many descriptions."""
    solution = Solution()
    input_strs = ["eat","tea","tan","ate","nat","bat"]
    expected_result = [["bat"],["nat","tan"],["ate","eat","tea"]]
    # with pytest.raises(NotImplementedError):
    #     solution.groupAnagrams(input_strs)
    assert sort_result(solution.groupAnagrams(input_strs)) == sort_result(expected_result)


# --- Tests for char_freq ---

def test_char_freq_empty_string():
    """Tests char_freq with an empty string."""
    expected = tuple([0] * 26)
    assert Solution.char_freq("") == expected

def test_char_freq_simple_string():
    """Tests char_freq with a simple string."""
    expected = [0] * 26
    expected[0] = 1 # a
    expected[1] = 1 # b
    expected[2] = 1 # c
    assert Solution.char_freq("abc") == tuple(expected)

def test_char_freq_repeated_chars():
    """Tests char_freq with repeated characters."""
    expected = [0] * 26
    expected[0] = 2 # a
    expected[1] = 2 # b
    expected[2] = 1 # c
    assert Solution.char_freq("aabbc") == tuple(expected)

def test_char_freq_end_of_alphabet():
    """Tests char_freq with characters z, y, x."""
    expected = [0] * 26
    expected[23] = 1 # x
    expected[24] = 1 # y
    expected[25] = 1 # z
    assert Solution.char_freq("zyx") == tuple(expected)

def test_char_freq_single_char_type():
    """Tests char_freq with only one type of character."""
    expected = [0] * 26
    expected[0] = 3 # a
    assert Solution.char_freq("aaa") == tuple(expected)

def test_char_freq_non_alpha_chars():
    """Tests char_freq ignores non-lowercase-alpha characters (optional test)."""
    # This test assumes non-lowercase-alpha chars should be ignored.
    # Adjust if the requirements differ (e.g., raise error, handle uppercase).
    expected = [0] * 26
    expected[0] = 1 # a
    expected[1] = 1 # b
    assert Solution.char_freq("a1b B?") == tuple(expected)

def test_empty_list():
    """Tests an empty input list."""
    solution = Solution()
    input_strs = []
    expected_result = []
    # with pytest.raises(NotImplementedError):
    #     solution.groupAnagrams(input_strs)
    assert sort_result(solution.groupAnagrams(input_strs)) == sort_result(expected_result)

def test_list_with_empty_strings():
    """Tests a list containing empty strings."""
    solution = Solution()
    input_strs = ["", "b", ""]
    expected_result = [["", ""], ["b"]]
    # with pytest.raises(NotImplementedError):
    #     solution.groupAnagrams(input_strs)
    assert sort_result(solution.groupAnagrams(input_strs)) == sort_result(expected_result)

def test_no_anagrams():
    """Tests a list where no strings are anagrams of each other."""
    solution = Solution()
    input_strs = ["abc", "def", "ghi"]
    expected_result = [["abc"], ["def"], ["ghi"]]
    # with pytest.raises(NotImplementedError):
    #     solution.groupAnagrams(input_strs)
    assert sort_result(solution.groupAnagrams(input_strs)) == sort_result(expected_result)

def test_all_anagrams():
    """Tests a list where all strings are anagrams of each other."""
    solution = Solution()
    input_strs = ["listen", "silent", "enlist"]
    expected_result = [["enlist", "listen", "silent"]]
    # with pytest.raises(NotImplementedError):
    #     solution.groupAnagrams(input_strs)
    assert sort_result(solution.groupAnagrams(input_strs)) == sort_result(expected_result)

def test_single_character_strings():
    """Tests a list with single character strings."""
    solution = Solution()
    input_strs = ["a", "b", "a", "c", "b"]
    expected_result = [["a", "a"], ["b", "b"], ["c"]]
    # with pytest.raises(NotImplementedError):
    #     solution.groupAnagrams(input_strs)
    assert sort_result(solution.groupAnagrams(input_strs)) == sort_result(expected_result)

def test_duplicates_in_input():
    """Tests a list containing duplicate strings."""
    solution = Solution()
    input_strs = ["eat", "tea", "eat"]
    expected_result = [["eat", "eat", "tea"]]
    # with pytest.raises(NotImplementedError):
    #     solution.groupAnagrams(input_strs)
    assert sort_result(solution.groupAnagrams(input_strs)) == sort_result(expected_result)


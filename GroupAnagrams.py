#Group Anagrams
#Solved 
#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
from typing import List
import pytest
from collections import defaultdict

#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a list of strings.
        """
        def char_freq(s: str) -> tuple[int, ...]:
            return tuple(sum ( 1 for c in s if ord(c) - ord('a') == i) for i in range(26))

        freq_to_lists = dict()
        for s in strs:
            key = char_freq(s)
            freq_to_lists[key] = freq_to_lists.get(key, []) + [s]

        return freq_to_lists.values()

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


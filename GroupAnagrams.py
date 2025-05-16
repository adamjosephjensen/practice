#Group Anagrams
#Solved 
#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
from typing import List
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


#Group Anagrams
#Solved 
#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
from typing import List
from collections import defaultdict

class Solution:
    @staticmethod
    def char_freq(s):
        freq_arr = [0] * 26
        for c in s:
            if 'a' <= c <= 'z':
                freq_arr[ord(c) - ord('a')] += 1
        return tuple(freq_arr)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        naive approach: 
            for every string
                sort the string, that is its key
                the val is the list of strings that are anagrams
            return the values
            complexity (n*mlogm for sort, where m is the length of the average word)
        
        want O(n*m), so use a frequency counter method

        for each string:
            count its frequency
            put it in the dictionary with its anagrams
        return the values
        """
        
        dd = defaultdict(list)

        for s in strs:
            _count = Solution.char_freq(s)
            dd[_count].append(s)
        
        return list(dd.values())

class OldSolution:
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


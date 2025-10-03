class _2025_10_03_Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        scratch

        s = "AABABBA", k = 1

        """
        pass

class Brute_Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You are given a string s consisting of only uppercase english characters
        and an integer k.

        You can choose up to k characters of the string and replace them
        with any other uppercase English character.

        After performing at most k replacements, return the length of the longest substring
        which contains only one distinct character.
        
        Sliding window problem, use a hashmap to store index -> new char

        Brute force to pass the tests.
        """
        _max: int = 0
        n = len(s)
        for ll in range(n):
            for rr in range(ll+1, n+1):
                substr = s[ll:rr]
                if len(substr) < _max:
                    continue
                # we are only concerned with this one string, so check if it meets the criteria
                # 1. Find the most frequent character
                # 2. Count the other characters and see if the count is less than k
                # if yes, see if it is less than max
                # if not, continue
                counts = [0 for _ in range(26)]
                for char in substr:
                    i = ord(char) - ord('A')
                    counts[i] += 1
                max_i = counts.index(max(counts))
                letter = chr(ord('A') + max_i)
                off_letters = len(substr) - max(counts)
                if off_letters <= k:
                    # this works
                    _max = max(len(substr), _max)
        return _max

Solution = Brute_Solution

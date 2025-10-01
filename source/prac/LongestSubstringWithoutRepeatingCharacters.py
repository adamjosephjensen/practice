class _2025_10_01_A_Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        use sliding window
        """
        l, r = 0, 0
        n = len(s)
        _max = 0
        bag = set()
        # idea: grow a window to the right until you hit a duplicate
        # when you hit a duplicate, shrink the window by incrementing 'l'
        while n - l -_max > 0:
            if s[r] not in bag:
                bag.add(s[r])
                r += 1
                _max = max(len(bag), _max)
            else:
                bag.remove(s[l])
                l += 1
        return _max


class _2025_10_01_Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring
        without duplicate characters.

        Brute force: for every substring, check whether the substring
        1) contains duplicates
        2) is longer than the longest string

        We could be smart about it by checking strings in order of
        decreasing length.
        """
        _max = 0
        for length in range(len(s), 0, -1): # check length 1
            for start in range(0, len(s) - length + 1):
                substr = s[start:start+length]
                if len(substr) == len(set(substr)):
                    # no duplicates
                    _max = max(len(substr), _max)
            
            if _max > length:
                break
        
        return _max

Solution = _2025_10_01_A_Solution

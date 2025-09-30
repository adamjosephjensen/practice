class _2025_09_25_Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        check all substrings of the appropriate length of s2 as an array representation against s1
        """
        def histogram(s):
            arr = [0] * 26
            for char in s:
                _i = ord(char) - ord('a')
                arr[_i] += 1
            return arr
        
        n = len(s2)
        offset = len(s1)
        target_histogram = histogram(s1)

        for ll in range(n - offset +1): # double check
            cur_histogram = histogram(s2[ll:ll+offset])
            if cur_histogram == target_histogram:
                return True

        return False

Solution = _2025_09_25_Solution

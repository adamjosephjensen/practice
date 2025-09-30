# Based on the third Solution class in the notebook cell
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        def count_chars(text_str): # Renamed from 'count' for clarity
            counts = {}
            for c in text_str:
                counts[c] = counts.get(c, 0) + 1
            return counts

        s_counts = count_chars(s)
        t_counts = count_chars(t)
        
        return s_counts == t_counts

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def reverse(_s): # Helper defined inside in notebook
            return _s[::-1]
        stripped = ''.join([c for c in s.lower() if c.isalnum()])
        return stripped == reverse(stripped)

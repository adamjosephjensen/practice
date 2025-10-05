# source/prac/GenerateParentheses.py
# You are given an integer n. Return all well-formed parentheses
# strings that you can generate with n pairs of parentheses.
# 1 -> 1
# 2 -> 2
# 3 -> 5
from typing import List

class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        """
        Open parens go on a stack
        can either open a parenthesis or close it
        All start with "("
        Options
        1. generate all strings with the given chars
        2. filter for well-formed
        """
        stack = []
        res = []
        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append(''.join(stack))

            if open_n < n:
                stack.append('(')
                backtrack(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(')')
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0,0)
        return res

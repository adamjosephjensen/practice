from collections import deque # deque was used in GrokSolution

class Solution: # Based on GrokSolution from notebook
    def isValid(self, s: str) -> bool:
        stack = [] # Python list can be used as a stack
        matches = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in matches: # c is an opening bracket
                stack.append(c)
            elif not stack or matches.get(stack.pop()) != c: # c is a closing bracket
                return False
        return not stack # True if stack is empty, False otherwise

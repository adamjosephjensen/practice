# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:
# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        for tok in tokens:
            if tok in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if tok == '+':
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(tok))

        return stack[-1] if stack else None
           

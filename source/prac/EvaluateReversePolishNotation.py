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
        _stack = tokens
        while len(_stack) > 1:
            # process RPN
            left = int(_stack.pop(0))
            right = int(_stack.pop(0))
            op = _stack.pop(0)
            res = 0
            if op == '+':
                res = left + right
            elif op == '-':
                res = left - right
            elif op == '*':
                res = left * right
            elif op == '/':
                # division truncates towards zero
                res = int(left / right)
            else:
                print(f"left: {left}, right: {right}, op: {op}, _stack: {_stack}, res: {res}")
                assert 0, "wrong operator"
            print(f"_stack: {_stack}, res: {res}")
            _stack = [res] + tokens
            print(f"_stack after mutation: {_stack}")

        return int(_stack[0])
           

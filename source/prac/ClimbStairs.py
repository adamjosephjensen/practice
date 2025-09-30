# 1 way to climb 1 or 0 stairs
## 2 ways to climb 2 stairs (1+1, 2)
### 3 ways to climb 3 steps (1+1+1, 2+1, 1+2)
#### 3 + 2 = 5 ways to climb 4 steps
##### 5+3 = 8 ways to climb 5 steps
######

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of n stairs,
        taking either 1 or 2 steps at a time. Uses memoization for efficiency.
        """
        # Use a fresh memo dictionary for each call to climbStairs
        memo = {}
        def climb(n, memo):
            if n <= 1: return 1
            if n in memo: return memo[n]
            memo[n] = climb(n-1, memo) + climb(n-2, memo)
            return memo[n]
        return climb(n, memo)

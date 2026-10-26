class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1   # ways to reach step 1 (two steps behind step 3)
        prev1 = 2   # ways to reach step 2 (one step behind step 3)
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1

# Time Complexity  : O(N)
# Space Complexity : O(1)
# by ar-sayeem [Oct 26, 2026]
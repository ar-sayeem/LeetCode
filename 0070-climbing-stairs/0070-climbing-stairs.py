class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci iteration
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [February 1, 2026]

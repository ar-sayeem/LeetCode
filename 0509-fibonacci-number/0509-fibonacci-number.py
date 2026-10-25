class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev, curr = 0, 1
        for i in range(2, n + 1):   # from step 2 up to n
            prev, curr = curr, prev + curr

        return curr

# Time Complexity  : O(N)
# Space Complexity : O(1)
# by ar-sayeem [Oct 25, 2026]
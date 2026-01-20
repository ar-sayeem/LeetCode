class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        cs = 0
        ms = float(-inf)

        for n in nums:
            if cs < 0:
                cs = 0
            cs += n
            ms = max(cs, ms)
        return ms


# cs = CurrentSum | ms = MaxSum
# Time Complexity : O(n)
# Space Complexity : O(1)
# by ar - sayeem[January 20, 2026]

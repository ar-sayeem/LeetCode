from typing import List

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:      # one house = rob it
            return nums[0]
        
        def rob_line(start, end):
            prev = 0
            curr = 0

            for i in range(start, end + 1):
                prev, curr = curr, max(curr, prev + nums[i])
            return curr
        
        return max(rob_line(0, n - 2), rob_line(1, n - 1))

# Time Complexity  : O(n)
# Space Complexity : O(1)
# by ar-sayeem [Nov 04, 2026]
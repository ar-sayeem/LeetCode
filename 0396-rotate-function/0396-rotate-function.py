from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        curr_func = 0
        total_sum = sum(nums)
        n = len(nums)

        for i, num in enumerate(nums):
            curr_func += i * num

        ans = curr_func

        for i in range(n - 1, 0, -1):
            curr_func = curr_func + total_sum - n * nums[i]
            ans = max(ans, curr_func)

        return ans


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 01, 2026]

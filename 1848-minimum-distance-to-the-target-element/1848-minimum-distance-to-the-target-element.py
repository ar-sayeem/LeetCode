from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(i - start))
        return ans


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [April 13, 2026]

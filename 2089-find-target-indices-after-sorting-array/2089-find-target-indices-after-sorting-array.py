from typing import List

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = 0
        same = 0

        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                same += 1

        return list(range(smaller, smaller + same))

# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [Oct 19, 2026]
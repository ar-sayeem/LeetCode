from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()  # sorted nums List
        n = len(nums)

        return nums == list(range(1, n)) + [n - 1]
        #             [1, 2, ..., n - 1] + [n - 1]


# Time Complexity   : O(N log N)
# Space Complexity  : O(N)
# by ar-sayeem [May 14, 2026]
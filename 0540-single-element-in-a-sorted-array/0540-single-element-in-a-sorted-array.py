from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 1:
                mid -= 1        # force mid to be even

            if nums[mid] == nums[mid + 1]:  # target at right half
                left = mid + 2
            else:                           # target at left half
                right = mid

        return nums[left]


# Time Complexity   : O(log N)
# Space Complexity  : O(1)
# by ar-sayeem [April 26, 2026]

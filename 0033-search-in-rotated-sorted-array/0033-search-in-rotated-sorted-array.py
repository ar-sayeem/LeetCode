from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[left] <= nums[mid]:
                # target in left sorted part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1     # search left
                else:
                    left = mid + 1      # search right
                    
            else:
                # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1      # search right
                else:
                    right = mid - 1     # search left
        return -1

# Time Complexity   : O(log N)
# Space Complexity  : O(1)
# by ar-sayeem [April 25, 2026]
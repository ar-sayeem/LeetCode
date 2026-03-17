class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0     # initial leftSum

        for i, num in enumerate(nums):
            rightSum = totalSum - num - leftSum
            if leftSum == rightSum:
                return i
            leftSum += num      # accumulate left sum
        return -1                   # no pivot available


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 17, 2026]
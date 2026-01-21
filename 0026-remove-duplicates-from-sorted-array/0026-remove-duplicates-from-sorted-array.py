class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1
        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[k] = nums[n]
                k += 1
        return k


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [January 21, 2026]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = n * (n + 1) // 2
        actualSum = sum(nums)
        return expectedSum - actualSum


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [March 08, 2026]

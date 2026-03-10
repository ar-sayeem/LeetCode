class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOne = 0

        for i in nums:
            if i == 1:
                count += 1
                maxOne = max(count, maxOne)
            else:
                count = 0
        return maxOne


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 10, 2026]

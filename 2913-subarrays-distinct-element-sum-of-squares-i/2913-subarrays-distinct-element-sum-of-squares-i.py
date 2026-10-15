class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                c = len(seen)
                total += c * c

        return total

# Time Complexity   : O(n^2)
# Space Complexity  : O(n)
# by ar-sayeem [Oct 15, 2026]
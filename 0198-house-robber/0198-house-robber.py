class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0   # best loot 2 house ago
        prev1 = 0   # best loot 1 house ago

        for money in nums:
            curr = max(prev1, money + prev2)
            prev2 = prev1
            prev1 = curr
        return prev1    # return last best

# Time Complexity  : O(N)
# Space Complexity : O(1)
# by ar-sayeem [Nov 01, 2026]
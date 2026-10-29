from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        first = 0
        second = 0

        for i in range(2, n + 1):
            curr = min(second + cost[i - 1], first + cost[i - 2])
            first = second
            second = curr
        
        return second

# Time Complexity  : O(N)
# Space Complexity : O(1)
# by ar-sayeem [Oct 29, 2026]
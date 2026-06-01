class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = sum(cost)

        for i in range(2, len(cost), 3):
            total -= cost[i]

        return total


# Time Complexity   : O(N log N)
# Space Complexity  : O(1)
# by ar-sayeem [June 01, 2026]

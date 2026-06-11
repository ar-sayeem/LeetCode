from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0

        for i in range(len(tickets)):
            if i <= k:
                ans += min(tickets[i], tickets[k])
            else:
                ans += min(tickets[i], tickets[k] - 1)

        return ans


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [June 11, 2026]
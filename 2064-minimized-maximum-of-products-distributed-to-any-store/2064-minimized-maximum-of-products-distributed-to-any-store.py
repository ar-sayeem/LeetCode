from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(mid):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / mid)
            return stores <= n

        left, right = 1, max(quantities)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            if can_distribute(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


# Time Complexity   : O(M × log(max(Q)))
# Space Complexity  : O(1)
# by ar-sayeem [April 28, 2026]

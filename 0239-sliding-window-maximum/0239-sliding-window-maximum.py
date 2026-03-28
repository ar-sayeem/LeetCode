from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        dq = deque()    # stores INDICES

        l = 0   # left boundary

        for r in range(n):
            # newer bigger than back element, so remove
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)    # add curr index to the back

            # front index out of window, so remove
            if l > dq[0]:
                dq.popleft()

            # (r + 1) = curr window size
            if (r + 1) >= k:
                ans.append(nums[dq[0]])     # front of deque = max
                l += 1      # shrink window from left

        return ans


# Time Complexity: O(n)
# Space Complexity: O(k)
# by ar-sayeem [March 28, 2026]
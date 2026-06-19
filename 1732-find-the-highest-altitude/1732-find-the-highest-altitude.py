from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr = 0
        for g in gain:
            curr += g
            max_alt = max(max_alt, curr)

        return max_alt

# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [Jume 19, 2026]
from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        maxDist = 0

        for i in range(n):
            if colors[i] != colors[0]:
                maxDist = max(maxDist, i)               # distance from house 0 to house i
            if colors[i] != colors[n - 1]:
                maxDist = max(maxDist, (n - 1) - i)     # distance from house i to house n-1

        return maxDist

# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [April 20, 2026]
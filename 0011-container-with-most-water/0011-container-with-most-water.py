class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        MaxWater = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            CurrWater = w * h
            MaxWater = max(MaxWater, CurrWater)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return MaxWater


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [January 26, 2026]

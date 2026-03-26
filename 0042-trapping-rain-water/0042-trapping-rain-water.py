class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n           # tallest bar seen so far from the left
        leftMax[0] = height[0]      # seed: first bar is its own max
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])     # carry forward the bigger of prev max vs current bar

        rightMax = [0] * n          # tallest bar seen so far from the right
        rightMax[n - 1] = height[n - 1]     # seed: last bar is its own max
        for i in range(n - 2, -1, -1):              # iterate backwards, stop includes index 0
            rightMax[i] = max(rightMax[i + 1], height[i])       # carry forward the bigger of prev max vs current bar

        water = 0
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]   # shorter wall decides water level, subtract bar height

        return water


# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [March 26, 2026]
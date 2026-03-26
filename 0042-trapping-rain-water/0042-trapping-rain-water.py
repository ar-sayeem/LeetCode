class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1  # two pointers starting from both end
        leftMax = rightMax = 0
        water = 0

        while left < right:     # stops when pointer meet
            if height[left] <= height[right]:
                leftMax = max(leftMax, height[left])    # left max
                water += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])     # right max
                water += rightMax - height[right]
                right -= 1

        return water


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 26, 2026]

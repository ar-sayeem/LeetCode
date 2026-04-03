from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # store indices
        maxArea = 0
        heights.append(0)  # sentinel to flash stack

        for i in range(len(heights)):
            # current bar is smaller than the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                # remove the top index from stack and get it's height
                h = heights[stack.pop()]
                w = i if not stack else (i - stack[-1] - 1)
                maxArea = max(maxArea, h * w)
            stack.append(i)
        return maxArea


# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [April 03, 2026]

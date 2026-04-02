from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n

        # loop right -> left twice
        for i in range(2 * n - 1, -1, -1):
            curr = nums[i % n]

            # pop values that can't be the next greater element
            while stack and stack[-1] <= curr:
                stack.pop()

            # top of stack is the next greater element
            if i < n:
                ans[i] = stack[-1] if stack else -1
            stack.append(curr)

        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [April 02, 2026]

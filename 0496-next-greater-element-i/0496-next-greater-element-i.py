from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = len(nums2)
        stack = []
        mapNextGreater = {}

        for i in range(n2 - 1, -1, -1):
            # stack available and next greater not possible then pop
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                # stack empty -> no greater -> return -1
                mapNextGreater[nums2[i]] = -1
            else:
                # greater is the top of the stack
                mapNextGreater[nums2[i]] = stack[-1]

            stack.append(nums2[i])

        return [mapNextGreater[j] for j in nums1]   # lookup in map


# Time Complexity: O(m + n)
# Space Complexity: O(n)
# by ar-sayeem [April 01, 2026]

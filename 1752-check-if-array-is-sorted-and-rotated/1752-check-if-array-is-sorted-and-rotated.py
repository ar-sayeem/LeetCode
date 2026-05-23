from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n <= 1:
            return True

        decend = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                decend += 1
            if decend > 1:
                return False
        
        # 1st element > than last element, so it's a decend
        if nums[0] < nums[n - 1]:
            decend += 1

        return decend <= 1


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 23, 2026]
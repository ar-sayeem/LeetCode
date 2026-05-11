from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - 1, -1, -1):
            x = nums[i]             # 78
            while x > 0:
                ans.append(x % 10)  # [8]
                x //= 10            # [78->7]
        ans.reverse()           
        return ans

# Time Complexity   : O(N x D)
# Space Complexity  : O(N x D)
# by ar-sayeem [May 11, 2026]
